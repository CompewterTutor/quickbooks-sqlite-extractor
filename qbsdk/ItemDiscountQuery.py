from enum import Enum
from typing import List, Optional
from datetime import datetime
from lxml import etree
from sqlalchemy import create_engine, Column, String, Integer, Float, Boolean, DateTime
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

class ItemDiscountQueryRq:
    def __init__(self, list_id: Optional[List[str]] = None, full_name: Optional[List[str]] = None, max_returned: Optional[int] = None,
                 active_status: Optional[ActiveStatus] = None, from_modified_date: Optional[datetime] = None, to_modified_date: Optional[datetime] = None,
                 name_filter: Optional[MatchCriterion] = None, name_range_filter: Optional[MatchCriterion] = None, include_ret_element: Optional[List[str]] = None,
                 owner_id: Optional[List[str]] = None):
        self.list_id = list_id
        self.full_name = full_name
        self.max_returned = max_returned
        self.active_status = active_status
        self.from_modified_date = from_modified_date
        self.to_modified_date = to_modified_date
        self.name_filter = name_filter
        self.name_range_filter = name_range_filter
        self.include_ret_element = include_ret_element
        self.owner_id = owner_id

    def to_xml(self) -> str:
        xml = f'''<?xml version="1.0" encoding="utf-8"?>
<?qbxml version="16.0"?>
<QBXML>
    <QBXMLMsgsRq onError="stopOnError">
        <ItemDiscountQueryRq>
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
                <MatchCriterion>{self.name_filter.value}</MatchCriterion>
                <Name>{self.name_filter}</Name>
            </NameFilter>
            '''
        if self.name_range_filter:
            xml += f'''
            <NameRangeFilter>
                <MatchCriterion>{self.name_range_filter.value}</MatchCriterion>
                <Name>{self.name_range_filter}</Name>
            </NameRangeFilter>
            '''
        if self.include_ret_element:
            for element in self.include_ret_element:
                xml += f'<IncludeRetElement>{element}</IncludeRetElement>'
        if self.owner_id:
            for owner_id in self.owner_id:
                xml += f'<OwnerID>{owner_id}</OwnerID>'
        xml += '''
        </ItemDiscountQueryRq>
    </QBXMLMsgsRq>
</QBXML>
        '''
        return xml

    def from_response_xml(self, response_xml: str):
        root = etree.fromstring(response_xml.encode('utf-8'))
        item_discount_rets = root.findall('.//ItemDiscountRet')
        self.item_discounts = [ItemDiscountRet.from_xml(etree.tostring(item_discount_ret)) for item_discount_ret in item_discount_rets]
        self.item_discounts = [item_discount for item_discount in self.item_discounts if item_discount is not None]

class ItemDiscountRet(Base):
    __tablename__ = 'ItemDiscountRet'

    list_id = Column(String, primary_key=True)
    time_created = Column(DateTime)
    time_modified = Column(DateTime)
    edit_sequence = Column(String)
    name = Column(String)
    full_name = Column(String)
    bar_code_value = Column(String, nullable=True)
    is_active = Column(Boolean, nullable=True)
    class_list_id = Column(String, nullable=True)
    class_full_name = Column(String, nullable=True)
    parent_list_id = Column(String, nullable=True)
    parent_full_name = Column(String, nullable=True)
    sublevel = Column(Integer)
    item_desc = Column(String, nullable=True)
    sales_tax_code_list_id = Column(String, nullable=True)
    sales_tax_code_full_name = Column(String, nullable=True)
    discount_rate = Column(Float, nullable=True)
    discount_rate_percent = Column(Float, nullable=True)
    account_list_id = Column(String, nullable=True)
    account_full_name = Column(String, nullable=True)
    external_guid = Column(String, nullable=True)

    @staticmethod
    def from_xml(xml_str: str):
        root = etree.fromstring(xml_str)
        item_discount_ret = root if root.tag == 'ItemDiscountRet' else root.find('.//ItemDiscountRet')
        if item_discount_ret is None:
            return None

        def get_text(element, tag):
            child = element.find(tag)
            return child.text if child is not None else None

        return ItemDiscountRet(
            list_id=get_text(item_discount_ret, 'ListID'),
            time_created=datetime.fromisoformat(get_text(item_discount_ret, 'TimeCreated')) if get_text(item_discount_ret, 'TimeCreated') else None,
            time_modified=datetime.fromisoformat(get_text(item_discount_ret, 'TimeModified')) if get_text(item_discount_ret, 'TimeModified') else None,
            edit_sequence=get_text(item_discount_ret, 'EditSequence'),
            name=get_text(item_discount_ret, 'Name'),
            full_name=get_text(item_discount_ret, 'FullName'),
            bar_code_value=get_text(item_discount_ret, 'BarCodeValue'),
            is_active=get_text(item_discount_ret, 'IsActive') == 'true' if get_text(item_discount_ret, 'IsActive') else None,
            class_list_id=get_text(item_discount_ret, 'ClassRef/ListID'),
            class_full_name=get_text(item_discount_ret, 'ClassRef/FullName'),
            parent_list_id=get_text(item_discount_ret, 'ParentRef/ListID'),
            parent_full_name=get_text(item_discount_ret, 'ParentRef/FullName'),
            sublevel=int(get_text(item_discount_ret, 'Sublevel')) if get_text(item_discount_ret, 'Sublevel') else None,
            item_desc=get_text(item_discount_ret, 'ItemDesc'),
            sales_tax_code_list_id=get_text(item_discount_ret, 'SalesTaxCodeRef/ListID'),
            sales_tax_code_full_name=get_text(item_discount_ret, 'SalesTaxCodeRef/FullName'),
            discount_rate=float(get_text(item_discount_ret, 'DiscountRate')) if get_text(item_discount_ret, 'DiscountRate') else None,
            discount_rate_percent=float(get_text(item_discount_ret, 'DiscountRatePercent')) if get_text(item_discount_ret, 'DiscountRatePercent') else None,
            account_list_id=get_text(item_discount_ret, 'AccountRef/ListID'),
            account_full_name=get_text(item_discount_ret, 'AccountRef/FullName'),
            external_guid=get_text(item_discount_ret, 'ExternalGUID')
        )

class ItemDiscountQueryRs:
    def __init__(self, status_code: int, status_severity: str, status_message: str, ret_count: int, item_discount_ret: Optional[List[ItemDiscountRet]] = None):
        self.status_code = status_code
        self.status_severity = status_severity
        self.status_message = status_message
        self.ret_count = ret_count
        self.item_discount_ret = item_discount_ret

def create_item_discount_table_if_not_exists(engine):
    Base.metadata.create_all(engine)

def generate_item_discount_query_xml(query: ItemDiscountQueryRq) -> str:
    xml = f'''<?xml version="1.0" encoding="utf-8"?>
<?qbxml version="16.0"?>
<QBXML>
    <QBXMLMsgsRq onError="stopOnError">
        <ItemDiscountQueryRq>
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
            <MatchCriterion>{query.name_filter.value}</MatchCriterion>
            <Name>{query.name_filter}</Name>
        </NameFilter>
        '''
    if query.name_range_filter:
        xml += f'''
        <NameRangeFilter>
            <MatchCriterion>{query.name_range_filter.value}</MatchCriterion>
            <Name>{query.name_range_filter}</Name>
        </NameRangeFilter>
        '''
    if query.include_ret_element:
        for element in query.include_ret_element:
            xml += f'<IncludeRetElement>{element}</IncludeRetElement>'
    if query.owner_id:
        for owner_id in query.owner_id:
            xml += f'<OwnerID>{owner_id}</OwnerID>'
    xml += '''
        </ItemDiscountQueryRq>
    </QBXMLMsgsRq>
</QBXML>
    '''
    return xml