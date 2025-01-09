from enum import Enum
from typing import List, Optional
from datetime import datetime
from lxml import etree
from sqlalchemy import create_engine, Column, String, DateTime, Boolean, Integer
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker

Base = declarative_base()

class MatchCriterion(Enum):
    STARTS_WITH = "StartsWith"
    CONTAINS = "Contains"
    ENDS_WITH = "EndsWith"

class ActiveStatus(Enum):
    ACTIVE_ONLY = "ActiveOnly"
    INACTIVE_ONLY = "InactiveOnly"
    ALL = "All"

class NameFilter:
    def __init__(self, match_criterion: MatchCriterion, name: str):
        self.match_criterion = match_criterion
        self.name = name

class NameRangeFilter:
    def __init__(self, from_name: Optional[str] = None, to_name: Optional[str] = None):
        self.from_name = from_name
        self.to_name = to_name

class CustomerTypeQueryRq:
    def __init__(self, list_id: Optional[List[str]] = None, full_name: Optional[List[str]] = None, max_returned: Optional[int] = None,
                 active_status: Optional[ActiveStatus] = None, from_modified_date: Optional[datetime] = None, to_modified_date: Optional[datetime] = None,
                 name_filter: Optional[NameFilter] = None, name_range_filter: Optional[NameRangeFilter] = None, include_ret_element: Optional[List[str]] = None):
        self.list_id = list_id
        self.full_name = full_name
        self.max_returned = max_returned
        self.active_status = active_status
        self.from_modified_date = from_modified_date
        self.to_modified_date = to_modified_date
        self.name_filter = name_filter
        self.name_range_filter = name_range_filter
        self.include_ret_element = include_ret_element

    def to_xml(self) -> str:
        xml = f'''<?xml version="1.0" encoding="utf-8"?>
<?qbxml version="16.0"?>
<QBXML>
    <QBXMLMsgsRq onError="stopOnError">
        <CustomerTypeQueryRq>
    '''
        if self.list_id:
            for list_id in self.list_id:
                xml += f'<ListID>{list_id}</ListID>'
        if self.full_name:
            for full_name in self.full_name:
                xml += f'<FullName>{full_name}</FullName>'
        if self.max_returned:
            xml += f'<MaxReturned>{self.max_returned}</MaxReturned>'
        if self.active_status:
            xml += f'<ActiveStatus>{self.active_status.value}</ActiveStatus>'
        if self.from_modified_date:
            xml += f'<FromModifiedDate>{self.from_modified_date.isoformat()}</FromModifiedDate>'
        if self.to_modified_date:
            xml += f'<ToModifiedDate>{self.to_modified_date.isoformat()}</ToModifiedDate>'
        if self.name_filter:
            xml += f'''
            <NameFilter>
                <MatchCriterion>{self.name_filter.match_criterion.value}</MatchCriterion>
                <Name>{self.name_filter.name}</Name>
            </NameFilter>
            '''
        if self.name_range_filter:
            xml += '<NameRangeFilter>'
            if self.name_range_filter.from_name:
                xml += f'<FromName>{self.name_range_filter.from_name}</FromName>'
            if self.name_range_filter.to_name:
                xml += f'<ToName>{self.name_range_filter.to_name}</ToName>'
            xml += '</NameRangeFilter>'
        if self.include_ret_element:
            for element in self.include_ret_element:
                xml += f'<IncludeRetElement>{element}</IncludeRetElement>'
        xml += '''
        </CustomerTypeQueryRq>
    </QBXMLMsgsRq>
</QBXML>
        '''
        return xml

    def from_response_xml(self, response_xml: str):
        root = etree.fromstring(response_xml.encode('utf-8'))
        customer_type_rets = root.findall('.//CustomerTypeRet')
        self.customer_types = [CustomerTypeRet.from_xml(etree.tostring(customer_type_ret)) for customer_type_ret in customer_type_rets]
        self.customer_types = [customer_type for customer_type in self.customer_types if customer_type is not None]

class CustomerTypeRet(Base):
    __tablename__ = 'CustomerTypeRet'

    list_id = Column(String, primary_key=True)
    time_created = Column(DateTime)
    time_modified = Column(DateTime)
    edit_sequence = Column(String)
    name = Column(String)
    full_name = Column(String)
    is_active = Column(Boolean, nullable=True)
    parent_list_id = Column(String, nullable=True)
    parent_full_name = Column(String, nullable=True)
    sublevel = Column(Integer)

    @staticmethod
    def from_xml(xml_str: str):
        root = etree.fromstring(xml_str)
        customer_type_ret = root if root.tag == 'CustomerTypeRet' else root.find('.//CustomerTypeRet')
        if customer_type_ret is None:
            return None

        def get_text(element, tag):
            child = element.find(tag)
            return child.text if child is not None else None

        return CustomerTypeRet(
            list_id=get_text(customer_type_ret, 'ListID'),
            time_created=datetime.fromisoformat(get_text(customer_type_ret, 'TimeCreated')) if get_text(customer_type_ret, 'TimeCreated') else None,
            time_modified=datetime.fromisoformat(get_text(customer_type_ret, 'TimeModified')) if get_text(customer_type_ret, 'TimeModified') else None,
            edit_sequence=get_text(customer_type_ret, 'EditSequence'),
            name=get_text(customer_type_ret, 'Name'),
            full_name=get_text(customer_type_ret, 'FullName'),
            is_active=get_text(customer_type_ret, 'IsActive') == 'true' if get_text(customer_type_ret, 'IsActive') else None,
            parent_list_id=get_text(customer_type_ret, 'ParentRef/ListID'),
            parent_full_name=get_text(customer_type_ret, 'ParentRef/FullName'),
            sublevel=int(get_text(customer_type_ret, 'Sublevel')) if get_text(customer_type_ret, 'Sublevel') else None
        )

class CustomerTypeQueryRs:
    def __init__(self, status_code: int, status_severity: str, status_message: str, ret_count: int, customer_type_ret: Optional[List[CustomerTypeRet]] = None):
        self.status_code = status_code
        self.status_severity = status_severity
        self.status_message = status_message
        self.ret_count = ret_count
        self.customer_type_ret = customer_type_ret

def create_customer_type_table_if_not_exists(engine):
    Base.metadata.create_all(engine)

def generate_customer_type_query_xml(query: CustomerTypeQueryRq) -> str:
    xml = f'''<?xml version="1.0" encoding="utf-8"?>
<?qbxml version="16.0"?>
<QBXML>
    <QBXMLMsgsRq onError="stopOnError">
        <CustomerTypeQueryRq>
    '''
    if query.list_id:
        for list_id in query.list_id:
            xml += f'<ListID>{list_id}</ListID>'
    if query.full_name:
        for full_name in query.full_name:
            xml += f'<FullName>{full_name}</FullName>'
    if query.max_returned:
        xml += f'<MaxReturned>{query.max_returned}</MaxReturned>'
    if query.active_status:
        xml += f'<ActiveStatus>{query.active_status.value}</ActiveStatus>'
    if query.from_modified_date:
        xml += f'<FromModifiedDate>{query.from_modified_date.isoformat()}</FromModifiedDate>'
    if query.to_modified_date:
        xml += f'<ToModifiedDate>{query.to_modified_date.isoformat()}</ToModifiedDate>'
    if query.name_filter:
        xml += f'''
        <NameFilter>
            <MatchCriterion>{query.name_filter.match_criterion.value}</MatchCriterion>
            <Name>{query.name_filter.name}</Name>
        </NameFilter>
        '''
    if query.name_range_filter:
        xml += '<NameRangeFilter>'
        if query.name_range_filter.from_name:
            xml += f'<FromName>{query.name_range_filter.from_name}</FromName>'
        if query.name_range_filter.to_name:
            xml += f'<ToName>{query.name_range_filter.to_name}</ToName>'
        xml += '</NameRangeFilter>'
    if query.include_ret_element:
        for element in query.include_ret_element:
            xml += f'<IncludeRetElement>{element}</IncludeRetElement>'
    xml += '''
        </CustomerTypeQueryRq>
    </QBXMLMsgsRq>
</QBXML>
    '''
    return xml