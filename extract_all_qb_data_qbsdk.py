import sqlite3
from lxml import etree
import argparse
import os

import win32com.client  # COM interface

from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy import Column, Integer, String, ForeignKey, Float

from qbsdk.customerQuery import CustomerQueryRq, CustomerQueryRs, Base
from qbsdk.AccountQuery import AccountQueryRq, AccountQueryRs, Base as AccountBase
from qbsdk.BillQuery import BillQueryRq, BillQueryRs, Base as BillBase
from qbsdk.CheckQuery import CheckQueryRq, CheckQueryRs, Base as CheckBase
from qbsdk.ClassQuery import ClassQueryRq, ClassQueryRs, Base as ClassBase
from qbsdk.CompanyQuery import CompanyQueryRq, CompanyQueryRs, Base as CompanyBase
from qbsdk.CreditCardChargeQuery import CreditCardChargeQueryRq, CreditCardChargeQueryRs, Base as CreditCardChargeBase
from qbsdk.CreditCardCreditQuery import CreditCardCreditQueryRq, CreditCardCreditQueryRs, Base as CreditCardCreditBase
from qbsdk.CompanyActivityQuery import CompanyActivityQueryRq, CompanyActivityQueryRs, Base as CompanyActivityBase
from qbsdk.CurrencyQuery import CurrencyQueryRq, CurrencyQueryRs, Base as CurrencyBase
from qbsdk.CustomerMsgQuery import CustomerMsgQueryRq, CustomerMsgQueryRs, Base as CustomerMsgBase
from qbsdk.CustomerTypeQuery import CustomerTypeQueryRq, CustomerTypeQueryRs, Base as CustomerTypeBase
from qbsdk.DepositQuery import DepositQueryRq, DepositQueryRs, Base as DepositBase
from qbsdk.EmployeeQuery import EmployeeQueryRq, EmployeeQueryRs, Base as EmployeeBase
from qbsdk.EntityQuery import EntityQueryRq, EntityQueryRs, Base as EntityBase


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



def test_customer_object():
    customerQuery = CustomerQueryRq()
    #customerQuery.max_returned = 5
    customerQuery.owner_id = 0
    print("Requesting Customer: \n", customerQuery.to_xml())
    # Connect to quickbooks and send xml
    session_manager, ticket = connect_to_quickbooks()
    response = query_quickbooks(session_manager, ticket, customerQuery.to_xml())
    print(response)
    debug_engine = create_engine('sqlite:///debug.db', echo=True)
    customerQuery.from_response_xml(response)
    print("Customer Objects: \n", customerQuery.customers)
    Base.metadata.create_all(debug_engine)

    DebugSession = sessionmaker(bind=debug_engine)
    debug_session = DebugSession()
    for customer in customerQuery.customers:
        debug_session.add(customer)
    debug_session.commit()
    debug_session.close()
    close_connection(session_manager, ticket)


def test_account_object():
    accountQuery = AccountQueryRq()
    print("Requesting Account: \n", accountQuery.to_xml())
    # Connect to quickbooks and send xml
    session_manager, ticket = connect_to_quickbooks()
    response = query_quickbooks(session_manager, ticket, accountQuery.to_xml())
    print(response)
    debug_engine = create_engine('sqlite:///debug.db', echo=True)
    accountQuery.from_response_xml(response)
    print("Account Objects: \n", accountQuery.accounts)
    AccountBase.metadata.create_all(debug_engine)

    DebugSession = sessionmaker(bind=debug_engine)
    debug_session = DebugSession()
    for account in accountQuery.accounts:
        debug_session.add(account)
    debug_session.commit()
    debug_session.close()
    close_connection(session_manager, ticket)


def test_bill_object():
    billQuery = BillQueryRq()
    print("Requesting Bill: \n", billQuery.to_xml())
    # Connect to quickbooks and send xml
    session_manager, ticket = connect_to_quickbooks()
    response = query_quickbooks(session_manager, ticket, billQuery.to_xml())
    print(response)
    debug_engine = create_engine('sqlite:///debug.db', echo=True)
    billQuery.from_response_xml(response)
    print("Bill Objects: \n", billQuery.bills)
    BillBase.metadata.create_all(debug_engine)

    DebugSession = sessionmaker(bind=debug_engine)
    debug_session = DebugSession()
    for bill in billQuery.bills:
        debug_session.add(bill)
    debug_session.commit()
    debug_session.close()
    close_connection(session_manager, ticket)


def test_check_object():
    checkQuery = CheckQueryRq()
    print("Requesting Check: \n", checkQuery.to_xml())
    # Connect to quickbooks and send xml
    session_manager, ticket = connect_to_quickbooks()
    response = query_quickbooks(session_manager, ticket, checkQuery.to_xml())
    print(response)
    debug_engine = create_engine('sqlite:///debug.db', echo=True)
    checkQuery.from_response_xml(response)
    print("Check Objects: \n", checkQuery.checks)
    CheckBase.metadata.create_all(debug_engine)

    DebugSession = sessionmaker(bind=debug_engine)
    debug_session = DebugSession()
    for check in checkQuery.checks:
        debug_session.add(check)
    debug_session.commit()
    debug_session.close()
    close_connection(session_manager, ticket)


def test_class_object():
    classQuery = ClassQueryRq()
    print("Requesting Class: \n", classQuery.to_xml())
    # Connect to quickbooks and send xml
    session_manager, ticket = connect_to_quickbooks()
    response = query_quickbooks(session_manager, ticket, classQuery.to_xml())
    print(response)
    debug_engine = create_engine('sqlite:///debug.db', echo=True)
    classQuery.from_response_xml(response)
    print("Class Objects: \n", classQuery.classes)
    ClassBase.metadata.create_all(debug_engine)

    DebugSession = sessionmaker(bind=debug_engine)
    debug_session = DebugSession()
    for cls in classQuery.classes:
        debug_session.add(cls)
    debug_session.commit()
    debug_session.close()
    close_connection(session_manager, ticket)


def test_company_object():
    companyQuery = CompanyQueryRq()
    print("Requesting Company: \n", companyQuery.to_xml())
    # Connect to quickbooks and send xml
    session_manager, ticket = connect_to_quickbooks()
    response = query_quickbooks(session_manager, ticket, companyQuery.to_xml())
    print(response)
    debug_engine = create_engine('sqlite:///debug.db', echo=True)
    companyQuery.from_response_xml(response)
    print("Company Objects: \n", companyQuery.companies)
    CompanyBase.metadata.create_all(debug_engine)

    DebugSession = sessionmaker(bind=debug_engine)
    debug_session = DebugSession()
    for company in companyQuery.companies:
        debug_session.add(company)
    debug_session.commit()
    debug_session.close()
    close_connection(session_manager, ticket)


def test_cc_charge_object():
    ccChargeQuery = CreditCardChargeQueryRq()
    print("Requesting Credit Card Charge: \n", ccChargeQuery.to_xml())
    # Connect to quickbooks and send xml
    session_manager, ticket = connect_to_quickbooks()
    response = query_quickbooks(session_manager, ticket, ccChargeQuery.to_xml())
    print(response)
    debug_engine = create_engine('sqlite:///debug.db', echo=True)
    ccChargeQuery.from_response_xml(response)
    print("Credit Card Charge Objects: \n", ccChargeQuery.cc_charges)
    CreditCardChargeBase.metadata.create_all(debug_engine)

    DebugSession = sessionmaker(bind=debug_engine)
    debug_session = DebugSession()
    for cc_charge in ccChargeQuery.cc_charges:
        debug_session.add(cc_charge)
    debug_session.commit()
    debug_session.close()
    close_connection(session_manager, ticket)


def test_cc_credit_object():
    ccCreditQuery = CreditCardCreditQueryRq()
    print("Requesting Credit Card Credit: \n", ccCreditQuery.to_xml())
    # Connect to quickbooks and send xml
    session_manager, ticket = connect_to_quickbooks()
    response = query_quickbooks(session_manager, ticket, ccCreditQuery.to_xml())
    print(response)
    debug_engine = create_engine('sqlite:///debug.db', echo=True)
    ccCreditQuery.from_response_xml(response)
    print("Credit Card Credit Objects: \n", ccCreditQuery.cc_credits)
    CreditCardCreditBase.metadata.create_all(debug_engine)

    DebugSession = sessionmaker(bind=debug_engine)
    debug_session = DebugSession()
    for cc_credit in ccCreditQuery.cc_credits:
        debug_session.add(cc_credit)
    debug_session.commit()
    debug_session.close()
    close_connection(session_manager, ticket)


def test_company_activity_object():
    companyActivityQuery = CompanyActivityQueryRq()
    print("Requesting Company Activity: \n", companyActivityQuery.to_xml())
    # Connect to quickbooks and send xml
    session_manager, ticket = connect_to_quickbooks()
    response = query_quickbooks(session_manager, ticket, companyActivityQuery.to_xml())
    print(response)
    debug_engine = create_engine('sqlite:///debug.db', echo=True)
    companyActivityQuery.from_response_xml(response)
    print("Company Activity Objects: \n", companyActivityQuery.company_activities)
    CompanyActivityBase.metadata.create_all(debug_engine)

    DebugSession = sessionmaker(bind=debug_engine)
    debug_session = DebugSession()
    for activity in companyActivityQuery.company_activities:
        debug_session.add(activity)
    debug_session.commit()
    debug_session.close()
    close_connection(session_manager, ticket)


def test_currency_object():
    currencyQuery = CurrencyQueryRq()
    print("Requesting Currency: \n", currencyQuery.to_xml())
    # Connect to quickbooks and send xml
    session_manager, ticket = connect_to_quickbooks()
    response = query_quickbooks(session_manager, ticket, currencyQuery.to_xml())
    print(response)
    debug_engine = create_engine('sqlite:///debug.db', echo=True)
    currencyQuery.from_response_xml(response)
    print("Currency Objects: \n", currencyQuery.currencies)
    CurrencyBase.metadata.create_all(debug_engine)

    DebugSession = sessionmaker(bind=debug_engine)
    debug_session = DebugSession()
    for currency in currencyQuery.currencies:
        debug_session.add(currency)
    debug_session.commit()
    debug_session.close()
    close_connection(session_manager, ticket)


def export_table_raw(session_manager, ticket, table_name, query_xml, sqlite_conn):
    """Export raw data from QuickBooks."""
    response = query_quickbooks(session_manager, ticket, query_xml)
    root = etree.fromstring(response.encode('utf-8'))
    records = root.xpath(f"//{table_name}Ret")

    if not records:
        print(f"No data found for {table_name}.")
        return

    # Create table in SQLite
    cursor = sqlite_conn.cursor()
    columns = [elem.tag for elem in records[0]]
    create_table_query = f"""CREATE TABLE IF NOT EXISTS {table_name} (
                             id INTEGER PRIMARY KEY AUTOINCREMENT,
                             {', '.join(f'{col} TEXT' for col in columns)}
                             )"""
    cursor.execute(create_table_query)

    # Insert data into SQLite
    for record in records:
        values = [record.find(col).text if record.find(col) is not None else None for col in columns]
        placeholders = ', '.join(['?'] * len(values))
        cursor.execute(f"INSERT INTO {table_name} VALUES (NULL, {placeholders})", values)

    sqlite_conn.commit()


def normalize_transactions(session_manager, ticket, sqlite_conn):
    """Normalize transactions and split into multiple tables."""
    # Query Transactions
    query = """<?xml version="1.0" ?>
    <?qbxml version="13.0"?>
    <QBXML>
        <QBXMLMsgsRq onError="stopOnError">
            <TxnQueryRq>
                <IncludeLineItems>true</IncludeLineItems>
            </TxnQueryRq>
        </QBXMLMsgsRq>
    </QBXML>"""
    response = query_quickbooks(session_manager, ticket, query)
    root = etree.fromstring(response.encode('utf-8'))
    transactions = root.xpath("//TxnRet")

    # Create normalized tables
    cursor = sqlite_conn.cursor()
    cursor.execute("""
        CREATE TABLE IF NOT EXISTS Transactions (
            TxnID TEXT PRIMARY KEY,
            TxnType TEXT,
            TxnDate TEXT,
            TotalAmount TEXT
        )
    """)
    cursor.execute("""
        CREATE TABLE IF NOT EXISTS TransactionLineItems (
            LineItemID INTEGER PRIMARY KEY AUTOINCREMENT,
            TxnID TEXT,
            ItemName TEXT,
            Quantity TEXT,
            Rate TEXT,
            Amount TEXT,
            FOREIGN KEY (TxnID) REFERENCES Transactions(TxnID)
        )
    """)

    # Insert data
    for txn in transactions:
        txn_id = txn.find("TxnID").text
        txn_type = txn.find("TxnType").text if txn.find("TxnType") is not None else None
        txn_date = txn.find("TxnDate").text if txn.find("TxnDate") is not None else None
        total_amount = txn.find("TotalAmount").text if txn.find("TotalAmount") is not None else None

        cursor.execute("""
            INSERT OR IGNORE INTO Transactions (TxnID, TxnType, TxnDate, TotalAmount)
            VALUES (?, ?, ?, ?)
        """, (txn_id, txn_type, txn_date, total_amount))

        # Process line items
        for line in txn.xpath(".//InvoiceLineRet"):
            item_name = line.find("ItemRef/FullName").text if line.find("ItemRef/FullName") is not None else None
            quantity = line.find("Quantity").text if line.find("Quantity") is not None else None
            rate = line.find("Rate").text if line.find("Rate") is not None else None
            amount = line.find("Amount").text if line.find("Amount") is not None else None

            cursor.execute("""
                INSERT INTO TransactionLineItems (TxnID, ItemName, Quantity, Rate, Amount)
                VALUES (?, ?, ?, ?, ?)
            """, (txn_id, item_name, quantity, rate, amount))

    sqlite_conn.commit()


def export_all_data(session_manager, ticket, sqlite_conn, normalize=False):
    """Export all data from QuickBooks, either raw or normalized."""
    # List of tables and queries
    queries = {
        "Customer": """
            <?xml version="1.0" ?>
            <?qbxml version="16.0"?>
            <QBXML>
                <QBXMLMsgsRq onError="stopOnError">
                    <CustomerQueryRq>
                        <OwnerID>0</OwnerID>
                    </CustomerQueryRq>
                </QBXMLMsgsRq>
            </QBXML>
        """,
        "Vendor": """
            <?xml version="1.0" ?>
            <?qbxml version="16.0"?>
            <QBXML>
                <QBXMLMsgsRq onError="stopOnError">
                    <VendorQueryRq>
                        <OwnerID>0</OwnerID>
                    </VendorQueryRq>
                </QBXMLMsgsRq>
            </QBXML>
        """
    }

    for table, query in queries.items():
        export_table_raw(session_manager, ticket, table, query, sqlite_conn)

    # Normalize transactions if requested
    if normalize:
        normalize_transactions(session_manager, ticket, sqlite_conn)


def test_connection():
    """Test connection to QuickBooks."""
    try:
        session_manager, ticket = connect_to_quickbooks()
        close_connection(session_manager, ticket)
        print("Connection to QuickBooks successful.")
    except Exception as e:
        print(f"Failed to connect to QuickBooks: {e}")

def test_quickbooks_query():
    """Test QuickBooks query."""
    session_manager, ticket = connect_to_quickbooks()
    query = """<?xml version="1.0" ?>
    <?qbxml version="16.0"?>
    <QBXML>
        <QBXMLMsgsRq onError="stopOnError">
            <CustomerQueryRq>
                <MaxReturned>5</MaxReturned>
                <OwnerID>0</OwnerID>
            </CustomerQueryRq>
        </QBXMLMsgsRq>
    </QBXML>"""
    response = query_quickbooks(session_manager, ticket, query)
    print(response)
    close_connection(session_manager, ticket)


def test_customer_msg_object():
    customerMsgQuery = CustomerMsgQueryRq()
    print("Requesting Customer Message: \n", customerMsgQuery.to_xml())
    # Connect to quickbooks and send xml
    session_manager, ticket = connect_to_quickbooks()
    response = query_quickbooks(session_manager, ticket, customerMsgQuery.to_xml())
    print(response)
    debug_engine = create_engine('sqlite:///debug.db', echo=True)
    customerMsgQuery.from_response_xml(response)
    print("Customer Message Objects: \n", customerMsgQuery.customer_msgs)
    CustomerMsgBase.metadata.create_all(debug_engine)

    DebugSession = sessionmaker(bind=debug_engine)
    debug_session = DebugSession()
    for msg in customerMsgQuery.customer_msgs:
        debug_session.add(msg)
    debug_session.commit()
    debug_session.close()
    close_connection(session_manager, ticket)


def test_customer_type_object():
    customerTypeQuery = CustomerTypeQueryRq()
    print("Requesting Customer Type: \n", customerTypeQuery.to_xml())
    # Connect to quickbooks and send xml
    session_manager, ticket = connect_to_quickbooks()
    response = query_quickbooks(session_manager, ticket, customerTypeQuery.to_xml())
    print(response)
    debug_engine = create_engine('sqlite:///debug.db', echo=True)
    customerTypeQuery.from_response_xml(response)
    print("Customer Type Objects: \n", customerTypeQuery.customer_types)
    CustomerTypeBase.metadata.create_all(debug_engine)

    DebugSession = sessionmaker(bind=debug_engine)
    debug_session = DebugSession()
    for customer_type in customerTypeQuery.customer_types:
        debug_session.add(customer_type)
    debug_session.commit()
    debug_session.close()
    close_connection(session_manager, ticket)


def test_deposit_object():
    depositQuery = DepositQueryRq()
    print("Requesting Deposit: \n", depositQuery.to_xml())
    # Connect to quickbooks and send xml
    session_manager, ticket = connect_to_quickbooks()
    response = query_quickbooks(session_manager, ticket, depositQuery.to_xml())
    print(response)
    debug_engine = create_engine('sqlite:///debug.db', echo=True)
    depositQuery.from_response_xml(response)
    print("Deposit Objects: \n", depositQuery.deposits)
    DepositBase.metadata.create_all(debug_engine)

    DebugSession = sessionmaker(bind=debug_engine)
    debug_session = DebugSession()
    for deposit in depositQuery.deposits:
        debug_session.add(deposit)
    debug_session.commit()
    debug_session.close()
    close_connection(session_manager, ticket)


def test_employee_object():
    employeeQuery = EmployeeQueryRq()
    print("Requesting Employee: \n", employeeQuery.to_xml())
    # Connect to quickbooks and send xml
    session_manager, ticket = connect_to_quickbooks()
    response = query_quickbooks(session_manager, ticket, employeeQuery.to_xml())
    print(response)
    debug_engine = create_engine('sqlite:///debug.db', echo=True)
    employeeQuery.from_response_xml(response)
    print("Employee Objects: \n", employeeQuery.employees)
    EmployeeBase.metadata.create_all(debug_engine)

    DebugSession = sessionmaker(bind=debug_engine)
    debug_session = DebugSession()
    for employee in employeeQuery.employees:
        debug_session.add(employee)
    debug_session.commit()
    debug_session.close()
    close_connection(session_manager, ticket)


def test_entity_object():
    entityQuery = EntityQueryRq()
    print("Requesting Entity: \n", entityQuery.to_xml())
    # Connect to quickbooks and send xml
    session_manager, ticket = connect_to_quickbooks()
    response = query_quickbooks(session_manager, ticket, entityQuery.to_xml())
    print(response)
    debug_engine = create_engine('sqlite:///debug.db', echo=True)
    entityQuery.from_response_xml(response)
    print("Entity Objects: \n", entityQuery.entities)
    EntityBase.metadata.create_all(debug_engine)

    DebugSession = sessionmaker(bind=debug_engine)
    debug_session = DebugSession()
    for entity in entityQuery.entities:
        debug_session.add(entity)
    debug_session.commit()
    debug_session.close()
    close_connection(session_manager, ticket)


def main():
    parser = argparse.ArgumentParser(description="Export QuickBooks SDK data to SQLite", add_help=False)
    parser.add_argument('-raw', action='store_true', help='Export raw data as is.')
    parser.add_argument('-nf', action='store_true', help='Export data in normalized first normal form.')
    parser.add_argument('-both', action='store_true', help='Export both raw and 1NF data into separate files.')
    parser.add_argument('-testconn', action='store_true', help='Test connection to QuickBooks.')
    parser.add_argument('-help', action='store_true', help='Show usage information.')
    parser.add_argument('-testquery', action='store_true', help='Test QuickBooks query.')
    parser.add_argument('-testcustomer', action='store_true', help='Test Customer object.')
    parser.add_argument('-testaccount', action='store_true', help='Test Account object.')
    parser.add_argument('-testbill', action='store_true', help='Test Bill object.')
    parser.add_argument('-testcheck', action='store_true', help='Test Check object.')
    parser.add_argument('-testclass', action='store_true', help='Test Class object.')
    parser.add_argument('-testcompany', action='store_true', help='Test Company object.')
    parser.add_argument('-testcccharge', action='store_true', help='Test Credit Card Charge object.')
    parser.add_argument('-testcccredit', action='store_true', help='Test Credit Card Credit object.')
    parser.add_argument('-testcoactivity', action='store_true', help='Test Company Activity object.')
    parser.add_argument('-testcurrency', action='store_true', help='Test Currency object.')
    parser.add_argument('-testcustmsg', action='store_true', help='Test Customer Message object.')
    parser.add_argument('-testcusttype', action='store_true', help='Test Customer Type object.')
    parser.add_argument('-testdeposit', action='store_true', help='Test Deposit object.')
    parser.add_argument('-testemployee', action='store_true', help='Test Employee object.')
    parser.add_argument('-testentity', action='store_true', help='Test Entity object.')
    args = parser.parse_args()

    if args.help:
        print("""
Usage: python export_qb_sdk_to_sqlite.py [OPTIONS]

Options:
  -raw         Export raw QuickBooks data as-is to a SQLite database.
  -nf         Export QuickBooks data normalized to First Normal Form (1NF).
  -both        Export both raw and 1NF data into two separate SQLite databases.
  -testconn    Test connection to QuickBooks.
  -help        Show this usage information.
  -testquery   Test QuickBooks query.
  -testcustomer Test Customer object.
  -testaccount Test Account object.
  -testbill    Test Bill object.
  -testcheck   Test Check object.
  -testclass   Test Class object.
  -testcompany Test Company object.
  -testcccharge Test Credit Card Charge object.
  -testcccredit Test Credit Card Credit object.
  -testcoactivity Test Company Activity object.
  -testcurrency Test Currency object.
  -testcustmsg Test Customer Message object.
  -testcusttype Test Customer Type object.
  -testdeposit Test Deposit object.
  -testemployee Test Employee object.
  -testentity Test Entity object.
        """)
        return

    if args.testconn:
        test_connection()
        return

    if args.testcustomer:
        test_customer_object()
        return

    if args.testaccount:
        test_account_object()
        return

    if args.testbill:
        test_bill_object()
        return

    if args.testcheck:
        test_check_object()
        return

    if args.testclass:
        test_class_object()
        return

    if args.testcompany:
        test_company_object()
        return

    if args.testcccharge:
        test_cc_charge_object()
        return

    if args.testcccredit:
        test_cc_credit_object()
        return

    if args.testcoactivity:
        test_company_activity_object()
        return

    if args.testcurrency:
        test_currency_object()
        return

    if args.testcustmsg:
        test_customer_msg_object()
        return

    if args.testcusttype:
        test_customer_type_object()
        return

    if args.testdeposit:
        test_deposit_object()
        return

    if args.testemployee:
        test_employee_object()
        return

    if args.testentity:
        test_entity_object()
        return

    session_manager, ticket = connect_to_quickbooks()

    if args.raw or args.both:
        conn = sqlite3.connect('quickbooks_raw_data.db')
        export_all_data(session_manager, ticket, conn, normalize=False)
        conn.close()

    if args.nf or args.both:
        conn = sqlite3.connect('quickbooks_1nf_data.db')
        export_all_data(session_manager, ticket, conn, normalize=True)
        conn.close()
    if args.testquery:
        test_quickbooks_query()

    close_connection(session_manager, ticket)


if __name__ == "__main__":
    main()