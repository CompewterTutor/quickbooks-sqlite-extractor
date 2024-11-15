# Script to extract all data from QuickBooks via ODBC and store it in SQLite database
# 
# Author: Michael Morrissey
# Date: 2024-11-15
# Version: 0.1

# Import required libraries
import pyodbc
import sqlite3

# Connect to QuickBooks via ODBC
qb_conn = pyodbc.connect('DSN=QuickBooks Data;')

# List of tables to extract data from
tables = ['Customer', 'Vendor', 'Account', 'Transaction']

# Connect to SQLite
sqlite_conn = sqlite3.connect('quickbooks_data.db')
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
                             {', '.join(f'{col} TEXT' for col in columns)}
                             )"""
    cursor.execute(create_table_query)
    
    # Insert data into SQLite
    for row in data:
        placeholders = ', '.join(['?'] * len(row))
        cursor.execute(f"INSERT INTO {table} VALUES ({placeholders})", row)
    
    sqlite_conn.commit()
    qb_cursor.close()

# Close connections
qb_conn.close()
sqlite_conn.close()

print("Data export completed successfully.")
