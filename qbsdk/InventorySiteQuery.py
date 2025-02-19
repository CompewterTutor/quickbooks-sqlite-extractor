from enum import Enum
from typing import List, Optional
from datetime import datetime
from lxml import etree
from sqlalchemy import create_engine, Column, String, Integer, Boolean, DateTime
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

class InventorySiteQueryRq:
    def __init__(self, list_id: Optional[List[str]] = None, full_name: Optional[List[str]] = None, active_status: Optional[ActiveStatus] = None,
                 from_modified_date: Optional[datetime] = None, to_modified_date: Optional[datetime] = None, name_filter: Optional[MatchCriterion] = None,
                 name_range_filter: Optional[MatchCriterion] = None, include_ret_element: Optional[List[str]] = None):
        self.list_id = list_id
        self.full_name = full_name
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
        <InventorySiteQueryRq>
    '''
        if self.list_id:
            for list_id in self.list_id:
                xml += f'<ListID>{list_id}</ListID>'
        if self.full_name:
            for full_name in self.full_name:
                xml += f'<FullName>{full_name}</FullName>'
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
        xml += '''
        </InventorySiteQueryRq>
    </QBXMLMsgsRq>
</QBXML>
        '''
        return xml

    def from_response_xml(self, response_xml: str):
        root = etree.fromstring(response_xml.encode('utf-8'))
        inventory_site_rets = root.findall('.//InventorySiteRet')
        self.inventory_sites = [InventorySiteRet.from_xml(etree.tostring(inventory_site_ret)) for inventory_site_ret in inventory_site_rets]
        self.inventory_sites = [inventory_site for inventory_site in self.inventory_sites if inventory_site is not None]

class InventorySiteRet(Base):
    __tablename__ = 'InventorySiteRet'

    list_id = Column(String, primary_key=True)
    time_created = Column(DateTime)
    time_modified = Column(DateTime)
    edit_sequence = Column(String)
    name = Column(String, nullable=True)
    is_active = Column(Boolean, nullable=True)
    parent_list_id = Column(String, nullable=True)
    parent_full_name = Column(String, nullable=True)
    is_default_site = Column(Boolean, nullable=True)
    site_desc = Column(String, nullable=True)
    contact = Column(String, nullable=True)
    phone = Column(String, nullable=True)
    fax = Column(String, nullable=True)
    email = Column(String, nullable=True)
    addr1 = Column(String, nullable=True)
    addr2 = Column(String, nullable=True)
    addr3 = Column(String, nullable=True)
    addr4 = Column(String, nullable=True)
    addr5 = Column(String, nullable=True)
    city = Column(String, nullable=True)
    state = Column(String, nullable=True)
    postal_code = Column(String, nullable=True)
    country = Column(String, nullable=True)

    @staticmethod
    def from_xml(xml_str: str):
        root = etree.fromstring(xml_str)
        inventory_site_ret = root if root.tag == 'InventorySiteRet' else root.find('.//InventorySiteRet')
        if inventory_site_ret is None:
            return None

        def get_text(element, tag):
            child = element.find(tag)
            return child.text if child is not None else None

        return InventorySiteRet(
            list_id=get_text(inventory_site_ret, 'ListID'),
            time_created=datetime.fromisoformat(get_text(inventory_site_ret, 'TimeCreated')) if get_text(inventory_site_ret, 'TimeCreated') else None,
            time_modified=datetime.fromisoformat(get_text(inventory_site_ret, 'TimeModified')) if get_text(inventory_site_ret, 'TimeModified') else None,
            edit_sequence=get_text(inventory_site_ret, 'EditSequence'),
            name=get_text(inventory_site_ret, 'Name'),
            is_active=get_text(inventory_site_ret, 'IsActive') == 'true' if get_text(inventory_site_ret, 'IsActive') else None,
            parent_list_id=get_text(inventory_site_ret, 'ParentSiteRef/ListID'),
            parent_full_name=get_text(inventory_site_ret, 'ParentSiteRef/FullName'),
            is_default_site=get_text(inventory_site_ret, 'IsDefaultSite') == 'true' if get_text(inventory_site_ret, 'IsDefaultSite') else None,
            site_desc=get_text(inventory_site_ret, 'SiteDesc'),
            contact=get_text(inventory_site_ret, 'Contact'),
            phone=get_text(inventory_site_ret, 'Phone'),
            fax=get_text(inventory_site_ret, 'Fax'),
            email=get_text(inventory_site_ret, 'Email'),
            addr1=get_text(inventory_site_ret, 'SiteAddress/Addr1'),
            addr2=get_text(inventory_site_ret, 'SiteAddress/Addr2'),
            addr3=get_text(inventory_site_ret, 'SiteAddress/Addr3'),
            addr4=get_text(inventory_site_ret, 'SiteAddress/Addr4'),
            addr5=get_text(inventory_site_ret, 'SiteAddress/Addr5'),
            city=get_text(inventory_site_ret, 'SiteAddress/City'),
            state=get_text(inventory_site_ret, 'SiteAddress/State'),
            postal_code=get_text(inventory_site_ret, 'SiteAddress/PostalCode'),
            country=get_text(inventory_site_ret, 'SiteAddress/Country')
        )

class InventorySiteQueryRs:
    def __init__(self, status_code: int, status_severity: str, status_message: str, ret_count: int, inventory_site_ret: Optional[List[InventorySiteRet]] = None):
        self.status_code = status_code
        self.status_severity = status_severity
        self.status_message = status_message
        self.ret_count = ret_count
        self.inventory_site_ret = inventory_site_ret

def create_inventory_site_table_if_not_exists(engine):
    Base.metadata.create_all(engine)

def generate_inventory_site_query_xml(query: InventorySiteQueryRq) -> str:
    xml = f'''<?xml version="1.0" encoding="utf-8"?>
<?qbxml version="16.0"?>
<QBXML>
    <QBXMLMsgsRq onError="stopOnError">
        <InventorySiteQueryRq>
    '''
    if query.list_id:
        for list_id in query.list_id:
            xml += f'<ListID>{list_id}</ListID>'
    if query.full_name:
        for full_name in query.full_name:
            xml += f'<FullName>{full_name}</FullName>'
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
    xml += '''
        </InventorySiteQueryRq>
    </QBXMLMsgsRq>
</QBXML>
    '''
    return xml