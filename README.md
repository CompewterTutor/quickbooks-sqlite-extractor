# Quickbooks SQLite Extractor

## Installation
Install python and required libraries:
```
pip install pyodbc sqlite3
```
Setup Quickbooks ODBC Driver for easier integration:
* Download and install the QOBDC Driver for Quickbooks Desktop from (https://quodbc.com)[QODBC]
* Configure the driver to connect to your Quickbooks Company File



## Usage
```
Usage: python export_qb_to_sqlite.py [OPTIONS]

Options:
  -raw         Export raw QuickBooks data as-is to a SQLite database.
  -1nf         Export QuickBooks data normalized to First Normal Form (1NF).
  -both        Export both raw and 1NF data into two separate SQLite databases.
  -help        Show this usage information.
```

## Data Schema considerations
The table schema produced by the script above is not first normal form (1NF) by default. Here's why:

    Potential Repeated Groups:
        QuickBooks tables like Transaction might contain fields with multiple values (e.g., line items) in a single record.
    Unstructured Data:
        Some fields might store unstructured or semi-structured data, such as concatenated lists or JSON-like strings.

### Ensuring First Normal Form (1NF)

To make the schema conform to 1NF:

    No Repeating Groups or Arrays:
        Ensure that each column contains only atomic (indivisible) values.
    Unique Rows:
        Each row in the table must be unique, with a primary key.
    Single Valued Columns:
        Every column must contain a single value for a single row.

## Viewing the data
You can use any Sqlite database viewer to query the data that you export from Quickbooks.


## Troubleshooting

* DSN Not Found: Ensure that the ODBC Data Source is configured properly
* Quickbooks Errors: Make sure Quickbooks is running and the company file is open
* Permissions: Ensure the user has the necessary permissions in Quickbooks to read data

