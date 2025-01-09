from enum import Enum
from typing import List, Optional
from datetime import datetime
from lxml import etree
from sqlalchemy import create_engine, Column, String, Integer, Float, Boolean, DateTime
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

class AccountType(Enum):
    ACCOUNTS_PAYABLE = "AccountsPayable"
    ACCOUNTS_RECEIVABLE = "AccountsReceivable"
    BANK = "Bank"
    COST_OF_GOODS_SOLD = "CostOfGoodsSold"
    CREDIT_CARD = "CreditCard"
    EQUITY = "Equity"
    EXPENSE = "Expense"
    FIXED_ASSET = "FixedAsset"
    INCOME = "Income"
    LONG_TERM_LIABILITY = "LongTermLiability"
    NON_POSTING = "NonPosting"
    OTHER_ASSET = "OtherAsset"
    OTHER_CURRENT_ASSET = "OtherCurrentAsset"
    OTHER_CURRENT_LIABILITY = "OtherCurrentLiability"
    OTHER_EXPENSE = "OtherExpense"
    OTHER_INCOME = "OtherIncome"

class NameFilter:
    def __init__(self, match_criterion: MatchCriterion, name: str):
        self.match_criterion = match_criterion
        self.name = name

class NameRangeFilter:
    def __init__(self, from_name: Optional[str] = None, to_name: Optional[str] = None):
        self.from_name = from_name
        self.to_name = to_name

class AccountQueryRq:
    def __init__(self, list_id: Optional[List[str]] = None, full_name: Optional[List[str]] = None, max_returned: Optional[int] = None,
                 active_status: Optional[ActiveStatus] = None, from_modified_date: Optional[datetime] = None, to_modified_date: Optional[datetime] = None,
                 name_filter: Optional[NameFilter] = None, name_range_filter: Optional[NameRangeFilter] = None, account_type: Optional[List[AccountType]] = None,
                 include_ret_element: Optional[List[str]] = None, owner_id: Optional[List[str]] = None):
        self.list_id = list_id
        self.full_name = full_name
        self.max_returned = max_returned
        self.active_status = active_status
        self.from_modified_date = from_modified_date
        self.to_modified_date = to_modified_date
        self.name_filter = name_filter
        self.name_range_filter = name_range_filter
        self.account_type = account_type
        self.include_ret_element = include_ret_element
        self.owner_id = owner_id

    def to_xml(self) -> str:
        xml = f'''<?xml version="1.0" encoding="utf-8"?>
<?qbxml version="16.0"?>
<QBXML>
    <QBXMLMsgsRq onError="stopOnError">
        <AccountQueryRq>
    '''
        if self.list_id:
            for list_id in self.list_id:
                xml += f'<ListID>{list_id}</ListID>'
        if self.full_name:
            for full_name in self.full_name:
                xml += f'<FullName>{full_name}</FullName>'
        if self.max_returned:
            xml += f'<MaxReturned>{self.max_returned}</MaxReturned>'
        if self.active_status:
            xml += f'<ActiveStatus>{self.active_status.value}</ActiveStatus>'
        if self.from_modified_date:
            xml += f'<FromModifiedDate>{self.from_modified_date.isoformat()}</FromModifiedDate>'
        if self.to_modified_date:
            xml += f'<ToModifiedDate>{self.to_modified_date.isoformat()}</ToModifiedDate>'
        if self.name_filter:
            xml += f'''
            <NameFilter>
                <MatchCriterion>{self.name_filter.match_criterion.value}</MatchCriterion>
                <Name>{self.name_filter.name}</Name>
            </NameFilter>
            '''
        if self.name_range_filter:
            xml += '<NameRangeFilter>'
            if self.name_range_filter.from_name:
                xml += f'<FromName>{self.name_range_filter.from_name}</FromName>'
            if self.name_range_filter.to_name:
                xml += f'<ToName>{self.name_range_filter.to_name}</ToName>'
            xml += '</NameRangeFilter>'
        if self.account_type:
            for account_type in self.account_type:
                xml += f'<AccountType>{account_type.value}</AccountType>'
        if self.include_ret_element:
            for element in self.include_ret_element:
                xml += f'<IncludeRetElement>{element}</IncludeRetElement>'
        if self.owner_id:
            for owner_id in self.owner_id:
                xml += f'<OwnerID>{owner_id}</OwnerID>'
        xml += '''
        </AccountQueryRq>
    </QBXMLMsgsRq>
</QBXML>
        '''
        return xml

    def from_response_xml(self, response_xml: str):
        root = etree.fromstring(response_xml.encode('utf-8'))
        account_rets = root.findall('.//AccountRet')
        self.accounts = [AccountRet.from_xml(etree.tostring(account_ret)) for account_ret in account_rets]
        self.accounts = [account for account in self.accounts if account is not None]

class AccountRet(Base):
    __tablename__ = 'AccountRet'

    list_id = Column(String, primary_key=True)
    time_created = Column(DateTime)
    time_modified = Column(DateTime)
    edit_sequence = Column(String)
    name = Column(String)
    full_name = Column(String)
    is_active = Column(Boolean, nullable=True)
    parent_list_id = Column(String, nullable=True)
    parent_full_name = Column(String, nullable=True)
    sublevel = Column(Integer)
    account_type = Column(String)
    special_account_type = Column(String, nullable=True)
    is_tax_account = Column(Boolean, nullable=True)
    account_number = Column(String, nullable=True)
    bank_number = Column(String, nullable=True)
    desc = Column(String, nullable=True)
    balance = Column(Float, nullable=True)
    total_balance = Column(Float, nullable=True)
    sales_tax_code_list_id = Column(String, nullable=True)
    sales_tax_code_full_name = Column(String, nullable=True)
    tax_line_id = Column(Integer, nullable=True)
    tax_line_name = Column(String, nullable=True)
    cash_flow_classification = Column(String, nullable=True)
    currency_list_id = Column(String, nullable=True)
    currency_full_name = Column(String, nullable=True)
    owner_id = Column(String, nullable=True)
    data_ext_name = Column(String, nullable=True)
    data_ext_type = Column(String, nullable=True)
    data_ext_value = Column(String, nullable=True)

    @staticmethod
    def from_xml(xml_str: str):
        root = etree.fromstring(xml_str)
        account_ret = root if root.tag == 'AccountRet' else root.find('.//AccountRet')
        if account_ret is None:
            return None

        def get_text(element, tag):
            child = element.find(tag)
            return child.text if child is not None else None

        return AccountRet(
            list_id=get_text(account_ret, 'ListID'),
            time_created=datetime.fromisoformat(get_text(account_ret, 'TimeCreated')) if get_text(account_ret, 'TimeCreated') else None,
            time_modified=datetime.fromisoformat(get_text(account_ret, 'TimeModified')) if get_text(account_ret, 'TimeModified') else None,
            edit_sequence=get_text(account_ret, 'EditSequence'),
            name=get_text(account_ret, 'Name'),
            full_name=get_text(account_ret, 'FullName'),
            is_active=get_text(account_ret, 'IsActive') == 'true' if get_text(account_ret, 'IsActive') else None,
            parent_list_id=get_text(account_ret, 'ParentRef/ListID'),
            parent_full_name=get_text(account_ret, 'ParentRef/FullName'),
            sublevel=int(get_text(account_ret, 'Sublevel')) if get_text(account_ret, 'Sublevel') else None,
            account_type=get_text(account_ret, 'AccountType'),
            special_account_type=get_text(account_ret, 'SpecialAccountType'),
            is_tax_account=get_text(account_ret, 'IsTaxAccount') == 'true' if get_text(account_ret, 'IsTaxAccount') else None,
            account_number=get_text(account_ret, 'AccountNumber'),
            bank_number=get_text(account_ret, 'BankNumber'),
            desc=get_text(account_ret, 'Desc'),
            balance=float(get_text(account_ret, 'Balance')) if get_text(account_ret, 'Balance') else None,
            total_balance=float(get_text(account_ret, 'TotalBalance')) if get_text(account_ret, 'TotalBalance') else None,
            sales_tax_code_list_id=get_text(account_ret, 'SalesTaxCodeRef/ListID'),
            sales_tax_code_full_name=get_text(account_ret, 'SalesTaxCodeRef/FullName'),
            tax_line_id=int(get_text(account_ret, 'TaxLineInfoRet/TaxLineID')) if get_text(account_ret, 'TaxLineInfoRet/TaxLineID') else None,
            tax_line_name=get_text(account_ret, 'TaxLineInfoRet/TaxLineName'),
            cash_flow_classification=get_text(account_ret, 'CashFlowClassification'),
            currency_list_id=get_text(account_ret, 'CurrencyRef/ListID'),
            currency_full_name=get_text(account_ret, 'CurrencyRef/FullName'),
            owner_id=get_text(account_ret, 'OwnerID'),
            data_ext_name=get_text(account_ret, 'DataExtRet/DataExtName'),
            data_ext_type=get_text(account_ret, 'DataExtRet/DataExtType'),
            data_ext_value=get_text(account_ret, 'DataExtRet/DataExtValue')
        )

class AccountQueryRs:
    def __init__(self, status_code: int, status_severity: str, status_message: str, ret_count: int, account_ret: Optional[List[AccountRet]] = None):
        self.status_code = status_code
        self.status_severity = status_severity
        self.status_message = status_message
        self.ret_count = ret_count
        self.account_ret = account_ret

def create_account_table_if_not_exists(engine):
    Base.metadata.create_all(engine)

def generate_account_query_xml(query: AccountQueryRq) -> str:
    xml = f'''<?xml version="1.0" encoding="utf-8"?>
<?qbxml version="16.0"?>
<QBXML>
    <QBXMLMsgsRq onError="stopOnError">
        <AccountQueryRq>
    '''
    if query.list_id:
        for list_id in query.list_id:
            xml += f'<ListID>{list_id}</ListID>'
    if query.full_name:
        for full_name in query.full_name:
            xml += f'<FullName>{full_name}</FullName>'
    if query.max_returned:
        xml += f'<MaxReturned>{query.max_returned}</MaxReturned>'
    if query.active_status:
        xml += f'<ActiveStatus>{query.active_status.value}</ActiveStatus>'
    if query.from_modified_date:
        xml += f'<FromModifiedDate>{query.from_modified_date.isoformat()}</FromModifiedDate>'
    if query.to_modified_date:
        xml += f'<ToModifiedDate>{query.to_modified_date.isoformat()}</ToModifiedDate>'
    if query.name_filter:
        xml += f'''
        <NameFilter>
            <MatchCriterion>{query.name_filter.match_criterion.value}</MatchCriterion>
            <Name>{query.name_filter.name}</Name>
        </NameFilter>
        '''
    if query.name_range_filter:
        xml += '<NameRangeFilter>'
        if query.name_range_filter.from_name:
            xml += f'<FromName>{query.name_range_filter.from_name}</FromName>'
        if query.name_range_filter.to_name:
            xml += f'<ToName>{query.name_range_filter.to_name}</ToName>'
        xml += '</NameRangeFilter>'
    if query.account_type:
        for account_type in query.account_type:
            xml += f'<AccountType>{account_type.value}</AccountType>'
    if query.include_ret_element:
        for element in query.include_ret_element:
            xml += f'<IncludeRetElement>{element}</IncludeRetElement>'
    if query.owner_id:
        for owner_id in query.owner_id:
            xml += f'<OwnerID>{owner_id}</OwnerID>'
    xml += '''
        </AccountQueryRq>
    </QBXMLMsgsRq>
</QBXML>
    '''
    return xml