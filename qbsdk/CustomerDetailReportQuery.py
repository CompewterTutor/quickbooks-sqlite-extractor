from enum import Enum
from typing import List, Optional
from datetime import datetime
from lxml import etree
from sqlalchemy import create_engine, Column, String, Integer, DateTime
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker

Base = declarative_base()

class CustomDetailReportType(Enum):
    CUSTOM_TXN_DETAIL = "CustomTxnDetail"

class ReportDateMacro(Enum):
    ALL = "All"
    TODAY = "Today"
    THIS_WEEK = "ThisWeek"
    THIS_WEEK_TO_DATE = "ThisWeekToDate"
    THIS_MONTH = "ThisMonth"
    THIS_MONTH_TO_DATE = "ThisMonthToDate"
    THIS_QUARTER = "ThisQuarter"
    THIS_QUARTER_TO_DATE = "ThisQuarterToDate"
    THIS_YEAR = "ThisYear"
    THIS_YEAR_TO_DATE = "ThisYearToDate"
    YESTERDAY = "Yesterday"
    LAST_WEEK = "LastWeek"
    LAST_WEEK_TO_DATE = "LastWeekToDate"
    LAST_MONTH = "LastMonth"
    LAST_MONTH_TO_DATE = "LastMonthToDate"
    LAST_QUARTER = "LastQuarter"
    LAST_QUARTER_TO_DATE = "LastQuarterToDate"
    LAST_YEAR = "LastYear"
    LAST_YEAR_TO_DATE = "LastYearToDate"
    NEXT_WEEK = "NextWeek"
    NEXT_FOUR_WEEKS = "NextFourWeeks"
    NEXT_MONTH = "NextMonth"
    NEXT_QUARTER = "NextQuarter"
    NEXT_YEAR = "NextYear"

class AccountTypeFilter(Enum):
    ACCOUNTS_PAYABLE = "AccountsPayable"
    ACCOUNTS_RECEIVABLE = "AccountsReceivable"
    ALLOWED_FOR_1099 = "AllowedFor1099"
    AP_AND_SALES_TAX = "APAndSalesTax"
    AP_OR_CREDIT_CARD = "APOrCreditCard"
    AR_AND_AP = "ARAndAP"
    ASSET = "Asset"
    BALANCE_SHEET = "BalanceSheet"
    BANK = "Bank"
    BANK_AND_AR_AND_AP_AND_UF = "BankAndARAndAPAndUF"
    BANK_AND_UF = "BankAndUF"
    COST_OF_SALES = "CostOfSales"
    CREDIT_CARD = "CreditCard"
    CURRENT_ASSET = "CurrentAsset"
    CURRENT_ASSET_AND_EXPENSE = "CurrentAssetAndExpense"
    CURRENT_LIABILITY = "CurrentLiability"
    EQUITY = "Equity"
    EQUITY_AND_INCOME_AND_EXPENSE = "EquityAndIncomeAndExpense"
    EXPENSE_AND_OTHER_EXPENSE = "ExpenseAndOtherExpense"
    FIXED_ASSET = "FixedAsset"
    INCOME_AND_EXPENSE = "IncomeAndExpense"
    INCOME_AND_OTHER_INCOME = "IncomeAndOtherIncome"
    LIABILITY = "Liability"
    LIABILITY_AND_EQUITY = "LiabilityAndEquity"
    LONG_TERM_LIABILITY = "LongTermLiability"
    NON_POSTING = "NonPosting"
    ORDINARY_EXPENSE = "OrdinaryExpense"
    ORDINARY_INCOME = "OrdinaryIncome"
    ORDINARY_INCOME_AND_COGS = "OrdinaryIncomeAndCOGS"
    ORDINARY_INCOME_AND_EXPENSE = "OrdinaryIncomeAndExpense"
    OTHER_ASSET = "OtherAsset"
    OTHER_CURRENT_ASSET = "OtherCurrentAsset"
    OTHER_CURRENT_LIABILITY = "OtherCurrentLiability"
    OTHER_EXPENSE = "OtherExpense"
    OTHER_INCOME = "OtherIncome"
    OTHER_INCOME_OR_EXPENSE = "OtherIncomeOrExpense"

class EntityTypeFilter(Enum):
    CUSTOMER = "Customer"
    EMPLOYEE = "Employee"
    OTHER_NAME = "OtherName"
    VENDOR = "Vendor"

class ItemTypeFilter(Enum):
    ALL_EXCEPT_FIXED_ASSET = "AllExceptFixedAsset"
    ASSEMBLY = "Assembly"
    DISCOUNT = "Discount"
    FIXED_ASSET = "FixedAsset"
    INVENTORY = "Inventory"
    INVENTORY_AND_ASSEMBLY = "InventoryAndAssembly"
    NON_INVENTORY = "NonInventory"
    OTHER_CHARGE = "OtherCharge"
    PAYMENT = "Payment"
    SALES = "Sales"
    SALES_TAX = "SalesTax"
    SERVICE = "Service"

class TxnTypeFilter(Enum):
    ALL = "All"
    AR_REFUND_CREDIT_CARD = "ARRefundCreditCard"
    BILL = "Bill"
    BILL_PAYMENT_CHECK = "BillPaymentCheck"
    BILL_PAYMENT_CREDIT_CARD = "BillPaymentCreditCard"
    BUILD_ASSEMBLY = "BuildAssembly"
    CHARGE = "Charge"
    CHECK = "Check"
    CREDIT_CARD_CHARGE = "CreditCardCharge"
    CREDIT_CARD_CREDIT = "CreditCardCredit"
    CREDIT_MEMO = "CreditMemo"
    DEPOSIT = "Deposit"
    ESTIMATE = "Estimate"
    INVENTORY_ADJUSTMENT = "InventoryAdjustment"
    INVOICE = "Invoice"
    ITEM_RECEIPT = "ItemReceipt"
    JOURNAL_ENTRY = "JournalEntry"
    LIABILITY_ADJUSTMENT = "LiabilityAdjustment"
    PAYCHECK = "Paycheck"
    PAYROLL_LIABILITY_CHECK = "PayrollLiabilityCheck"
    PURCHASE_ORDER = "PurchaseOrder"
    RECEIVE_PAYMENT = "ReceivePayment"
    SALES_ORDER = "SalesOrder"
    SALES_RECEIPT = "SalesReceipt"
    SALES_TAX_PAYMENT_CHECK = "SalesTaxPaymentCheck"
    TRANSFER = "Transfer"
    VENDOR_CREDIT = "VendorCredit"
    YTD_ADJUSTMENT = "YTDAdjustment"

class ReportDetailLevelFilter(Enum):
    ALL = "All"
    ALL_EXCEPT_SUMMARY = "AllExceptSummary"
    SUMMARY_ONLY = "SummaryOnly"

class ReportPostingStatusFilter(Enum):
    EITHER = "Either"
    NON_POSTING = "NonPosting"
    POSTING = "Posting"

class SummarizeRowsBy(Enum):
    ACCOUNT = "Account"
    BALANCE_SHEET = "BalanceSheet"
    CLASS = "Class"
    CUSTOMER = "Customer"
    CUSTOMER_TYPE = "CustomerType"
    DAY = "Day"
    EMPLOYEE = "Employee"
    FOUR_WEEK = "FourWeek"
    HALF_MONTH = "HalfMonth"
    INCOME_STATEMENT = "IncomeStatement"
    ITEM_DETAIL = "ItemDetail"
    ITEM_TYPE = "ItemType"
    MONTH = "Month"
    PAYEE = "Payee"
    PAYMENT_METHOD = "PaymentMethod"
    PAYROLL_ITEM_DETAIL = "PayrollItemDetail"
    PAYROLL_YTD_DETAIL = "PayrollYtdDetail"
    QUARTER = "Quarter"
    SALES_REP = "SalesRep"
    SALES_TAX_CODE = "SalesTaxCode"
    SHIP_METHOD = "ShipMethod"
    TAX_LINE = "TaxLine"
    TERMS = "Terms"
    TOTAL_ONLY = "TotalOnly"
    TWO_WEEK = "TwoWeek"
    VENDOR = "Vendor"
    VENDOR_TYPE = "VendorType"
    WEEK = "Week"
    YEAR = "Year"

class IncludeColumn(Enum):
    ACCOUNT = "Account"
    AGING = "Aging"
    AMOUNT = "Amount"
    AMOUNT_DIFFERENCE = "AmountDifference"
    AVERAGE_COST = "AverageCost"
    BILLED_DATE = "BilledDate"
    BILLING_STATUS = "BillingStatus"
    CALCULATED_AMOUNT = "CalculatedAmount"
    CLASS = "Class"
    CLEARED_STATUS = "ClearedStatus"
    COST_PRICE = "CostPrice"
    CREDIT = "Credit"
    CURRENCY = "Currency"
    DATE = "Date"
    DEBIT = "Debit"
    DELIVERY_DATE = "DeliveryDate"
    DUE_DATE = "DueDate"
    ESTIMATE_ACTIVE = "EstimateActive"
    EXCHANGE_RATE = "ExchangeRate"
    FOB = "FOB"
    INCOME_SUBJECT_TO_TAX = "IncomeSubjectToTax"
    INVOICED = "Invoiced"
    ITEM = "Item"
    ITEM_DESC = "ItemDesc"
    LAST_MODIFIED_BY = "LastModifiedBy"
    LATEST_OR_PRIOR_STATE = "LatestOrPriorState"
    MEMO = "Memo"
    MODIFIED_TIME = "ModifiedTime"
    NAME = "Name"
    NAME_ACCOUNT_NUMBER = "NameAccountNumber"
    NAME_ADDRESS = "NameAddress"
    NAME_CITY = "NameCity"
    NAME_CONTACT = "NameContact"
    NAME_EMAIL = "NameEmail"
    NAME_FAX = "NameFax"
    NAME_PHONE = "NamePhone"
    NAME_STATE = "NameState"
    NAME_ZIP = "NameZip"
    OPEN_BALANCE = "OpenBalance"
    ORIGINAL_AMOUNT = "OriginalAmount"
    PAID_AMOUNT = "PaidAmount"
    PAID_STATUS = "PaidStatus"
    PAID_THROUGH_DATE = "PaidThroughDate"
    PAYMENT_METHOD = "PaymentMethod"
    PAYROLL_ITEM = "PayrollItem"
    PO_NUMBER = "PONumber"
    PRINT_STATUS = "PrintStatus"
    PROGRESS_AMOUNT = "ProgressAmount"
    PROGRESS_PERCENT = "ProgressPercent"
    QUANTITY = "Quantity"
    QUANTITY_AVAILABLE = "QuantityAvailable"
    QUANTITY_ON_HAND = "QuantityOnHand"
    QUANTITY_ON_SALES_ORDER = "QuantityOnSalesOrder"
    RECEIVED_QUANTITY = "ReceivedQuantity"
    REF_NUMBER = "RefNumber"
    RUNNING_BALANCE = "RunningBalance"
    SALES_REP = "SalesRep"
    SALES_TAX_CODE = "SalesTaxCode"
    SERIAL_OR_LOT_NUMBER = "SerialOrLotNumber"
    SHIP_DATE = "ShipDate"
    SHIP_METHOD = "ShipMethod"
    SOURCE_NAME = "SourceName"
    SPLIT_ACCOUNT = "SplitAccount"
    SSN_OR_TAX_ID = "SSNOrTaxID"
    TAX_LINE = "TaxLine"
    TAX_TABLE_VERSION = "TaxTableVersion"
    TERMS = "Terms"
    TXN_ID = "TxnID"
    TXN_NUMBER = "TxnNumber"
    TXN_TYPE = "TxnType"
    UNIT_PRICE = "UnitPrice"
    USER_EDIT = "UserEdit"
    VALUE_ON_HAND = "ValueOnHand"
    WAGE_BASE = "WageBase"
    WAGE_BASE_TIPS = "WageBaseTips"

class ReportBasis(Enum):
    ACCRUAL = "Accrual"
    CASH = "Cash"
    NONE = "None"

class CustomerDetailReportQueryRq:
    def __init__(self, custom_detail_report_type: CustomDetailReportType, display_report: Optional[bool] = None, from_report_date: Optional[datetime] = None,
                 to_report_date: Optional[datetime] = None, report_date_macro: Optional[ReportDateMacro] = None, account_type_filter: Optional[AccountTypeFilter] = None,
                 entity_type_filter: Optional[EntityTypeFilter] = None, item_type_filter: Optional[ItemTypeFilter] = None, txn_type_filter: Optional[TxnTypeFilter] = None,
                 report_detail_level_filter: Optional[ReportDetailLevelFilter] = None, report_posting_status_filter: Optional[ReportPostingStatusFilter] = None,
                 summarize_rows_by: Optional[SummarizeRowsBy] = None, include_column: Optional[List[IncludeColumn]] = None, include_accounts: Optional[str] = None,
                 report_open_balance_as_of: Optional[str] = None, report_basis: Optional[ReportBasis] = None):
        self.custom_detail_report_type = custom_detail_report_type
        self.display_report = display_report
        self.from_report_date = from_report_date
        self.to_report_date = to_report_date
        self.report_date_macro = report_date_macro
        self.account_type_filter = account_type_filter
        self.entity_type_filter = entity_type_filter
        self.item_type_filter = item_type_filter
        self.txn_type_filter = txn_type_filter
        self.report_detail_level_filter = report_detail_level_filter
        self.report_posting_status_filter = report_posting_status_filter
        self.summarize_rows_by = summarize_rows_by
        self.include_column = include_column
        self.include_accounts = include_accounts
        self.report_open_balance_as_of = report_open_balance_as_of
        self.report_basis = report_basis

    def to_xml(self) -> str:
        xml = f'''<?xml version="1.0" encoding="utf-8"?>
<?qbxml version="16.0"?>
<QBXML>
    <QBXMLMsgsRq onError="stopOnError">
        <CustomDetailReportQueryRq>
            <CustomDetailReportType>{self.custom_detail_report_type.value}</CustomDetailReportType>
        '''
        if self.display_report is not None:
            xml += f'<DisplayReport>{str(self.display_report).lower()}</DisplayReport>'
        if self.from_report_date:
            xml += f'<FromReportDate>{self.from_report_date.isoformat()}</FromReportDate>'
        if self.to_report_date:
            xml += f'<ToReportDate>{self.to_report_date.isoformat()}</ToReportDate>'
        if self.report_date_macro:
            xml += f'<ReportDateMacro>{self.report_date_macro.value}</ReportDateMacro>'
        if self.account_type_filter:
            xml += f'<AccountTypeFilter>{self.account_type_filter.value}</AccountTypeFilter>'
        if self.entity_type_filter:
            xml += f'<EntityTypeFilter>{self.entity_type_filter.value}</EntityTypeFilter>'
        if self.item_type_filter:
            xml += f'<ItemTypeFilter>{self.item_type_filter.value}</ItemTypeFilter>'
        if self.txn_type_filter:
            xml += f'<TxnTypeFilter>{self.txn_type_filter.value}</TxnTypeFilter>'
        if self.report_detail_level_filter:
            xml += f'<ReportDetailLevelFilter>{self.report_detail_level_filter.value}</ReportDetailLevelFilter>'
        if self.report_posting_status_filter:
            xml += f'<ReportPostingStatusFilter>{self.report_posting_status_filter.value}</ReportPostingStatusFilter>'
        if self.summarize_rows_by:
            xml += f'<SummarizeRowsBy>{self.summarize_rows_by.value}</SummarizeRowsBy>'
        if self.include_column:
            for column in self.include_column:
                xml += f'<IncludeColumn>{column.value}</IncludeColumn>'
        if self.include_accounts:
            xml += f'<IncludeAccounts>{self.include_accounts}</IncludeAccounts>'
        if self.report_open_balance_as_of:
            xml += f'<ReportOpenBalanceAsOf>{self.report_open_balance_as_of}</ReportOpenBalanceAsOf>'
        if self.report_basis:
            xml += f'<ReportBasis>{self.report_basis.value}</ReportBasis>'
        xml += '''
        </CustomDetailReportQueryRq>
    </QBXMLMsgsRq>
</QBXML>
        '''
        return xml

    def from_response_xml(self, response_xml: str):
        root = etree.fromstring(response_xml.encode('utf-8'))
        report_rets = root.findall('.//ReportRet')
        self.reports = [ReportRet.from_xml(etree.tostring(report_ret)) for report_ret in report_rets]
        self.reports = [report for report in self.reports if report is not None]

class ReportRet(Base):
    __tablename__ = 'ReportRet'

    id = Column(Integer, primary_key=True, autoincrement=True)
    report_title = Column(String)
    report_subtitle = Column(String)
    report_basis = Column(String)
    num_rows = Column(Integer)
    num_columns = Column(Integer)
    num_col_title_rows = Column(Integer)

    @staticmethod
    def from_xml(xml_str: str):
        root = etree.fromstring(xml_str)
        report_ret = root if root.tag == 'ReportRet' else root.find('.//ReportRet')
        if report_ret is None:
            return None

        def get_text(element, tag):
            child = element.find(tag)
            return child.text if child is not None else None

        return ReportRet(
            report_title=get_text(report_ret, 'ReportTitle'),
            report_subtitle=get_text(report_ret, 'ReportSubtitle'),
            report_basis=get_text(report_ret, 'ReportBasis'),
            num_rows=int(get_text(report_ret, 'NumRows')) if get_text(report_ret, 'NumRows') else None,
            num_columns=int(get_text(report_ret, 'NumColumns')) if get_text(report_ret, 'NumColumns') else None,
            num_col_title_rows=int(get_text(report_ret, 'NumColTitleRows')) if get_text(report_ret, 'NumColTitleRows') else None
        )

class CustomerDetailReportQueryRs:
    def __init__(self, status_code: int, status_severity: str, status_message: str, report_ret: Optional[List[ReportRet]] = None):
        self.status_code = status_code
        self.status_severity = status_severity
        self.status_message = status_message
        self.report_ret = report_ret

def create_report_table_if_not_exists(engine):
    Base.metadata.create_all(engine)

def generate_customer_detail_report_query_xml(query: CustomerDetailReportQueryRq) -> str:
    xml = f'''<?xml version="1.0" encoding="utf-8"?>
<?qbxml version="16.0"?>
<QBXML>
    <QBXMLMsgsRq onError="stopOnError">
        <CustomDetailReportQueryRq>
            <CustomDetailReportType>{query.custom_detail_report_type.value}</CustomDetailReportType>
        '''
    if query.display_report is not None:
        xml += f'<DisplayReport>{str(query.display_report).lower()}</DisplayReport>'
    if query.from_report_date:
        xml += f'<FromReportDate>{query.from_report_date.isoformat()}</FromReportDate>'
    if query.to_report_date:
        xml += f'<ToReportDate>{query.to_report_date.isoformat()}</ToReportDate>'
    if query.report_date_macro:
        xml += f'<ReportDateMacro>{query.report_date_macro.value}</ReportDateMacro>'
    if query.account_type_filter:
        xml += f'<AccountTypeFilter>{query.account_type_filter.value}</AccountTypeFilter>'
    if query.entity_type_filter:
        xml += f'<EntityTypeFilter>{query.entity_type_filter.value}</EntityTypeFilter>'
    if query.item_type_filter:
        xml += f'<ItemTypeFilter>{query.item_type_filter.value}</ItemTypeFilter>'
    if query.txn_type_filter:
        xml += f'<TxnTypeFilter>{query.txn_type_filter.value}</TxnTypeFilter>'
    if query.report_detail_level_filter:
        xml += f'<ReportDetailLevelFilter>{query.report_detail_level_filter.value}</ReportDetailLevelFilter>'
    if query.report_posting_status_filter:
        xml += f'<ReportPostingStatusFilter>{query.report_posting_status_filter.value}</ReportPostingStatusFilter>'
    if query.summarize_rows_by:
        xml += f'<SummarizeRowsBy>{query.summarize_rows_by.value}</SummarizeRowsBy>'
    if query.include_column:
        for column in query.include_column:
            xml += f'<IncludeColumn>{column.value}</IncludeColumn>'
    if query.include_accounts:
        xml += f'<IncludeAccounts>{query.include_accounts