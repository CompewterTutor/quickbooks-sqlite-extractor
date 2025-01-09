from enum import Enum
from typing import List, Optional
from datetime import datetime
from lxml import etree
from sqlalchemy import create_engine, Column, String, DateTime, Float, Integer
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker

Base = declarative_base()

class MatchCriterion(Enum):
    STARTS_WITH = "StartsWith"
    CONTAINS = "Contains"
    ENDS_WITH = "EndsWith"

class ActiveStatus(Enum):
    ACTIVE_ONLY = "ActiveOnly"
    INACTIVE_ONLY = "InactiveOnly"
    ALL = "All"

class DateMacro(Enum):
    ALL = "All"
    TODAY = "Today"
    THIS_WEEK = "ThisWeek"
    THIS_WEEK_TO_DATE = "ThisWeekToDate"
    THIS_MONTH = "ThisMonth"
    THIS_MONTH_TO_DATE = "ThisMonthToDate"
    THIS_CALENDAR_QUARTER = "ThisCalendarQuarter"
    THIS_CALENDAR_QUARTER_TO_DATE = "ThisCalendarQuarterToDate"
    THIS_FISCAL_QUARTER = "ThisFiscalQuarter"
    THIS_FISCAL_QUARTER_TO_DATE = "ThisFiscalQuarterToDate"
    THIS_CALENDAR_YEAR = "ThisCalendarYear"
    THIS_CALENDAR_YEAR_TO_DATE = "ThisCalendarYearToDate"
    THIS_FISCAL_YEAR = "ThisFiscalYear"
    THIS_FISCAL_YEAR_TO_DATE = "ThisFiscalYearToDate"
    YESTERDAY = "Yesterday"
    LAST_WEEK = "LastWeek"
    LAST_WEEK_TO_DATE = "LastWeekToDate"
    LAST_MONTH = "LastMonth"
    LAST_MONTH_TO_DATE = "LastMonthToDate"
    LAST_CALENDAR_QUARTER = "LastCalendarQuarter"
    LAST_CALENDAR_QUARTER_TO_DATE = "LastCalendarQuarterToDate"
    LAST_FISCAL_QUARTER = "LastFiscalQuarter"
    LAST_FISCAL_QUARTER_TO_DATE = "LastFiscalQuarterToDate"
    LAST_CALENDAR_YEAR = "LastCalendarYear"
    LAST_CALENDAR_YEAR_TO_DATE = "LastCalendarYearToDate"
    LAST_FISCAL_YEAR = "LastFiscalYear"
    LAST_FISCAL_YEAR_TO_DATE = "LastFiscalYearToDate"
    NEXT_WEEK = "NextWeek"
    NEXT_FOUR_WEEKS = "NextFourWeeks"
    NEXT_MONTH = "NextMonth"
    NEXT_CALENDAR_QUARTER = "NextCalendarQuarter"
    NEXT_CALENDAR_YEAR = "NextCalendarYear"
    NEXT_FISCAL_QUARTER = "NextFiscalQuarter"
    NEXT_FISCAL_YEAR = "NextFiscalYear"

class DepositQueryRq:
    def __init__(self, txn_id: Optional[List[str]] = None, max_returned: Optional[int] = None, from_modified_date: Optional[datetime] = None,
                 to_modified_date: Optional[datetime] = None, from_txn_date: Optional[datetime] = None, to_txn_date: Optional[datetime] = None,
                 date_macro: Optional[DateMacro] = None, include_line_items: Optional[bool] = None, include_ret_element: Optional[List[str]] = None,
                 owner_id: Optional[List[str]] = None):
        self.txn_id = txn_id
        self.max_returned = max_returned
        self.from_modified_date = from_modified_date
        self.to_modified_date = to_modified_date
        self.from_txn_date = from_txn_date
        self.to_txn_date = to_txn_date
        self.date_macro = date_macro
        self.include_line_items = include_line_items
        self.include_ret_element = include_ret_element
        self.owner_id = owner_id

    def to_xml(self) -> str:
        xml = f'''<?xml version="1.0" encoding="utf-8"?>
<?qbxml version="16.0"?>
<QBXML>
    <QBXMLMsgsRq onError="stopOnError">
        <DepositQueryRq>
    '''
        if self.txn_id:
            for txn_id in self.txn_id:
                xml += f'<TxnID>{txn_id}</TxnID>'
        if self.max_returned:
            xml += f'<MaxReturned>{self.max_returned}</MaxReturned>'
        if self.from_modified_date:
            xml += f'<FromModifiedDate>{self.from_modified_date.isoformat()}</FromModifiedDate>'
        if self.to_modified_date:
            xml += f'<ToModifiedDate>{self.to_modified_date.isoformat()}</ToModifiedDate>'
        if self.from_txn_date:
            xml += f'<FromTxnDate>{self.from_txn_date.isoformat()}</FromTxnDate>'
        if self.to_txn_date:
            xml += f'<ToTxnDate>{self.to_txn_date.isoformat()}</ToTxnDate>'
        if self.date_macro:
            xml += f'<DateMacro>{self.date_macro.value}</DateMacro>'
        if self.include_line_items is not None:
            xml += f'<IncludeLineItems>{str(self.include_line_items).lower()}</IncludeLineItems>'
        if self.include_ret_element:
            for element in self.include_ret_element:
                xml += f'<IncludeRetElement>{element}</IncludeRetElement>'
        if self.owner_id:
            for owner_id in self.owner_id:
                xml += f'<OwnerID>{owner_id}</OwnerID>'
        xml += '''
        </DepositQueryRq>
    </QBXMLMsgsRq>
</QBXML>
        '''
        return xml

    def from_response_xml(self, response_xml: str):
        root = etree.fromstring(response_xml.encode('utf-8'))
        deposit_rets = root.findall('.//DepositRet')
        self.deposits = [DepositRet.from_xml(etree.tostring(deposit_ret)) for deposit_ret in deposit_rets]
        self.deposits = [deposit for deposit in self.deposits if deposit is not None]

class DepositRet(Base):
    __tablename__ = 'DepositRet'

    txn_id = Column(String, primary_key=True)
    time_created = Column(DateTime)
    time_modified = Column(DateTime)
    edit_sequence = Column(String)
    txn_number = Column(Integer, nullable=True)
    txn_date = Column(DateTime)
    deposit_to_account_list_id = Column(String, nullable=True)
    deposit_to_account_full_name = Column(String, nullable=True)
    memo = Column(String, nullable=True)
    deposit_total = Column(Float, nullable=True)
    currency_list_id = Column(String, nullable=True)
    currency_full_name = Column(String, nullable=True)
    exchange_rate = Column(Float, nullable=True)
    deposit_total_in_home_currency = Column(Float, nullable=True)
    external_guid = Column(String, nullable=True)

    @staticmethod
    def from_xml(xml_str: str):
        root = etree.fromstring(xml_str)
        deposit_ret = root if root.tag == 'DepositRet' else root.find('.//DepositRet')
        if deposit_ret is None:
            return None

        def get_text(element, tag):
            child = element.find(tag)
            return child.text if child is not None else None

        return DepositRet(
            txn_id=get_text(deposit_ret, 'TxnID'),
            time_created=datetime.fromisoformat(get_text(deposit_ret, 'TimeCreated')) if get_text(deposit_ret, 'TimeCreated') else None,
            time_modified=datetime.fromisoformat(get_text(deposit_ret, 'TimeModified')) if get_text(deposit_ret, 'TimeModified') else None,
            edit_sequence=get_text(deposit_ret, 'EditSequence'),
            txn_number=int(get_text(deposit_ret, 'TxnNumber')) if get_text(deposit_ret, 'TxnNumber') else None,
            txn_date=datetime.fromisoformat(get_text(deposit_ret, 'TxnDate')) if get_text(deposit_ret, 'TxnDate') else None,
            deposit_to_account_list_id=get_text(deposit_ret, 'DepositToAccountRef/ListID'),
            deposit_to_account_full_name=get_text(deposit_ret, 'DepositToAccountRef/FullName'),
            memo=get_text(deposit_ret, 'Memo'),
            deposit_total=float(get_text(deposit_ret, 'DepositTotal')) if get_text(deposit_ret, 'DepositTotal') else None,
            currency_list_id=get_text(deposit_ret, 'CurrencyRef/ListID'),
            currency_full_name=get_text(deposit_ret, 'CurrencyRef/FullName'),
            exchange_rate=float(get_text(deposit_ret, 'ExchangeRate')) if get_text(deposit_ret, 'ExchangeRate') else None,
            deposit_total_in_home_currency=float(get_text(deposit_ret, 'DepositTotalInHomeCurrency')) if get_text(deposit_ret, 'DepositTotalInHomeCurrency') else None,
            external_guid=get_text(deposit_ret, 'ExternalGUID')
        )

class DepositQueryRs:
    def __init__(self, status_code: int, status_severity: str, status_message: str, ret_count: int, deposit_ret: Optional[List[DepositRet]] = None):
        self.status_code = status_code
        self.status_severity = status_severity
        self.status_message = status_message
        self.ret_count = ret_count
        self.deposit_ret = deposit_ret

def create_deposit_table_if_not_exists(engine):
    Base.metadata.create_all(engine)

def generate_deposit_query_xml(query: DepositQueryRq) -> str:
    xml = f'''<?xml version="1.0" encoding="utf-8"?>
<?qbxml version="16.0"?>
<QBXML>
    <QBXMLMsgsRq onError="stopOnError">
        <DepositQueryRq>
    '''
    if query.txn_id:
        for txn_id in query.txn_id:
            xml += f'<TxnID>{txn_id}</TxnID>'
    if query.max_returned:
        xml += f'<MaxReturned>{query.max_returned}</MaxReturned>'
    if query.from_modified_date:
        xml += f'<FromModifiedDate>{query.from_modified_date.isoformat()}</FromModifiedDate>'
    if query.to_modified_date:
        xml += f'<ToModifiedDate>{query.to_modified_date.isoformat()}</ToModifiedDate>'
    if query.from_txn_date:
        xml += f'<FromTxnDate>{query.from_txn_date.isoformat()}</FromTxnDate>'
    if query.to_txn_date:
        xml += f'<ToTxnDate>{query.to_txn_date.isoformat()}</ToTxnDate>'
    if query.date_macro:
        xml += f'<DateMacro>{query.date_macro.value}</DateMacro>'
    if query.include_line_items is not None:
        xml += f'<IncludeLineItems>{str(query.include_line_items).lower()}</IncludeLineItems>'
    if query.include_ret_element:
        for element in query.include_ret_element:
            xml += f'<IncludeRetElement>{element}</IncludeRetElement>'
    if query.owner_id:
        for owner_id in query.owner_id:
            xml += f'<OwnerID>{owner_id}</OwnerID>'
    xml += '''
        </DepositQueryRq>
    </QBXMLMsgsRq>
</QBXML>
    '''
    return xml