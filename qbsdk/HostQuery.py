from typing import List, Optional
from lxml import etree
from sqlalchemy import create_engine, Column, String, Integer, Boolean
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker

Base = declarative_base()

class HostQueryRq:
    def __init__(self, include_max_capacity: Optional[bool] = None, include_ret_element: Optional[List[str]] = None):
        self.include_max_capacity = include_max_capacity
        self.include_ret_element = include_ret_element

    def to_xml(self) -> str:
        xml = f'''<?xml version="1.0" encoding="utf-8"?>
<?qbxml version="16.0"?>
<QBXML>
    <QBXMLMsgsRq onError="stopOnError">
        <HostQueryRq>
    '''
        if self.include_max_capacity is not None:
            xml += f'''
            <IncludeListMetaData>
                <IncludeMaxCapacity>{str(self.include_max_capacity).lower()}</IncludeMaxCapacity>
            </IncludeListMetaData>
            '''
        if self.include_ret_element:
            for element in self.include_ret_element:
                xml += f'<IncludeRetElement>{element}</IncludeRetElement>'
        xml += '''
        </HostQueryRq>
    </QBXMLMsgsRq>
</QBXML>
        '''
        return xml

    def from_response_xml(self, response_xml: str):
        root = etree.fromstring(response_xml.encode('utf-8'))
        host_rets = root.findall('.//HostRet')
        self.hosts = [HostRet.from_xml(etree.tostring(host_ret)) for host_ret in host_rets]
        self.hosts = [host for host in self.hosts if host is not None]

class HostRet(Base):
    __tablename__ = 'HostRet'

    product_name = Column(String, primary_key=True)
    major_version = Column(String)
    minor_version = Column(String)
    country = Column(String, nullable=True)
    supported_qbxml_version = Column(String)
    is_automatic_login = Column(Boolean, nullable=True)
    qb_file_mode = Column(String)
    max_capacity = Column(Integer, nullable=True)

    @staticmethod
    def from_xml(xml_str: str):
        root = etree.fromstring(xml_str)
        host_ret = root if root.tag == 'HostRet' else root.find('.//HostRet')
        if host_ret is None:
            return None

        def get_text(element, tag):
            child = element.find(tag)
            return child.text if child is not None else None

        return HostRet(
            product_name=get_text(host_ret, 'ProductName'),
            major_version=get_text(host_ret, 'MajorVersion'),
            minor_version=get_text(host_ret, 'MinorVersion'),
            country=get_text(host_ret, 'Country'),
            supported_qbxml_version=get_text(host_ret, 'SupportedQBXMLVersion'),
            is_automatic_login=get_text(host_ret, 'IsAutomaticLogin') == 'true' if get_text(host_ret, 'IsAutomaticLogin') else None,
            qb_file_mode=get_text(host_ret, 'QBFileMode'),
            max_capacity=int(get_text(host_ret, 'MaxCapacity')) if get_text(host_ret, 'MaxCapacity') else None
        )

class HostQueryRs:
    def __init__(self, status_code: int, status_severity: str, status_message: str, host_ret: Optional[List[HostRet]] = None):
        self.status_code = status_code
        self.status_severity = status_severity
        self.status_message = status_message
        self.host_ret = host_ret

def create_host_table_if_not_exists(engine):
    Base.metadata.create_all(engine)

def generate_host_query_xml(query: HostQueryRq) -> str:
    xml = f'''<?xml version="1.0" encoding="utf-8"?>
<?qbxml version="16.0"?>
<QBXML>
    <QBXMLMsgsRq onError="stopOnError">
        <HostQueryRq>
    '''
    if query.include_max_capacity is not None:
        xml += f'''
        <IncludeListMetaData>
            <IncludeMaxCapacity>{str(query.include_max_capacity).lower()}</IncludeMaxCapacity>
        </IncludeListMetaData>
        '''
    if query.include_ret_element:
        for element in query.include_ret_element:
            xml += f'<IncludeRetElement>{element}</IncludeRetElement>'
    xml += '''
        </HostQueryRq>
    </QBXMLMsgsRq>
</QBXML>
    '''
    return xml