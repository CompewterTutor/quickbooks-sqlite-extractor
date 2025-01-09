from typing import List, Optional
from datetime import datetime
from lxml import etree
from sqlalchemy import create_engine, Column, String, DateTime, Boolean
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker

Base = declarative_base()

class CurrencyQueryRq:
    def __init__(self, list_id: Optional[List[str]] = None, full_name: Optional[List[str]] = None, include_ret_element: Optional[List[str]] = None):
        self.list_id = list_id
        self.full_name = full_name
        self.include_ret_element = include_ret_element

    def to_xml(self) -> str:
        xml = f'''<?xml version="1.0" encoding="utf-8"?>
<?qbxml version="16.0"?>
<QBXML>
    <QBXMLMsgsRq onError="stopOnError">
        <CurrencyQueryRq>
    '''
        if self.list_id:
            for list_id in self.list_id:
                xml += f'<ListID>{list_id}</ListID>'
        if self.full_name:
            for full_name in self.full_name:
                xml += f'<FullName>{full_name}</FullName>'
        if self.include_ret_element:
            for element in self.include_ret_element:
                xml += f'<IncludeRetElement>{element}</IncludeRetElement>'
        xml += '''
        </CurrencyQueryRq>
    </QBXMLMsgsRq>
</QBXML>
        '''
        return xml

    def from_response_xml(self, response_xml: str):
        root = etree.fromstring(response_xml.encode('utf-8'))
        currency_rets = root.findall('.//CurrencyRet')
        self.currencies = [CurrencyRet.from_xml(etree.tostring(currency_ret)) for currency_ret in currency_rets]
        self.currencies = [currency for currency in self.currencies if currency is not None]

class CurrencyRet(Base):
    __tablename__ = 'CurrencyRet'

    list_id = Column(String, primary_key=True)
    time_created = Column(DateTime)
    time_modified = Column(DateTime)
    edit_sequence = Column(String)
    name = Column(String)
    is_active = Column(Boolean, nullable=True)
    currency_code = Column(String)
    currency_format = Column(String, nullable=True)
    currency_symbol = Column(String, nullable=True)

    @staticmethod
    def from_xml(xml_str: str):
        root = etree.fromstring(xml_str)
        currency_ret = root if root.tag == 'CurrencyRet' else root.find('.//CurrencyRet')
        if currency_ret is None:
            return None

        def get_text(element, tag):
            child = element.find(tag)
            return child.text if child is not None else None

        return CurrencyRet(
            list_id=get_text(currency_ret, 'ListID'),
            time_created=datetime.fromisoformat(get_text(currency_ret, 'TimeCreated')) if get_text(currency_ret, 'TimeCreated') else None,
            time_modified=datetime.fromisoformat(get_text(currency_ret, 'TimeModified')) if get_text(currency_ret, 'TimeModified') else None,
            edit_sequence=get_text(currency_ret, 'EditSequence'),
            name=get_text(currency_ret, 'Name'),
            is_active=get_text(currency_ret, 'IsActive') == 'true' if get_text(currency_ret, 'IsActive') else None,
            currency_code=get_text(currency_ret, 'CurrencyCode'),
            currency_format=get_text(currency_ret, 'CurrencyFormat'),
            currency_symbol=get_text(currency_ret, 'CurrencySymbol')
        )

class CurrencyQueryRs:
    def __init__(self, status_code: int, status_severity: str, status_message: str, currency_ret: Optional[List[CurrencyRet]] = None):
        self.status_code = status_code
        self.status_severity = status_severity
        self.status_message = status_message
        self.currency_ret = currency_ret

def create_currency_table_if_not_exists(engine):
    Base.metadata.create_all(engine)

def generate_currency_query_xml(query: CurrencyQueryRq) -> str:
    xml = f'''<?xml version="1.0" encoding="utf-8"?>
<?qbxml version="16.0"?>
<QBXML>
    <QBXMLMsgsRq onError="stopOnError">
        <CurrencyQueryRq>
    '''
    if query.list_id:
        for list_id in query.list_id:
            xml += f'<ListID>{list_id}</ListID>'
    if query.full_name:
        for full_name in query.full_name:
            xml += f'<FullName>{full_name}</FullName>'
    if query.include_ret_element:
        for element in query.include_ret_element:
            xml += f'<IncludeRetElement>{element}</IncludeRetElement>'
    xml += '''
        </CurrencyQueryRq>
    </QBXMLMsgsRq>
</QBXML>
    '''
    return xml