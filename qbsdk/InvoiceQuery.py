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

class PaidStatus(Enum):
    ALL = "All"
    PAID_ONLY = "PaidOnly"
    NOT_PAID_ONLY = "NotPaidOnly"

class InvoiceQueryRq:
    def __init__(self, txn_id: Optional[List[str]] = None, ref_number: Optional[List[str]] = None, ref_number_case_sensitive: Optional[List[str]] = None,
                 max_returned: Optional[int] = None, from_modified_date: Optional[datetime] = None, to_modified_date: Optional[datetime] = None,
                 from_txn_date: Optional[datetime] = None, to_txn_date: Optional[datetime] = None, match_criterion: Optional[MatchCriterion] = None,
                 paid_status: Optional[PaidStatus] = None, include_line_items: Optional[bool] = None, include_linked_txns: Optional[bool] = None,
                 include_ret_element: Optional[List[str]] = None, owner_id: Optional[List[str]] = None):
        self.txn_id = txn_id
        self.ref_number = ref_number
        self.ref_number_case_sensitive = ref_number_case_sensitive
        self.max_returned = max_returned
        self.from_modified_date = from_modified_date
        self.to_modified_date = to_modified_date
        self.from_txn_date = from_txn_date
        self.to_txn_date = to_txn_date
        self.match_criterion = match_criterion
        self.paid_status = paid_status
        self.include_line_items = include_line_items
        self.include_linked_txns = include_linked_txns
        self.include_ret_element = include_ret_element
        self.owner_id = owner_id

    def to_xml(self) -> str:
        xml = f'''<?xml version="1.0" encoding="utf-8"?>
<?qbxml version="16.0"?>
<QBXML>
    <QBXMLMsgsRq onError="stopOnError">
        <InvoiceQueryRq>
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
            xml += f'''
            <RefNumberFilter>
                <MatchCriterion>{self.match_criterion.value}</MatchCriterion>
                <RefNumber>{self.ref_number}</RefNumber>
            </RefNumberFilter>
            '''
        if self.paid_status:
            xml += f'<PaidStatus>{self.paid_status.value}</PaidStatus>'
        if self.include_line_items is not None:
            xml += f'<IncludeLineItems>{str(self.include_line_items).lower()}</IncludeLineItems>'
        if self.include_linked_txns is not None:
            xml += f'<IncludeLinkedTxns>{str(self.include_linked_txns).lower()}</IncludeLinkedTxns>'
        if self.include_ret_element:
            for element in self.include_ret_element:
                xml += f'<IncludeRetElement>{element}</IncludeRetElement>'
        if self.owner_id:
            for owner_id in self.owner_id:
                xml += f'<OwnerID>{owner_id}</OwnerID>'
        xml += '''
        </InvoiceQueryRq>
    </QBXMLMsgsRq>
</QBXML>
        '''
        return xml

    def from_response_xml(self, response_xml: str):
        root = etree.fromstring(response_xml.encode('utf-8'))
        invoice_rets = root.findall('.//InvoiceRet')
        self.invoices = [InvoiceRet.from_xml(etree.tostring(invoice_ret)) for invoice_ret in invoice_rets]
        self.invoices = [invoice for invoice in self.invoices if invoice is not None]

class InvoiceRet(Base):
    __tablename__ = 'InvoiceRet'

    txn_id = Column(String, primary_key=True)
    time_created = Column(DateTime)
    time_modified = Column(DateTime)
    edit_sequence = Column(String)
    txn_number = Column(Integer, nullable=True)
    customer_list_id = Column(String, nullable=True)
    customer_full_name = Column(String, nullable=True)
    class_list_id = Column(String, nullable=True)
    class_full_name = Column(String, nullable=True)
    ar_account_list_id = Column(String, nullable=True)
    ar_account_full_name = Column(String, nullable=True)
    template_list_id = Column(String, nullable=True)
    template_full_name = Column(String, nullable=True)
    txn_date = Column(DateTime)
    ref_number = Column(String, nullable=True)
    bill_address = Column(String, nullable=True)
    ship_address = Column(String, nullable=True)
    is_pending = Column(Boolean, nullable=True)
    is_finance_charge = Column(Boolean, nullable=True)
    po_number = Column(String, nullable=True)
    terms_list_id = Column(String, nullable=True)
    terms_full_name = Column(String, nullable=True)
    due_date = Column(DateTime, nullable=True)
    sales_rep_list_id = Column(String, nullable=True)
    sales_rep_full_name = Column(String, nullable=True)
    fob = Column(String, nullable=True)
    ship_date = Column(DateTime, nullable=True)
    ship_method_list_id = Column(String, nullable=True)
    ship_method_full_name = Column(String, nullable=True)
    subtotal = Column(Float, nullable=True)
    item_sales_tax_list_id = Column(String, nullable=True)
    item_sales_tax_full_name = Column(String, nullable=True)
    sales_tax_percentage = Column(Float, nullable=True)
    sales_tax_total = Column(Float, nullable=True)
    applied_amount = Column(Float, nullable=True)
    balance_remaining = Column(Float, nullable=True)
    currency_list_id = Column(String, nullable=True)
    currency_full_name = Column(String, nullable=True)
    exchange_rate = Column(Float, nullable=True)
    balance_remaining_in_home_currency = Column(Float, nullable=True)
    memo = Column(String, nullable=True)
    is_paid = Column(Boolean, nullable=True)
    customer_msg_list_id = Column(String, nullable=True)
    customer_msg_full_name = Column(String, nullable=True)
    is_to_be_printed = Column(Boolean, nullable=True)
    is_to_be_emailed = Column(Boolean, nullable=True)
    is_tax_included = Column(Boolean, nullable=True)
    customer_sales_tax_code_list_id = Column(String, nullable=True)
    customer_sales_tax_code_full_name = Column(String, nullable=True)
    suggested_discount_amount = Column(Float, nullable=True)
    suggested_discount_date = Column(DateTime, nullable=True)
    other = Column(String, nullable=True)
    external_guid = Column(String, nullable=True)

    @staticmethod
    def from_xml(xml_str: str):
        root = etree.fromstring(xml_str)
        invoice_ret = root if root.tag == 'InvoiceRet' else root.find('.//InvoiceRet')
        if invoice_ret is None:
            return None

        def get_text(element, tag):
            child = element.find(tag)
            return child.text if child is not None else None

        return InvoiceRet(
            txn_id=get_text(invoice_ret, 'TxnID'),
            time_created=datetime.fromisoformat(get_text(invoice_ret, 'TimeCreated')) if get_text(invoice_ret, 'TimeCreated') else None,
            time_modified=datetime.fromisoformat(get_text(invoice_ret, 'TimeModified')) if get_text(invoice_ret, 'TimeModified') else None,
            edit_sequence=get_text(invoice_ret, 'EditSequence'),
            txn_number=int(get_text(invoice_ret, 'TxnNumber')) if get_text(invoice_ret, 'TxnNumber') else None,
            customer_list_id=get_text(invoice_ret, 'CustomerRef/ListID'),
            customer_full_name=get_text(invoice_ret, 'CustomerRef/FullName'),
            class_list_id=get_text(invoice_ret, 'ClassRef/ListID'),
            class_full_name=get_text(invoice_ret, 'ClassRef/FullName'),
            ar_account_list_id=get_text(invoice_ret, 'ARAccountRef/ListID'),
            ar_account_full_name=get_text(invoice_ret, 'ARAccountRef/FullName'),
            template_list_id=get_text(invoice_ret, 'TemplateRef/ListID'),
            template_full_name=get_text(invoice_ret, 'TemplateRef/FullName'),
            txn_date=datetime.fromisoformat(get_text(invoice_ret, 'TxnDate')) if get_text(invoice_ret, 'TxnDate') else None,
            ref_number=get_text(invoice_ret, 'RefNumber'),
            bill_address=get_text(invoice_ret, 'BillAddress/Addr1'),
            ship_address=get_text(invoice_ret, 'ShipAddress/Addr1'),
            is_pending=get_text(invoice_ret, 'IsPending') == 'true' if get_text(invoice_ret, 'IsPending') else None,
            is_finance_charge=get_text(invoice_ret, 'IsFinanceCharge') == 'true' if get_text(invoice_ret, 'IsFinanceCharge') else None,
            po_number=get_text(invoice_ret, 'PONumber'),
            terms_list_id=get_text(invoice_ret, 'TermsRef/ListID'),
            terms_full_name=get_text(invoice_ret, 'TermsRef/FullName'),
            due_date=datetime.fromisoformat(get_text(invoice_ret, 'DueDate')) if get_text(invoice_ret, 'DueDate') else None,
            sales_rep_list_id=get_text(invoice_ret, 'SalesRepRef/ListID'),
            sales_rep_full_name=get_text(invoice_ret, 'SalesRepRef/FullName'),
            fob=get_text(invoice_ret, 'FOB'),
            ship_date=datetime.fromisoformat(get_text(invoice_ret, 'ShipDate')) if get_text(invoice_ret, 'ShipDate') else None,
            ship_method_list_id=get_text(invoice_ret, 'ShipMethodRef/ListID'),
            ship_method_full_name=get_text(invoice_ret, 'ShipMethodRef/FullName'),
            subtotal=float(get_text(invoice_ret, 'Subtotal')) if get_text(invoice_ret, 'Subtotal') else None,
            item_sales_tax_list_id=get_text(invoice_ret, 'ItemSalesTaxRef/ListID'),
            item_sales_tax_full_name=get_text(invoice_ret, 'ItemSalesTaxRef/FullName'),
            sales_tax_percentage=float(get_text(invoice_ret, 'SalesTaxPercentage')) if get_text(invoice_ret, 'SalesTaxPercentage') else None,
            sales_tax_total=float(get_text(invoice_ret, 'SalesTaxTotal')) if get_text(invoice_ret, 'SalesTaxTotal') else None,
            applied_amount=float(get_text(invoice_ret, 'AppliedAmount')) if get_text(invoice_ret, 'AppliedAmount') else None,
            balance_remaining=float(get_text(invoice_ret, 'BalanceRemaining')) if get_text(invoice_ret, 'BalanceRemaining') else None,
            currency_list_id=get_text(invoice_ret, 'CurrencyRef/ListID'),
            currency_full_name=get_text(invoice_ret, 'CurrencyRef/FullName'),
            exchange_rate=float(get_text(invoice_ret, 'ExchangeRate')) if get_text(invoice_ret, 'ExchangeRate') else None,
            balance_remaining_in_home_currency=float(get_text(invoice_ret, 'BalanceRemainingInHomeCurrency')) if get_text(invoice_ret, 'BalanceRemainingInHomeCurrency') else None,
            memo=get_text(invoice_ret, 'Memo'),
            is_paid=get_text(invoice_ret, 'IsPaid') == 'true' if get_text(invoice_ret, 'IsPaid') else None,
            customer_msg_list_id=get_text(invoice_ret, 'CustomerMsgRef/ListID'),
            customer_msg_full_name=get_text(invoice_ret, 'CustomerMsgRef/FullName'),
            is_to_be_printed=get_text(invoice_ret, 'IsToBePrinted') == 'true' if get_text(invoice_ret, 'IsToBePrinted') else None,
            is_to_be_emailed=get_text(invoice_ret, 'IsToBeEmailed') == 'true' if get_text(invoice_ret, 'IsToBeEmailed') else None,
            is_tax_included=get_text(invoice_ret, 'IsTaxIncluded') == 'true' if get_text(invoice_ret, 'IsTaxIncluded') else None,
            customer_sales_tax_code_list_id=get_text(invoice_ret, 'CustomerSalesTaxCodeRef/ListID'),
            customer_sales_tax_code_full_name=get_text(invoice_ret, 'CustomerSalesTaxCodeRef/FullName'),
            suggested_discount_amount=float(get_text(invoice_ret, 'SuggestedDiscountAmount')) if get_text(invoice_ret, 'SuggestedDiscountAmount') else None,
            suggested_discount_date=datetime.fromisoformat(get_text(invoice_ret, 'SuggestedDiscountDate')) if get_text(invoice_ret, 'SuggestedDiscountDate') else None,
            other=get_text(invoice_ret, 'Other'),
            external_guid=get_text(invoice_ret, 'ExternalGUID')
        )

class InvoiceQueryRs:
    def __init__(self, status_code: int, status_severity: str, status_message: str, ret_count: int, invoice_ret: Optional[List[InvoiceRet]] = None):
        self.status_code = status_code
        self.status_severity = status_severity
        self.status_message = status_message
        self.ret_count = ret_count
        self.invoice_ret = invoice_ret

def create_invoice_table_if_not_exists(engine):
    Base.metadata.create_all(engine)

def generate_invoice_query_xml(query: InvoiceQueryRq) -> str:
    xml = f'''<?xml version="1.0" encoding="utf-8"?>
<?qbxml version="16.0"?>
<QBXML>
    <QBXMLMsgsRq onError="stopOnError">
        <InvoiceQueryRq>
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
        xml += f'''
        <RefNumberFilter>
            <MatchCriterion>{query.match_criterion.value}</MatchCriterion>
            <RefNumber>{query.ref_number}</RefNumber>
        </RefNumberFilter>
        '''
    if query.paid_status:
        xml += f'<PaidStatus>{query.paid_status.value}</PaidStatus>'
    if query.include_line_items is not None:
        xml += f'<IncludeLineItems>{str(query.include_line_items).lower()}</IncludeLineItems>'
    if query.include_linked_txns is not None:
        xml += f'<IncludeLinkedTxns>{str(query.include_linked_txns).lower()}</IncludeLinkedTxns>'
    if query.include_ret_element:
        for element in query.include_ret_element:
            xml += f'<IncludeRetElement>{element}</IncludeRetElement>'
    if query.owner_id:
        for owner_id in query.owner_id:
            xml += f'<OwnerID>{owner_id}</OwnerID>'
    xml += '''
        </InvoiceQueryRq>
    </QBXMLMsgsRq>
</QBXML>
    '''
    return xml