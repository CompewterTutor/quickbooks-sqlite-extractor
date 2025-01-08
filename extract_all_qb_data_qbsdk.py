import win32com.client  # COM interface
import sqlite3
from lxml import etree
import argparse
import os


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
            <?qbxml version="13.0"?>
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
            <?qbxml version="13.0"?>
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


def main():
    parser = argparse.ArgumentParser(description="Export QuickBooks SDK data to SQLite", add_help=False)
    parser.add_argument('-raw', action='store_true', help='Export raw data as is.')
    parser.add_argument('-1nf', action='store_true', help='Export data in normalized first normal form.')
    parser.add_argument('-both', action='store_true', help='Export both raw and 1NF data into separate files.')
    parser.add_argument('-help', action='store_true', help='Show usage information.')
    args = parser.parse_args()

    if args.help:
        print("""
Usage: python export_qb_sdk_to_sqlite.py [OPTIONS]

Options:
  -raw         Export raw QuickBooks data as-is to a SQLite database.
  -1nf         Export QuickBooks data normalized to First Normal Form (1NF).
  -both        Export both raw and 1NF data into two separate SQLite databases.
  -help        Show this usage information.
        """)
        return

    session_manager, ticket = connect_to_quickbooks()

    if args.raw or args.both:
        conn = sqlite3.connect('quickbooks_raw_data.db')
        export_all_data(session_manager, ticket, conn, normalize=False)
        conn.close()

    if args._1nf or args.both:
        conn = sqlite3.connect('quickbooks_1nf_data.db')
        export_all_data(session_manager, ticket, conn, normalize=True)
        conn.close()

    close_connection(session_manager, ticket)


if __name__ == "__main__":
    main()
