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

class CreditCardChargeQueryRq:
    def __init__(self, txn_id: Optional[List[str]] = None, ref_number: Optional[List[str]] = None, ref_number_case_sensitive: Optional[List[str]] = None,
                 max_returned: Optional[int] = None, from_modified_date: Optional[datetime] = None, to_modified_date: Optional[datetime] = None,
                 from_txn_date: Optional[datetime] = None, to_txn_date: Optional[datetime] = None, match_criterion: Optional[MatchCriterion] = None,
                 include_line_items: Optional[bool] = None, include_ret_element: Optional[List[str]] = None, owner_id: Optional[List[str]] = None):
        self.txn_id = txn_id
        self.ref_number = ref_number
        self.ref_number_case_sensitive = ref_number_case_sensitive
        self.max_returned = max_returned
        self.from_modified_date = from_modified_date
        self.to_modified_date = to_modified_date
        self.from_txn_date = from_txn_date
        self.to_txn_date = to_txn_date
        self.match_criterion = match_criterion
        self.include_line_items = include_line_items
        self.include_ret_element = include_ret_element
        self.owner_id = owner_id

    def to_xml(self) -> str:
        xml = f'''<?xml version="1.0" encoding="utf-8"?>
<?qbxml version="16.0"?>
<QBXML>
    <QBXMLMsgsRq onError="stopOnError">
        <CreditCardChargeQueryRq>
    '''
        if self.txn_id:
            for txn_id in self.txn_id:
                xml += f'<TxnID>{txn_id}</TxnID>'
        if self.ref_number:
            for ref_number in self.ref_number:
                xml += f'<RefNumber>{ref_number}</RefNumber>'
        if self.ref_number_case_sensitive:
            for ref_number_case_sensitive in self.ref_number_case_sensitive:
                xml += f'<RefNumberCaseSensitive>{ref_number_case_sensitive}</RefNumberCaseSensitive>'
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
        if self.match_criterion:
            xml += f'<MatchCriterion>{self.match_criterion.value}</MatchCriterion>'
        if self.include_line_items is not None:
            xml += f'<IncludeLineItems>{str(self.include_line_items).lower()}</IncludeLineItems>'
        if self.include_ret_element:
            for element in self.include_ret_element:
                xml += f'<IncludeRetElement>{element}</IncludeRetElement>'
        if self.owner_id:
            for owner_id in self.owner_id:
                xml += f'<OwnerID>{owner_id}</OwnerID>'
        xml += '''
        </CreditCardChargeQueryRq>
    </QBXMLMsgsRq>
</QBXML>
        '''
        return xml

    def from_response_xml(self, response_xml: str):
        root = etree.fromstring(response_xml.encode('utf-8'))
        cc_charge_rets = root.findall('.//CreditCardChargeRet')
        self.cc_charges = [CreditCardChargeRet.from_xml(etree.tostring(cc_charge_ret)) for cc_charge_ret in cc_charge_rets]
        self.cc_charges = [cc_charge for cc_charge in self.cc_charges if cc_charge is not None]

class CreditCardChargeRet(Base):
    __tablename__ = 'CreditCardChargeRet'

    txn_id = Column(String, primary_key=True)
    time_created = Column(DateTime)
    time_modified = Column(DateTime)
    edit_sequence = Column(String)
    txn_number = Column(Integer, nullable=True)
    account_list_id = Column(String, nullable=True)
    account_full_name = Column(String, nullable=True)
    payee_list_id = Column(String, nullable=True)
    payee_full_name = Column(String, nullable=True)
    ref_number = Column(String, nullable=True)
    txn_date = Column(DateTime)
    amount = Column(Float)
    currency_list_id = Column(String, nullable=True)
    currency_full_name = Column(String, nullable=True)
    exchange_rate = Column(Float, nullable=True)
    amount_in_home_currency = Column(Float, nullable=True)
    memo = Column(String, nullable=True)
    is_tax_included = Column(Boolean, nullable=True)
    sales_tax_code_list_id = Column(String, nullable=True)
    sales_tax_code_full_name = Column(String, nullable=True)
    external_guid = Column(String, nullable=True)

    @staticmethod
    def from_xml(xml_str: str):
        root = etree.fromstring(xml_str)
        cc_charge_ret = root if root.tag == 'CreditCardChargeRet' else root.find('.//CreditCardChargeRet')
        if cc_charge_ret is None:
            return None

        def get_text(element, tag):
            child = element.find(tag)
            return child.text if child is not None else None

        return CreditCardChargeRet(
            txn_id=get_text(cc_charge_ret, 'TxnID'),
            time_created=datetime.fromisoformat(get_text(cc_charge_ret, 'TimeCreated')) if get_text(cc_charge_ret, 'TimeCreated') else None,
            time_modified=datetime.fromisoformat(get_text(cc_charge_ret, 'TimeModified')) if get_text(cc_charge_ret, 'TimeModified') else None,
            edit_sequence=get_text(cc_charge_ret, 'EditSequence'),
            txn_number=int(get_text(cc_charge_ret, 'TxnNumber')) if get_text(cc_charge_ret, 'TxnNumber') else None,
            account_list_id=get_text(cc_charge_ret, 'AccountRef/ListID'),
            account_full_name=get_text(cc_charge_ret, 'AccountRef/FullName'),
            payee_list_id=get_text(cc_charge_ret, 'PayeeEntityRef/ListID'),
            payee_full_name=get_text(cc_charge_ret, 'PayeeEntityRef/FullName'),
            ref_number=get_text(cc_charge_ret, 'RefNumber'),
            txn_date=datetime.fromisoformat(get_text(cc_charge_ret, 'TxnDate')) if get_text(cc_charge_ret, 'TxnDate') else None,
            amount=float(get_text(cc_charge_ret, 'Amount')) if get_text(cc_charge_ret, 'Amount') else None,
            currency_list_id=get_text(cc_charge_ret, 'CurrencyRef/ListID'),
            currency_full_name=get_text(cc_charge_ret, 'CurrencyRef/FullName'),
            exchange_rate=float(get_text(cc_charge_ret, 'ExchangeRate')) if get_text(cc_charge_ret, 'ExchangeRate') else None,
            amount_in_home_currency=float(get_text(cc_charge_ret, 'AmountInHomeCurrency')) if get_text(cc_charge_ret, 'AmountInHomeCurrency') else None,
            memo=get_text(cc_charge_ret, 'Memo'),
            is_tax_included=get_text(cc_charge_ret, 'IsTaxIncluded') == 'true' if get_text(cc_charge_ret, 'IsTaxIncluded') else None,
            sales_tax_code_list_id=get_text(cc_charge_ret, 'SalesTaxCodeRef/ListID'),
            sales_tax_code_full_name=get_text(cc_charge_ret, 'SalesTaxCodeRef/FullName'),
            external_guid=get_text(cc_charge_ret, 'ExternalGUID')
        )

class CreditCardChargeQueryRs:
    def __init__(self, status_code: int, status_severity: str, status_message: str, ret_count: int, cc_charge_ret: Optional[List[CreditCardChargeRet]] = None):
        self.status_code = status_code
        self.status_severity = status_severity
        self.status_message = status_message
        self.ret_count = ret_count
        self.cc_charge_ret = cc_charge_ret

def create_cc_charge_table_if_not_exists(engine):
    Base.metadata.create_all(engine)

def generate_cc_charge_query_xml(query: CreditCardChargeQueryRq) -> str:
    xml = f'''<?xml version="1.0" encoding="utf-8"?>
<?qbxml version="16.0"?>
<QBXML>
    <QBXMLMsgsRq onError="stopOnError">
        <CreditCardChargeQueryRq>
    '''
    if query.txn_id:
        for txn_id in query.txn_id:
            xml += f'<TxnID>{txn_id}</TxnID>'
    if query.ref_number:
        for ref_number in query.ref_number:
            xml += f'<RefNumber>{ref_number}</RefNumber>'
    if query.ref_number_case_sensitive:
        for ref_number_case_sensitive in query.ref_number_case_sensitive:
            xml += f'<RefNumberCaseSensitive>{ref_number_case_sensitive}</RefNumberCaseSensitive>'
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
    if query.match_criterion:
        xml += f'<MatchCriterion>{query.match_criterion.value}</MatchCriterion>'
    if query.include_line_items is not None:
        xml += f'<IncludeLineItems>{str(query.include_line_items).lower()}</IncludeLineItems>'
    if query.include_ret_element:
        for element in query.include_ret_element:
            xml += f'<IncludeRetElement>{element}</IncludeRetElement>'
    if query.owner_id:
        for owner_id in query.owner_id:
            xml += f'<OwnerID>{owner_id}</OwnerID>'
    xml += '''
        </CreditCardChargeQueryRq>
    </QBXMLMsgsRq>
</QBXML>
    '''
    return xml