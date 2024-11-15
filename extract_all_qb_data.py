# Script to extract all data from QuickBooks via ODBC and store it in SQLite database
# 
# Author: Michael Morrissey
# Date: 2024-11-15
# Version: 0.1

# Import required libraries
import pyodbc
import sqlite3
import argparse
import os

def export_raw_data(qb_conn, sqlite_conn, tables):
    cursor = sqlite_conn.cursor()
    for table in tables:
        # Fetch data from QuickBooks
        query = f"SELECT * FROM {table}"
        qb_cursor = qb_conn.cursor()
        qb_cursor.execute(query)

        # Fetch column names and data
        columns = [column[0] for column in qb_cursor.description]
        data = qb_cursor.fetchall()

        # Create table in SQLite
        create_table_query = f"""CREATE TABLE IF NOT EXISTS {table} (
                                 id INTEGER PRIMARY KEY AUTOINCREMENT,
                                 {', '.join(f'{col} TEXT' for col in columns)}
                                 )"""
        cursor.execute(create_table_query)

        # Insert data into SQLite
        for row in data:
            placeholders = ', '.join(['?'] * len(row))
            cursor.execute(f"INSERT INTO {table} ({', '.join(columns)}) VALUES ({placeholders})", row)

        sqlite_conn.commit()
        qb_cursor.close()

def normalize_to_1nf(qb_conn, sqlite_conn):
    cursor = sqlite_conn.cursor()

    # Normalize Customer Table (Example)
    query = "SELECT CustomerID, Name, ContactInfo FROM Customer"
    qb_cursor = qb_conn.cursor()
    qb_cursor.execute(query)
    columns = [column[0] for column in qb_cursor.description]

    create_table_query = """CREATE TABLE IF NOT EXISTS Customers (
                            CustomerID INTEGER PRIMARY KEY,
                            Name TEXT,
                            ContactInfo TEXT
                            )"""
    cursor.execute(create_table_query)

    data = qb_cursor.fetchall()
    for row in data:
        placeholders = ', '.join(['?'] * len(row))
        cursor.execute(f"INSERT INTO Customers ({', '.join(columns)}) VALUES ({placeholders})", row)

    sqlite_conn.commit()
    qb_cursor.close()

def main():
    parser = argparse.ArgumentParser(description="Export QuickBooks data to SQLite", add_help=False)
    parser.add_argument('-raw', action='store_true', help='Export raw data as is.')
    parser.add_argument('-1nf', action='store_true', help='Export data in normalized first normal form.')
    parser.add_argument('-both', action='store_true', help='Export both raw and 1NF data into separate files.')
    parser.add_argument('-help', action='store_true', help='Show usage information.')

    args = parser.parse_args()

    if args.help:
        print("""
Usage: python export_qb_to_sqlite.py [OPTIONS]

Options:
  -raw         Export raw QuickBooks data as-is to a SQLite database.
  -1nf         Export QuickBooks data normalized to First Normal Form (1NF).
  -both        Export both raw and 1NF data into two separate SQLite databases.
  -help        Show this usage information.
        """)
        return

    qb_conn = pyodbc.connect('DSN=QuickBooks Data;')

    if args.both or args.raw:
        raw_db = 'quickbooks_raw_data.db'
        if os.path.exists(raw_db):
            os.remove(raw_db)
        raw_conn = sqlite3.connect(raw_db)
        tables = ['Customer', 'Vendor', 'Account', 'Transaction']  # Adjust for actual tables
        export_raw_data(qb_conn, raw_conn, tables)
        raw_conn.close()
        print(f"Raw data exported to {raw_db}")

    if args.both or args._1nf:
        normalized_db = 'quickbooks_1nf_data.db'
        if os.path.exists(normalized_db):
            os.remove(normalized_db)
        nf_conn = sqlite3.connect(normalized_db)
        normalize_to_1nf(qb_conn, nf_conn)
        nf_conn.close()
        print(f"1NF data exported to {normalized_db}")

    qb_conn.close()

if __name__ == "__main__":
    main()
