
from abc import ABC, abstractmethod
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker
from sqlalchemy import create_engine
import win32com.client  # COM interface

Base = declarative_base()

class QBQuery(Base, ABC):
    __abstract__ = True

    @abstractmethod
    def from_xml(self, xml_str: str):
        pass

    @abstractmethod
    def to_xml(self) -> str:
        pass

    @abstractmethod
    def query_quickbooks(self, session_manager, ticket):
        pass

    @staticmethod
    def connect_to_quickbooks():
        """Establish a connection to QuickBooks."""
        session_manager = win32com.client.Dispatch("QBXMLRP2.RequestProcessor")
        session_manager.OpenConnection("", "QuickBooks Data Export")
        ticket = session_manager.BeginSession("", 2)  # 2 = No UI mode
        return session_manager, ticket

    @staticmethod
    def close_connection(session_manager, ticket):
        """Close the QuickBooks connection."""
        session_manager.EndSession(ticket)
        session_manager.CloseConnection()

    @staticmethod
    def process_request(session_manager, ticket, request_xml):
        """Send qbXML request and get a response."""
        response = session_manager.ProcessRequest(ticket, request_xml)
        return response