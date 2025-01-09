from enum import Enum
from typing import List, Optional
from datetime import datetime
from lxml import etree
from sqlalchemy import create_engine, Column, String, DateTime, Boolean, Integer, Float
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

class EntityQueryRq:
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
        <EntityQueryRq>
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
        </EntityQueryRq>
    </QBXMLMsgsRq>
</QBXML>
        '''
        return xml

    def from_response_xml(self, response_xml: str):
        root = etree.fromstring(response_xml.encode('utf-8'))
        entity_rets = root.findall('.//CustomerRet') + root.findall('.//EmployeeRet') + root.findall('.//VendorRet')
        self.entities = [EntityRet.from_xml(etree.tostring(entity_ret)) for entity_ret in entity_rets]
        self.entities = [entity for entity in self.entities if entity is not None]

class EntityRet(Base):
    __tablename__ = 'EntityRet'

    list_id = Column(String, primary_key=True)
    time_created = Column(DateTime)
    time_modified = Column(DateTime)
    edit_sequence = Column(String)
    name = Column(String)
    full_name = Column(String)
    is_active = Column(Boolean, nullable=True)
    sublevel = Column(Integer)
    company_name = Column(String, nullable=True)
    salutation = Column(String, nullable=True)
    first_name = Column(String, nullable=True)
    middle_name = Column(String, nullable=True)
    last_name = Column(String, nullable=True)
    job_title = Column(String, nullable=True)
    phone = Column(String, nullable=True)
    alt_phone = Column(String, nullable=True)
    fax = Column(String, nullable=True)
    email = Column(String, nullable=True)
    cc = Column(String, nullable=True)
    contact = Column(String, nullable=True)
    alt_contact = Column(String, nullable=True)
    balance = Column(Float, nullable=True)
    total_balance = Column(Float, nullable=True)
    resale_number = Column(String, nullable=True)
    account_number = Column(String, nullable=True)
    credit_limit = Column(Float, nullable=True)
    job_status = Column(String, nullable=True)
    job_start_date = Column(DateTime, nullable=True)
    job_projected_end_date = Column(DateTime, nullable=True)
    job_end_date = Column(DateTime, nullable=True)
    job_desc = Column(String, nullable=True)
    notes = Column(String, nullable=True)
    external_guid = Column(String, nullable=True)
    tax_registration_number = Column(String, nullable=True)

    @staticmethod
    def from_xml(xml_str: str):
        root = etree.fromstring(xml_str)
        entity_ret = root if root.tag in ['CustomerRet', 'EmployeeRet', 'VendorRet'] else root.find('.//CustomerRet') or root.find('.//EmployeeRet') or root.find('.//VendorRet')
        if entity_ret is None:
            return None

        def get_text(element, tag):
            child = element.find(tag)
            return child.text if child is not None else None

        return EntityRet(
            list_id=get_text(entity_ret, 'ListID'),
            time_created=datetime.fromisoformat(get_text(entity_ret, 'TimeCreated')) if get_text(entity_ret, 'TimeCreated') else None,
            time_modified=datetime.fromisoformat(get_text(entity_ret, 'TimeModified')) if get_text(entity_ret, 'TimeModified') else None,
            edit_sequence=get_text(entity_ret, 'EditSequence'),
            name=get_text(entity_ret, 'Name'),
            full_name=get_text(entity_ret, 'FullName'),
            is_active=get_text(entity_ret, 'IsActive') == 'true' if get_text(entity_ret, 'IsActive') else None,
            sublevel=int(get_text(entity_ret, 'Sublevel')) if get_text(entity_ret, 'Sublevel') else None,
            company_name=get_text(entity_ret, 'CompanyName'),
            salutation=get_text(entity_ret, 'Salutation'),
            first_name=get_text(entity_ret, 'FirstName'),
            middle_name=get_text(entity_ret, 'MiddleName'),
            last_name=get_text(entity_ret, 'LastName'),
            job_title=get_text(entity_ret, 'JobTitle'),
            phone=get_text(entity_ret, 'Phone'),
            alt_phone=get_text(entity_ret, 'AltPhone'),
            fax=get_text(entity_ret, 'Fax'),
            email=get_text(entity_ret, 'Email'),
            cc=get_text(entity_ret, 'Cc'),
            contact=get_text(entity_ret, 'Contact'),
            alt_contact=get_text(entity_ret, 'AltContact'),
            balance=float(get_text(entity_ret, 'Balance')) if get_text(entity_ret, 'Balance') else None,
            total_balance=float(get_text(entity_ret, 'TotalBalance')) if get_text(entity_ret, 'TotalBalance') else None,
            resale_number=get_text(entity_ret, 'ResaleNumber'),
            account_number=get_text(entity_ret, 'AccountNumber'),
            credit_limit=float(get_text(entity_ret, 'CreditLimit')) if get_text(entity_ret, 'CreditLimit') else None,
            job_status=get_text(entity_ret, 'JobStatus'),
            job_start_date=datetime.fromisoformat(get_text(entity_ret, 'JobStartDate')) if get_text(entity_ret, 'JobStartDate') else None,
            job_projected_end_date=datetime.fromisoformat(get_text(entity_ret, 'JobProjectedEndDate')) if get_text(entity_ret, 'JobProjectedEndDate') else None,
            job_end_date=datetime.fromisoformat(get_text(entity_ret, 'JobEndDate')) if get_text(entity_ret, 'JobEndDate') else None,
            job_desc=get_text(entity_ret, 'JobDesc'),
            notes=get_text(entity_ret, 'Notes'),
            external_guid=get_text(entity_ret, 'ExternalGUID'),
            tax_registration_number=get_text(entity_ret, 'TaxRegistrationNumber')
        )

class EntityQueryRs:
    def __init__(self, status_code: int, status_severity: str, status_message: str, ret_count: int, entity_ret: Optional[List[EntityRet]] = None):
        self.status_code = status_code
        self.status_severity = status_severity
        self.status_message = status_message
        self.ret_count = ret_count
        self.entity_ret = entity_ret

def create_entity_table_if_not_exists(engine):
    Base.metadata.create_all(engine)

def generate_entity_query_xml(query: EntityQueryRq) -> str:
    xml = f'''<?xml version="1.0" encoding="utf-8"?>
<?qbxml version="16.0"?>
<QBXML>
    <QBXMLMsgsRq onError="stopOnError">
        <EntityQueryRq>
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
        </EntityQueryRq>
    </QBXMLMsgsRq>
</QBXML>
    '''
    return xml