from enum import Enum
from typing import List, Optional
from datetime import datetime
from lxml import etree
from sqlalchemy import create_engine, Column, String, Integer, Boolean, DateTime
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker

Base = declarative_base()

class CompanyQueryRq:
    def __init__(self, include_ret_element: Optional[List[str]] = None, owner_id: Optional[List[str]] = None):
        self.include_ret_element = include_ret_element
        self.owner_id = owner_id

    def to_xml(self) -> str:
        xml = f'''<?xml version="1.0" encoding="utf-8"?>
<?qbxml version="16.0"?>
<QBXML>
    <QBXMLMsgsRq onError="stopOnError">
        <CompanyQueryRq>
    '''
        if self.include_ret_element:
            for element in self.include_ret_element:
                xml += f'<IncludeRetElement>{element}</IncludeRetElement>'
        if self.owner_id:
            for owner_id in self.owner_id:
                xml += f'<OwnerID>{owner_id}</OwnerID>'
        xml += '''
        </CompanyQueryRq>
    </QBXMLMsgsRq>
</QBXML>
        '''
        return xml

    def from_response_xml(self, response_xml: str):
        root = etree.fromstring(response_xml.encode('utf-8'))
        company_rets = root.findall('.//CompanyRet')
        self.companies = [CompanyRet.from_xml(etree.tostring(company_ret)) for company_ret in company_rets]
        self.companies = [company for company in self.companies if company is not None]

class CompanyRet(Base):
    __tablename__ = 'CompanyRet'

    id = Column(Integer, primary_key=True, autoincrement=True)  # Add this line
    is_sample_company = Column(Boolean)
    company_name = Column(String, nullable=True)
    legal_company_name = Column(String, nullable=True)
    addr1 = Column(String, nullable=True)
    addr2 = Column(String, nullable=True)
    addr3 = Column(String, nullable=True)
    addr4 = Column(String, nullable=True)
    addr5 = Column(String, nullable=True)
    city = Column(String, nullable=True)
    state = Column(String, nullable=True)
    postal_code = Column(String, nullable=True)
    country = Column(String, nullable=True)
    note = Column(String, nullable=True)
    phone = Column(String, nullable=True)
    fax = Column(String, nullable=True)
    email = Column(String, nullable=True)
    company_website = Column(String, nullable=True)
    first_month_fiscal_year = Column(String, nullable=True)
    first_month_income_tax_year = Column(String, nullable=True)
    company_type = Column(String, nullable=True)
    ein = Column(String, nullable=True)
    ssn = Column(String, nullable=True)
    tax_form = Column(String, nullable=True)
    accountant_copy_exists = Column(Boolean, nullable=True)
    dividing_date = Column(DateTime, nullable=True)
    external_guid = Column(String, nullable=True)

    @staticmethod
    def from_xml(xml_str: str):
        root = etree.fromstring(xml_str)
        company_ret = root if root.tag == 'CompanyRet' else root.find('.//CompanyRet')
        if company_ret is None:
            return None

        def get_text(element, tag):
            child = element.find(tag)
            return child.text if child is not None else None

        return CompanyRet(
            is_sample_company=get_text(company_ret, 'IsSampleCompany') == 'true' if get_text(company_ret, 'IsSampleCompany') else None,
            company_name=get_text(company_ret, 'CompanyName'),
            legal_company_name=get_text(company_ret, 'LegalCompanyName'),
            addr1=get_text(company_ret, 'Address/Addr1'),
            addr2=get_text(company_ret, 'Address/Addr2'),
            addr3=get_text(company_ret, 'Address/Addr3'),
            addr4=get_text(company_ret, 'Address/Addr4'),
            addr5=get_text(company_ret, 'Address/Addr5'),
            city=get_text(company_ret, 'Address/City'),
            state=get_text(company_ret, 'Address/State'),
            postal_code=get_text(company_ret, 'Address/PostalCode'),
            country=get_text(company_ret, 'Address/Country'),
            note=get_text(company_ret, 'Address/Note'),
            phone=get_text(company_ret, 'Phone'),
            fax=get_text(company_ret, 'Fax'),
            email=get_text(company_ret, 'Email'),
            company_website=get_text(company_ret, 'CompanyWebSite'),
            first_month_fiscal_year=get_text(company_ret, 'FirstMonthFiscalYear'),
            first_month_income_tax_year=get_text(company_ret, 'FirstMonthIncomeTaxYear'),
            company_type=get_text(company_ret, 'CompanyType'),
            ein=get_text(company_ret, 'EIN'),
            ssn=get_text(company_ret, 'SSN'),
            tax_form=get_text(company_ret, 'TaxForm'),
            accountant_copy_exists=get_text(company_ret, 'AccountantCopy/AccountantCopyExists') == 'true' if get_text(company_ret, 'AccountantCopy/AccountantCopyExists') else None,
            dividing_date=datetime.fromisoformat(get_text(company_ret, 'AccountantCopy/DividingDate')) if get_text(company_ret, 'AccountantCopy/DividingDate') else None,
            external_guid=get_text(company_ret, 'ExternalGUID')
        )

class CompanyQueryRs:
    def __init__(self, status_code: int, status_severity: str, status_message: str, company_ret: Optional[List[CompanyRet]] = None):
        self.status_code = status_code
        self.status_severity = status_severity
        self.status_message = status_message
        self.company_ret = company_ret

def create_company_table_if_not_exists(engine):
    Base.metadata.create_all(engine)

def generate_company_query_xml(query: CompanyQueryRq) -> str:
    xml = f'''<?xml version="1.0" encoding="utf-8"?>
<?qbxml version="16.0"?>
<QBXML>
    <QBXMLMsgsRq onError="stopOnError">
        <CompanyQueryRq>
    '''
    if query.include_ret_element:
        for element in query.include_ret_element:
            xml += f'<IncludeRetElement>{element}</IncludeRetElement>'
    if query.owner_id:
        for owner_id in query.owner_id:
            xml += f'<OwnerID>{owner_id}</OwnerID>'
    xml += '''
        </CompanyQueryRq>
    </QBXMLMsgsRq>
</QBXML>
    '''
    return xml