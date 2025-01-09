from enum import Enum
from typing import List, Optional
from datetime import datetime
from lxml import etree
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy import Column, Integer, String

class ActiveStatus(Enum):
    ACTIVE_ONLY = "ActiveOnly"
    INACTIVE_ONLY = "InactiveOnly"
    ALL = "All"

class MatchCriterion(Enum):
    STARTS_WITH = "StartsWith"
    CONTAINS = "Contains"
    ENDS_WITH = "EndsWith"

class Operator(Enum):
    LESS_THAN = "LessThan"
    LESS_THAN_EQUAL = "LessThanEqual"
    EQUAL = "Equal"
    GREATER_THAN = "GreaterThan"
    GREATER_THAN_EQUAL = "GreaterThanEqual"

class SalesTaxCountry(Enum):
    AUSTRALIA = "Australia"
    CANADA = "Canada"
    UK = "UK"
    US = "US"

class JobStatus(Enum):
    AWARDED = "Awarded"
    CLOSED = "Closed"
    IN_PROGRESS = "InProgress"
    NONE = "None"
    NOT_AWARDED = "NotAwarded"
    PENDING = "Pending"

class PreferredDeliveryMethod(Enum):
    NONE = "None"
    EMAIL = "Email"
    FAX = "Fax"

class DataExtType(Enum):
    AMT = "AMTTYPE"
    DATETIME = "DATETIMETYPE"
    INT = "INTTYPE"
    PERCENT = "PERCENTTYPE"
    PRICE = "PRICETYPE"
    QUAN = "QUANTYPE"
    STR1024 = "STR1024TYPE"
    STR255 = "STR255TYPE"

class NameFilter:
    def __init__(self, match_criterion: MatchCriterion, name: str):
        self.match_criterion = match_criterion
        self.name = name

class NameRangeFilter:
    def __init__(self, from_name: Optional[str] = None, to_name: Optional[str] = None):
        self.from_name = from_name
        self.to_name = to_name

class TotalBalanceFilter:
    def __init__(self, operator: Operator, amount: float):
        self.operator = operator
        self.amount = amount

class CustomerQueryRq:
    def __init__(self, list_id: Optional[List[str]] = None, full_name: Optional[List[str]] = None, max_returned: Optional[int] = None,
                 active_status: Optional[ActiveStatus] = None, from_modified_date: Optional[datetime] = None, to_modified_date: Optional[datetime] = None,
                 name_filter: Optional[NameFilter] = None, name_range_filter: Optional[NameRangeFilter] = None, total_balance_filter: Optional[TotalBalanceFilter] = None,
                 include_ret_element: Optional[List[str]] = None, owner_id: Optional[List[str]] = None):
        self.list_id = list_id
        self.full_name = full_name
        self.max_returned = max_returned
        self.active_status = active_status
        self.from_modified_date = from_modified_date
        self.to_modified_date = to_modified_date
        self.name_filter = name_filter
        self.name_range_filter = name_range_filter
        self.total_balance_filter = total_balance_filter
        self.include_ret_element = include_ret_element
        self.owner_id = owner_id
        self.customers = []

    def to_xml(self) -> str:
        xml = f'''<?xml version="1.0" encoding="utf-8"?>
<?qbxml version="16.0"?>
<QBXML>
    <QBXMLMsgsRq onError="stopOnError">
        <CustomerQueryRq>
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
        if self.total_balance_filter:
            xml += f'''
            <TotalBalanceFilter>
                <Operator>{self.total_balance_filter.operator.value}</Operator>
                <Amount>{self.total_balance_filter.amount}</Amount>
            </TotalBalanceFilter>
            '''
        if self.include_ret_element:
            for element in self.include_ret_element:
                xml += f'<IncludeRetElement>{element}</IncludeRetElement>'
        if self.owner_id:
            for owner_id in self.owner_id:
                xml += f'<OwnerID>{owner_id}</OwnerID>'
        xml += '''
        </CustomerQueryRq>
    </QBXMLMsgsRq>
</QBXML>
        '''
        return xml

    def from_response_xml(self, response_xml: str):
        root = etree.fromstring(response_xml.encode('utf-8'))
        customer_rets = root.findall('.//CustomerRet')
        self.customers = [CustomerRet.from_xml(etree.tostring(customer_ret)) for customer_ret in customer_rets]
        self.customers = [customer for customer in self.customers if customer is not None]

from sqlalchemy import create_engine, Column, String, Integer, Float, Boolean, DateTime
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker

Base = declarative_base()

from lxml import etree

class CustomerRet(Base):
    __tablename__ = 'CustomerRet'

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
        customer_ret = root if root.tag == 'CustomerRet' else root.find('.//CustomerRet')
        if customer_ret is None:
            return None

        def get_text(element, tag):
            child = element.find(tag)
            return child.text if child is not None else None

        return CustomerRet(
            list_id=get_text(customer_ret, 'ListID'),
            time_created=datetime.fromisoformat(get_text(customer_ret, 'TimeCreated')) if get_text(customer_ret, 'TimeCreated') else None,
            time_modified=datetime.fromisoformat(get_text(customer_ret, 'TimeModified')) if get_text(customer_ret, 'TimeModified') else None,
            edit_sequence=get_text(customer_ret, 'EditSequence'),
            name=get_text(customer_ret, 'Name'),
            full_name=get_text(customer_ret, 'FullName'),
            is_active=get_text(customer_ret, 'IsActive') == 'true' if get_text(customer_ret, 'IsActive') else None,
            sublevel=int(get_text(customer_ret, 'Sublevel')) if get_text(customer_ret, 'Sublevel') else None,
            company_name=get_text(customer_ret, 'CompanyName'),
            salutation=get_text(customer_ret, 'Salutation'),
            first_name=get_text(customer_ret, 'FirstName'),
            middle_name=get_text(customer_ret, 'MiddleName'),
            last_name=get_text(customer_ret, 'LastName'),
            job_title=get_text(customer_ret, 'JobTitle'),
            phone=get_text(customer_ret, 'Phone'),
            alt_phone=get_text(customer_ret, 'AltPhone'),
            fax=get_text(customer_ret, 'Fax'),
            email=get_text(customer_ret, 'Email'),
            cc=get_text(customer_ret, 'Cc'),
            contact=get_text(customer_ret, 'Contact'),
            alt_contact=get_text(customer_ret, 'AltContact'),
            balance=float(get_text(customer_ret, 'Balance')) if get_text(customer_ret, 'Balance') else None,
            total_balance=float(get_text(customer_ret, 'TotalBalance')) if get_text(customer_ret, 'TotalBalance') else None,
            resale_number=get_text(customer_ret, 'ResaleNumber'),
            account_number=get_text(customer_ret, 'AccountNumber'),
            credit_limit=float(get_text(customer_ret, 'CreditLimit')) if get_text(customer_ret, 'CreditLimit') else None,
            job_status=get_text(customer_ret, 'JobStatus'),
            job_start_date=datetime.fromisoformat(get_text(customer_ret, 'JobStartDate')) if get_text(customer_ret, 'JobStartDate') else None,
            job_projected_end_date=datetime.fromisoformat(get_text(customer_ret, 'JobProjectedEndDate')) if get_text(customer_ret, 'JobProjectedEndDate') else None,
            job_end_date=datetime.fromisoformat(get_text(customer_ret, 'JobEndDate')) if get_text(customer_ret, 'JobEndDate') else None,
            job_desc=get_text(customer_ret, 'JobDesc'),
            notes=get_text(customer_ret, 'Notes'),
            external_guid=get_text(customer_ret, 'ExternalGUID'),
            tax_registration_number=get_text(customer_ret, 'TaxRegistrationNumber')
        )

class CustomerQueryRs:
    def __init__(self, status_code: int, status_severity: str, status_message: str, ret_count: int, iterator_remaining_count: Optional[int] = None, iterator_id: Optional[str] = None,
                 customer_ret: Optional[List[CustomerRet]] = None):
        self.status_code = status_code
        self.status_severity = status_severity
        self.status_message = status_message
        self.ret_count = ret_count
        self.iterator_remaining_count = iterator_remaining_count
        self.iterator_id = iterator_id
        self.customer_ret = customer_ret

import sqlite3

def create_customer_table_if_not_exists(conn: sqlite3.Connection):
    cursor = conn.cursor()
    cursor.execute('''
        CREATE TABLE IF NOT EXISTS CustomerRet (
            ListID TEXT PRIMARY KEY,
            TimeCreated TEXT,
            TimeModified TEXT,
            EditSequence TEXT,
            Name TEXT,
            FullName TEXT,
            IsActive BOOLEAN,
            Sublevel INTEGER,
            CompanyName TEXT,
            Salutation TEXT,
            FirstName TEXT,
            MiddleName TEXT,
            LastName TEXT,
            JobTitle TEXT,
            Phone TEXT,
            AltPhone TEXT,
            Fax TEXT,
            Email TEXT,
            Cc TEXT,
            Contact TEXT,
            AltContact TEXT,
            Balance REAL,
            TotalBalance REAL,
            ResaleNumber TEXT,
            AccountNumber TEXT,
            CreditLimit REAL,
            JobStatus TEXT,
            JobStartDate TEXT,
            JobProjectedEndDate TEXT,
            JobEndDate TEXT,
            JobDesc TEXT,
            Notes TEXT,
            ExternalGUID TEXT,
            TaxRegistrationNumber TEXT
        )
    ''')
    conn.commit()

def create_customer_table_if_not_exists(engine):
    Base.metadata.create_all(engine)

def generate_customer_query_xml(query: CustomerQueryRq) -> str:
    xml = f'''<?xml version="1.0" encoding="utf-8"?>
<?qbxml version="16.0"?>
<QBXML>
    <QBXMLMsgsRq onError="stopOnError">
        <CustomerQueryRq>
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
    if query.total_balance_filter:
        xml += f'''
        <TotalBalanceFilter>
            <Operator>{query.total_balance_filter.operator.value}</Operator>
            <Amount>{query.total_balance_filter.amount}</Amount>
        </TotalBalanceFilter>
        '''
    if query.include_ret_element:
        for element in query.include_ret_element:
            xml += f'<IncludeRetElement>{element}</IncludeRetElement>'
    if query.owner_id:
        for owner_id in query.owner_id:
            xml += f'<OwnerID>{owner_id}</OwnerID>'
    xml += '''
        </CustomerQueryRq>
    </QBXMLMsgsRq>
</QBXML>
    '''
    return xml