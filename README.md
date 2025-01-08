# Quickbooks SQLite Extractor

# Using Quickbooks SDK

# QuickBooks SDK Data Export Script

This script exports all historical data from QuickBooks Desktop using the **QuickBooks SDK** and saves it into **SQLite databases**. It supports both **raw exports** and **normalized (1NF) exports**, providing flexibility for data analysis.

---

## Features

- **Read-Only Data Access**: Ensures no changes are made to the QuickBooks file.
- **Raw Data Export**: Exports data as-is for quick access and analysis.
- **Normalized Data Export (1NF)**: Splits complex data (e.g., transactions with line items) into separate tables for a normalized database structure.
- **Dual Export Option**: Exports both raw and normalized data into separate SQLite databases if desired.
- **Command-Line Interface**: Allows flexible usage through command-line options.

---

## Requirements

- QuickBooks Desktop installed.
- QuickBooks company file open during execution.
- **QuickBooks Desktop SDK** installed. Download it from [Intuit Developer](https://developer.intuit.com/).
- Python 3.x installed.
- Required Python Libraries:
  ```bash
  pip install pywin32 lxml
  ```

---

## Setup Instructions

1. Install **QuickBooks SDK** and configure **QBXMLRP2 Request Processor**.
2. Ensure QuickBooks is **running** and the **company file** is open.
3. Install Python dependencies:
   ```bash
   pip install pywin32 lxml
   ```
4. Save the script as `export_qb_sdk_to_sqlite.py`.

---

## Usage

### Command-Line Options

```
Usage: python export_qb_sdk_to_sqlite.py [OPTIONS]

Options:
  -raw         Export raw QuickBooks data as-is to a SQLite database.
  -1nf         Export QuickBooks data normalized to First Normal Form (1NF).
  -both        Export both raw and 1NF data into separate SQLite databases.
  -help        Show this usage information.
```

### Examples

- **Export Raw Data Only**:
  ```bash
  python export_qb_sdk_to_sqlite.py -raw
  ```
- **Export 1NF Normalized Data Only**:
  ```bash
  python export_qb_sdk_to_sqlite.py -1nf
  ```
- **Export Both Versions**:
  ```bash
  python export_qb_sdk_to_sqlite.py -both
  ```
- **View Help**:
  ```bash
  python export_qb_sdk_to_sqlite.py -help
  ```

---

## Outputs

- **Raw Data**: Stored in `quickbooks_raw_data.db`.
- **1NF Normalized Data**: Stored in `quickbooks_1nf_data.db`.

### Example Tables:

- **Raw Tables**: Customers, Vendors, Accounts, Transactions.
- **Normalized Tables**:
  - `Transactions`: Summary of transactions.
  - `TransactionLineItems`: Line items linked to transactions.

---

## Safety Notes

- **Read-Only Access**: The script uses read-only queries and cannot modify the QuickBooks file.
- **Permissions**: QuickBooks will prompt for access permissions during the first run—ensure to allow **read-only access**.
- **Testing**: Test the script with a **sample QuickBooks file** before using it on live data.

---

## Troubleshooting

1. **Connection Errors**:
   - Ensure QuickBooks is running and the company file is open.
   - Verify QuickBooks SDK and Request Processor are installed.
2. **Missing Data**:
   - Check QuickBooks permissions for the connected app.
   - Verify query filters in the script.
3. **Python Errors**:
   - Ensure dependencies (`pywin32` and `lxml`) are installed.
   - Run the script in a virtual environment if conflicts occur.

---

## License

This project is licensed under the **MIT License**.

---

## Contributions

Contributions and improvements are welcome! Feel free to submit a pull request.

---

## Support

For questions or assistance, contact [[your\_email@example.com](mailto\:your_email@example.com)].



# Using QBOBDC

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

