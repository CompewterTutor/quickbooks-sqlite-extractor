### XMLOps
# ```
# <?xml version="1.0" encoding="utf-8"?>
# <?qbxml version="16.0"?>
# <QBXML>
#         <QBXMLMsgsRq onError="stopOnError">
#                 <CustomerQueryRq metaData="ENUMTYPE" iterator="ENUMTYPE" iteratorID="UUIDTYPE">
#                         <!-- BEGIN OR -->
#                                 <ListID >IDTYPE</ListID> <!-- optional, may repeat -->
#                         <!-- OR -->
#                                 <FullName >STRTYPE</FullName> <!-- optional, may repeat -->
#                         <!-- OR -->
#                                 <MaxReturned >INTTYPE</MaxReturned> <!-- optional -->
#                                 <!-- ActiveStatus may have one of the following values: ActiveOnly [DEFAULT], InactiveOnly, All -->
#                                 <ActiveStatus >ENUMTYPE</ActiveStatus> <!-- optional -->
#                                 <FromModifiedDate >DATETIMETYPE</FromModifiedDate> <!-- optional -->
#                                 <ToModifiedDate >DATETIMETYPE</ToModifiedDate> <!-- optional -->
#                                 <!-- BEGIN OR -->
#                                         <NameFilter> <!-- optional -->
#                                                 <!-- MatchCriterion may have one of the following values: StartsWith, Contains, EndsWith -->
#                                                 <MatchCriterion >ENUMTYPE</MatchCriterion> <!-- required -->
#                                                 <Name >STRTYPE</Name> <!-- required -->
#                                         </NameFilter>
#                                 <!-- OR -->
#                                         <NameRangeFilter> <!-- optional -->
#                                                 <FromName >STRTYPE</FromName> <!-- optional -->
#                                                 <ToName >STRTYPE</ToName> <!-- optional -->
#                                         </NameRangeFilter>
#                                 <!-- END OR -->
#                                 <TotalBalanceFilter> <!-- optional -->
#                                         <!-- Operator may have one of the following values: LessThan, LessThanEqual, Equal, GreaterThan, GreaterThanEqual -->
#                                         <Operator >ENUMTYPE</Operator> <!-- required -->
#                                         <Amount >AMTTYPE</Amount> <!-- required -->
#                                 </TotalBalanceFilter>
#                                 <CurrencyFilter> <!-- optional -->
#                                         <!-- BEGIN OR -->
#                                                 <ListID >IDTYPE</ListID> <!-- optional, may repeat -->
#                                         <!-- OR -->
#                                                 <FullName >STRTYPE</FullName> <!-- optional, may repeat -->
#                                         <!-- END OR -->
#                                 </CurrencyFilter>
#                                 <ClassFilter> <!-- optional -->
#                                         <!-- BEGIN OR -->
#                                                 <ListID >IDTYPE</ListID> <!-- optional, may repeat -->
#                                         <!-- OR -->
#                                                 <FullName >STRTYPE</FullName> <!-- optional, may repeat -->
#                                         <!-- OR -->
#                                                 <ListIDWithChildren >IDTYPE</ListIDWithChildren> <!-- optional -->
#                                         <!-- OR -->
#                                                 <FullNameWithChildren >STRTYPE</FullNameWithChildren> <!-- optional -->
#                                         <!-- END OR -->
#                                 </ClassFilter>
#                         <!-- END OR -->
#                         <IncludeRetElement >STRTYPE</IncludeRetElement> <!-- optional, may repeat -->
#                         <OwnerID >GUIDTYPE</OwnerID> <!-- optional, may repeat -->
#                 </CustomerQueryRq>

#                 <CustomerQueryRs statusCode="INTTYPE" statusSeverity="STRTYPE" statusMessage="STRTYPE" retCount="INTTYPE" iteratorRemainingCount="INTTYPE" iteratorID="UUIDTYPE">
#                         <CustomerRet> <!-- optional, may repeat -->
#                                 <ListID >IDTYPE</ListID> <!-- required -->
#                                 <TimeCreated >DATETIMETYPE</TimeCreated> <!-- required -->
#                                 <TimeModified >DATETIMETYPE</TimeModified> <!-- required -->
#                                 <EditSequence >STRTYPE</EditSequence> <!-- required -->
#                                 <Name >STRTYPE</Name> <!-- required -->
#                                 <FullName >STRTYPE</FullName> <!-- required -->
#                                 <IsActive >BOOLTYPE</IsActive> <!-- optional -->
#                                 <ClassRef> <!-- optional -->
#                                         <ListID >IDTYPE</ListID> <!-- optional -->
#                                         <FullName >STRTYPE</FullName> <!-- optional -->
#                                 </ClassRef>
#                                 <ParentRef> <!-- optional -->
#                                         <ListID >IDTYPE</ListID> <!-- optional -->
#                                         <FullName >STRTYPE</FullName> <!-- optional -->
#                                 </ParentRef>
#                                 <Sublevel >INTTYPE</Sublevel> <!-- required -->
#                                 <CompanyName >STRTYPE</CompanyName> <!-- optional -->
#                                 <Salutation >STRTYPE</Salutation> <!-- optional -->
#                                 <FirstName >STRTYPE</FirstName> <!-- optional -->
#                                 <MiddleName >STRTYPE</MiddleName> <!-- optional -->
#                                 <LastName >STRTYPE</LastName> <!-- optional -->
#                                 <JobTitle >STRTYPE</JobTitle> <!-- optional -->
#                                 <BillAddress> <!-- optional -->
#                                         <Addr1 >STRTYPE</Addr1> <!-- optional -->
#                                         <Addr2 >STRTYPE</Addr2> <!-- optional -->
#                                         <Addr3 >STRTYPE</Addr3> <!-- optional -->
#                                         <Addr4 >STRTYPE</Addr4> <!-- optional -->
#                                         <Addr5 >STRTYPE</Addr5> <!-- optional -->
#                                         <City >STRTYPE</City> <!-- optional -->
#                                         <State >STRTYPE</State> <!-- optional -->
#                                         <PostalCode >STRTYPE</PostalCode> <!-- optional -->
#                                         <Country >STRTYPE</Country> <!-- optional -->
#                                         <Note >STRTYPE</Note> <!-- optional -->
#                                 </BillAddress>
#                                 <BillAddressBlock> <!-- optional -->
#                                         <Addr1 >STRTYPE</Addr1> <!-- optional -->
#                                         <Addr2 >STRTYPE</Addr2> <!-- optional -->
#                                         <Addr3 >STRTYPE</Addr3> <!-- optional -->
#                                         <Addr4 >STRTYPE</Addr4> <!-- optional -->
#                                         <Addr5 >STRTYPE</Addr5> <!-- optional -->
#                                 </BillAddressBlock>
#                                 <ShipAddress> <!-- optional -->
#                                         <Addr1 >STRTYPE</Addr1> <!-- optional -->
#                                         <Addr2 >STRTYPE</Addr2> <!-- optional -->
#                                         <Addr3 >STRTYPE</Addr3> <!-- optional -->
#                                         <Addr4 >STRTYPE</Addr4> <!-- optional -->
#                                         <Addr5 >STRTYPE</Addr5> <!-- optional -->
#                                         <City >STRTYPE</City> <!-- optional -->
#                                         <State >STRTYPE</State> <!-- optional -->
#                                         <PostalCode >STRTYPE</PostalCode> <!-- optional -->
#                                         <Country >STRTYPE</Country> <!-- optional -->
#                                         <Note >STRTYPE</Note> <!-- optional -->
#                                 </ShipAddress>
#                                 <ShipAddressBlock> <!-- optional -->
#                                         <Addr1 >STRTYPE</Addr1> <!-- optional -->
#                                         <Addr2 >STRTYPE</Addr2> <!-- optional -->
#                                         <Addr3 >STRTYPE</Addr3> <!-- optional -->
#                                         <Addr4 >STRTYPE</Addr4> <!-- optional -->
#                                         <Addr5 >STRTYPE</Addr5> <!-- optional -->
#                                 </ShipAddressBlock>
#                                 <ShipToAddress> <!-- must occur 0 - 50 times -->
#                                         <Name >STRTYPE</Name> <!-- required -->
#                                         <Addr1 >STRTYPE</Addr1> <!-- optional -->
#                                         <Addr2 >STRTYPE</Addr2> <!-- optional -->
#                                         <Addr3 >STRTYPE</Addr3> <!-- optional -->
#                                         <Addr4 >STRTYPE</Addr4> <!-- optional -->
#                                         <Addr5 >STRTYPE</Addr5> <!-- optional -->
#                                         <City >STRTYPE</City> <!-- optional -->
#                                         <State >STRTYPE</State> <!-- optional -->
#                                         <PostalCode >STRTYPE</PostalCode> <!-- optional -->
#                                         <Country >STRTYPE</Country> <!-- optional -->
#                                         <Note >STRTYPE</Note> <!-- optional -->
#                                         <DefaultShipTo >BOOLTYPE</DefaultShipTo> <!-- optional -->
#                                 </ShipToAddress>
#                                 <Phone >STRTYPE</Phone> <!-- optional -->
#                                 <AltPhone >STRTYPE</AltPhone> <!-- optional -->
#                                 <Fax >STRTYPE</Fax> <!-- optional -->
#                                 <Email >STRTYPE</Email> <!-- optional -->
#                                 <Cc >STRTYPE</Cc> <!-- optional -->
#                                 <Contact >STRTYPE</Contact> <!-- optional -->
#                                 <AltContact >STRTYPE</AltContact> <!-- optional -->
#                                 <AdditionalContactRef> <!-- must occur 0 - 8 times -->
#                                         <ContactName >STRTYPE</ContactName> <!-- required -->
#                                         <ContactValue >STRTYPE</ContactValue> <!-- required -->
#                                 </AdditionalContactRef>
#                                 <ContactsRet> <!-- optional, may repeat -->
#                                         <ListID >IDTYPE</ListID> <!-- required -->
#                                         <TimeCreated >DATETIMETYPE</TimeCreated> <!-- required -->
#                                         <TimeModified >DATETIMETYPE</TimeModified> <!-- required -->
#                                         <EditSequence >STRTYPE</EditSequence> <!-- required -->
#                                         <Contact >STRTYPE</Contact> <!-- optional -->
#                                         <Salutation >STRTYPE</Salutation> <!-- optional -->
#                                         <FirstName >STRTYPE</FirstName> <!-- required -->
#                                         <MiddleName >STRTYPE</MiddleName> <!-- optional -->
#                                         <LastName >STRTYPE</LastName> <!-- optional -->
#                                         <JobTitle >STRTYPE</JobTitle> <!-- optional -->
#                                         <AdditionalContactRef> <!-- must occur 0 - 5 times -->
#                                                 <ContactName >STRTYPE</ContactName> <!-- required -->
#                                                 <ContactValue >STRTYPE</ContactValue> <!-- required -->
#                                         </AdditionalContactRef>
#                                 </ContactsRet>
#                                 <CustomerTypeRef> <!-- optional -->
#                                         <ListID >IDTYPE</ListID> <!-- optional -->
#                                         <FullName >STRTYPE</FullName> <!-- optional -->
#                                 </CustomerTypeRef>
#                                 <TermsRef> <!-- optional -->
#                                         <ListID >IDTYPE</ListID> <!-- optional -->
#                                         <FullName >STRTYPE</FullName> <!-- optional -->
#                                 </TermsRef>
#                                 <SalesRepRef> <!-- optional -->
#                                         <ListID >IDTYPE</ListID> <!-- optional -->
#                                         <FullName >STRTYPE</FullName> <!-- optional -->
#                                 </SalesRepRef>
#                                 <Balance >AMTTYPE</Balance> <!-- optional -->
#                                 <TotalBalance >AMTTYPE</TotalBalance> <!-- optional -->
#                                 <SalesTaxCodeRef> <!-- optional -->
#                                         <ListID >IDTYPE</ListID> <!-- optional -->
#                                         <FullName >STRTYPE</FullName> <!-- optional -->
#                                 </SalesTaxCodeRef>
#                                 <ItemSalesTaxRef> <!-- optional -->
#                                         <ListID >IDTYPE</ListID> <!-- optional -->
#                                         <FullName >STRTYPE</FullName> <!-- optional -->
#                                 </ItemSalesTaxRef>
#                                 <!-- SalesTaxCountry may have one of the following values: Australia, Canada [DEFAULT], UK, US -->
#                                 <SalesTaxCountry >ENUMTYPE</SalesTaxCountry> <!-- optional -->
#                                 <ResaleNumber >STRTYPE</ResaleNumber> <!-- optional -->
#                                 <AccountNumber >STRTYPE</AccountNumber> <!-- optional -->
#                                 <CreditLimit >AMTTYPE</CreditLimit> <!-- optional -->
#                                 <PreferredPaymentMethodRef> <!-- optional -->
#                                         <ListID >IDTYPE</ListID> <!-- optional -->
#                                         <FullName >STRTYPE</FullName> <!-- optional -->
#                                 </PreferredPaymentMethodRef>
#                                 <CreditCardInfo> <!-- optional -->
#                                         <CreditCardNumber >STRTYPE</CreditCardNumber> <!-- optional -->
#                                         <ExpirationMonth >INTTYPE</ExpirationMonth> <!-- optional -->
#                                         <ExpirationYear >INTTYPE</ExpirationYear> <!-- optional -->
#                                         <NameOnCard >STRTYPE</NameOnCard> <!-- optional -->
#                                         <CreditCardAddress >STRTYPE</CreditCardAddress> <!-- optional -->
#                                         <CreditCardPostalCode >STRTYPE</CreditCardPostalCode> <!-- optional -->
#                                 </CreditCardInfo>
#                                 <!-- JobStatus may have one of the following values: Awarded, Closed, InProgress, None [DEFAULT], NotAwarded, Pending -->
#                                 <JobStatus >ENUMTYPE</JobStatus> <!-- optional -->
#                                 <JobStartDate >DATETYPE</JobStartDate> <!-- optional -->
#                                 <JobProjectedEndDate >DATETYPE</JobProjectedEndDate> <!-- optional -->
#                                 <JobEndDate >DATETYPE</JobEndDate> <!-- optional -->
#                                 <JobDesc >STRTYPE</JobDesc> <!-- optional -->
#                                 <JobTypeRef> <!-- optional -->
#                                         <ListID >IDTYPE</ListID> <!-- optional -->
#                                         <FullName >STRTYPE</FullName> <!-- optional -->
#                                 </JobTypeRef>
#                                 <Notes >STRTYPE</Notes> <!-- optional -->
#                                 <AdditionalNotesRet> <!-- optional, may repeat -->
#                                         <NoteID >INTTYPE</NoteID> <!-- required -->
#                                         <Date >DATETYPE</Date> <!-- required -->
#                                         <Note >STRTYPE</Note> <!-- required -->
#                                 </AdditionalNotesRet>
#                                 <!-- PreferredDeliveryMethod may have one of the following values: None [Default], Email, Fax -->
#                                 <PreferredDeliveryMethod >ENUMTYPE</PreferredDeliveryMethod> <!-- optional -->
#                                 <PriceLevelRef> <!-- optional -->
#                                         <ListID >IDTYPE</ListID> <!-- optional -->
#                                         <FullName >STRTYPE</FullName> <!-- optional -->
#                                 </PriceLevelRef>
#                                 <ExternalGUID >GUIDTYPE</ExternalGUID> <!-- optional -->
#                                 <TaxRegistrationNumber >STRTYPE</TaxRegistrationNumber> <!-- optional -->
#                                 <CurrencyRef> <!-- optional -->
#                                         <ListID >IDTYPE</ListID> <!-- optional -->
#                                         <FullName >STRTYPE</FullName> <!-- optional -->
#                                 </CurrencyRef>
#                                 <DataExtRet> <!-- optional, may repeat -->
#                                         <OwnerID >GUIDTYPE</OwnerID> <!-- optional -->
#                                         <DataExtName >STRTYPE</DataExtName> <!-- required -->
#                                         <!-- DataExtType may have one of the following values: AMTTYPE, DATETIMETYPE, INTTYPE, PERCENTTYPE, PRICETYPE, QUANTYPE, STR1024TYPE, STR255TYPE -->
#                                         <DataExtType >ENUMTYPE</DataExtType> <!-- required -->
#                                         <DataExtValue >STRTYPE</DataExtValue> <!-- required -->
#                                 </DataExtRet>
#                         </CustomerRet>
#                 </CustomerQueryRs>
#         </QBXMLMsgsRq>
# </QBXML>

from enum import Enum
from typing import List, Optional
from datetime import datetime


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
        root = etree.fromstring(xml_str.encode('utf-8'))
        customer_ret = root.find('.//CustomerRet')
        if customer_ret is None:
            return None

        def get_text(element, tag):
            child = element.find(tag)
            return child.text if child is not None else None

        return CustomerRet(
            list_id=get_text(customer_ret, 'ListID'),
            time_created=datetime.fromisoformat(get_text(customer_ret, 'TimeCreated')),
            time_modified=datetime.fromisoformat(get_text(customer_ret, 'TimeModified')),
            edit_sequence=get_text(customer_ret, 'EditSequence'),
            name=get_text(customer_ret, 'Name'),
            full_name=get_text(customer_ret, 'FullName'),
            is_active=get_text(customer_ret, 'IsActive') == 'true',
            sublevel=int(get_text(customer_ret, 'Sublevel')),
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