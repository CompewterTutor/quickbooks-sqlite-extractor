from typing import List, Optional
from datetime import datetime
from lxml import etree
from sqlalchemy import create_engine, Column, String, DateTime, Integer
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker

Base = declarative_base()

class CompanyActivityQueryRq:
    def __init__(self, include_ret_element: Optional[List[str]] = None):
        self.include_ret_element = include_ret_element

    def to_xml(self) -> str:
        xml = f'''<?xml version="1.0" encoding="utf-8"?>
<?qbxml version="16.0"?>
<QBXML>
    <QBXMLMsgsRq onError="stopOnError">
        <CompanyActivityQueryRq>
    '''
        if self.include_ret_element:
            for element in self.include_ret_element:
                xml += f'<IncludeRetElement>{element}</IncludeRetElement>'
        xml += '''
        </CompanyActivityQueryRq>
    </QBXMLMsgsRq>
</QBXML>
        '''
        return xml

    def from_response_xml(self, response_xml: str):
        root = etree.fromstring(response_xml.encode('utf-8'))
        company_activity_rets = root.findall('.//CompanyActivityRet')
        self.company_activities = [CompanyActivityRet.from_xml(etree.tostring(company_activity_ret)) for company_activity_ret in company_activity_rets]
        self.company_activities = [activity for activity in self.company_activities if activity is not None]

class CompanyActivityRet(Base):
    __tablename__ = 'CompanyActivityRet'

    id = Column(Integer, primary_key=True, autoincrement=True)
    last_restore_time = Column(DateTime)
    last_condense_time = Column(DateTime)

    @staticmethod
    def from_xml(xml_str: str):
        root = etree.fromstring(xml_str)
        company_activity_ret = root if root.tag == 'CompanyActivityRet' else root.find('.//CompanyActivityRet')
        if company_activity_ret is None:
            return None

        def get_text(element, tag):
            child = element.find(tag)
            return child.text if child is not None else None

        return CompanyActivityRet(
            last_restore_time=datetime.fromisoformat(get_text(company_activity_ret, 'LastRestoreTime')) if get_text(company_activity_ret, 'LastRestoreTime') else None,
            last_condense_time=datetime.fromisoformat(get_text(company_activity_ret, 'LastCondenseTime')) if get_text(company_activity_ret, 'LastCondenseTime') else None
        )

class CompanyActivityQueryRs:
    def __init__(self, status_code: int, status_severity: str, status_message: str, company_activity_ret: Optional[List[CompanyActivityRet]] = None):
        self.status_code = status_code
        self.status_severity = status_severity
        self.status_message = status_message
        self.company_activity_ret = company_activity_ret

def create_company_activity_table_if_not_exists(engine):
    Base.metadata.create_all(engine)

def generate_company_activity_query_xml(query: CompanyActivityQueryRq) -> str:
    xml = f'''<?xml version="1.0" encoding="utf-8"?>
<?qbxml version="16.0"?>
<QBXML>
    <QBXMLMsgsRq onError="stopOnError">
        <CompanyActivityQueryRq>
    '''
    if query.include_ret_element:
        for element in query.include_ret_element:
            xml += f'<IncludeRetElement>{element}</IncludeRetElement>'
    xml += '''
        </CompanyActivityQueryRq>
    </QBXMLMsgsRq>
</QBXML>
    '''
    return xml