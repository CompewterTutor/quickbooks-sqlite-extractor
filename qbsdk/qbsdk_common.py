import sqlite3
from lxml import etree
import argparse
import os

import win32com.client  # COM interface


def connect_to_quickbooks():
    """Establish a connection to QuickBooks."""
    session_manager = win32com.client.Dispatch("QBXMLRP2.RequestProcessor")
    session_manager.OpenConnection("", "QuickBooks Data Export")
    ticket = session_manager.BeginSession("", 2)  # 2 = No UI mode
    return session_manager, ticket


def close_connection(session_manager, ticket):
    """Close the QuickBooks connection."""
    session_manager.EndSession(ticket)
    session_manager.CloseConnection()


def query_quickbooks(session_manager, ticket, request_xml):
    """Send qbXML request and get a response."""
    response = session_manager.ProcessRequest(ticket, request_xml)
    return response

