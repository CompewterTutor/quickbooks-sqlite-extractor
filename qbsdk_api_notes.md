API Notes

## AccountQuery

### Request

### Response

### XMLOps
'''xml
<?xml version="1.0" encoding="utf-8"?>
<?qbxml version="16.0"?>
<QBXML>
        <QBXMLMsgsRq onError="stopOnError">
                <AccountQueryRq metaData="ENUMTYPE">
                        <!-- BEGIN OR -->
                                <ListID >IDTYPE</ListID> <!-- optional, may repeat -->
                        <!-- OR -->
                                <FullName >STRTYPE</FullName> <!-- optional, may repeat -->
                        <!-- OR -->
                                <MaxReturned >INTTYPE</MaxReturned> <!-- optional -->
                                <!-- ActiveStatus may have one of the following values: ActiveOnly [DEFAULT], InactiveOnly, All -->
                                <ActiveStatus >ENUMTYPE</ActiveStatus> <!-- optional -->
                                <FromModifiedDate >DATETIMETYPE</FromModifiedDate> <!-- optional -->
                                <ToModifiedDate >DATETIMETYPE</ToModifiedDate> <!-- optional -->
                                <!-- BEGIN OR -->
                                        <NameFilter> <!-- optional -->
                                                <!-- MatchCriterion may have one of the following values: StartsWith, Contains, EndsWith -->
                                                <MatchCriterion >ENUMTYPE</MatchCriterion> <!-- required -->
                                                <Name >STRTYPE</Name> <!-- required -->
                                        </NameFilter>
                                <!-- OR -->
                                        <NameRangeFilter> <!-- optional -->
                                                <FromName >STRTYPE</FromName> <!-- optional -->
                                                <ToName >STRTYPE</ToName> <!-- optional -->
                                        </NameRangeFilter>
                                <!-- END OR -->
                                <!-- AccountType may have one of the following values: AccountsPayable, AccountsReceivable, Bank, CostOfGoodsSold, CreditCard, Equity, Expense, FixedAsset, Income, LongTermLiability, NonPosting, OtherAsset, OtherCurrentAsset, OtherCurrentLiability, OtherExpense, OtherIncome -->
                                <AccountType >ENUMTYPE</AccountType> <!-- optional, may repeat -->
                                <CurrencyFilter> <!-- optional -->
                                        <!-- BEGIN OR -->
                                                <ListID >IDTYPE</ListID> <!-- optional, may repeat -->
                                        <!-- OR -->
                                                <FullName >STRTYPE</FullName> <!-- optional, may repeat -->
                                        <!-- END OR -->
                                </CurrencyFilter>
                        <!-- END OR -->
                        <IncludeRetElement >STRTYPE</IncludeRetElement> <!-- optional, may repeat -->
                        <OwnerID >GUIDTYPE</OwnerID> <!-- optional, may repeat -->
                </AccountQueryRq>

                <AccountQueryRs statusCode="INTTYPE" statusSeverity="STRTYPE" statusMessage="STRTYPE" retCount="INTTYPE">
                        <AccountRet> <!-- optional, may repeat -->
                                <ListID >IDTYPE</ListID> <!-- required -->
                                <TimeCreated >DATETIMETYPE</TimeCreated> <!-- required -->
                                <TimeModified >DATETIMETYPE</TimeModified> <!-- required -->
                                <EditSequence >STRTYPE</EditSequence> <!-- required -->
                                <Name >STRTYPE</Name> <!-- required -->
                                <FullName >STRTYPE</FullName> <!-- required -->
                                <IsActive >BOOLTYPE</IsActive> <!-- optional -->
                                <ParentRef> <!-- optional -->
                                        <ListID >IDTYPE</ListID> <!-- optional -->
                                        <FullName >STRTYPE</FullName> <!-- optional -->
                                </ParentRef>
                                <Sublevel >INTTYPE</Sublevel> <!-- required -->
                                <!-- AccountType may have one of the following values: AccountsPayable, AccountsReceivable, Bank, CostOfGoodsSold, CreditCard, Equity, Expense, FixedAsset, Income, LongTermLiability, NonPosting, OtherAsset, OtherCurrentAsset, OtherCurrentLiability, OtherExpense, OtherIncome -->
                                <AccountType >ENUMTYPE</AccountType> <!-- required -->
                                <!-- SpecialAccountType may have one of the following values: AccountsPayable, AccountsReceivable, CondenseItemAdjustmentExpenses, CostOfGoodsSold, DirectDepositLiabilities, Estimates, ExchangeGainLoss, InventoryAssets, ItemReceiptAccount, OpeningBalanceEquity, PayrollExpenses, PayrollLiabilities, PettyCash, PurchaseOrders, ReconciliationDifferences, RetainedEarnings, SalesOrders, SalesTaxPayable, UncategorizedExpenses, UncategorizedIncome, UndepositedFunds -->
                                <SpecialAccountType >ENUMTYPE</SpecialAccountType> <!-- optional -->
                                <IsTaxAccount >BOOLTYPE</IsTaxAccount> <!-- optional -->
                                <AccountNumber >STRTYPE</AccountNumber> <!-- optional -->
                                <BankNumber >STRTYPE</BankNumber> <!-- optional -->
                                <Desc >STRTYPE</Desc> <!-- optional -->
                                <Balance >AMTTYPE</Balance> <!-- optional -->
                                <TotalBalance >AMTTYPE</TotalBalance> <!-- optional -->
                                <SalesTaxCodeRef> <!-- optional -->
                                        <ListID >IDTYPE</ListID> <!-- optional -->
                                        <FullName >STRTYPE</FullName> <!-- optional -->
                                </SalesTaxCodeRef>
                                <TaxLineInfoRet> <!-- optional -->
                                        <TaxLineID >INTTYPE</TaxLineID> <!-- required -->
                                        <TaxLineName >STRTYPE</TaxLineName> <!-- optional -->
                                </TaxLineInfoRet>
                                <!-- CashFlowClassification may have one of the following values: None, Operating, Investing, Financing, NotApplicable -->
                                <CashFlowClassification >ENUMTYPE</CashFlowClassification> <!-- optional -->
                                <CurrencyRef> <!-- optional -->
                                        <ListID >IDTYPE</ListID> <!-- optional -->
                                        <FullName >STRTYPE</FullName> <!-- optional -->
                                </CurrencyRef>
                                <DataExtRet> <!-- optional, may repeat -->
                                        <OwnerID >GUIDTYPE</OwnerID> <!-- optional -->
                                        <DataExtName >STRTYPE</DataExtName> <!-- required -->
                                        <!-- DataExtType may have one of the following values: AMTTYPE, DATETIMETYPE, INTTYPE, PERCENTTYPE, PRICETYPE, QUANTYPE, STR1024TYPE, STR255TYPE -->
                                        <DataExtType >ENUMTYPE</DataExtType> <!-- required -->
                                        <DataExtValue >STRTYPE</DataExtValue> <!-- required -->
                                </DataExtRet>
                        </AccountRet>
                </AccountQueryRs>
        </QBXMLMsgsRq>
</QBXML>

'''

## BillQuery
### XMLOps
```
<?xml version="1.0" encoding="utf-8"?>
<?qbxml version="16.0"?>
<QBXML>
        <QBXMLMsgsRq onError="stopOnError">
                <BillQueryRq metaData="ENUMTYPE" iterator="ENUMTYPE" iteratorID="UUIDTYPE">
                        <!-- BEGIN OR -->
                                <TxnID >IDTYPE</TxnID> <!-- optional, may repeat -->
                        <!-- OR -->
                                <RefNumber >STRTYPE</RefNumber> <!-- optional, may repeat -->
                        <!-- OR -->
                                <RefNumberCaseSensitive >STRTYPE</RefNumberCaseSensitive> <!-- optional, may repeat -->
                        <!-- OR -->
                                <MaxReturned >INTTYPE</MaxReturned> <!-- optional -->
                                <!-- BEGIN OR -->
                                        <ModifiedDateRangeFilter> <!-- optional -->
                                                <FromModifiedDate >DATETIMETYPE</FromModifiedDate> <!-- optional -->
                                                <ToModifiedDate >DATETIMETYPE</ToModifiedDate> <!-- optional -->
                                        </ModifiedDateRangeFilter>
                                <!-- OR -->
                                        <TxnDateRangeFilter> <!-- optional -->
                                                <!-- BEGIN OR -->
                                                        <FromTxnDate >DATETYPE</FromTxnDate> <!-- optional -->
                                                        <ToTxnDate >DATETYPE</ToTxnDate> <!-- optional -->
                                                <!-- OR -->
                                                        <!-- DateMacro may have one of the following values: All, Today, ThisWeek, ThisWeekToDate, ThisMonth, ThisMonthToDate, ThisCalendarQuarter, ThisCalendarQuarterToDate, ThisFiscalQuarter, ThisFiscalQuarterToDate, ThisCalendarYear, ThisCalendarYearToDate, ThisFiscalYear, ThisFiscalYearToDate, Yesterday, LastWeek, LastWeekToDate, LastMonth, LastMonthToDate, LastCalendarQuarter, LastCalendarQuarterToDate, LastFiscalQuarter, LastFiscalQuarterToDate, LastCalendarYear, LastCalendarYearToDate, LastFiscalYear, LastFiscalYearToDate, NextWeek, NextFourWeeks, NextMonth, NextCalendarQuarter, NextCalendarYear, NextFiscalQuarter, NextFiscalYear -->
                                                        <DateMacro >ENUMTYPE</DateMacro> <!-- optional -->
                                                <!-- END OR -->
                                        </TxnDateRangeFilter>
                                <!-- END OR -->
                                <EntityFilter> <!-- optional -->
                                        <!-- BEGIN OR -->
                                                <ListID >IDTYPE</ListID> <!-- optional, may repeat -->
                                        <!-- OR -->
                                                <FullName >STRTYPE</FullName> <!-- optional, may repeat -->
                                        <!-- OR -->
                                                <ListIDWithChildren >IDTYPE</ListIDWithChildren> <!-- optional -->
                                        <!-- OR -->
                                                <FullNameWithChildren >STRTYPE</FullNameWithChildren> <!-- optional -->
                                        <!-- END OR -->
                                </EntityFilter>
                                <AccountFilter> <!-- optional -->
                                        <!-- BEGIN OR -->
                                                <ListID >IDTYPE</ListID> <!-- optional, may repeat -->
                                        <!-- OR -->
                                                <FullName >STRTYPE</FullName> <!-- optional, may repeat -->
                                        <!-- OR -->
                                                <ListIDWithChildren >IDTYPE</ListIDWithChildren> <!-- optional -->
                                        <!-- OR -->
                                                <FullNameWithChildren >STRTYPE</FullNameWithChildren> <!-- optional -->
                                        <!-- END OR -->
                                </AccountFilter>
                                <!-- BEGIN OR -->
                                        <RefNumberFilter> <!-- optional -->
                                                <!-- MatchCriterion may have one of the following values: StartsWith, Contains, EndsWith -->
                                                <MatchCriterion >ENUMTYPE</MatchCriterion> <!-- required -->
                                                <RefNumber >STRTYPE</RefNumber> <!-- required -->
                                        </RefNumberFilter>
                                <!-- OR -->
                                        <RefNumberRangeFilter> <!-- optional -->
                                                <FromRefNumber >STRTYPE</FromRefNumber> <!-- optional -->
                                                <ToRefNumber >STRTYPE</ToRefNumber> <!-- optional -->
                                        </RefNumberRangeFilter>
                                <!-- END OR -->
                                <CurrencyFilter> <!-- optional -->
                                        <!-- BEGIN OR -->
                                                <ListID >IDTYPE</ListID> <!-- optional, may repeat -->
                                        <!-- OR -->
                                                <FullName >STRTYPE</FullName> <!-- optional, may repeat -->
                                        <!-- END OR -->
                                </CurrencyFilter>
                                <!-- PaidStatus may have one of the following values: All [DEFAULT], PaidOnly, NotPaidOnly -->
                                <PaidStatus >ENUMTYPE</PaidStatus> <!-- optional -->
                        <!-- END OR -->
                        <IncludeLineItems >BOOLTYPE</IncludeLineItems> <!-- optional -->
                        <IncludeLinkedTxns >BOOLTYPE</IncludeLinkedTxns> <!-- optional -->
                        <IncludeRetElement >STRTYPE</IncludeRetElement> <!-- optional, may repeat -->
                        <OwnerID >GUIDTYPE</OwnerID> <!-- optional, may repeat -->
                </BillQueryRq>

                <BillQueryRs statusCode="INTTYPE" statusSeverity="STRTYPE" statusMessage="STRTYPE" retCount="INTTYPE" iteratorRemainingCount="INTTYPE" iteratorID="UUIDTYPE">
                        <BillRet> <!-- optional, may repeat -->
                                <TxnID >IDTYPE</TxnID> <!-- required -->
                                <TimeCreated >DATETIMETYPE</TimeCreated> <!-- required -->
                                <TimeModified >DATETIMETYPE</TimeModified> <!-- required -->
                                <EditSequence >STRTYPE</EditSequence> <!-- required -->
                                <TxnNumber >INTTYPE</TxnNumber> <!-- optional -->
                                <VendorRef> <!-- required -->
                                        <ListID >IDTYPE</ListID> <!-- optional -->
                                        <FullName >STRTYPE</FullName> <!-- optional -->
                                </VendorRef>
                                <VendorAddress> <!-- optional -->
                                        <Addr1 >STRTYPE</Addr1> <!-- optional -->
                                        <Addr2 >STRTYPE</Addr2> <!-- optional -->
                                        <Addr3 >STRTYPE</Addr3> <!-- optional -->
                                        <Addr4 >STRTYPE</Addr4> <!-- optional -->
                                        <Addr5 >STRTYPE</Addr5> <!-- optional -->
                                        <City >STRTYPE</City> <!-- optional -->
                                        <State >STRTYPE</State> <!-- optional -->
                                        <PostalCode >STRTYPE</PostalCode> <!-- optional -->
                                        <Country >STRTYPE</Country> <!-- optional -->
                                        <Note >STRTYPE</Note> <!-- optional -->
                                </VendorAddress>
                                <APAccountRef> <!-- optional -->
                                        <ListID >IDTYPE</ListID> <!-- optional -->
                                        <FullName >STRTYPE</FullName> <!-- optional -->
                                </APAccountRef>
                                <TxnDate >DATETYPE</TxnDate> <!-- required -->
                                <DueDate >DATETYPE</DueDate> <!-- optional -->
                                <AmountDue >AMTTYPE</AmountDue> <!-- required -->
                                <CurrencyRef> <!-- optional -->
                                        <ListID >IDTYPE</ListID> <!-- optional -->
                                        <FullName >STRTYPE</FullName> <!-- optional -->
                                </CurrencyRef>
                                <ExchangeRate >FLOATTYPE</ExchangeRate> <!-- optional -->
                                <AmountDueInHomeCurrency >AMTTYPE</AmountDueInHomeCurrency> <!-- optional -->
                                <RefNumber >STRTYPE</RefNumber> <!-- optional -->
                                <IsPending>BOOLTYPE</IsPending> <!-- optional -->
                                <TermsRef> <!-- optional -->
                                        <ListID >IDTYPE</ListID> <!-- optional -->
                                        <FullName >STRTYPE</FullName> <!-- optional -->
                                </TermsRef>
                                <Memo >STRTYPE</Memo> <!-- optional -->
                                <IsTaxIncluded >BOOLTYPE</IsTaxIncluded> <!-- optional -->
                                <SalesTaxCodeRef> <!-- optional -->
                                        <ListID >IDTYPE</ListID> <!-- optional -->
                                        <FullName >STRTYPE</FullName> <!-- optional -->
                                </SalesTaxCodeRef>
                                <IsPaid >BOOLTYPE</IsPaid> <!-- optional -->
                                <ExternalGUID >GUIDTYPE</ExternalGUID> <!-- optional -->
                                <LinkedTxn> <!-- optional, may repeat -->
                                        <TxnID >IDTYPE</TxnID> <!-- required -->
                                        <!-- TxnType may have one of the following values: ARRefundCreditCard, Bill, BillPaymentCheck, BillPaymentCreditCard, BuildAssembly, Charge, Check, CreditCardCharge, CreditCardCredit, CreditMemo, Deposit, Estimate, InventoryAdjustment, Invoice, ItemReceipt, JournalEntry, LiabilityAdjustment, Paycheck, PayrollLiabilityCheck, PurchaseOrder, ReceivePayment, SalesOrder, SalesReceipt, SalesTaxPaymentCheck, Transfer, VendorCredit, YTDAdjustment -->
                                        <TxnType >ENUMTYPE</TxnType> <!-- required -->
                                        <TxnDate >DATETYPE</TxnDate> <!-- required -->
                                        <RefNumber >STRTYPE</RefNumber> <!-- optional -->
                                        <!-- LinkType may have one of the following values: AMTTYPE, QUANTYPE -->
                                        <LinkType >ENUMTYPE</LinkType> <!-- optional -->
                                        <Amount >AMTTYPE</Amount> <!-- required -->
                                </LinkedTxn>
                                <ExpenseLineRet> <!-- optional, may repeat -->
                                        <TxnLineID >IDTYPE</TxnLineID> <!-- required -->
                                        <AccountRef> <!-- optional -->
                                                <ListID >IDTYPE</ListID> <!-- optional -->
                                                <FullName >STRTYPE</FullName> <!-- optional -->
                                        </AccountRef>
                                        <Amount >AMTTYPE</Amount> <!-- optional -->
                                        <Memo >STRTYPE</Memo> <!-- optional -->
                                        <CustomerRef> <!-- optional -->
                                                <ListID >IDTYPE</ListID> <!-- optional -->
                                                <FullName >STRTYPE</FullName> <!-- optional -->
                                        </CustomerRef>
                                        <ClassRef> <!-- optional -->
                                                <ListID >IDTYPE</ListID> <!-- optional -->
                                                <FullName >STRTYPE</FullName> <!-- optional -->
                                        </ClassRef>
                                        <SalesTaxCodeRef> <!-- optional -->
                                                <ListID >IDTYPE</ListID> <!-- optional -->
                                                <FullName >STRTYPE</FullName> <!-- optional -->
                                        </SalesTaxCodeRef>
                                        <!-- BillableStatus may have one of the following values: Billable, NotBillable, HasBeenBilled -->
                                        <BillableStatus >ENUMTYPE</BillableStatus> <!-- optional -->
                                        <SalesRepRef> <!-- optional -->
                                                <ListID >IDTYPE</ListID> <!-- optional -->
                                                <FullName >STRTYPE</FullName> <!-- optional -->
                                        </SalesRepRef>
                                        <DataExtRet> <!-- optional, may repeat -->
                                                <OwnerID >GUIDTYPE</OwnerID> <!-- optional -->
                                                <DataExtName >STRTYPE</DataExtName> <!-- required -->
                                                <!-- DataExtType may have one of the following values: AMTTYPE, DATETIMETYPE, INTTYPE, PERCENTTYPE, PRICETYPE, QUANTYPE, STR1024TYPE, STR255TYPE -->
                                                <DataExtType >ENUMTYPE</DataExtType> <!-- required -->
                                                <DataExtValue >STRTYPE</DataExtValue> <!-- required -->
                                        </DataExtRet>
                                </ExpenseLineRet>
                                <!-- BEGIN OR -->
                                        <ItemLineRet> <!-- optional -->
                                                <TxnLineID >IDTYPE</TxnLineID> <!-- required -->
                                                <ItemRef> <!-- optional -->
                                                        <ListID >IDTYPE</ListID> <!-- optional -->
                                                        <FullName >STRTYPE</FullName> <!-- optional -->
                                                </ItemRef>
                                                <InventorySiteRef> <!-- optional -->
                                                        <ListID >IDTYPE</ListID> <!-- optional -->
                                                        <FullName >STRTYPE</FullName> <!-- optional -->
                                                </InventorySiteRef>
                                                <InventorySiteLocationRef> <!-- optional -->
                                                        <ListID >IDTYPE</ListID> <!-- optional -->
                                                        <FullName >STRTYPE</FullName> <!-- optional -->
                                                </InventorySiteLocationRef>
                                                <!-- BEGIN OR -->
                                                        <SerialNumber >STRTYPE</SerialNumber> <!-- optional -->
                                                <!-- OR -->
                                                        <LotNumber >STRTYPE</LotNumber> <!-- optional -->
                                                <!-- END OR -->
                                                <ExpirationDateForSerialLotNumber >STRTYPE</ExpirationDateForSerialLotNumber> <!-- optional -->
                                                <Desc >STRTYPE</Desc> <!-- optional -->
                                                <Quantity >QUANTYPE</Quantity> <!-- optional -->
                                                <UnitOfMeasure >STRTYPE</UnitOfMeasure> <!-- optional -->
                                                <OverrideUOMSetRef> <!-- optional -->
                                                        <ListID >IDTYPE</ListID> <!-- optional -->
                                                        <FullName >STRTYPE</FullName> <!-- optional -->
                                                </OverrideUOMSetRef>
                                                <Cost >PRICETYPE</Cost> <!-- optional -->
                                                <Amount >AMTTYPE</Amount> <!-- optional -->
                                                <CustomerRef> <!-- optional -->
                                                        <ListID >IDTYPE</ListID> <!-- optional -->
                                                        <FullName >STRTYPE</FullName> <!-- optional -->
                                                </CustomerRef>
                                                <ClassRef> <!-- optional -->
                                                        <ListID >IDTYPE</ListID> <!-- optional -->
                                                        <FullName >STRTYPE</FullName> <!-- optional -->
                                                </ClassRef>
                                                <SalesTaxCodeRef> <!-- optional -->
                                                        <ListID >IDTYPE</ListID> <!-- optional -->
                                                        <FullName >STRTYPE</FullName> <!-- optional -->
                                                </SalesTaxCodeRef>
                                                <!-- BillableStatus may have one of the following values: Billable, NotBillable, HasBeenBilled -->
                                                <BillableStatus >ENUMTYPE</BillableStatus> <!-- optional -->
                                                <SalesRepRef> <!-- optional -->
                                                        <ListID >IDTYPE</ListID> <!-- optional -->
                                                        <FullName >STRTYPE</FullName> <!-- optional -->
                                                </SalesRepRef>
                                                <DataExtRet> <!-- optional, may repeat -->
                                                        <OwnerID >GUIDTYPE</OwnerID> <!-- optional -->
                                                        <DataExtName >STRTYPE</DataExtName> <!-- required -->
                                                        <!-- DataExtType may have one of the following values: AMTTYPE, DATETIMETYPE, INTTYPE, PERCENTTYPE, PRICETYPE, QUANTYPE, STR1024TYPE, STR255TYPE -->
                                                        <DataExtType >ENUMTYPE</DataExtType> <!-- required -->
                                                        <DataExtValue >STRTYPE</DataExtValue> <!-- required -->
                                                </DataExtRet>
                                        </ItemLineRet>
                                <!-- OR -->
                                        <ItemGroupLineRet> <!-- optional -->
                                                <TxnLineID >IDTYPE</TxnLineID> <!-- required -->
                                                <ItemGroupRef> <!-- required -->
                                                        <ListID >IDTYPE</ListID> <!-- optional -->
                                                        <FullName >STRTYPE</FullName> <!-- optional -->
                                                </ItemGroupRef>
                                                <Desc >STRTYPE</Desc> <!-- optional -->
                                                <Quantity >QUANTYPE</Quantity> <!-- optional -->
                                                <UnitOfMeasure >STRTYPE</UnitOfMeasure> <!-- optional -->
                                                <OverrideUOMSetRef> <!-- optional -->
                                                        <ListID >IDTYPE</ListID> <!-- optional -->
                                                        <FullName >STRTYPE</FullName> <!-- optional -->
                                                </OverrideUOMSetRef>
                                                <TotalAmount >AMTTYPE</TotalAmount> <!-- required -->
                                                <ItemLineRet> <!-- optional, may repeat -->
                                                        <TxnLineID >IDTYPE</TxnLineID> <!-- required -->
                                                        <ItemRef> <!-- optional -->
                                                                <ListID >IDTYPE</ListID> <!-- optional -->
                                                                <FullName >STRTYPE</FullName> <!-- optional -->
                                                        </ItemRef>
                                                        <InventorySiteRef> <!-- optional -->
                                                                <ListID >IDTYPE</ListID> <!-- optional -->
                                                                <FullName >STRTYPE</FullName> <!-- optional -->
                                                        </InventorySiteRef>
                                                        <InventorySiteLocationRef> <!-- optional -->
                                                                <ListID >IDTYPE</ListID> <!-- optional -->
                                                                <FullName >STRTYPE</FullName> <!-- optional -->
                                                        </InventorySiteLocationRef>
                                                        <!-- BEGIN OR -->
                                                                <SerialNumber >STRTYPE</SerialNumber> <!-- optional -->
                                                        <!-- OR -->
                                                                <LotNumber >STRTYPE</LotNumber> <!-- optional -->
                                                        <!-- END OR -->
                                                        <ExpirationDateForSerialLotNumber >STRTYPE</ExpirationDateForSerialLotNumber> <!-- optional -->
                                                        <Desc >STRTYPE</Desc> <!-- optional -->
                                                        <Quantity >QUANTYPE</Quantity> <!-- optional -->
                                                        <UnitOfMeasure >STRTYPE</UnitOfMeasure> <!-- optional -->
                                                        <OverrideUOMSetRef> <!-- optional -->
                                                                <ListID >IDTYPE</ListID> <!-- optional -->
                                                                <FullName >STRTYPE</FullName> <!-- optional -->
                                                        </OverrideUOMSetRef>
                                                        <Cost >PRICETYPE</Cost> <!-- optional -->
                                                        <Amount >AMTTYPE</Amount> <!-- optional -->
                                                        <CustomerRef> <!-- optional -->
                                                                <ListID >IDTYPE</ListID> <!-- optional -->
                                                                <FullName >STRTYPE</FullName> <!-- optional -->
                                                        </CustomerRef>
                                                        <ClassRef> <!-- optional -->
                                                                <ListID >IDTYPE</ListID> <!-- optional -->
                                                                <FullName >STRTYPE</FullName> <!-- optional -->
                                                        </ClassRef>
                                                        <SalesTaxCodeRef> <!-- optional -->
                                                                <ListID >IDTYPE</ListID> <!-- optional -->
                                                                <FullName >STRTYPE</FullName> <!-- optional -->
                                                        </SalesTaxCodeRef>
                                                        <!-- BillableStatus may have one of the following values: Billable, NotBillable, HasBeenBilled -->
                                                        <BillableStatus >ENUMTYPE</BillableStatus> <!-- optional -->
                                                        <SalesRepRef> <!-- optional -->
                                                                <ListID >IDTYPE</ListID> <!-- optional -->
                                                                <FullName >STRTYPE</FullName> <!-- optional -->
                                                        </SalesRepRef>
                                                        <DataExtRet> <!-- optional, may repeat -->
                                                                <OwnerID >GUIDTYPE</OwnerID> <!-- optional -->
                                                                <DataExtName >STRTYPE</DataExtName> <!-- required -->
                                                                <!-- DataExtType may have one of the following values: AMTTYPE, DATETIMETYPE, INTTYPE, PERCENTTYPE, PRICETYPE, QUANTYPE, STR1024TYPE, STR255TYPE -->
                                                                <DataExtType >ENUMTYPE</DataExtType> <!-- required -->
                                                                <DataExtValue >STRTYPE</DataExtValue> <!-- required -->
                                                        </DataExtRet>
                                                </ItemLineRet>
                                                <DataExt> <!-- optional, may repeat -->
                                                        <OwnerID >GUIDTYPE</OwnerID> <!-- required -->
                                                        <DataExtName >STRTYPE</DataExtName> <!-- required -->
                                                        <DataExtValue >STRTYPE</DataExtValue> <!-- required -->
                                                </DataExt>
                                        </ItemGroupLineRet>
                                <!-- END OR -->
                                <OpenAmount >AMTTYPE</OpenAmount> <!-- optional -->
                                <DataExtRet> <!-- optional, may repeat -->
                                        <OwnerID >GUIDTYPE</OwnerID> <!-- optional -->
                                        <DataExtName >STRTYPE</DataExtName> <!-- required -->
                                        <!-- DataExtType may have one of the following values: AMTTYPE, DATETIMETYPE, INTTYPE, PERCENTTYPE, PRICETYPE, QUANTYPE, STR1024TYPE, STR255TYPE -->
                                        <DataExtType >ENUMTYPE</DataExtType> <!-- required -->
                                        <DataExtValue >STRTYPE</DataExtValue> <!-- required -->
                                </DataExtRet>
                        </BillRet>
                </BillQueryRs>
        </QBXMLMsgsRq>
</QBXML>

```

## Check Query
### XMLOps
```
<?xml version="1.0" encoding="utf-8"?>
<?qbxml version="16.0"?>
<QBXML>
        <QBXMLMsgsRq onError="stopOnError">
                <CheckQueryRq metaData="ENUMTYPE" iterator="ENUMTYPE" iteratorID="UUIDTYPE">
                        <!-- BEGIN OR -->
                                <TxnID >IDTYPE</TxnID> <!-- optional, may repeat -->
                        <!-- OR -->
                                <RefNumber >STRTYPE</RefNumber> <!-- optional, may repeat -->
                        <!-- OR -->
                                <RefNumberCaseSensitive >STRTYPE</RefNumberCaseSensitive> <!-- optional, may repeat -->
                        <!-- OR -->
                                <MaxReturned >INTTYPE</MaxReturned> <!-- optional -->
                                <!-- BEGIN OR -->
                                        <ModifiedDateRangeFilter> <!-- optional -->
                                                <FromModifiedDate >DATETIMETYPE</FromModifiedDate> <!-- optional -->
                                                <ToModifiedDate >DATETIMETYPE</ToModifiedDate> <!-- optional -->
                                        </ModifiedDateRangeFilter>
                                <!-- OR -->
                                        <TxnDateRangeFilter> <!-- optional -->
                                                <!-- BEGIN OR -->
                                                        <FromTxnDate >DATETYPE</FromTxnDate> <!-- optional -->
                                                        <ToTxnDate >DATETYPE</ToTxnDate> <!-- optional -->
                                                <!-- OR -->
                                                        <!-- DateMacro may have one of the following values: All, Today, ThisWeek, ThisWeekToDate, ThisMonth, ThisMonthToDate, ThisCalendarQuarter, ThisCalendarQuarterToDate, ThisFiscalQuarter, ThisFiscalQuarterToDate, ThisCalendarYear, ThisCalendarYearToDate, ThisFiscalYear, ThisFiscalYearToDate, Yesterday, LastWeek, LastWeekToDate, LastMonth, LastMonthToDate, LastCalendarQuarter, LastCalendarQuarterToDate, LastFiscalQuarter, LastFiscalQuarterToDate, LastCalendarYear, LastCalendarYearToDate, LastFiscalYear, LastFiscalYearToDate, NextWeek, NextFourWeeks, NextMonth, NextCalendarQuarter, NextCalendarYear, NextFiscalQuarter, NextFiscalYear -->
                                                        <DateMacro >ENUMTYPE</DateMacro> <!-- optional -->
                                                <!-- END OR -->
                                        </TxnDateRangeFilter>
                                <!-- END OR -->
                                <EntityFilter> <!-- optional -->
                                        <!-- BEGIN OR -->
                                                <ListID >IDTYPE</ListID> <!-- optional, may repeat -->
                                        <!-- OR -->
                                                <FullName >STRTYPE</FullName> <!-- optional, may repeat -->
                                        <!-- OR -->
                                                <ListIDWithChildren >IDTYPE</ListIDWithChildren> <!-- optional -->
                                        <!-- OR -->
                                                <FullNameWithChildren >STRTYPE</FullNameWithChildren> <!-- optional -->
                                        <!-- END OR -->
                                </EntityFilter>
                                <AccountFilter> <!-- optional -->
                                        <!-- BEGIN OR -->
                                                <ListID >IDTYPE</ListID> <!-- optional, may repeat -->
                                        <!-- OR -->
                                                <FullName >STRTYPE</FullName> <!-- optional, may repeat -->
                                        <!-- OR -->
                                                <ListIDWithChildren >IDTYPE</ListIDWithChildren> <!-- optional -->
                                        <!-- OR -->
                                                <FullNameWithChildren >STRTYPE</FullNameWithChildren> <!-- optional -->
                                        <!-- END OR -->
                                </AccountFilter>
                                <!-- BEGIN OR -->
                                        <RefNumberFilter> <!-- optional -->
                                                <!-- MatchCriterion may have one of the following values: StartsWith, Contains, EndsWith -->
                                                <MatchCriterion >ENUMTYPE</MatchCriterion> <!-- required -->
                                                <RefNumber >STRTYPE</RefNumber> <!-- required -->
                                        </RefNumberFilter>
                                <!-- OR -->
                                        <RefNumberRangeFilter> <!-- optional -->
                                                <FromRefNumber >STRTYPE</FromRefNumber> <!-- optional -->
                                                <ToRefNumber >STRTYPE</ToRefNumber> <!-- optional -->
                                        </RefNumberRangeFilter>
                                <!-- END OR -->
                                <CurrencyFilter> <!-- optional -->
                                        <!-- BEGIN OR -->
                                                <ListID >IDTYPE</ListID> <!-- optional, may repeat -->
                                        <!-- OR -->
                                                <FullName >STRTYPE</FullName> <!-- optional, may repeat -->
                                        <!-- END OR -->
                                </CurrencyFilter>
                        <!-- END OR -->
                        <IncludeLineItems >BOOLTYPE</IncludeLineItems> <!-- optional -->
                        <IncludeLinkedTxns >BOOLTYPE</IncludeLinkedTxns> <!-- optional -->
                        <IncludeRetElement >STRTYPE</IncludeRetElement> <!-- optional, may repeat -->
                        <OwnerID >GUIDTYPE</OwnerID> <!-- optional, may repeat -->
                </CheckQueryRq>

                <CheckQueryRs statusCode="INTTYPE" statusSeverity="STRTYPE" statusMessage="STRTYPE" retCount="INTTYPE" iteratorRemainingCount="INTTYPE" iteratorID="UUIDTYPE">
                        <CheckRet> <!-- optional, may repeat -->
                                <TxnID >IDTYPE</TxnID> <!-- required -->
                                <TimeCreated >DATETIMETYPE</TimeCreated> <!-- required -->
                                <TimeModified >DATETIMETYPE</TimeModified> <!-- required -->
                                <EditSequence >STRTYPE</EditSequence> <!-- required -->
                                <TxnNumber >INTTYPE</TxnNumber> <!-- optional -->
                                <AccountRef> <!-- required -->
                                        <ListID >IDTYPE</ListID> <!-- optional -->
                                        <FullName >STRTYPE</FullName> <!-- optional -->
                                </AccountRef>
                                <PayeeEntityRef> <!-- optional -->
                                        <ListID >IDTYPE</ListID> <!-- optional -->
                                        <FullName >STRTYPE</FullName> <!-- optional -->
                                </PayeeEntityRef>
                                <RefNumber >STRTYPE</RefNumber> <!-- optional -->
                                <TxnDate >DATETYPE</TxnDate> <!-- required -->
                                <Amount >AMTTYPE</Amount> <!-- required -->
                                <CurrencyRef> <!-- optional -->
                                        <ListID >IDTYPE</ListID> <!-- optional -->
                                        <FullName >STRTYPE</FullName> <!-- optional -->
                                </CurrencyRef>
                                <ExchangeRate >FLOATTYPE</ExchangeRate> <!-- optional -->
                                <AmountInHomeCurrency >AMTTYPE</AmountInHomeCurrency> <!-- optional -->
                                <Memo >STRTYPE</Memo> <!-- optional -->
                                <Address> <!-- optional -->
                                        <Addr1 >STRTYPE</Addr1> <!-- optional -->
                                        <Addr2 >STRTYPE</Addr2> <!-- optional -->
                                        <Addr3 >STRTYPE</Addr3> <!-- optional -->
                                        <Addr4 >STRTYPE</Addr4> <!-- optional -->
                                        <Addr5 >STRTYPE</Addr5> <!-- optional -->
                                        <City >STRTYPE</City> <!-- optional -->
                                        <State >STRTYPE</State> <!-- optional -->
                                        <PostalCode >STRTYPE</PostalCode> <!-- optional -->
                                        <Country >STRTYPE</Country> <!-- optional -->
                                        <Note >STRTYPE</Note> <!-- optional -->
                                </Address>
                                <AddressBlock> <!-- optional -->
                                        <Addr1 >STRTYPE</Addr1> <!-- optional -->
                                        <Addr2 >STRTYPE</Addr2> <!-- optional -->
                                        <Addr3 >STRTYPE</Addr3> <!-- optional -->
                                        <Addr4 >STRTYPE</Addr4> <!-- optional -->
                                        <Addr5 >STRTYPE</Addr5> <!-- optional -->
                                </AddressBlock>
                                <IsPending>BOOLTYPE</IsPending> <!-- optional -->
                                <IsToBePrinted >BOOLTYPE</IsToBePrinted> <!-- optional -->
                                <IsTaxIncluded >BOOLTYPE</IsTaxIncluded> <!-- optional -->
                                <SalesTaxCodeRef> <!-- optional -->
                                        <ListID >IDTYPE</ListID> <!-- optional -->
                                        <FullName >STRTYPE</FullName> <!-- optional -->
                                </SalesTaxCodeRef>
                                <ExternalGUID >GUIDTYPE</ExternalGUID> <!-- optional -->
                                <LinkedTxn> <!-- optional, may repeat -->
                                        <TxnID >IDTYPE</TxnID> <!-- required -->
                                        <!-- TxnType may have one of the following values: ARRefundCreditCard, Bill, BillPaymentCheck, BillPaymentCreditCard, BuildAssembly, Charge, Check, CreditCardCharge, CreditCardCredit, CreditMemo, Deposit, Estimate, InventoryAdjustment, Invoice, ItemReceipt, JournalEntry, LiabilityAdjustment, Paycheck, PayrollLiabilityCheck, PurchaseOrder, ReceivePayment, SalesOrder, SalesReceipt, SalesTaxPaymentCheck, Transfer, VendorCredit, YTDAdjustment -->
                                        <TxnType >ENUMTYPE</TxnType> <!-- required -->
                                        <TxnDate >DATETYPE</TxnDate> <!-- required -->
                                        <RefNumber >STRTYPE</RefNumber> <!-- optional -->
                                        <!-- LinkType may have one of the following values: AMTTYPE, QUANTYPE -->
                                        <LinkType >ENUMTYPE</LinkType> <!-- optional -->
                                        <Amount >AMTTYPE</Amount> <!-- required -->
                                </LinkedTxn>
                                <ExpenseLineRet> <!-- optional, may repeat -->
                                        <TxnLineID >IDTYPE</TxnLineID> <!-- required -->
                                        <AccountRef> <!-- optional -->
                                                <ListID >IDTYPE</ListID> <!-- optional -->
                                                <FullName >STRTYPE</FullName> <!-- optional -->
                                        </AccountRef>
                                        <Amount >AMTTYPE</Amount> <!-- optional -->
                                        <Memo >STRTYPE</Memo> <!-- optional -->
                                        <CustomerRef> <!-- optional -->
                                                <ListID >IDTYPE</ListID> <!-- optional -->
                                                <FullName >STRTYPE</FullName> <!-- optional -->
                                        </CustomerRef>
                                        <ClassRef> <!-- optional -->
                                                <ListID >IDTYPE</ListID> <!-- optional -->
                                                <FullName >STRTYPE</FullName> <!-- optional -->
                                        </ClassRef>
                                        <SalesTaxCodeRef> <!-- optional -->
                                                <ListID >IDTYPE</ListID> <!-- optional -->
                                                <FullName >STRTYPE</FullName> <!-- optional -->
                                        </SalesTaxCodeRef>
                                        <!-- BillableStatus may have one of the following values: Billable, NotBillable, HasBeenBilled -->
                                        <BillableStatus >ENUMTYPE</BillableStatus> <!-- optional -->
                                        <SalesRepRef> <!-- optional -->
                                                <ListID >IDTYPE</ListID> <!-- optional -->
                                                <FullName >STRTYPE</FullName> <!-- optional -->
                                        </SalesRepRef>
                                        <DataExtRet> <!-- optional, may repeat -->
                                                <OwnerID >GUIDTYPE</OwnerID> <!-- optional -->
                                                <DataExtName >STRTYPE</DataExtName> <!-- required -->
                                                <!-- DataExtType may have one of the following values: AMTTYPE, DATETIMETYPE, INTTYPE, PERCENTTYPE, PRICETYPE, QUANTYPE, STR1024TYPE, STR255TYPE -->
                                                <DataExtType >ENUMTYPE</DataExtType> <!-- required -->
                                                <DataExtValue >STRTYPE</DataExtValue> <!-- required -->
                                        </DataExtRet>
                                </ExpenseLineRet>
                                <!-- BEGIN OR -->
                                        <ItemLineRet> <!-- optional -->
                                                <TxnLineID >IDTYPE</TxnLineID> <!-- required -->
                                                <ItemRef> <!-- optional -->
                                                        <ListID >IDTYPE</ListID> <!-- optional -->
                                                        <FullName >STRTYPE</FullName> <!-- optional -->
                                                </ItemRef>
                                                <InventorySiteRef> <!-- optional -->
                                                        <ListID >IDTYPE</ListID> <!-- optional -->
                                                        <FullName >STRTYPE</FullName> <!-- optional -->
                                                </InventorySiteRef>
                                                <InventorySiteLocationRef> <!-- optional -->
                                                        <ListID >IDTYPE</ListID> <!-- optional -->
                                                        <FullName >STRTYPE</FullName> <!-- optional -->
                                                </InventorySiteLocationRef>
                                                <!-- BEGIN OR -->
                                                        <SerialNumber >STRTYPE</SerialNumber> <!-- optional -->
                                                <!-- OR -->
                                                        <LotNumber >STRTYPE</LotNumber> <!-- optional -->
                                                <!-- END OR -->
                                                <ExpirationDateForSerialLotNumber >STRTYPE</ExpirationDateForSerialLotNumber> <!-- optional -->
                                                <Desc >STRTYPE</Desc> <!-- optional -->
                                                <Quantity >QUANTYPE</Quantity> <!-- optional -->
                                                <UnitOfMeasure >STRTYPE</UnitOfMeasure> <!-- optional -->
                                                <OverrideUOMSetRef> <!-- optional -->
                                                        <ListID >IDTYPE</ListID> <!-- optional -->
                                                        <FullName >STRTYPE</FullName> <!-- optional -->
                                                </OverrideUOMSetRef>
                                                <Cost >PRICETYPE</Cost> <!-- optional -->
                                                <Amount >AMTTYPE</Amount> <!-- optional -->
                                                <CustomerRef> <!-- optional -->
                                                        <ListID >IDTYPE</ListID> <!-- optional -->
                                                        <FullName >STRTYPE</FullName> <!-- optional -->
                                                </CustomerRef>
                                                <ClassRef> <!-- optional -->
                                                        <ListID >IDTYPE</ListID> <!-- optional -->
                                                        <FullName >STRTYPE</FullName> <!-- optional -->
                                                </ClassRef>
                                                <SalesTaxCodeRef> <!-- optional -->
                                                        <ListID >IDTYPE</ListID> <!-- optional -->
                                                        <FullName >STRTYPE</FullName> <!-- optional -->
                                                </SalesTaxCodeRef>
                                                <!-- BillableStatus may have one of the following values: Billable, NotBillable, HasBeenBilled -->
                                                <BillableStatus >ENUMTYPE</BillableStatus> <!-- optional -->
                                                <SalesRepRef> <!-- optional -->
                                                        <ListID >IDTYPE</ListID> <!-- optional -->
                                                        <FullName >STRTYPE</FullName> <!-- optional -->
                                                </SalesRepRef>
                                                <DataExtRet> <!-- optional, may repeat -->
                                                        <OwnerID >GUIDTYPE</OwnerID> <!-- optional -->
                                                        <DataExtName >STRTYPE</DataExtName> <!-- required -->
                                                        <!-- DataExtType may have one of the following values: AMTTYPE, DATETIMETYPE, INTTYPE, PERCENTTYPE, PRICETYPE, QUANTYPE, STR1024TYPE, STR255TYPE -->
                                                        <DataExtType >ENUMTYPE</DataExtType> <!-- required -->
                                                        <DataExtValue >STRTYPE</DataExtValue> <!-- required -->
                                                </DataExtRet>
                                        </ItemLineRet>
                                <!-- OR -->
                                        <ItemGroupLineRet> <!-- optional -->
                                                <TxnLineID >IDTYPE</TxnLineID> <!-- required -->
                                                <ItemGroupRef> <!-- required -->
                                                        <ListID >IDTYPE</ListID> <!-- optional -->
                                                        <FullName >STRTYPE</FullName> <!-- optional -->
                                                </ItemGroupRef>
                                                <Desc >STRTYPE</Desc> <!-- optional -->
                                                <Quantity >QUANTYPE</Quantity> <!-- optional -->
                                                <UnitOfMeasure >STRTYPE</UnitOfMeasure> <!-- optional -->
                                                <OverrideUOMSetRef> <!-- optional -->
                                                        <ListID >IDTYPE</ListID> <!-- optional -->
                                                        <FullName >STRTYPE</FullName> <!-- optional -->
                                                </OverrideUOMSetRef>
                                                <TotalAmount >AMTTYPE</TotalAmount> <!-- required -->
                                                <ItemLineRet> <!-- optional, may repeat -->
                                                        <TxnLineID >IDTYPE</TxnLineID> <!-- required -->
                                                        <ItemRef> <!-- optional -->
                                                                <ListID >IDTYPE</ListID> <!-- optional -->
                                                                <FullName >STRTYPE</FullName> <!-- optional -->
                                                        </ItemRef>
                                                        <InventorySiteRef> <!-- optional -->
                                                                <ListID >IDTYPE</ListID> <!-- optional -->
                                                                <FullName >STRTYPE</FullName> <!-- optional -->
                                                        </InventorySiteRef>
                                                        <InventorySiteLocationRef> <!-- optional -->
                                                                <ListID >IDTYPE</ListID> <!-- optional -->
                                                                <FullName >STRTYPE</FullName> <!-- optional -->
                                                        </InventorySiteLocationRef>
                                                        <!-- BEGIN OR -->
                                                                <SerialNumber >STRTYPE</SerialNumber> <!-- optional -->
                                                        <!-- OR -->
                                                                <LotNumber >STRTYPE</LotNumber> <!-- optional -->
                                                        <!-- END OR -->
                                                        <ExpirationDateForSerialLotNumber >STRTYPE</ExpirationDateForSerialLotNumber> <!-- optional -->
                                                        <Desc >STRTYPE</Desc> <!-- optional -->
                                                        <Quantity >QUANTYPE</Quantity> <!-- optional -->
                                                        <UnitOfMeasure >STRTYPE</UnitOfMeasure> <!-- optional -->
                                                        <OverrideUOMSetRef> <!-- optional -->
                                                                <ListID >IDTYPE</ListID> <!-- optional -->
                                                                <FullName >STRTYPE</FullName> <!-- optional -->
                                                        </OverrideUOMSetRef>
                                                        <Cost >PRICETYPE</Cost> <!-- optional -->
                                                        <Amount >AMTTYPE</Amount> <!-- optional -->
                                                        <CustomerRef> <!-- optional -->
                                                                <ListID >IDTYPE</ListID> <!-- optional -->
                                                                <FullName >STRTYPE</FullName> <!-- optional -->
                                                        </CustomerRef>
                                                        <ClassRef> <!-- optional -->
                                                                <ListID >IDTYPE</ListID> <!-- optional -->
                                                                <FullName >STRTYPE</FullName> <!-- optional -->
                                                        </ClassRef>
                                                        <SalesTaxCodeRef> <!-- optional -->
                                                                <ListID >IDTYPE</ListID> <!-- optional -->
                                                                <FullName >STRTYPE</FullName> <!-- optional -->
                                                        </SalesTaxCodeRef>
                                                        <!-- BillableStatus may have one of the following values: Billable, NotBillable, HasBeenBilled -->
                                                        <BillableStatus >ENUMTYPE</BillableStatus> <!-- optional -->
                                                        <SalesRepRef> <!-- optional -->
                                                                <ListID >IDTYPE</ListID> <!-- optional -->
                                                                <FullName >STRTYPE</FullName> <!-- optional -->
                                                        </SalesRepRef>
                                                        <DataExtRet> <!-- optional, may repeat -->
                                                                <OwnerID >GUIDTYPE</OwnerID> <!-- optional -->
                                                                <DataExtName >STRTYPE</DataExtName> <!-- required -->
                                                                <!-- DataExtType may have one of the following values: AMTTYPE, DATETIMETYPE, INTTYPE, PERCENTTYPE, PRICETYPE, QUANTYPE, STR1024TYPE, STR255TYPE -->
                                                                <DataExtType >ENUMTYPE</DataExtType> <!-- required -->
                                                                <DataExtValue >STRTYPE</DataExtValue> <!-- required -->
                                                        </DataExtRet>
                                                </ItemLineRet>
                                                <DataExt> <!-- optional, may repeat -->
                                                        <OwnerID >GUIDTYPE</OwnerID> <!-- required -->
                                                        <DataExtName >STRTYPE</DataExtName> <!-- required -->
                                                        <DataExtValue >STRTYPE</DataExtValue> <!-- required -->
                                                </DataExt>
                                        </ItemGroupLineRet>
                                <!-- END OR -->
                                <DataExtRet> <!-- optional, may repeat -->
                                        <OwnerID >GUIDTYPE</OwnerID> <!-- optional -->
                                        <DataExtName >STRTYPE</DataExtName> <!-- required -->
                                        <!-- DataExtType may have one of the following values: AMTTYPE, DATETIMETYPE, INTTYPE, PERCENTTYPE, PRICETYPE, QUANTYPE, STR1024TYPE, STR255TYPE -->
                                        <DataExtType >ENUMTYPE</DataExtType> <!-- required -->
                                        <DataExtValue >STRTYPE</DataExtValue> <!-- required -->
                                </DataExtRet>
                        </CheckRet>
                </CheckQueryRs>
        </QBXMLMsgsRq>
</QBXML>
```

## ClassQuery
### XMLOps
```
<?xml version="1.0" encoding="utf-8"?>
<?qbxml version="16.0"?>
<QBXML>
        <QBXMLMsgsRq onError="stopOnError">
                <ClassQueryRq metaData="ENUMTYPE">
                        <!-- BEGIN OR -->
                                <ListID >IDTYPE</ListID> <!-- optional, may repeat -->
                        <!-- OR -->
                                <FullName >STRTYPE</FullName> <!-- optional, may repeat -->
                        <!-- OR -->
                                <MaxReturned >INTTYPE</MaxReturned> <!-- optional -->
                                <!-- ActiveStatus may have one of the following values: ActiveOnly [DEFAULT], InactiveOnly, All -->
                                <ActiveStatus >ENUMTYPE</ActiveStatus> <!-- optional -->
                                <FromModifiedDate >DATETIMETYPE</FromModifiedDate> <!-- optional -->
                                <ToModifiedDate >DATETIMETYPE</ToModifiedDate> <!-- optional -->
                                <!-- BEGIN OR -->
                                        <NameFilter> <!-- optional -->
                                                <!-- MatchCriterion may have one of the following values: StartsWith, Contains, EndsWith -->
                                                <MatchCriterion >ENUMTYPE</MatchCriterion> <!-- required -->
                                                <Name >STRTYPE</Name> <!-- required -->
                                        </NameFilter>
                                <!-- OR -->
                                        <NameRangeFilter> <!-- optional -->
                                                <FromName >STRTYPE</FromName> <!-- optional -->
                                                <ToName >STRTYPE</ToName> <!-- optional -->
                                        </NameRangeFilter>
                                <!-- END OR -->
                        <!-- END OR -->
                        <IncludeRetElement >STRTYPE</IncludeRetElement> <!-- optional, may repeat -->
                </ClassQueryRq>

                <ClassQueryRs statusCode="INTTYPE" statusSeverity="STRTYPE" statusMessage="STRTYPE" retCount="INTTYPE">
                        <ClassRet> <!-- optional, may repeat -->
                                <ListID >IDTYPE</ListID> <!-- required -->
                                <TimeCreated >DATETIMETYPE</TimeCreated> <!-- required -->
                                <TimeModified >DATETIMETYPE</TimeModified> <!-- required -->
                                <EditSequence >STRTYPE</EditSequence> <!-- required -->
                                <Name >STRTYPE</Name> <!-- required -->
                                <FullName >STRTYPE</FullName> <!-- required -->
                                <IsActive >BOOLTYPE</IsActive> <!-- optional -->
                                <ParentRef> <!-- optional -->
                                        <ListID >IDTYPE</ListID> <!-- optional -->
                                        <FullName >STRTYPE</FullName> <!-- optional -->
                                </ParentRef>
                                <Sublevel >INTTYPE</Sublevel> <!-- required -->
                        </ClassRet>
                </ClassQueryRs>
        </QBXMLMsgsRq>
</QBXML>
```

## CompanyQuery
### XMLOps
```
<?xml version="1.0" encoding="utf-8"?>
<?qbxml version="16.0"?>
<QBXML>
        <QBXMLMsgsRq onError="stopOnError">
                <CompanyQueryRq>
                        <IncludeRetElement >STRTYPE</IncludeRetElement> <!-- optional, may repeat -->
                        <OwnerID >GUIDTYPE</OwnerID> <!-- optional, may repeat -->
                </CompanyQueryRq>

                <CompanyQueryRs statusCode="INTTYPE" statusSeverity="STRTYPE" statusMessage="STRTYPE">
                        <CompanyRet> <!-- optional -->
                                <IsSampleCompany >BOOLTYPE</IsSampleCompany> <!-- required -->
                                <CompanyName >STRTYPE</CompanyName> <!-- optional -->
                                <LegalCompanyName >STRTYPE</LegalCompanyName> <!-- optional -->
                                <Address> <!-- optional -->
                                        <Addr1 >STRTYPE</Addr1> <!-- optional -->
                                        <Addr2 >STRTYPE</Addr2> <!-- optional -->
                                        <Addr3 >STRTYPE</Addr3> <!-- optional -->
                                        <Addr4 >STRTYPE</Addr4> <!-- optional -->
                                        <Addr5 >STRTYPE</Addr5> <!-- optional -->
                                        <City >STRTYPE</City> <!-- optional -->
                                        <State >STRTYPE</State> <!-- optional -->
                                        <PostalCode >STRTYPE</PostalCode> <!-- optional -->
                                        <Country >STRTYPE</Country> <!-- optional -->
                                        <Note >STRTYPE</Note> <!-- optional -->
                                </Address>
                                <AddressBlock> <!-- optional -->
                                        <Addr1 >STRTYPE</Addr1> <!-- optional -->
                                        <Addr2 >STRTYPE</Addr2> <!-- optional -->
                                        <Addr3 >STRTYPE</Addr3> <!-- optional -->
                                        <Addr4 >STRTYPE</Addr4> <!-- optional -->
                                        <Addr5 >STRTYPE</Addr5> <!-- optional -->
                                </AddressBlock>
                                <LegalAddress> <!-- optional -->
                                        <Addr1 >STRTYPE</Addr1> <!-- optional -->
                                        <Addr2 >STRTYPE</Addr2> <!-- optional -->
                                        <Addr3 >STRTYPE</Addr3> <!-- optional -->
                                        <Addr4 >STRTYPE</Addr4> <!-- optional -->
                                        <Addr5 >STRTYPE</Addr5> <!-- optional -->
                                        <City >STRTYPE</City> <!-- optional -->
                                        <State >STRTYPE</State> <!-- optional -->
                                        <PostalCode >STRTYPE</PostalCode> <!-- optional -->
                                        <Country >STRTYPE</Country> <!-- optional -->
                                        <Note >STRTYPE</Note> <!-- optional -->
                                </LegalAddress>
                                <CompanyAddressForCustomer> <!-- optional -->
                                        <Addr1 >STRTYPE</Addr1> <!-- optional -->
                                        <Addr2 >STRTYPE</Addr2> <!-- optional -->
                                        <Addr3 >STRTYPE</Addr3> <!-- optional -->
                                        <Addr4 >STRTYPE</Addr4> <!-- optional -->
                                        <Addr5 >STRTYPE</Addr5> <!-- optional -->
                                        <City >STRTYPE</City> <!-- optional -->
                                        <State >STRTYPE</State> <!-- optional -->
                                        <PostalCode >STRTYPE</PostalCode> <!-- optional -->
                                        <Country >STRTYPE</Country> <!-- optional -->
                                        <Note >STRTYPE</Note> <!-- optional -->
                                </CompanyAddressForCustomer>
                                <CompanyAddressBlockForCustomer> <!-- optional -->
                                        <Addr1 >STRTYPE</Addr1> <!-- optional -->
                                        <Addr2 >STRTYPE</Addr2> <!-- optional -->
                                        <Addr3 >STRTYPE</Addr3> <!-- optional -->
                                        <Addr4 >STRTYPE</Addr4> <!-- optional -->
                                        <Addr5 >STRTYPE</Addr5> <!-- optional -->
                                </CompanyAddressBlockForCustomer>
                                <Phone >STRTYPE</Phone> <!-- optional -->
                                <Fax >STRTYPE</Fax> <!-- optional -->
                                <Email >STRTYPE</Email> <!-- optional -->
                                <CompanyWebSite >STRTYPE</CompanyWebSite> <!-- optional -->
                                <!-- FirstMonthFiscalYear may have one of the following values: January, February, March, April, May, June, July, August, September, October, November, December -->
                                <FirstMonthFiscalYear >ENUMTYPE</FirstMonthFiscalYear> <!-- optional -->
                                <!-- FirstMonthIncomeTaxYear may have one of the following values: January, February, March, April, May, June, July, August, September, October, November, December -->
                                <FirstMonthIncomeTaxYear >ENUMTYPE</FirstMonthIncomeTaxYear> <!-- optional -->
                                <CompanyType >STRTYPE</CompanyType> <!-- optional -->
                                <EIN >STRTYPE</EIN> <!-- optional -->
                                <SSN >STRTYPE</SSN> <!-- optional -->
                                <!-- TaxForm may have one of the following values: Form1040, Form1065, Form1120, Form1120S, Form990, Form990PF, Form990T, OtherOrNone -->
                                <TaxForm >ENUMTYPE</TaxForm> <!-- optional -->
                                <SubscribedServices> <!-- optional -->
                                        <Service> <!-- optional, may repeat -->
                                                <Name >STRTYPE</Name> <!-- required -->
                                                <Domain >STRTYPE</Domain> <!-- required -->
                                                <!-- ServiceStatus may have one of the following values: Active, Expired, Never, Pending, Suspended, Terminated, Trial -->
                                                <ServiceStatus >ENUMTYPE</ServiceStatus> <!-- required -->
                                        </Service>
                                </SubscribedServices>
                                <AccountantCopy> <!-- optional -->
                                        <AccountantCopyExists >BOOLTYPE</AccountantCopyExists> <!-- required -->
                                        <DividingDate >DATETYPE</DividingDate> <!-- optional -->
                                </AccountantCopy>
                                <DataExtRet> <!-- optional, may repeat -->
                                        <OwnerID >GUIDTYPE</OwnerID> <!-- optional -->
                                        <DataExtName >STRTYPE</DataExtName> <!-- required -->
                                        <!-- DataExtType may have one of the following values: AMTTYPE, DATETIMETYPE, INTTYPE, PERCENTTYPE, PRICETYPE, QUANTYPE, STR1024TYPE, STR255TYPE -->
                                        <DataExtType >ENUMTYPE</DataExtType> <!-- required -->
                                        <DataExtValue >STRTYPE</DataExtValue> <!-- required -->
                                </DataExtRet>
                        </CompanyRet>
                </CompanyQueryRs>
        </QBXMLMsgsRq>
</QBXML>
```

## CreditCard Charge Query
### XMLOps
<?xml version="1.0" encoding="utf-8"?>
<?qbxml version="16.0"?>
<QBXML>
        <QBXMLMsgsRq onError="stopOnError">
                <CreditCardChargeQueryRq metaData="ENUMTYPE" iterator="ENUMTYPE" iteratorID="UUIDTYPE">
                        <!-- BEGIN OR -->
                                <TxnID >IDTYPE</TxnID> <!-- optional, may repeat -->
                        <!-- OR -->
                                <RefNumber >STRTYPE</RefNumber> <!-- optional, may repeat -->
                        <!-- OR -->
                                <RefNumberCaseSensitive >STRTYPE</RefNumberCaseSensitive> <!-- optional, may repeat -->
                        <!-- OR -->
                                <MaxReturned >INTTYPE</MaxReturned> <!-- optional -->
                                <!-- BEGIN OR -->
                                        <ModifiedDateRangeFilter> <!-- optional -->
                                                <FromModifiedDate >DATETIMETYPE</FromModifiedDate> <!-- optional -->
                                                <ToModifiedDate >DATETIMETYPE</ToModifiedDate> <!-- optional -->
                                        </ModifiedDateRangeFilter>
                                <!-- OR -->
                                        <TxnDateRangeFilter> <!-- optional -->
                                                <!-- BEGIN OR -->
                                                        <FromTxnDate >DATETYPE</FromTxnDate> <!-- optional -->
                                                        <ToTxnDate >DATETYPE</ToTxnDate> <!-- optional -->
                                                <!-- OR -->
                                                        <!-- DateMacro may have one of the following values: All, Today, ThisWeek, ThisWeekToDate, ThisMonth, ThisMonthToDate, ThisCalendarQuarter, ThisCalendarQuarterToDate, ThisFiscalQuarter, ThisFiscalQuarterToDate, ThisCalendarYear, ThisCalendarYearToDate, ThisFiscalYear, ThisFiscalYearToDate, Yesterday, LastWeek, LastWeekToDate, LastMonth, LastMonthToDate, LastCalendarQuarter, LastCalendarQuarterToDate, LastFiscalQuarter, LastFiscalQuarterToDate, LastCalendarYear, LastCalendarYearToDate, LastFiscalYear, LastFiscalYearToDate, NextWeek, NextFourWeeks, NextMonth, NextCalendarQuarter, NextCalendarYear, NextFiscalQuarter, NextFiscalYear -->
                                                        <DateMacro >ENUMTYPE</DateMacro> <!-- optional -->
                                                <!-- END OR -->
                                        </TxnDateRangeFilter>
                                <!-- END OR -->
                                <EntityFilter> <!-- optional -->
                                        <!-- BEGIN OR -->
                                                <ListID >IDTYPE</ListID> <!-- optional, may repeat -->
                                        <!-- OR -->
                                                <FullName >STRTYPE</FullName> <!-- optional, may repeat -->
                                        <!-- OR -->
                                                <ListIDWithChildren >IDTYPE</ListIDWithChildren> <!-- optional -->
                                        <!-- OR -->
                                                <FullNameWithChildren >STRTYPE</FullNameWithChildren> <!-- optional -->
                                        <!-- END OR -->
                                </EntityFilter>
                                <AccountFilter> <!-- optional -->
                                        <!-- BEGIN OR -->
                                                <ListID >IDTYPE</ListID> <!-- optional, may repeat -->
                                        <!-- OR -->
                                                <FullName >STRTYPE</FullName> <!-- optional, may repeat -->
                                        <!-- OR -->
                                                <ListIDWithChildren >IDTYPE</ListIDWithChildren> <!-- optional -->
                                        <!-- OR -->
                                                <FullNameWithChildren >STRTYPE</FullNameWithChildren> <!-- optional -->
                                        <!-- END OR -->
                                </AccountFilter>
                                <!-- BEGIN OR -->
                                        <RefNumberFilter> <!-- optional -->
                                                <!-- MatchCriterion may have one of the following values: StartsWith, Contains, EndsWith -->
                                                <MatchCriterion >ENUMTYPE</MatchCriterion> <!-- required -->
                                                <RefNumber >STRTYPE</RefNumber> <!-- required -->
                                        </RefNumberFilter>
                                <!-- OR -->
                                        <RefNumberRangeFilter> <!-- optional -->
                                                <FromRefNumber >STRTYPE</FromRefNumber> <!-- optional -->
                                                <ToRefNumber >STRTYPE</ToRefNumber> <!-- optional -->
                                        </RefNumberRangeFilter>
                                <!-- END OR -->
                                <CurrencyFilter> <!-- optional -->
                                        <!-- BEGIN OR -->
                                                <ListID >IDTYPE</ListID> <!-- optional, may repeat -->
                                        <!-- OR -->
                                                <FullName >STRTYPE</FullName> <!-- optional, may repeat -->
                                        <!-- END OR -->
                                </CurrencyFilter>
                        <!-- END OR -->
                        <IncludeLineItems >BOOLTYPE</IncludeLineItems> <!-- optional -->
                        <IncludeRetElement >STRTYPE</IncludeRetElement> <!-- optional, may repeat -->
                        <OwnerID >GUIDTYPE</OwnerID> <!-- optional, may repeat -->
                </CreditCardChargeQueryRq>

                <CreditCardChargeQueryRs statusCode="INTTYPE" statusSeverity="STRTYPE" statusMessage="STRTYPE" retCount="INTTYPE" iteratorRemainingCount="INTTYPE" iteratorID="UUIDTYPE">
                        <CreditCardChargeRet> <!-- optional, may repeat -->
                                <TxnID >IDTYPE</TxnID> <!-- required -->
                                <TimeCreated >DATETIMETYPE</TimeCreated> <!-- required -->
                                <TimeModified >DATETIMETYPE</TimeModified> <!-- required -->
                                <EditSequence >STRTYPE</EditSequence> <!-- required -->
                                <TxnNumber >INTTYPE</TxnNumber> <!-- optional -->
                                <AccountRef> <!-- required -->
                                        <ListID >IDTYPE</ListID> <!-- optional -->
                                        <FullName >STRTYPE</FullName> <!-- optional -->
                                </AccountRef>
                                <PayeeEntityRef> <!-- optional -->
                                        <ListID >IDTYPE</ListID> <!-- optional -->
                                        <FullName >STRTYPE</FullName> <!-- optional -->
                                </PayeeEntityRef>
                                <TxnDate >DATETYPE</TxnDate> <!-- required -->
                                <Amount >AMTTYPE</Amount> <!-- required -->
                                <CurrencyRef> <!-- optional -->
                                        <ListID >IDTYPE</ListID> <!-- optional -->
                                        <FullName >STRTYPE</FullName> <!-- optional -->
                                </CurrencyRef>
                                <ExchangeRate >FLOATTYPE</ExchangeRate> <!-- optional -->
                                <AmountInHomeCurrency >AMTTYPE</AmountInHomeCurrency> <!-- optional -->
                                <RefNumber >STRTYPE</RefNumber> <!-- optional -->
                                <Memo >STRTYPE</Memo> <!-- optional -->
                                <IsTaxIncluded >BOOLTYPE</IsTaxIncluded> <!-- optional -->
                                <SalesTaxCodeRef> <!-- optional -->
                                        <ListID >IDTYPE</ListID> <!-- optional -->
                                        <FullName >STRTYPE</FullName> <!-- optional -->
                                </SalesTaxCodeRef>
                                <ExternalGUID >GUIDTYPE</ExternalGUID> <!-- optional -->
                                <ExpenseLineRet> <!-- optional, may repeat -->
                                        <TxnLineID >IDTYPE</TxnLineID> <!-- required -->
                                        <AccountRef> <!-- optional -->
                                                <ListID >IDTYPE</ListID> <!-- optional -->
                                                <FullName >STRTYPE</FullName> <!-- optional -->
                                        </AccountRef>
                                        <Amount >AMTTYPE</Amount> <!-- optional -->
                                        <Memo >STRTYPE</Memo> <!-- optional -->
                                        <CustomerRef> <!-- optional -->
                                                <ListID >IDTYPE</ListID> <!-- optional -->
                                                <FullName >STRTYPE</FullName> <!-- optional -->
                                        </CustomerRef>
                                        <ClassRef> <!-- optional -->
                                                <ListID >IDTYPE</ListID> <!-- optional -->
                                                <FullName >STRTYPE</FullName> <!-- optional -->
                                        </ClassRef>
                                        <SalesTaxCodeRef> <!-- optional -->
                                                <ListID >IDTYPE</ListID> <!-- optional -->
                                                <FullName >STRTYPE</FullName> <!-- optional -->
                                        </SalesTaxCodeRef>
                                        <!-- BillableStatus may have one of the following values: Billable, NotBillable, HasBeenBilled -->
                                        <BillableStatus >ENUMTYPE</BillableStatus> <!-- optional -->
                                        <SalesRepRef> <!-- optional -->
                                                <ListID >IDTYPE</ListID> <!-- optional -->
                                                <FullName >STRTYPE</FullName> <!-- optional -->
                                        </SalesRepRef>
                                        <DataExtRet> <!-- optional, may repeat -->
                                                <OwnerID >GUIDTYPE</OwnerID> <!-- optional -->
                                                <DataExtName >STRTYPE</DataExtName> <!-- required -->
                                                <!-- DataExtType may have one of the following values: AMTTYPE, DATETIMETYPE, INTTYPE, PERCENTTYPE, PRICETYPE, QUANTYPE, STR1024TYPE, STR255TYPE -->
                                                <DataExtType >ENUMTYPE</DataExtType> <!-- required -->
                                                <DataExtValue >STRTYPE</DataExtValue> <!-- required -->
                                        </DataExtRet>
                                </ExpenseLineRet>
                                <!-- BEGIN OR -->
                                        <ItemLineRet> <!-- optional -->
                                                <TxnLineID >IDTYPE</TxnLineID> <!-- required -->
                                                <ItemRef> <!-- optional -->
                                                        <ListID >IDTYPE</ListID> <!-- optional -->
                                                        <FullName >STRTYPE</FullName> <!-- optional -->
                                                </ItemRef>
                                                <InventorySiteRef> <!-- optional -->
                                                        <ListID >IDTYPE</ListID> <!-- optional -->
                                                        <FullName >STRTYPE</FullName> <!-- optional -->
                                                </InventorySiteRef>
                                                <InventorySiteLocationRef> <!-- optional -->
                                                        <ListID >IDTYPE</ListID> <!-- optional -->
                                                        <FullName >STRTYPE</FullName> <!-- optional -->
                                                </InventorySiteLocationRef>
                                                <!-- BEGIN OR -->
                                                        <SerialNumber >STRTYPE</SerialNumber> <!-- optional -->
                                                <!-- OR -->
                                                        <LotNumber >STRTYPE</LotNumber> <!-- optional -->
                                                <!-- END OR -->
                                                <ExpirationDateForSerialLotNumber>STRTYPE</ExpirationDateForSerialLotNumber> <!-- optional -->
                                                <Desc >STRTYPE</Desc> <!-- optional -->
                                                <Quantity >QUANTYPE</Quantity> <!-- optional -->
                                                <UnitOfMeasure >STRTYPE</UnitOfMeasure> <!-- optional -->
                                                <OverrideUOMSetRef> <!-- optional -->
                                                        <ListID >IDTYPE</ListID> <!-- optional -->
                                                        <FullName >STRTYPE</FullName> <!-- optional -->
                                                </OverrideUOMSetRef>
                                                <Cost >PRICETYPE</Cost> <!-- optional -->
                                                <Amount >AMTTYPE</Amount> <!-- optional -->
                                                <CustomerRef> <!-- optional -->
                                                        <ListID >IDTYPE</ListID> <!-- optional -->
                                                        <FullName >STRTYPE</FullName> <!-- optional -->
                                                </CustomerRef>
                                                <ClassRef> <!-- optional -->
                                                        <ListID >IDTYPE</ListID> <!-- optional -->
                                                        <FullName >STRTYPE</FullName> <!-- optional -->
                                                </ClassRef>
                                                <SalesTaxCodeRef> <!-- optional -->
                                                        <ListID >IDTYPE</ListID> <!-- optional -->
                                                        <FullName >STRTYPE</FullName> <!-- optional -->
                                                </SalesTaxCodeRef>
                                                <!-- BillableStatus may have one of the following values: Billable, NotBillable, HasBeenBilled -->
                                                <BillableStatus >ENUMTYPE</BillableStatus> <!-- optional -->
                                                <SalesRepRef> <!-- optional -->
                                                        <ListID >IDTYPE</ListID> <!-- optional -->
                                                        <FullName >STRTYPE</FullName> <!-- optional -->
                                                </SalesRepRef>
                                                <DataExtRet> <!-- optional, may repeat -->
                                                        <OwnerID >GUIDTYPE</OwnerID> <!-- optional -->
                                                        <DataExtName >STRTYPE</DataExtName> <!-- required -->
                                                        <!-- DataExtType may have one of the following values: AMTTYPE, DATETIMETYPE, INTTYPE, PERCENTTYPE, PRICETYPE, QUANTYPE, STR1024TYPE, STR255TYPE -->
                                                        <DataExtType >ENUMTYPE</DataExtType> <!-- required -->
                                                        <DataExtValue >STRTYPE</DataExtValue> <!-- required -->
                                                </DataExtRet>
                                        </ItemLineRet>
                                <!-- OR -->
                                        <ItemGroupLineRet> <!-- optional -->
                                                <TxnLineID >IDTYPE</TxnLineID> <!-- required -->
                                                <ItemGroupRef> <!-- required -->
                                                        <ListID >IDTYPE</ListID> <!-- optional -->
                                                        <FullName >STRTYPE</FullName> <!-- optional -->
                                                </ItemGroupRef>
                                                <Desc >STRTYPE</Desc> <!-- optional -->
                                                <Quantity >QUANTYPE</Quantity> <!-- optional -->
                                                <UnitOfMeasure >STRTYPE</UnitOfMeasure> <!-- optional -->
                                                <OverrideUOMSetRef> <!-- optional -->
                                                        <ListID >IDTYPE</ListID> <!-- optional -->
                                                        <FullName >STRTYPE</FullName> <!-- optional -->
                                                </OverrideUOMSetRef>
                                                <TotalAmount >AMTTYPE</TotalAmount> <!-- required -->
                                                <ItemLineRet> <!-- optional, may repeat -->
                                                        <TxnLineID >IDTYPE</TxnLineID> <!-- required -->
                                                        <ItemRef> <!-- optional -->
                                                                <ListID >IDTYPE</ListID> <!-- optional -->
                                                                <FullName >STRTYPE</FullName> <!-- optional -->
                                                        </ItemRef>
                                                        <InventorySiteRef> <!-- optional -->
                                                                <ListID >IDTYPE</ListID> <!-- optional -->
                                                                <FullName >STRTYPE</FullName> <!-- optional -->
                                                        </InventorySiteRef>
                                                        <InventorySiteLocationRef> <!-- optional -->
                                                                <ListID >IDTYPE</ListID> <!-- optional -->
                                                                <FullName >STRTYPE</FullName> <!-- optional -->
                                                        </InventorySiteLocationRef>
                                                        <!-- BEGIN OR -->
                                                                <SerialNumber >STRTYPE</SerialNumber> <!-- optional -->
                                                        <!-- OR -->
                                                                <LotNumber >STRTYPE</LotNumber> <!-- optional -->
                                                        <!-- END OR -->
                                                        <ExpirationDateForSerialLotNumber>STRTYPE</ExpirationDateForSerialLotNumber> <!-- optional -->
                                                        <Desc >STRTYPE</Desc> <!-- optional -->
                                                        <Quantity >QUANTYPE</Quantity> <!-- optional -->
                                                        <UnitOfMeasure >STRTYPE</UnitOfMeasure> <!-- optional -->
                                                        <OverrideUOMSetRef> <!-- optional -->
                                                                <ListID >IDTYPE</ListID> <!-- optional -->
                                                                <FullName >STRTYPE</FullName> <!-- optional -->
                                                        </OverrideUOMSetRef>
                                                        <Cost >PRICETYPE</Cost> <!-- optional -->
                                                        <Amount >AMTTYPE</Amount> <!-- optional -->
                                                        <CustomerRef> <!-- optional -->
                                                                <ListID >IDTYPE</ListID> <!-- optional -->
                                                                <FullName >STRTYPE</FullName> <!-- optional -->
                                                        </CustomerRef>
                                                        <ClassRef> <!-- optional -->
                                                                <ListID >IDTYPE</ListID> <!-- optional -->
                                                                <FullName >STRTYPE</FullName> <!-- optional -->
                                                        </ClassRef>
                                                        <SalesTaxCodeRef> <!-- optional -->
                                                                <ListID >IDTYPE</ListID> <!-- optional -->
                                                                <FullName >STRTYPE</FullName> <!-- optional -->
                                                        </SalesTaxCodeRef>
                                                        <!-- BillableStatus may have one of the following values: Billable, NotBillable, HasBeenBilled -->
                                                        <BillableStatus >ENUMTYPE</BillableStatus> <!-- optional -->
                                                        <SalesRepRef> <!-- optional -->
                                                                <ListID >IDTYPE</ListID> <!-- optional -->
                                                                <FullName >STRTYPE</FullName> <!-- optional -->
                                                        </SalesRepRef>
                                                        <DataExtRet> <!-- optional, may repeat -->
                                                                <OwnerID >GUIDTYPE</OwnerID> <!-- optional -->
                                                                <DataExtName >STRTYPE</DataExtName> <!-- required -->
                                                                <!-- DataExtType may have one of the following values: AMTTYPE, DATETIMETYPE, INTTYPE, PERCENTTYPE, PRICETYPE, QUANTYPE, STR1024TYPE, STR255TYPE -->
                                                                <DataExtType >ENUMTYPE</DataExtType> <!-- required -->
                                                                <DataExtValue >STRTYPE</DataExtValue> <!-- required -->
                                                        </DataExtRet>
                                                </ItemLineRet>
                                                <DataExt> <!-- optional, may repeat -->
                                                        <OwnerID >GUIDTYPE</OwnerID> <!-- required -->
                                                        <DataExtName >STRTYPE</DataExtName> <!-- required -->
                                                        <DataExtValue >STRTYPE</DataExtValue> <!-- required -->
                                                </DataExt>
                                        </ItemGroupLineRet>
                                <!-- END OR -->
                                <DataExtRet> <!-- optional, may repeat -->
                                        <OwnerID >GUIDTYPE</OwnerID> <!-- optional -->
                                        <DataExtName >STRTYPE</DataExtName> <!-- required -->
                                        <!-- DataExtType may have one of the following values: AMTTYPE, DATETIMETYPE, INTTYPE, PERCENTTYPE, PRICETYPE, QUANTYPE, STR1024TYPE, STR255TYPE -->
                                        <DataExtType >ENUMTYPE</DataExtType> <!-- required -->
                                        <DataExtValue >STRTYPE</DataExtValue> <!-- required -->
                                </DataExtRet>
                        </CreditCardChargeRet>
                </CreditCardChargeQueryRs>
        </QBXMLMsgsRq>
</QBXML>
```

## Credit Card Credit Query
### XMLOps
```
<?xml version="1.0" encoding="utf-8"?>
<?qbxml version="16.0"?>
<QBXML>
        <QBXMLMsgsRq onError="stopOnError">
                <CreditCardCreditQueryRq metaData="ENUMTYPE" iterator="ENUMTYPE" iteratorID="UUIDTYPE">
                        <!-- BEGIN OR -->
                                <TxnID >IDTYPE</TxnID> <!-- optional, may repeat -->
                        <!-- OR -->
                                <RefNumber >STRTYPE</RefNumber> <!-- optional, may repeat -->
                        <!-- OR -->
                                <RefNumberCaseSensitive >STRTYPE</RefNumberCaseSensitive> <!-- optional, may repeat -->
                        <!-- OR -->
                                <MaxReturned >INTTYPE</MaxReturned> <!-- optional -->
                                <!-- BEGIN OR -->
                                        <ModifiedDateRangeFilter> <!-- optional -->
                                                <FromModifiedDate >DATETIMETYPE</FromModifiedDate> <!-- optional -->
                                                <ToModifiedDate >DATETIMETYPE</ToModifiedDate> <!-- optional -->
                                        </ModifiedDateRangeFilter>
                                <!-- OR -->
                                        <TxnDateRangeFilter> <!-- optional -->
                                                <!-- BEGIN OR -->
                                                        <FromTxnDate >DATETYPE</FromTxnDate> <!-- optional -->
                                                        <ToTxnDate >DATETYPE</ToTxnDate> <!-- optional -->
                                                <!-- OR -->
                                                        <!-- DateMacro may have one of the following values: All, Today, ThisWeek, ThisWeekToDate, ThisMonth, ThisMonthToDate, ThisCalendarQuarter, ThisCalendarQuarterToDate, ThisFiscalQuarter, ThisFiscalQuarterToDate, ThisCalendarYear, ThisCalendarYearToDate, ThisFiscalYear, ThisFiscalYearToDate, Yesterday, LastWeek, LastWeekToDate, LastMonth, LastMonthToDate, LastCalendarQuarter, LastCalendarQuarterToDate, LastFiscalQuarter, LastFiscalQuarterToDate, LastCalendarYear, LastCalendarYearToDate, LastFiscalYear, LastFiscalYearToDate, NextWeek, NextFourWeeks, NextMonth, NextCalendarQuarter, NextCalendarYear, NextFiscalQuarter, NextFiscalYear -->
                                                        <DateMacro >ENUMTYPE</DateMacro> <!-- optional -->
                                                <!-- END OR -->
                                        </TxnDateRangeFilter>
                                <!-- END OR -->
                                <EntityFilter> <!-- optional -->
                                        <!-- BEGIN OR -->
                                                <ListID >IDTYPE</ListID> <!-- optional, may repeat -->
                                        <!-- OR -->
                                                <FullName >STRTYPE</FullName> <!-- optional, may repeat -->
                                        <!-- OR -->
                                                <ListIDWithChildren >IDTYPE</ListIDWithChildren> <!-- optional -->
                                        <!-- OR -->
                                                <FullNameWithChildren >STRTYPE</FullNameWithChildren> <!-- optional -->
                                        <!-- END OR -->
                                </EntityFilter>
                                <AccountFilter> <!-- optional -->
                                        <!-- BEGIN OR -->
                                                <ListID >IDTYPE</ListID> <!-- optional, may repeat -->
                                        <!-- OR -->
                                                <FullName >STRTYPE</FullName> <!-- optional, may repeat -->
                                        <!-- OR -->
                                                <ListIDWithChildren >IDTYPE</ListIDWithChildren> <!-- optional -->
                                        <!-- OR -->
                                                <FullNameWithChildren >STRTYPE</FullNameWithChildren> <!-- optional -->
                                        <!-- END OR -->
                                </AccountFilter>
                                <!-- BEGIN OR -->
                                        <RefNumberFilter> <!-- optional -->
                                                <!-- MatchCriterion may have one of the following values: StartsWith, Contains, EndsWith -->
                                                <MatchCriterion >ENUMTYPE</MatchCriterion> <!-- required -->
                                                <RefNumber >STRTYPE</RefNumber> <!-- required -->
                                        </RefNumberFilter>
                                <!-- OR -->
                                        <RefNumberRangeFilter> <!-- optional -->
                                                <FromRefNumber >STRTYPE</FromRefNumber> <!-- optional -->
                                                <ToRefNumber >STRTYPE</ToRefNumber> <!-- optional -->
                                        </RefNumberRangeFilter>
                                <!-- END OR -->
                                <CurrencyFilter> <!-- optional -->
                                        <!-- BEGIN OR -->
                                                <ListID >IDTYPE</ListID> <!-- optional, may repeat -->
                                        <!-- OR -->
                                                <FullName >STRTYPE</FullName> <!-- optional, may repeat -->
                                        <!-- END OR -->
                                </CurrencyFilter>
                        <!-- END OR -->
                        <IncludeLineItems >BOOLTYPE</IncludeLineItems> <!-- optional -->
                        <IncludeRetElement >STRTYPE</IncludeRetElement> <!-- optional, may repeat -->
                        <OwnerID >GUIDTYPE</OwnerID> <!-- optional, may repeat -->
                </CreditCardCreditQueryRq>

                <CreditCardCreditQueryRs statusCode="INTTYPE" statusSeverity="STRTYPE" statusMessage="STRTYPE" retCount="INTTYPE" iteratorRemainingCount="INTTYPE" iteratorID="UUIDTYPE">
                        <CreditCardCreditRet> <!-- optional, may repeat -->
                                <TxnID >IDTYPE</TxnID> <!-- required -->
                                <TimeCreated >DATETIMETYPE</TimeCreated> <!-- required -->
                                <TimeModified >DATETIMETYPE</TimeModified> <!-- required -->
                                <EditSequence >STRTYPE</EditSequence> <!-- required -->
                                <TxnNumber >INTTYPE</TxnNumber> <!-- optional -->
                                <AccountRef> <!-- required -->
                                        <ListID >IDTYPE</ListID> <!-- optional -->
                                        <FullName >STRTYPE</FullName> <!-- optional -->
                                </AccountRef>
                                <PayeeEntityRef> <!-- optional -->
                                        <ListID >IDTYPE</ListID> <!-- optional -->
                                        <FullName >STRTYPE</FullName> <!-- optional -->
                                </PayeeEntityRef>
                                <TxnDate >DATETYPE</TxnDate> <!-- required -->
                                <Amount >AMTTYPE</Amount> <!-- required -->
                                <CurrencyRef> <!-- optional -->
                                        <ListID >IDTYPE</ListID> <!-- optional -->
                                        <FullName >STRTYPE</FullName> <!-- optional -->
                                </CurrencyRef>
                                <ExchangeRate >FLOATTYPE</ExchangeRate> <!-- optional -->
                                <AmountInHomeCurrency >AMTTYPE</AmountInHomeCurrency> <!-- optional -->
                                <RefNumber >STRTYPE</RefNumber> <!-- optional -->
                                <Memo >STRTYPE</Memo> <!-- optional -->
                                <IsTaxIncluded >BOOLTYPE</IsTaxIncluded> <!-- optional -->
                                <SalesTaxCodeRef> <!-- optional -->
                                        <ListID >IDTYPE</ListID> <!-- optional -->
                                        <FullName >STRTYPE</FullName> <!-- optional -->
                                </SalesTaxCodeRef>
                                <ExternalGUID >GUIDTYPE</ExternalGUID> <!-- optional -->
                                <ExpenseLineRet> <!-- optional, may repeat -->
                                        <TxnLineID >IDTYPE</TxnLineID> <!-- required -->
                                        <AccountRef> <!-- optional -->
                                                <ListID >IDTYPE</ListID> <!-- optional -->
                                                <FullName >STRTYPE</FullName> <!-- optional -->
                                        </AccountRef>
                                        <Amount >AMTTYPE</Amount> <!-- optional -->
                                        <Memo >STRTYPE</Memo> <!-- optional -->
                                        <CustomerRef> <!-- optional -->
                                                <ListID >IDTYPE</ListID> <!-- optional -->
                                                <FullName >STRTYPE</FullName> <!-- optional -->
                                        </CustomerRef>
                                        <ClassRef> <!-- optional -->
                                                <ListID >IDTYPE</ListID> <!-- optional -->
                                                <FullName >STRTYPE</FullName> <!-- optional -->
                                        </ClassRef>
                                        <SalesTaxCodeRef> <!-- optional -->
                                                <ListID >IDTYPE</ListID> <!-- optional -->
                                                <FullName >STRTYPE</FullName> <!-- optional -->
                                        </SalesTaxCodeRef>
                                        <!-- BillableStatus may have one of the following values: Billable, NotBillable, HasBeenBilled -->
                                        <BillableStatus >ENUMTYPE</BillableStatus> <!-- optional -->
                                        <SalesRepRef> <!-- optional -->
                                                <ListID >IDTYPE</ListID> <!-- optional -->
                                                <FullName >STRTYPE</FullName> <!-- optional -->
                                        </SalesRepRef>
                                        <DataExtRet> <!-- optional, may repeat -->
                                                <OwnerID >GUIDTYPE</OwnerID> <!-- optional -->
                                                <DataExtName >STRTYPE</DataExtName> <!-- required -->
                                                <!-- DataExtType may have one of the following values: AMTTYPE, DATETIMETYPE, INTTYPE, PERCENTTYPE, PRICETYPE, QUANTYPE, STR1024TYPE, STR255TYPE -->
                                                <DataExtType >ENUMTYPE</DataExtType> <!-- required -->
                                                <DataExtValue >STRTYPE</DataExtValue> <!-- required -->
                                        </DataExtRet>
                                </ExpenseLineRet>
                                <!-- BEGIN OR -->
                                        <ItemLineRet> <!-- optional -->
                                                <TxnLineID >IDTYPE</TxnLineID> <!-- required -->
                                                <ItemRef> <!-- optional -->
                                                        <ListID >IDTYPE</ListID> <!-- optional -->
                                                        <FullName >STRTYPE</FullName> <!-- optional -->
                                                </ItemRef>
                                                <InventorySiteRef> <!-- optional -->
                                                        <ListID >IDTYPE</ListID> <!-- optional -->
                                                        <FullName >STRTYPE</FullName> <!-- optional -->
                                                </InventorySiteRef>
                                                <InventorySiteLocationRef> <!-- optional -->
                                                        <ListID >IDTYPE</ListID> <!-- optional -->
                                                        <FullName >STRTYPE</FullName> <!-- optional -->
                                                </InventorySiteLocationRef>
                                                <!-- BEGIN OR -->
                                                        <SerialNumber >STRTYPE</SerialNumber> <!-- optional -->
                                                <!-- OR -->
                                                        <LotNumber >STRTYPE</LotNumber> <!-- optional -->
                                                <!-- END OR -->
                                                <ExpirationDateForSerialLotNumber>STRTYPE</ExpirationDateForSerialLotNumber> <!-- optional -->
                                                <Desc >STRTYPE</Desc> <!-- optional -->
                                                <Quantity >QUANTYPE</Quantity> <!-- optional -->
                                                <UnitOfMeasure >STRTYPE</UnitOfMeasure> <!-- optional -->
                                                <OverrideUOMSetRef> <!-- optional -->
                                                        <ListID >IDTYPE</ListID> <!-- optional -->
                                                        <FullName >STRTYPE</FullName> <!-- optional -->
                                                </OverrideUOMSetRef>
                                                <Cost >PRICETYPE</Cost> <!-- optional -->
                                                <Amount >AMTTYPE</Amount> <!-- optional -->
                                                <CustomerRef> <!-- optional -->
                                                        <ListID >IDTYPE</ListID> <!-- optional -->
                                                        <FullName >STRTYPE</FullName> <!-- optional -->
                                                </CustomerRef>
                                                <ClassRef> <!-- optional -->
                                                        <ListID >IDTYPE</ListID> <!-- optional -->
                                                        <FullName >STRTYPE</FullName> <!-- optional -->
                                                </ClassRef>
                                                <SalesTaxCodeRef> <!-- optional -->
                                                        <ListID >IDTYPE</ListID> <!-- optional -->
                                                        <FullName >STRTYPE</FullName> <!-- optional -->
                                                </SalesTaxCodeRef>
                                                <!-- BillableStatus may have one of the following values: Billable, NotBillable, HasBeenBilled -->
                                                <BillableStatus >ENUMTYPE</BillableStatus> <!-- optional -->
                                                <SalesRepRef> <!-- optional -->
                                                        <ListID >IDTYPE</ListID> <!-- optional -->
                                                        <FullName >STRTYPE</FullName> <!-- optional -->
                                                </SalesRepRef>
                                                <DataExtRet> <!-- optional, may repeat -->
                                                        <OwnerID >GUIDTYPE</OwnerID> <!-- optional -->
                                                        <DataExtName >STRTYPE</DataExtName> <!-- required -->
                                                        <!-- DataExtType may have one of the following values: AMTTYPE, DATETIMETYPE, INTTYPE, PERCENTTYPE, PRICETYPE, QUANTYPE, STR1024TYPE, STR255TYPE -->
                                                        <DataExtType >ENUMTYPE</DataExtType> <!-- required -->
                                                        <DataExtValue >STRTYPE</DataExtValue> <!-- required -->
                                                </DataExtRet>
                                        </ItemLineRet>
                                <!-- OR -->
                                        <ItemGroupLineRet> <!-- optional -->
                                                <TxnLineID >IDTYPE</TxnLineID> <!-- required -->
                                                <ItemGroupRef> <!-- required -->
                                                        <ListID >IDTYPE</ListID> <!-- optional -->
                                                        <FullName >STRTYPE</FullName> <!-- optional -->
                                                </ItemGroupRef>
                                                <Desc >STRTYPE</Desc> <!-- optional -->
                                                <Quantity >QUANTYPE</Quantity> <!-- optional -->
                                                <UnitOfMeasure >STRTYPE</UnitOfMeasure> <!-- optional -->
                                                <OverrideUOMSetRef> <!-- optional -->
                                                        <ListID >IDTYPE</ListID> <!-- optional -->
                                                        <FullName >STRTYPE</FullName> <!-- optional -->
                                                </OverrideUOMSetRef>
                                                <TotalAmount >AMTTYPE</TotalAmount> <!-- required -->
                                                <ItemLineRet> <!-- optional, may repeat -->
                                                        <TxnLineID >IDTYPE</TxnLineID> <!-- required -->
                                                        <ItemRef> <!-- optional -->
                                                                <ListID >IDTYPE</ListID> <!-- optional -->
                                                                <FullName >STRTYPE</FullName> <!-- optional -->
                                                        </ItemRef>
                                                        <InventorySiteRef> <!-- optional -->
                                                                <ListID >IDTYPE</ListID> <!-- optional -->
                                                                <FullName >STRTYPE</FullName> <!-- optional -->
                                                        </InventorySiteRef>
                                                        <InventorySiteLocationRef> <!-- optional -->
                                                                <ListID >IDTYPE</ListID> <!-- optional -->
                                                                <FullName >STRTYPE</FullName> <!-- optional -->
                                                        </InventorySiteLocationRef>
                                                        <!-- BEGIN OR -->
                                                                <SerialNumber >STRTYPE</SerialNumber> <!-- optional -->
                                                        <!-- OR -->
                                                                <LotNumber >STRTYPE</LotNumber> <!-- optional -->
                                                        <!-- END OR -->
                                                        <ExpirationDateForSerialLotNumber>STRTYPE</ExpirationDateForSerialLotNumber> <!-- optional -->
                                                        <Desc >STRTYPE</Desc> <!-- optional -->
                                                        <Quantity >QUANTYPE</Quantity> <!-- optional -->
                                                        <UnitOfMeasure >STRTYPE</UnitOfMeasure> <!-- optional -->
                                                        <OverrideUOMSetRef> <!-- optional -->
                                                                <ListID >IDTYPE</ListID> <!-- optional -->
                                                                <FullName >STRTYPE</FullName> <!-- optional -->
                                                        </OverrideUOMSetRef>
                                                        <Cost >PRICETYPE</Cost> <!-- optional -->
                                                        <Amount >AMTTYPE</Amount> <!-- optional -->
                                                        <CustomerRef> <!-- optional -->
                                                                <ListID >IDTYPE</ListID> <!-- optional -->
                                                                <FullName >STRTYPE</FullName> <!-- optional -->
                                                        </CustomerRef>
                                                        <ClassRef> <!-- optional -->
                                                                <ListID >IDTYPE</ListID> <!-- optional -->
                                                                <FullName >STRTYPE</FullName> <!-- optional -->
                                                        </ClassRef>
                                                        <SalesTaxCodeRef> <!-- optional -->
                                                                <ListID >IDTYPE</ListID> <!-- optional -->
                                                                <FullName >STRTYPE</FullName> <!-- optional -->
                                                        </SalesTaxCodeRef>
                                                        <!-- BillableStatus may have one of the following values: Billable, NotBillable, HasBeenBilled -->
                                                        <BillableStatus >ENUMTYPE</BillableStatus> <!-- optional -->
                                                        <SalesRepRef> <!-- optional -->
                                                                <ListID >IDTYPE</ListID> <!-- optional -->
                                                                <FullName >STRTYPE</FullName> <!-- optional -->
                                                        </SalesRepRef>
                                                        <DataExtRet> <!-- optional, may repeat -->
                                                                <OwnerID >GUIDTYPE</OwnerID> <!-- optional -->
                                                                <DataExtName >STRTYPE</DataExtName> <!-- required -->
                                                                <!-- DataExtType may have one of the following values: AMTTYPE, DATETIMETYPE, INTTYPE, PERCENTTYPE, PRICETYPE, QUANTYPE, STR1024TYPE, STR255TYPE -->
                                                                <DataExtType >ENUMTYPE</DataExtType> <!-- required -->
                                                                <DataExtValue >STRTYPE</DataExtValue> <!-- required -->
                                                        </DataExtRet>
                                                </ItemLineRet>
                                                <DataExt> <!-- optional, may repeat -->
                                                        <OwnerID >GUIDTYPE</OwnerID> <!-- required -->
                                                        <DataExtName >STRTYPE</DataExtName> <!-- required -->
                                                        <DataExtValue >STRTYPE</DataExtValue> <!-- required -->
                                                </DataExt>
                                        </ItemGroupLineRet>
                                <!-- END OR -->
                                <DataExtRet> <!-- optional, may repeat -->
                                        <OwnerID >GUIDTYPE</OwnerID> <!-- optional -->
                                        <DataExtName >STRTYPE</DataExtName> <!-- required -->
                                        <!-- DataExtType may have one of the following values: AMTTYPE, DATETIMETYPE, INTTYPE, PERCENTTYPE, PRICETYPE, QUANTYPE, STR1024TYPE, STR255TYPE -->
                                        <DataExtType >ENUMTYPE</DataExtType> <!-- required -->
                                        <DataExtValue >STRTYPE</DataExtValue> <!-- required -->
                                </DataExtRet>
                        </CreditCardCreditRet>
                </CreditCardCreditQueryRs>
        </QBXMLMsgsRq>
</QBXML>
```
## CompanyActivityQuery
### XMLOps
```
<?xml version="1.0" encoding="utf-8"?>
<?qbxml version="16.0"?>
<QBXML>
        <QBXMLMsgsRq onError="stopOnError">
                <CompanyActivityQueryRq>
                        <IncludeRetElement >STRTYPE</IncludeRetElement> <!-- optional, may repeat -->
                </CompanyActivityQueryRq>

                <CompanyActivityQueryRs statusCode="INTTYPE" statusSeverity="STRTYPE" statusMessage="STRTYPE">
                        <CompanyActivityRet> <!-- optional -->
                                <LastRestoreTime >DATETIMETYPE</LastRestoreTime> <!-- required -->
                                <LastCondenseTime >DATETIMETYPE</LastCondenseTime> <!-- required -->
                        </CompanyActivityRet>
                </CompanyActivityQueryRs>
        </QBXMLMsgsRq>
</QBXML>

```

## Credit Memo Query
### XMLOps
```
<?xml version="1.0" encoding="utf-8"?>
<?qbxml version="16.0"?>
<QBXML>
        <QBXMLMsgsRq onError="stopOnError">
                <CreditMemoQueryRq metaData="ENUMTYPE" iterator="ENUMTYPE" iteratorID="UUIDTYPE">
                        <!-- BEGIN OR -->
                                <TxnID >IDTYPE</TxnID> <!-- optional, may repeat -->
                        <!-- OR -->
                                <RefNumber >STRTYPE</RefNumber> <!-- optional, may repeat -->
                        <!-- OR -->
                                <RefNumberCaseSensitive >STRTYPE</RefNumberCaseSensitive> <!-- optional, may repeat -->
                        <!-- OR -->
                                <MaxReturned >INTTYPE</MaxReturned> <!-- optional -->
                                <!-- BEGIN OR -->
                                        <ModifiedDateRangeFilter> <!-- optional -->
                                                <FromModifiedDate >DATETIMETYPE</FromModifiedDate> <!-- optional -->
                                                <ToModifiedDate >DATETIMETYPE</ToModifiedDate> <!-- optional -->
                                        </ModifiedDateRangeFilter>
                                <!-- OR -->
                                        <TxnDateRangeFilter> <!-- optional -->
                                                <!-- BEGIN OR -->
                                                        <FromTxnDate >DATETYPE</FromTxnDate> <!-- optional -->
                                                        <ToTxnDate >DATETYPE</ToTxnDate> <!-- optional -->
                                                <!-- OR -->
                                                        <!-- DateMacro may have one of the following values: All, Today, ThisWeek, ThisWeekToDate, ThisMonth, ThisMonthToDate, ThisCalendarQuarter, ThisCalendarQuarterToDate, ThisFiscalQuarter, ThisFiscalQuarterToDate, ThisCalendarYear, ThisCalendarYearToDate, ThisFiscalYear, ThisFiscalYearToDate, Yesterday, LastWeek, LastWeekToDate, LastMonth, LastMonthToDate, LastCalendarQuarter, LastCalendarQuarterToDate, LastFiscalQuarter, LastFiscalQuarterToDate, LastCalendarYear, LastCalendarYearToDate, LastFiscalYear, LastFiscalYearToDate, NextWeek, NextFourWeeks, NextMonth, NextCalendarQuarter, NextCalendarYear, NextFiscalQuarter, NextFiscalYear -->
                                                        <DateMacro >ENUMTYPE</DateMacro> <!-- optional -->
                                                <!-- END OR -->
                                        </TxnDateRangeFilter>
                                <!-- END OR -->
                                <EntityFilter> <!-- optional -->
                                        <!-- BEGIN OR -->
                                                <ListID >IDTYPE</ListID> <!-- optional, may repeat -->
                                        <!-- OR -->
                                                <FullName >STRTYPE</FullName> <!-- optional, may repeat -->
                                        <!-- OR -->
                                                <ListIDWithChildren >IDTYPE</ListIDWithChildren> <!-- optional -->
                                        <!-- OR -->
                                                <FullNameWithChildren >STRTYPE</FullNameWithChildren> <!-- optional -->
                                        <!-- END OR -->
                                </EntityFilter>
                                <AccountFilter> <!-- optional -->
                                        <!-- BEGIN OR -->
                                                <ListID >IDTYPE</ListID> <!-- optional, may repeat -->
                                        <!-- OR -->
                                                <FullName >STRTYPE</FullName> <!-- optional, may repeat -->
                                        <!-- OR -->
                                                <ListIDWithChildren >IDTYPE</ListIDWithChildren> <!-- optional -->
                                        <!-- OR -->
                                                <FullNameWithChildren >STRTYPE</FullNameWithChildren> <!-- optional -->
                                        <!-- END OR -->
                                </AccountFilter>
                                <!-- BEGIN OR -->
                                        <RefNumberFilter> <!-- optional -->
                                                <!-- MatchCriterion may have one of the following values: StartsWith, Contains, EndsWith -->
                                                <MatchCriterion >ENUMTYPE</MatchCriterion> <!-- required -->
                                                <RefNumber >STRTYPE</RefNumber> <!-- required -->
                                        </RefNumberFilter>
                                <!-- OR -->
                                        <RefNumberRangeFilter> <!-- optional -->
                                                <FromRefNumber >STRTYPE</FromRefNumber> <!-- optional -->
                                                <ToRefNumber >STRTYPE</ToRefNumber> <!-- optional -->
                                        </RefNumberRangeFilter>
                                <!-- END OR -->
                                <CurrencyFilter> <!-- optional -->
                                        <!-- BEGIN OR -->
                                                <ListID >IDTYPE</ListID> <!-- optional, may repeat -->
                                        <!-- OR -->
                                                <FullName >STRTYPE</FullName> <!-- optional, may repeat -->
                                        <!-- END OR -->
                                </CurrencyFilter>
                        <!-- END OR -->
                        <IncludeLineItems >BOOLTYPE</IncludeLineItems> <!-- optional -->
                        <IncludeLinkedTxns >BOOLTYPE</IncludeLinkedTxns> <!-- optional -->
                        <IncludeRetElement >STRTYPE</IncludeRetElement> <!-- optional, may repeat -->
                        <OwnerID >GUIDTYPE</OwnerID> <!-- optional, may repeat -->
                </CreditMemoQueryRq>

                <CreditMemoQueryRs statusCode="INTTYPE" statusSeverity="STRTYPE" statusMessage="STRTYPE" retCount="INTTYPE" iteratorRemainingCount="INTTYPE" iteratorID="UUIDTYPE">
                        <CreditMemoRet> <!-- optional, may repeat -->
                                <TxnID >IDTYPE</TxnID> <!-- required -->
                                <TimeCreated >DATETIMETYPE</TimeCreated> <!-- required -->
                                <TimeModified >DATETIMETYPE</TimeModified> <!-- required -->
                                <EditSequence >STRTYPE</EditSequence> <!-- required -->
                                <TxnNumber >INTTYPE</TxnNumber> <!-- optional -->
                                <CustomerRef> <!-- required -->
                                        <ListID >IDTYPE</ListID> <!-- optional -->
                                        <FullName >STRTYPE</FullName> <!-- optional -->
                                </CustomerRef>
                                <ClassRef> <!-- optional -->
                                        <ListID >IDTYPE</ListID> <!-- optional -->
                                        <FullName >STRTYPE</FullName> <!-- optional -->
                                </ClassRef>
                                <ARAccountRef> <!-- optional -->
                                        <ListID >IDTYPE</ListID> <!-- optional -->
                                        <FullName >STRTYPE</FullName> <!-- optional -->
                                </ARAccountRef>
                                <TemplateRef> <!-- optional -->
                                        <ListID >IDTYPE</ListID> <!-- optional -->
                                        <FullName >STRTYPE</FullName> <!-- optional -->
                                </TemplateRef>
                                <TxnDate >DATETYPE</TxnDate> <!-- required -->
                                <RefNumber >STRTYPE</RefNumber> <!-- optional -->
                                <BillAddress> <!-- optional -->
                                        <Addr1 >STRTYPE</Addr1> <!-- optional -->
                                        <Addr2 >STRTYPE</Addr2> <!-- optional -->
                                        <Addr3 >STRTYPE</Addr3> <!-- optional -->
                                        <Addr4 >STRTYPE</Addr4> <!-- optional -->
                                        <Addr5 >STRTYPE</Addr5> <!-- optional -->
                                        <City >STRTYPE</City> <!-- optional -->
                                        <State >STRTYPE</State> <!-- optional -->
                                        <PostalCode >STRTYPE</PostalCode> <!-- optional -->
                                        <Country >STRTYPE</Country> <!-- optional -->
                                        <Note >STRTYPE</Note> <!-- optional -->
                                </BillAddress>
                                <BillAddressBlock> <!-- optional -->
                                        <Addr1 >STRTYPE</Addr1> <!-- optional -->
                                        <Addr2 >STRTYPE</Addr2> <!-- optional -->
                                        <Addr3 >STRTYPE</Addr3> <!-- optional -->
                                        <Addr4 >STRTYPE</Addr4> <!-- optional -->
                                        <Addr5 >STRTYPE</Addr5> <!-- optional -->
                                </BillAddressBlock>
                                <ShipAddress> <!-- optional -->
                                        <Addr1 >STRTYPE</Addr1> <!-- optional -->
                                        <Addr2 >STRTYPE</Addr2> <!-- optional -->
                                        <Addr3 >STRTYPE</Addr3> <!-- optional -->
                                        <Addr4 >STRTYPE</Addr4> <!-- optional -->
                                        <Addr5 >STRTYPE</Addr5> <!-- optional -->
                                        <City >STRTYPE</City> <!-- optional -->
                                        <State >STRTYPE</State> <!-- optional -->
                                        <PostalCode >STRTYPE</PostalCode> <!-- optional -->
                                        <Country >STRTYPE</Country> <!-- optional -->
                                        <Note >STRTYPE</Note> <!-- optional -->
                                </ShipAddress>
                                <ShipAddressBlock> <!-- optional -->
                                        <Addr1 >STRTYPE</Addr1> <!-- optional -->
                                        <Addr2 >STRTYPE</Addr2> <!-- optional -->
                                        <Addr3 >STRTYPE</Addr3> <!-- optional -->
                                        <Addr4 >STRTYPE</Addr4> <!-- optional -->
                                        <Addr5 >STRTYPE</Addr5> <!-- optional -->
                                </ShipAddressBlock>
                                <IsPending >BOOLTYPE</IsPending> <!-- optional -->
                                <PONumber >STRTYPE</PONumber> <!-- optional -->
                                <TermsRef> <!-- optional -->
                                        <ListID >IDTYPE</ListID> <!-- optional -->
                                        <FullName >STRTYPE</FullName> <!-- optional -->
                                </TermsRef>
                                <DueDate >DATETYPE</DueDate> <!-- optional -->
                                <SalesRepRef> <!-- optional -->
                                        <ListID >IDTYPE</ListID> <!-- optional -->
                                        <FullName >STRTYPE</FullName> <!-- optional -->
                                </SalesRepRef>
                                <FOB >STRTYPE</FOB> <!-- optional -->
                                <ShipDate >DATETYPE</ShipDate> <!-- optional -->
                                <ShipMethodRef> <!-- optional -->
                                        <ListID >IDTYPE</ListID> <!-- optional -->
                                        <FullName >STRTYPE</FullName> <!-- optional -->
                                </ShipMethodRef>
                                <Subtotal >AMTTYPE</Subtotal> <!-- optional -->
                                <ItemSalesTaxRef> <!-- optional -->
                                        <ListID >IDTYPE</ListID> <!-- optional -->
                                        <FullName >STRTYPE</FullName> <!-- optional -->
                                </ItemSalesTaxRef>
                                <SalesTaxPercentage >PERCENTTYPE</SalesTaxPercentage> <!-- optional -->
                                <SalesTaxTotal >AMTTYPE</SalesTaxTotal> <!-- optional -->
                                <TotalAmount >AMTTYPE</TotalAmount> <!-- optional -->
                                <CreditRemaining >AMTTYPE</CreditRemaining> <!-- optional -->
                                <CurrencyRef> <!-- optional -->
                                        <ListID >IDTYPE</ListID> <!-- optional -->
                                        <FullName >STRTYPE</FullName> <!-- optional -->
                                </CurrencyRef>
                                <ExchangeRate >FLOATTYPE</ExchangeRate> <!-- optional -->
                                <CreditRemainingInHomeCurrency >AMTTYPE</CreditRemainingInHomeCurrency> <!-- optional -->
                                <Memo >STRTYPE</Memo> <!-- optional -->
                                <CustomerMsgRef> <!-- optional -->
                                        <ListID >IDTYPE</ListID> <!-- optional -->
                                        <FullName >STRTYPE</FullName> <!-- optional -->
                                </CustomerMsgRef>
                                <IsToBePrinted >BOOLTYPE</IsToBePrinted> <!-- optional -->
                                <IsToBeEmailed >BOOLTYPE</IsToBeEmailed> <!-- optional -->
                                <IsTaxIncluded >BOOLTYPE</IsTaxIncluded> <!-- optional -->
                                <CustomerSalesTaxCodeRef> <!-- optional -->
                                        <ListID >IDTYPE</ListID> <!-- optional -->
                                        <FullName >STRTYPE</FullName> <!-- optional -->
                                </CustomerSalesTaxCodeRef>
                                <Other >STRTYPE</Other> <!-- optional -->
                                <ExternalGUID >GUIDTYPE</ExternalGUID> <!-- optional -->
                                <LinkedTxn> <!-- optional, may repeat -->
                                        <TxnID >IDTYPE</TxnID> <!-- required -->
                                        <!-- TxnType may have one of the following values: ARRefundCreditCard, Bill, BillPaymentCheck, BillPaymentCreditCard, BuildAssembly, Charge, Check, CreditCardCharge, CreditCardCredit, CreditMemo, Deposit, Estimate, InventoryAdjustment, Invoice, ItemReceipt, JournalEntry, LiabilityAdjustment, Paycheck, PayrollLiabilityCheck, PurchaseOrder, ReceivePayment, SalesOrder, SalesReceipt, SalesTaxPaymentCheck, Transfer, VendorCredit, YTDAdjustment -->
                                        <TxnType >ENUMTYPE</TxnType> <!-- required -->
                                        <TxnDate >DATETYPE</TxnDate> <!-- required -->
                                        <RefNumber >STRTYPE</RefNumber> <!-- optional -->
                                        <!-- LinkType may have one of the following values: AMTTYPE, QUANTYPE -->
                                        <LinkType >ENUMTYPE</LinkType> <!-- optional -->
                                        <Amount >AMTTYPE</Amount> <!-- required -->
                                </LinkedTxn>
                                <!-- BEGIN OR -->
                                        <CreditMemoLineRet> <!-- optional -->
                                                <TxnLineID >IDTYPE</TxnLineID> <!-- required -->
                                                <ItemRef> <!-- optional -->
                                                        <ListID >IDTYPE</ListID> <!-- optional -->
                                                        <FullName >STRTYPE</FullName> <!-- optional -->
                                                </ItemRef>
                                                <Desc >STRTYPE</Desc> <!-- optional -->
                                                <Quantity >QUANTYPE</Quantity> <!-- optional -->
                                                <UnitOfMeasure >STRTYPE</UnitOfMeasure> <!-- optional -->
                                                <OverrideUOMSetRef> <!-- optional -->
                                                        <ListID >IDTYPE</ListID> <!-- optional -->
                                                        <FullName >STRTYPE</FullName> <!-- optional -->
                                                </OverrideUOMSetRef>
                                                <!-- BEGIN OR -->
                                                        <Rate >PRICETYPE</Rate> <!-- optional -->
                                                <!-- OR -->
                                                        <RatePercent >PERCENTTYPE</RatePercent> <!-- optional -->
                                                <!-- END OR -->
                                                <ClassRef> <!-- optional -->
                                                        <ListID >IDTYPE</ListID> <!-- optional -->
                                                        <FullName >STRTYPE</FullName> <!-- optional -->
                                                </ClassRef>
                                                <Amount >AMTTYPE</Amount> <!-- optional -->
                                                <InventorySiteRef> <!-- optional -->
                                                        <ListID >IDTYPE</ListID> <!-- optional -->
                                                        <FullName >STRTYPE</FullName> <!-- optional -->
                                                </InventorySiteRef>
                                                <InventorySiteLocationRef> <!-- optional -->
                                                        <ListID >IDTYPE</ListID> <!-- optional -->
                                                        <FullName >STRTYPE</FullName> <!-- optional -->
                                                </InventorySiteLocationRef>
                                                <!-- BEGIN OR -->
                                                        <SerialNumber >STRTYPE</SerialNumber> <!-- optional -->
                                                <!-- OR -->
                                                        <LotNumber >STRTYPE</LotNumber> <!-- optional -->
                                                <!-- END OR -->
                                                <ExpirationDateForSerialLotNumber>STRTYPE</ExpirationDateForSerialLotNumber> <!-- optional -->
                                                <ServiceDate >DATETYPE</ServiceDate> <!-- optional -->
                                                <SalesTaxCodeRef> <!-- optional -->
                                                        <ListID >IDTYPE</ListID> <!-- optional -->
                                                        <FullName >STRTYPE</FullName> <!-- optional -->
                                                </SalesTaxCodeRef>
                                                <Other1 >STRTYPE</Other1> <!-- optional -->
                                                <Other2 >STRTYPE</Other2> <!-- optional -->
                                                <CreditCardTxnInfo> <!-- optional -->
                                                        <CreditCardTxnInputInfo> <!-- required -->
                                                                <CreditCardNumber >STRTYPE</CreditCardNumber> <!-- required -->
                                                                <ExpirationMonth >INTTYPE</ExpirationMonth> <!-- required -->
                                                                <ExpirationYear >INTTYPE</ExpirationYear> <!-- required -->
                                                                <NameOnCard >STRTYPE</NameOnCard> <!-- required -->
                                                                <CreditCardAddress >STRTYPE</CreditCardAddress> <!-- optional -->
                                                                <CreditCardPostalCode >STRTYPE</CreditCardPostalCode> <!-- optional -->
                                                                <CommercialCardCode >STRTYPE</CommercialCardCode> <!-- optional -->
                                                                <!-- TransactionMode may have one of the following values: CardNotPresent [DEFAULT], CardPresent -->
                                                                <TransactionMode >ENUMTYPE</TransactionMode> <!-- optional -->
                                                                <!-- CreditCardTxnType may have one of the following values: Authorization, Capture, Charge, Refund, VoiceAuthorization -->
                                                                <CreditCardTxnType >ENUMTYPE</CreditCardTxnType> <!-- optional -->
                                                        </CreditCardTxnInputInfo>
                                                        <CreditCardTxnResultInfo> <!-- required -->
                                                                <ResultCode >INTTYPE</ResultCode> <!-- required -->
                                                                <ResultMessage >STRTYPE</ResultMessage> <!-- required -->
                                                                <CreditCardTransID >STRTYPE</CreditCardTransID> <!-- required -->
                                                                <MerchantAccountNumber >STRTYPE</MerchantAccountNumber> <!-- required -->
                                                                <AuthorizationCode >STRTYPE</AuthorizationCode> <!-- optional -->
                                                                <!-- AVSStreet may have one of the following values: Pass, Fail, NotAvailable -->
                                                                <AVSStreet >ENUMTYPE</AVSStreet> <!-- optional -->
                                                                <!-- AVSZip may have one of the following values: Pass, Fail, NotAvailable -->
                                                                <AVSZip >ENUMTYPE</AVSZip> <!-- optional -->
                                                                <!-- CardSecurityCodeMatch may have one of the following values: Pass, Fail, NotAvailable -->
                                                                <CardSecurityCodeMatch >ENUMTYPE</CardSecurityCodeMatch> <!-- optional -->
                                                                <ReconBatchID >STRTYPE</ReconBatchID> <!-- optional -->
                                                                <PaymentGroupingCode >INTTYPE</PaymentGroupingCode> <!-- optional -->
                                                                <!-- PaymentStatus may have one of the following values: Unknown, Completed -->
                                                                <PaymentStatus >ENUMTYPE</PaymentStatus> <!-- required -->
                                                                <TxnAuthorizationTime >DATETIMETYPE</TxnAuthorizationTime> <!-- required -->
                                                                <TxnAuthorizationStamp >INTTYPE</TxnAuthorizationStamp> <!-- optional -->
                                                                <ClientTransID >STRTYPE</ClientTransID> <!-- optional -->
                                                        </CreditCardTxnResultInfo>
                                                </CreditCardTxnInfo>
                                                <DataExtRet> <!-- optional, may repeat -->
                                                        <OwnerID >GUIDTYPE</OwnerID> <!-- optional -->
                                                        <DataExtName >STRTYPE</DataExtName> <!-- required -->
                                                        <!-- DataExtType may have one of the following values: AMTTYPE, DATETIMETYPE, INTTYPE, PERCENTTYPE, PRICETYPE, QUANTYPE, STR1024TYPE, STR255TYPE -->
                                                        <DataExtType >ENUMTYPE</DataExtType> <!-- required -->
                                                        <DataExtValue >STRTYPE</DataExtValue> <!-- required -->
                                                </DataExtRet>
                                        </CreditMemoLineRet>
                                <!-- OR -->
                                        <CreditMemoLineGroupRet> <!-- optional -->
                                                <TxnLineID >IDTYPE</TxnLineID> <!-- required -->
                                                <ItemGroupRef> <!-- required -->
                                                        <ListID >IDTYPE</ListID> <!-- optional -->
                                                        <FullName >STRTYPE</FullName> <!-- optional -->
                                                </ItemGroupRef>
                                                <Desc >STRTYPE</Desc> <!-- optional -->
                                                <Quantity >QUANTYPE</Quantity> <!-- optional -->
                                                <UnitOfMeasure >STRTYPE</UnitOfMeasure> <!-- optional -->
                                                <OverrideUOMSetRef> <!-- optional -->
                                                        <ListID >IDTYPE</ListID> <!-- optional -->
                                                        <FullName >STRTYPE</FullName> <!-- optional -->
                                                </OverrideUOMSetRef>
                                                <IsPrintItemsInGroup >BOOLTYPE</IsPrintItemsInGroup> <!-- required -->
                                                <TotalAmount >AMTTYPE</TotalAmount> <!-- required -->
                                                <CreditMemoLineRet> <!-- optional, may repeat -->
                                                        <TxnLineID >IDTYPE</TxnLineID> <!-- required -->
                                                        <ItemRef> <!-- optional -->
                                                                <ListID >IDTYPE</ListID> <!-- optional -->
                                                                <FullName >STRTYPE</FullName> <!-- optional -->
                                                        </ItemRef>
                                                        <Desc >STRTYPE</Desc> <!-- optional -->
                                                        <Quantity >QUANTYPE</Quantity> <!-- optional -->
                                                        <UnitOfMeasure >STRTYPE</UnitOfMeasure> <!-- optional -->
                                                        <OverrideUOMSetRef> <!-- optional -->
                                                                <ListID >IDTYPE</ListID> <!-- optional -->
                                                                <FullName >STRTYPE</FullName> <!-- optional -->
                                                        </OverrideUOMSetRef>
                                                        <!-- BEGIN OR -->
                                                                <Rate >PRICETYPE</Rate> <!-- optional -->
                                                        <!-- OR -->
                                                                <RatePercent >PERCENTTYPE</RatePercent> <!-- optional -->
                                                        <!-- END OR -->
                                                        <ClassRef> <!-- optional -->
                                                                <ListID >IDTYPE</ListID> <!-- optional -->
                                                                <FullName >STRTYPE</FullName> <!-- optional -->
                                                        </ClassRef>
                                                        <Amount >AMTTYPE</Amount> <!-- optional -->
                                                        <InventorySiteRef> <!-- optional -->
                                                                <ListID >IDTYPE</ListID> <!-- optional -->
                                                                <FullName >STRTYPE</FullName> <!-- optional -->
                                                        </InventorySiteRef>
                                                        <InventorySiteLocationRef> <!-- optional -->
                                                                <ListID >IDTYPE</ListID> <!-- optional -->
                                                                <FullName >STRTYPE</FullName> <!-- optional -->
                                                        </InventorySiteLocationRef>
                                                        <!-- BEGIN OR -->
                                                                <SerialNumber >STRTYPE</SerialNumber> <!-- optional -->
                                                        <!-- OR -->
                                                                <LotNumber >STRTYPE</LotNumber> <!-- optional -->
                                                        <!-- END OR -->
                                                        <ExpirationDateForSerialLotNumber>STRTYPE</ExpirationDateForSerialLotNumber> <!-- optional -->
                                                        <ServiceDate >DATETYPE</ServiceDate> <!-- optional -->
                                                        <SalesTaxCodeRef> <!-- optional -->
                                                                <ListID >IDTYPE</ListID> <!-- optional -->
                                                                <FullName >STRTYPE</FullName> <!-- optional -->
                                                        </SalesTaxCodeRef>
                                                        <Other1 >STRTYPE</Other1> <!-- optional -->
                                                        <Other2 >STRTYPE</Other2> <!-- optional -->
                                                        <CreditCardTxnInfo> <!-- optional -->
                                                                <CreditCardTxnInputInfo> <!-- required -->
                                                                        <CreditCardNumber >STRTYPE</CreditCardNumber> <!-- required -->
                                                                        <ExpirationMonth >INTTYPE</ExpirationMonth> <!-- required -->
                                                                        <ExpirationYear >INTTYPE</ExpirationYear> <!-- required -->
                                                                        <NameOnCard >STRTYPE</NameOnCard> <!-- required -->
                                                                        <CreditCardAddress >STRTYPE</CreditCardAddress> <!-- optional -->
                                                                        <CreditCardPostalCode >STRTYPE</CreditCardPostalCode> <!-- optional -->
                                                                        <CommercialCardCode >STRTYPE</CommercialCardCode> <!-- optional -->
                                                                        <!-- TransactionMode may have one of the following values: CardNotPresent [DEFAULT], CardPresent -->
                                                                        <TransactionMode >ENUMTYPE</TransactionMode> <!-- optional -->
                                                                        <!-- CreditCardTxnType may have one of the following values: Authorization, Capture, Charge, Refund, VoiceAuthorization -->
                                                                        <CreditCardTxnType >ENUMTYPE</CreditCardTxnType> <!-- optional -->
                                                                </CreditCardTxnInputInfo>
                                                                <CreditCardTxnResultInfo> <!-- required -->
                                                                        <ResultCode >INTTYPE</ResultCode> <!-- required -->
                                                                        <ResultMessage >STRTYPE</ResultMessage> <!-- required -->
                                                                        <CreditCardTransID >STRTYPE</CreditCardTransID> <!-- required -->
                                                                        <MerchantAccountNumber >STRTYPE</MerchantAccountNumber> <!-- required -->
                                                                        <AuthorizationCode >STRTYPE</AuthorizationCode> <!-- optional -->
                                                                        <!-- AVSStreet may have one of the following values: Pass, Fail, NotAvailable -->
                                                                        <AVSStreet >ENUMTYPE</AVSStreet> <!-- optional -->
                                                                        <!-- AVSZip may have one of the following values: Pass, Fail, NotAvailable -->
                                                                        <AVSZip >ENUMTYPE</AVSZip> <!-- optional -->
                                                                        <!-- CardSecurityCodeMatch may have one of the following values: Pass, Fail, NotAvailable -->
                                                                        <CardSecurityCodeMatch >ENUMTYPE</CardSecurityCodeMatch> <!-- optional -->
                                                                        <ReconBatchID >STRTYPE</ReconBatchID> <!-- optional -->
                                                                        <PaymentGroupingCode >INTTYPE</PaymentGroupingCode> <!-- optional -->
                                                                        <!-- PaymentStatus may have one of the following values: Unknown, Completed -->
                                                                        <PaymentStatus >ENUMTYPE</PaymentStatus> <!-- required -->
                                                                        <TxnAuthorizationTime >DATETIMETYPE</TxnAuthorizationTime> <!-- required -->
                                                                        <TxnAuthorizationStamp >INTTYPE</TxnAuthorizationStamp> <!-- optional -->
                                                                        <ClientTransID >STRTYPE</ClientTransID> <!-- optional -->
                                                                </CreditCardTxnResultInfo>
                                                        </CreditCardTxnInfo>
                                                        <DataExtRet> <!-- optional, may repeat -->
                                                                <OwnerID >GUIDTYPE</OwnerID> <!-- optional -->
                                                                <DataExtName >STRTYPE</DataExtName> <!-- required -->
                                                                <!-- DataExtType may have one of the following values: AMTTYPE, DATETIMETYPE, INTTYPE, PERCENTTYPE, PRICETYPE, QUANTYPE, STR1024TYPE, STR255TYPE -->
                                                                <DataExtType >ENUMTYPE</DataExtType> <!-- required -->
                                                                <DataExtValue >STRTYPE</DataExtValue> <!-- required -->
                                                        </DataExtRet>
                                                </CreditMemoLineRet>
                                                <DataExtRet> <!-- optional, may repeat -->
                                                        <OwnerID >GUIDTYPE</OwnerID> <!-- optional -->
                                                        <DataExtName >STRTYPE</DataExtName> <!-- required -->
                                                        <!-- DataExtType may have one of the following values: AMTTYPE, DATETIMETYPE, INTTYPE, PERCENTTYPE, PRICETYPE, QUANTYPE, STR1024TYPE, STR255TYPE -->
                                                        <DataExtType >ENUMTYPE</DataExtType> <!-- required -->
                                                        <DataExtValue >STRTYPE</DataExtValue> <!-- required -->
                                                </DataExtRet>
                                        </CreditMemoLineGroupRet>
                                <!-- END OR -->
                                <DataExtRet> <!-- optional, may repeat -->
                                        <OwnerID >GUIDTYPE</OwnerID> <!-- optional -->
                                        <DataExtName >STRTYPE</DataExtName> <!-- required -->
                                        <!-- DataExtType may have one of the following values: AMTTYPE, DATETIMETYPE, INTTYPE, PERCENTTYPE, PRICETYPE, QUANTYPE, STR1024TYPE, STR255TYPE -->
                                        <DataExtType >ENUMTYPE</DataExtType> <!-- required -->
                                        <DataExtValue >STRTYPE</DataExtValue> <!-- required -->
                                </DataExtRet>
                        </CreditMemoRet>
                </CreditMemoQueryRs>
        </QBXMLMsgsRq>
</QBXML>

```

## CurrencyQuery
### XMLOps
```
<?xml version="1.0" encoding="utf-8"?>
<?qbxml version="16.0"?>
<QBXML>
        <QBXMLMsgsRq onError="stopOnError">
                <CurrencyQueryRq metaData="ENUMTYPE">
                        <!-- BEGIN OR -->
                                <ListID >IDTYPE</ListID> <!-- optional, may repeat -->
                        <!-- OR -->
                                <FullName >STRTYPE</FullName> <!-- optional, may repeat -->
                        <!-- OR -->
                                <MaxReturned >INTTYPE</MaxReturned> <!-- optional -->
                                <!-- ActiveStatus may have one of the following values: ActiveOnly [DEFAULT], InactiveOnly, All -->
                                <ActiveStatus >ENUMTYPE</ActiveStatus> <!-- optional -->
                                <FromModifiedDate >DATETIMETYPE</FromModifiedDate> <!-- optional -->
                                <ToModifiedDate >DATETIMETYPE</ToModifiedDate> <!-- optional -->
                                <!-- BEGIN OR -->
                                        <NameFilter> <!-- optional -->
                                                <!-- MatchCriterion may have one of the following values: StartsWith, Contains, EndsWith -->
                                                <MatchCriterion >ENUMTYPE</MatchCriterion> <!-- required -->
                                                <Name >STRTYPE</Name> <!-- required -->
                                        </NameFilter>
                                <!-- OR -->
                                        <NameRangeFilter> <!-- optional -->
                                                <FromName >STRTYPE</FromName> <!-- optional -->
                                                <ToName >STRTYPE</ToName> <!-- optional -->
                                        </NameRangeFilter>
                                <!-- END OR -->
                        <!-- END OR -->
                        <IncludeRetElement >STRTYPE</IncludeRetElement> <!-- optional, may repeat -->
                </CurrencyQueryRq>

                <CurrencyQueryRs statusCode="INTTYPE" statusSeverity="STRTYPE" statusMessage="STRTYPE" retCount="INTTYPE">
                        <CurrencyRet> <!-- optional, may repeat -->
                                <ListID >IDTYPE</ListID> <!-- optional -->
                                <TimeCreated >DATETIMETYPE</TimeCreated> <!-- optional -->
                                <TimeModified >DATETIMETYPE</TimeModified> <!-- optional -->
                                <EditSequence >STRTYPE</EditSequence> <!-- optional -->
                                <Name >STRTYPE</Name> <!-- optional -->
                                <IsActive >BOOLTYPE</IsActive> <!-- optional -->
                                <CurrencyCode >STRTYPE</CurrencyCode> <!-- optional -->
                                <CurrencyFormat> <!-- optional -->
                                        <!-- ThousandSeparator may have one of the following values: Comma [DEFAULT], Period, Space, Apostrophe -->
                                        <ThousandSeparator >ENUMTYPE</ThousandSeparator> <!-- optional -->
                                        <!-- ThousandSeparatorGrouping may have one of the following values: XX_XXX_XXX [DEFAULT], X_XX_XX_XXX -->
                                        <ThousandSeparatorGrouping >ENUMTYPE</ThousandSeparatorGrouping> <!-- optional -->
                                        <!-- DecimalPlaces may have one of the following values: 0, 2 [DEFAULT] -->
                                        <DecimalPlaces >ENUMTYPE</DecimalPlaces> <!-- optional -->
                                        <!-- DecimalSeparator may have one of the following values: Period [DEFAULT], Comma -->
                                        <DecimalSeparator >ENUMTYPE</DecimalSeparator> <!-- optional -->
                                </CurrencyFormat>
                                <IsUserDefinedCurrency >BOOLTYPE</IsUserDefinedCurrency> <!-- optional -->
                                <ExchangeRate >FLOATTYPE</ExchangeRate> <!-- optional -->
                                <AsOfDate >DATETYPE</AsOfDate> <!-- optional -->
                        </CurrencyRet>
                </CurrencyQueryRs>
        </QBXMLMsgsRq>
</QBXML>

```
## CustomerDetailReportQuery
### XMLOps
```
<?xml version="1.0" encoding="utf-8"?>
<?qbxml version="16.0"?>
<QBXML>
        <QBXMLMsgsRq onError="stopOnError">
                <CustomDetailReportQueryRq>
                        <!-- CustomDetailReportType may have one of the following values: CustomTxnDetail -->
                        <CustomDetailReportType >ENUMTYPE</CustomDetailReportType> <!-- required -->
                        <DisplayReport >BOOLTYPE</DisplayReport> <!-- optional -->
                        <!-- BEGIN OR -->
                                <ReportPeriod> <!-- optional -->
                                        <FromReportDate >DATETYPE</FromReportDate> <!-- optional -->
                                        <ToReportDate >DATETYPE</ToReportDate> <!-- optional -->
                                </ReportPeriod>
                        <!-- OR -->
                                <!-- ReportDateMacro may have one of the following values: All, Today, ThisWeek, ThisWeekToDate, ThisMonth, ThisMonthToDate, ThisQuarter, ThisQuarterToDate, ThisYear, ThisYearToDate, Yesterday, LastWeek, LastWeekToDate, LastMonth, LastMonthToDate, LastQuarter, LastQuarterToDate, LastYear, LastYearToDate, NextWeek, NextFourWeeks, NextMonth, NextQuarter, NextYear -->
                                <ReportDateMacro >ENUMTYPE</ReportDateMacro> <!-- optional -->
                        <!-- END OR -->
                        <ReportAccountFilter> <!-- optional -->
                                <!-- BEGIN OR -->
                                        <!-- AccountTypeFilter may have one of the following values: AccountsPayable, AccountsReceivable, AllowedFor1099, APAndSalesTax, APOrCreditCard, ARAndAP, Asset, BalanceSheet, Bank, BankAndARAndAPAndUF, BankAndUF, CostOfSales, CreditCard, CurrentAsset, CurrentAssetAndExpense, CurrentLiability, Equity, EquityAndIncomeAndExpense, ExpenseAndOtherExpense, FixedAsset, IncomeAndExpense, IncomeAndOtherIncome, Liability, LiabilityAndEquity, LongTermLiability, NonPosting, OrdinaryExpense, OrdinaryIncome, OrdinaryIncomeAndCOGS, OrdinaryIncomeAndExpense, OtherAsset, OtherCurrentAsset, OtherCurrentLiability, OtherExpense, OtherIncome, OtherIncomeOrExpense -->
                                        <AccountTypeFilter >ENUMTYPE</AccountTypeFilter> <!-- optional -->
                                <!-- OR -->
                                        <ListID >IDTYPE</ListID> <!-- optional, may repeat -->
                                <!-- OR -->
                                        <FullName >STRTYPE</FullName> <!-- optional, may repeat -->
                                <!-- OR -->
                                        <ListIDWithChildren >IDTYPE</ListIDWithChildren> <!-- optional -->
                                <!-- OR -->
                                        <FullNameWithChildren >STRTYPE</FullNameWithChildren> <!-- optional -->
                                <!-- END OR -->
                        </ReportAccountFilter>
                        <ReportEntityFilter> <!-- optional -->
                                <!-- BEGIN OR -->
                                        <!-- EntityTypeFilter may have one of the following values: Customer, Employee, OtherName, Vendor -->
                                        <EntityTypeFilter >ENUMTYPE</EntityTypeFilter> <!-- optional -->
                                <!-- OR -->
                                        <ListID >IDTYPE</ListID> <!-- optional, may repeat -->
                                <!-- OR -->
                                        <FullName >STRTYPE</FullName> <!-- optional, may repeat -->
                                <!-- OR -->
                                        <ListIDWithChildren >IDTYPE</ListIDWithChildren> <!-- optional -->
                                <!-- OR -->
                                        <FullNameWithChildren >STRTYPE</FullNameWithChildren> <!-- optional -->
                                <!-- END OR -->
                        </ReportEntityFilter>
                        <ReportItemFilter> <!-- optional -->
                                <!-- BEGIN OR -->
                                        <!-- ItemTypeFilter may have one of the following values: AllExceptFixedAsset, Assembly, Discount, FixedAsset, Inventory, InventoryAndAssembly, NonInventory, OtherCharge, Payment, Sales, SalesTax, Service -->
                                        <ItemTypeFilter >ENUMTYPE</ItemTypeFilter> <!-- optional -->
                                <!-- OR -->
                                        <ListID >IDTYPE</ListID> <!-- optional, may repeat -->
                                <!-- OR -->
                                        <FullName >STRTYPE</FullName> <!-- optional, may repeat -->
                                <!-- OR -->
                                        <ListIDWithChildren >IDTYPE</ListIDWithChildren> <!-- optional -->
                                <!-- OR -->
                                        <FullNameWithChildren >STRTYPE</FullNameWithChildren> <!-- optional -->
                                <!-- END OR -->
                        </ReportItemFilter>
                        <ReportClassFilter> <!-- optional -->
                                <!-- BEGIN OR -->
                                        <ListID >IDTYPE</ListID> <!-- optional, may repeat -->
                                <!-- OR -->
                                        <FullName >STRTYPE</FullName> <!-- optional, may repeat -->
                                <!-- OR -->
                                        <ListIDWithChildren >IDTYPE</ListIDWithChildren> <!-- optional -->
                                <!-- OR -->
                                        <FullNameWithChildren >STRTYPE</FullNameWithChildren> <!-- optional -->
                                <!-- END OR -->
                        </ReportClassFilter>
                        <ReportTxnTypeFilter> <!-- optional -->
                                <!-- TxnTypeFilter may have one of the following values: All, ARRefundCreditCard, Bill, BillPaymentCheck, BillPaymentCreditCard, BuildAssembly, Charge, Check, CreditCardCharge, CreditCardCredit, CreditMemo, Deposit, Estimate, InventoryAdjustment, Invoice, ItemReceipt, JournalEntry, LiabilityAdjustment, Paycheck, PayrollLiabilityCheck, PurchaseOrder, ReceivePayment, SalesOrder, SalesReceipt, SalesTaxPaymentCheck, Transfer, VendorCredit, YTDAdjustment -->
                                <TxnTypeFilter >ENUMTYPE</TxnTypeFilter> <!-- required, may repeat -->
                        </ReportTxnTypeFilter>
                        <!-- BEGIN OR -->
                                <ReportModifiedDateRangeFilter> <!-- optional -->
                                        <FromReportModifiedDate >DATETYPE</FromReportModifiedDate> <!-- optional -->
                                        <ToReportModifiedDate >DATETYPE</ToReportModifiedDate> <!-- optional -->
                                </ReportModifiedDateRangeFilter>
                        <!-- OR -->
                                <!-- ReportModifiedDateRangeMacro may have one of the following values: All, Today, ThisWeek, ThisWeekToDate, ThisMonth, ThisMonthToDate, ThisQuarter, ThisQuarterToDate, ThisYear, ThisYearToDate, Yesterday, LastWeek, LastWeekToDate, LastMonth, LastMonthToDate, LastQuarter, LastQuarterToDate, LastYear, LastYearToDate, NextWeek, NextFourWeeks, NextMonth, NextQuarter, NextYear -->
                                <ReportModifiedDateRangeMacro >ENUMTYPE</ReportModifiedDateRangeMacro> <!-- optional -->
                        <!-- END OR -->
                        <!-- ReportDetailLevelFilter may have one of the following values: All [DEFAULT], AllExceptSummary, SummaryOnly -->
                        <ReportDetailLevelFilter >ENUMTYPE</ReportDetailLevelFilter> <!-- optional -->
                        <!-- ReportPostingStatusFilter may have one of the following values: Either, NonPosting, Posting -->
                        <ReportPostingStatusFilter >ENUMTYPE</ReportPostingStatusFilter> <!-- optional -->
                        <!-- SummarizeRowsBy may have one of the following values: Account, BalanceSheet, Class, Customer, CustomerType, Day, Employee, FourWeek, HalfMonth, IncomeStatement, ItemDetail, ItemType, Month, Payee, PaymentMethod, PayrollItemDetail, PayrollYtdDetail, Quarter, SalesRep, SalesTaxCode, ShipMethod, TaxLine, Terms, TotalOnly, TwoWeek, Vendor, VendorType, Week, Year -->
                        <SummarizeRowsBy >ENUMTYPE</SummarizeRowsBy> <!-- required -->
                        <!-- IncludeColumn may have one of the following values: Account, Aging, Amount, AmountDifference, AverageCost, BilledDate, BillingStatus, CalculatedAmount, Class, ClearedStatus, CostPrice, Credit, Currency, Date, Debit, DeliveryDate, DueDate, EstimateActive, ExchangeRate, FOB, IncomeSubjectToTax, Invoiced, Item, ItemDesc, LastModifiedBy, LatestOrPriorState, Memo, ModifiedTime, Name, NameAccountNumber, NameAddress, NameCity, NameContact, NameEmail, NameFax, NamePhone, NameState, NameZip, OpenBalance, OriginalAmount, PaidAmount, PaidStatus, PaidThroughDate, PaymentMethod, PayrollItem, PONumber, PrintStatus, ProgressAmount, ProgressPercent, Quantity, QuantityAvailable, QuantityOnHand, QuantityOnSalesOrder, ReceivedQuantity, RefNumber, RunningBalance, SalesRep, SalesTaxCode, SerialOrLotNumber, ShipDate, ShipMethod, SourceName, SplitAccount, SSNOrTaxID, TaxLine, TaxTableVersion, Terms, TxnID, TxnNumber, TxnType, UnitPrice, UserEdit, ValueOnHand, WageBase, WageBaseTips -->
                        <IncludeColumn >ENUMTYPE</IncludeColumn> <!-- required, may repeat -->
                        <!-- IncludeAccounts may have one of the following values: All, InUse -->
                        <IncludeAccounts >ENUMTYPE</IncludeAccounts> <!-- optional -->
                        <!-- ReportOpenBalanceAsOf may have one of the following values: ReportEndDate, Today [DEFAULT] -->
                        <ReportOpenBalanceAsOf >ENUMTYPE</ReportOpenBalanceAsOf> <!-- optional -->
                        <!-- ReportBasis may have one of the following values: Accrual, Cash, None [DEFAULT] -->
                        <ReportBasis >ENUMTYPE</ReportBasis> <!-- optional -->
                </CustomDetailReportQueryRq>

                <CustomDetailReportQueryRs statusCode="INTTYPE" statusSeverity="STRTYPE" statusMessage="STRTYPE">
                        <ReportRet> <!-- optional -->
                                <ReportTitle >STRTYPE</ReportTitle> <!-- required -->
                                <ReportSubtitle >STRTYPE</ReportSubtitle> <!-- required -->
                                <!-- ReportBasis may have one of the following values: Accrual, Cash, None [DEFAULT] -->
                                <ReportBasis >ENUMTYPE</ReportBasis> <!-- optional -->
                                <NumRows >INTTYPE</NumRows> <!-- required -->
                                <NumColumns >INTTYPE</NumColumns> <!-- required -->
                                <NumColTitleRows >INTTYPE</NumColTitleRows> <!-- required -->
                                <ColDesc colID="INTTYPE" dataType="ENUMTYPE"> <!-- required, may repeat -->
                                        <ColTitle titleRow="INTTYPE" value="STRTYPE"> <!-- required, may repeat -->
                                        </ColTitle>
                                        <!-- ColType may have one of the following values: Account, Addr1, Addr2, Addr3, Addr4, Addr5, Aging, Amount, AmountDifference, AverageCost, BilledDate, BillingStatus, Blank, CalculatedAmount, Class, ClearedStatus, CostPrice, CreateDate, Credit, CustomField, Date, Debit, DeliveryDate, DueDate, Duration, EarliestReceiptDate, EstimateActive, FOB, IncomeSubjectToTax, Invoiced, IsAdjustment, Item, ItemDesc, ItemVendor, Label, LastModifiedBy, LatestOrPriorState, Memo, ModifiedTime, Name, NameAccountNumber, NameAddress, NameCity, NameContact, NameEmail, NameFax, NamePhone, NameState, NameZip, OpenBalance, OriginalAmount, PaidAmount, PaidStatus, PaidThroughDate, PaymentMethod, PayrollItem, Percent, PercentChange, PercentOfTotalRetail, PercentOfTotalValue, PhysicalCount, PONumber, PrintStatus, ProgressAmount, ProgressPercent, Quantity, QuantityAvailable, QuantityOnHand, QuantityOnOrder, QuantityOnPendingBuild, QuantityOnSalesOrder, ReceivedQuantity, RefNumber, ReorderPoint, RetailValueOnHand, RunningBalance, SalesPerWeek, SalesRep, SalesTaxCode, ShipDate, ShipMethod, ShipToAddr1, ShipToAddr2, ShipToAddr3, ShipToAddr4, ShipToAddr5, SONumber, SourceName, SplitAccount, SSNOrTaxID, SuggestedReorder, TaxLine, TaxTableVersion, Terms, Total, TxnID, TxnNumber, TxnType, UnitPrice, UserEdit, ValueOnHand, WageBase, WageBaseTips -->
                                        <ColType >ENUMTYPE</ColType> <!-- required -->
                                </ColDesc>
                                <ReportData> <!-- optional -->
                                        <!-- BEGIN OR -->
                                                <DataRow> <!-- optional -->
                                                        <RowData rowType="ENUMTYPE" value="STRTYPE"> <!-- optional -->
                                                        </RowData>
                                                        <ColData colID="INTTYPE" value="STRTYPE" dataType="ENUMTYPE"> <!-- optional, may repeat -->
                                                        </ColData>
                                                </DataRow>
                                        <!-- OR -->
                                                <TextRow rowNumber="INTTYPE" value="STRTYPE"> <!-- optional -->
                                                </TextRow>
                                        <!-- OR -->
                                                <SubtotalRow> <!-- optional -->
                                                        <RowData rowType="ENUMTYPE" value="STRTYPE"> <!-- optional -->
                                                        </RowData>
                                                        <ColData colID="INTTYPE" value="STRTYPE" dataType="ENUMTYPE"> <!-- optional, may repeat -->
                                                        </ColData>
                                                </SubtotalRow>
                                        <!-- OR -->
                                                <TotalRow> <!-- optional -->
                                                        <RowData rowType="ENUMTYPE" value="STRTYPE"> <!-- optional -->
                                                        </RowData>
                                                        <ColData colID="INTTYPE" value="STRTYPE" dataType="ENUMTYPE"> <!-- optional, may repeat -->
                                                        </ColData>
                                                </TotalRow>
                                        <!-- END OR -->
                                </ReportData>
                        </ReportRet>
                </CustomDetailReportQueryRs>
        </QBXMLMsgsRq>
</QBXML>

```

## CustomerMsgQuery
### XMLOps
```
<?xml version="1.0" encoding="utf-8"?>
<?qbxml version="16.0"?>
<QBXML>
        <QBXMLMsgsRq onError="stopOnError">
                <CustomerMsgQueryRq metaData="ENUMTYPE">
                        <!-- BEGIN OR -->
                                <ListID >IDTYPE</ListID> <!-- optional, may repeat -->
                        <!-- OR -->
                                <FullName >STRTYPE</FullName> <!-- optional, may repeat -->
                        <!-- OR -->
                                <MaxReturned >INTTYPE</MaxReturned> <!-- optional -->
                                <!-- ActiveStatus may have one of the following values: ActiveOnly [DEFAULT], InactiveOnly, All -->
                                <ActiveStatus >ENUMTYPE</ActiveStatus> <!-- optional -->
                                <FromModifiedDate >DATETIMETYPE</FromModifiedDate> <!-- optional -->
                                <ToModifiedDate >DATETIMETYPE</ToModifiedDate> <!-- optional -->
                                <!-- BEGIN OR -->
                                        <NameFilter> <!-- optional -->
                                                <!-- MatchCriterion may have one of the following values: StartsWith, Contains, EndsWith -->
                                                <MatchCriterion >ENUMTYPE</MatchCriterion> <!-- required -->
                                                <Name >STRTYPE</Name> <!-- required -->
                                        </NameFilter>
                                <!-- OR -->
                                        <NameRangeFilter> <!-- optional -->
                                                <FromName >STRTYPE</FromName> <!-- optional -->
                                                <ToName >STRTYPE</ToName> <!-- optional -->
                                        </NameRangeFilter>
                                <!-- END OR -->
                        <!-- END OR -->
                        <IncludeRetElement >STRTYPE</IncludeRetElement> <!-- optional, may repeat -->
                </CustomerMsgQueryRq>

                <CustomerMsgQueryRs statusCode="INTTYPE" statusSeverity="STRTYPE" statusMessage="STRTYPE" retCount="INTTYPE">
                        <CustomerMsgRet> <!-- optional, may repeat -->
                                <ListID >IDTYPE</ListID> <!-- required -->
                                <TimeCreated >DATETIMETYPE</TimeCreated> <!-- required -->
                                <TimeModified >DATETIMETYPE</TimeModified> <!-- required -->
                                <EditSequence >STRTYPE</EditSequence> <!-- required -->
                                <Name >STRTYPE</Name> <!-- required -->
                                <IsActive >BOOLTYPE</IsActive> <!-- optional -->
                        </CustomerMsgRet>
                </CustomerMsgQueryRs>
        </QBXMLMsgsRq>
</QBXML>
```
## CustomerQuery
### XMLOps
```
<?xml version="1.0" encoding="utf-8"?>
<?qbxml version="16.0"?>
<QBXML>
        <QBXMLMsgsRq onError="stopOnError">
                <CustomerQueryRq metaData="ENUMTYPE" iterator="ENUMTYPE" iteratorID="UUIDTYPE">
                        <!-- BEGIN OR -->
                                <ListID >IDTYPE</ListID> <!-- optional, may repeat -->
                        <!-- OR -->
                                <FullName >STRTYPE</FullName> <!-- optional, may repeat -->
                        <!-- OR -->
                                <MaxReturned >INTTYPE</MaxReturned> <!-- optional -->
                                <!-- ActiveStatus may have one of the following values: ActiveOnly [DEFAULT], InactiveOnly, All -->
                                <ActiveStatus >ENUMTYPE</ActiveStatus> <!-- optional -->
                                <FromModifiedDate >DATETIMETYPE</FromModifiedDate> <!-- optional -->
                                <ToModifiedDate >DATETIMETYPE</ToModifiedDate> <!-- optional -->
                                <!-- BEGIN OR -->
                                        <NameFilter> <!-- optional -->
                                                <!-- MatchCriterion may have one of the following values: StartsWith, Contains, EndsWith -->
                                                <MatchCriterion >ENUMTYPE</MatchCriterion> <!-- required -->
                                                <Name >STRTYPE</Name> <!-- required -->
                                        </NameFilter>
                                <!-- OR -->
                                        <NameRangeFilter> <!-- optional -->
                                                <FromName >STRTYPE</FromName> <!-- optional -->
                                                <ToName >STRTYPE</ToName> <!-- optional -->
                                        </NameRangeFilter>
                                <!-- END OR -->
                                <TotalBalanceFilter> <!-- optional -->
                                        <!-- Operator may have one of the following values: LessThan, LessThanEqual, Equal, GreaterThan, GreaterThanEqual -->
                                        <Operator >ENUMTYPE</Operator> <!-- required -->
                                        <Amount >AMTTYPE</Amount> <!-- required -->
                                </TotalBalanceFilter>
                                <CurrencyFilter> <!-- optional -->
                                        <!-- BEGIN OR -->
                                                <ListID >IDTYPE</ListID> <!-- optional, may repeat -->
                                        <!-- OR -->
                                                <FullName >STRTYPE</FullName> <!-- optional, may repeat -->
                                        <!-- END OR -->
                                </CurrencyFilter>
                                <ClassFilter> <!-- optional -->
                                        <!-- BEGIN OR -->
                                                <ListID >IDTYPE</ListID> <!-- optional, may repeat -->
                                        <!-- OR -->
                                                <FullName >STRTYPE</FullName> <!-- optional, may repeat -->
                                        <!-- OR -->
                                                <ListIDWithChildren >IDTYPE</ListIDWithChildren> <!-- optional -->
                                        <!-- OR -->
                                                <FullNameWithChildren >STRTYPE</FullNameWithChildren> <!-- optional -->
                                        <!-- END OR -->
                                </ClassFilter>
                        <!-- END OR -->
                        <IncludeRetElement >STRTYPE</IncludeRetElement> <!-- optional, may repeat -->
                        <OwnerID >GUIDTYPE</OwnerID> <!-- optional, may repeat -->
                </CustomerQueryRq>

                <CustomerQueryRs statusCode="INTTYPE" statusSeverity="STRTYPE" statusMessage="STRTYPE" retCount="INTTYPE" iteratorRemainingCount="INTTYPE" iteratorID="UUIDTYPE">
                        <CustomerRet> <!-- optional, may repeat -->
                                <ListID >IDTYPE</ListID> <!-- required -->
                                <TimeCreated >DATETIMETYPE</TimeCreated> <!-- required -->
                                <TimeModified >DATETIMETYPE</TimeModified> <!-- required -->
                                <EditSequence >STRTYPE</EditSequence> <!-- required -->
                                <Name >STRTYPE</Name> <!-- required -->
                                <FullName >STRTYPE</FullName> <!-- required -->
                                <IsActive >BOOLTYPE</IsActive> <!-- optional -->
                                <ClassRef> <!-- optional -->
                                        <ListID >IDTYPE</ListID> <!-- optional -->
                                        <FullName >STRTYPE</FullName> <!-- optional -->
                                </ClassRef>
                                <ParentRef> <!-- optional -->
                                        <ListID >IDTYPE</ListID> <!-- optional -->
                                        <FullName >STRTYPE</FullName> <!-- optional -->
                                </ParentRef>
                                <Sublevel >INTTYPE</Sublevel> <!-- required -->
                                <CompanyName >STRTYPE</CompanyName> <!-- optional -->
                                <Salutation >STRTYPE</Salutation> <!-- optional -->
                                <FirstName >STRTYPE</FirstName> <!-- optional -->
                                <MiddleName >STRTYPE</MiddleName> <!-- optional -->
                                <LastName >STRTYPE</LastName> <!-- optional -->
                                <JobTitle >STRTYPE</JobTitle> <!-- optional -->
                                <BillAddress> <!-- optional -->
                                        <Addr1 >STRTYPE</Addr1> <!-- optional -->
                                        <Addr2 >STRTYPE</Addr2> <!-- optional -->
                                        <Addr3 >STRTYPE</Addr3> <!-- optional -->
                                        <Addr4 >STRTYPE</Addr4> <!-- optional -->
                                        <Addr5 >STRTYPE</Addr5> <!-- optional -->
                                        <City >STRTYPE</City> <!-- optional -->
                                        <State >STRTYPE</State> <!-- optional -->
                                        <PostalCode >STRTYPE</PostalCode> <!-- optional -->
                                        <Country >STRTYPE</Country> <!-- optional -->
                                        <Note >STRTYPE</Note> <!-- optional -->
                                </BillAddress>
                                <BillAddressBlock> <!-- optional -->
                                        <Addr1 >STRTYPE</Addr1> <!-- optional -->
                                        <Addr2 >STRTYPE</Addr2> <!-- optional -->
                                        <Addr3 >STRTYPE</Addr3> <!-- optional -->
                                        <Addr4 >STRTYPE</Addr4> <!-- optional -->
                                        <Addr5 >STRTYPE</Addr5> <!-- optional -->
                                </BillAddressBlock>
                                <ShipAddress> <!-- optional -->
                                        <Addr1 >STRTYPE</Addr1> <!-- optional -->
                                        <Addr2 >STRTYPE</Addr2> <!-- optional -->
                                        <Addr3 >STRTYPE</Addr3> <!-- optional -->
                                        <Addr4 >STRTYPE</Addr4> <!-- optional -->
                                        <Addr5 >STRTYPE</Addr5> <!-- optional -->
                                        <City >STRTYPE</City> <!-- optional -->
                                        <State >STRTYPE</State> <!-- optional -->
                                        <PostalCode >STRTYPE</PostalCode> <!-- optional -->
                                        <Country >STRTYPE</Country> <!-- optional -->
                                        <Note >STRTYPE</Note> <!-- optional -->
                                </ShipAddress>
                                <ShipAddressBlock> <!-- optional -->
                                        <Addr1 >STRTYPE</Addr1> <!-- optional -->
                                        <Addr2 >STRTYPE</Addr2> <!-- optional -->
                                        <Addr3 >STRTYPE</Addr3> <!-- optional -->
                                        <Addr4 >STRTYPE</Addr4> <!-- optional -->
                                        <Addr5 >STRTYPE</Addr5> <!-- optional -->
                                </ShipAddressBlock>
                                <ShipToAddress> <!-- must occur 0 - 50 times -->
                                        <Name >STRTYPE</Name> <!-- required -->
                                        <Addr1 >STRTYPE</Addr1> <!-- optional -->
                                        <Addr2 >STRTYPE</Addr2> <!-- optional -->
                                        <Addr3 >STRTYPE</Addr3> <!-- optional -->
                                        <Addr4 >STRTYPE</Addr4> <!-- optional -->
                                        <Addr5 >STRTYPE</Addr5> <!-- optional -->
                                        <City >STRTYPE</City> <!-- optional -->
                                        <State >STRTYPE</State> <!-- optional -->
                                        <PostalCode >STRTYPE</PostalCode> <!-- optional -->
                                        <Country >STRTYPE</Country> <!-- optional -->
                                        <Note >STRTYPE</Note> <!-- optional -->
                                        <DefaultShipTo >BOOLTYPE</DefaultShipTo> <!-- optional -->
                                </ShipToAddress>
                                <Phone >STRTYPE</Phone> <!-- optional -->
                                <AltPhone >STRTYPE</AltPhone> <!-- optional -->
                                <Fax >STRTYPE</Fax> <!-- optional -->
                                <Email >STRTYPE</Email> <!-- optional -->
                                <Cc >STRTYPE</Cc> <!-- optional -->
                                <Contact >STRTYPE</Contact> <!-- optional -->
                                <AltContact >STRTYPE</AltContact> <!-- optional -->
                                <AdditionalContactRef> <!-- must occur 0 - 8 times -->
                                        <ContactName >STRTYPE</ContactName> <!-- required -->
                                        <ContactValue >STRTYPE</ContactValue> <!-- required -->
                                </AdditionalContactRef>
                                <ContactsRet> <!-- optional, may repeat -->
                                        <ListID >IDTYPE</ListID> <!-- required -->
                                        <TimeCreated >DATETIMETYPE</TimeCreated> <!-- required -->
                                        <TimeModified >DATETIMETYPE</TimeModified> <!-- required -->
                                        <EditSequence >STRTYPE</EditSequence> <!-- required -->
                                        <Contact >STRTYPE</Contact> <!-- optional -->
                                        <Salutation >STRTYPE</Salutation> <!-- optional -->
                                        <FirstName >STRTYPE</FirstName> <!-- required -->
                                        <MiddleName >STRTYPE</MiddleName> <!-- optional -->
                                        <LastName >STRTYPE</LastName> <!-- optional -->
                                        <JobTitle >STRTYPE</JobTitle> <!-- optional -->
                                        <AdditionalContactRef> <!-- must occur 0 - 5 times -->
                                                <ContactName >STRTYPE</ContactName> <!-- required -->
                                                <ContactValue >STRTYPE</ContactValue> <!-- required -->
                                        </AdditionalContactRef>
                                </ContactsRet>
                                <CustomerTypeRef> <!-- optional -->
                                        <ListID >IDTYPE</ListID> <!-- optional -->
                                        <FullName >STRTYPE</FullName> <!-- optional -->
                                </CustomerTypeRef>
                                <TermsRef> <!-- optional -->
                                        <ListID >IDTYPE</ListID> <!-- optional -->
                                        <FullName >STRTYPE</FullName> <!-- optional -->
                                </TermsRef>
                                <SalesRepRef> <!-- optional -->
                                        <ListID >IDTYPE</ListID> <!-- optional -->
                                        <FullName >STRTYPE</FullName> <!-- optional -->
                                </SalesRepRef>
                                <Balance >AMTTYPE</Balance> <!-- optional -->
                                <TotalBalance >AMTTYPE</TotalBalance> <!-- optional -->
                                <SalesTaxCodeRef> <!-- optional -->
                                        <ListID >IDTYPE</ListID> <!-- optional -->
                                        <FullName >STRTYPE</FullName> <!-- optional -->
                                </SalesTaxCodeRef>
                                <ItemSalesTaxRef> <!-- optional -->
                                        <ListID >IDTYPE</ListID> <!-- optional -->
                                        <FullName >STRTYPE</FullName> <!-- optional -->
                                </ItemSalesTaxRef>
                                <!-- SalesTaxCountry may have one of the following values: Australia, Canada [DEFAULT], UK, US -->
                                <SalesTaxCountry >ENUMTYPE</SalesTaxCountry> <!-- optional -->
                                <ResaleNumber >STRTYPE</ResaleNumber> <!-- optional -->
                                <AccountNumber >STRTYPE</AccountNumber> <!-- optional -->
                                <CreditLimit >AMTTYPE</CreditLimit> <!-- optional -->
                                <PreferredPaymentMethodRef> <!-- optional -->
                                        <ListID >IDTYPE</ListID> <!-- optional -->
                                        <FullName >STRTYPE</FullName> <!-- optional -->
                                </PreferredPaymentMethodRef>
                                <CreditCardInfo> <!-- optional -->
                                        <CreditCardNumber >STRTYPE</CreditCardNumber> <!-- optional -->
                                        <ExpirationMonth >INTTYPE</ExpirationMonth> <!-- optional -->
                                        <ExpirationYear >INTTYPE</ExpirationYear> <!-- optional -->
                                        <NameOnCard >STRTYPE</NameOnCard> <!-- optional -->
                                        <CreditCardAddress >STRTYPE</CreditCardAddress> <!-- optional -->
                                        <CreditCardPostalCode >STRTYPE</CreditCardPostalCode> <!-- optional -->
                                </CreditCardInfo>
                                <!-- JobStatus may have one of the following values: Awarded, Closed, InProgress, None [DEFAULT], NotAwarded, Pending -->
                                <JobStatus >ENUMTYPE</JobStatus> <!-- optional -->
                                <JobStartDate >DATETYPE</JobStartDate> <!-- optional -->
                                <JobProjectedEndDate >DATETYPE</JobProjectedEndDate> <!-- optional -->
                                <JobEndDate >DATETYPE</JobEndDate> <!-- optional -->
                                <JobDesc >STRTYPE</JobDesc> <!-- optional -->
                                <JobTypeRef> <!-- optional -->
                                        <ListID >IDTYPE</ListID> <!-- optional -->
                                        <FullName >STRTYPE</FullName> <!-- optional -->
                                </JobTypeRef>
                                <Notes >STRTYPE</Notes> <!-- optional -->
                                <AdditionalNotesRet> <!-- optional, may repeat -->
                                        <NoteID >INTTYPE</NoteID> <!-- required -->
                                        <Date >DATETYPE</Date> <!-- required -->
                                        <Note >STRTYPE</Note> <!-- required -->
                                </AdditionalNotesRet>
                                <!-- PreferredDeliveryMethod may have one of the following values: None [Default], Email, Fax -->
                                <PreferredDeliveryMethod >ENUMTYPE</PreferredDeliveryMethod> <!-- optional -->
                                <PriceLevelRef> <!-- optional -->
                                        <ListID >IDTYPE</ListID> <!-- optional -->
                                        <FullName >STRTYPE</FullName> <!-- optional -->
                                </PriceLevelRef>
                                <ExternalGUID >GUIDTYPE</ExternalGUID> <!-- optional -->
                                <TaxRegistrationNumber >STRTYPE</TaxRegistrationNumber> <!-- optional -->
                                <CurrencyRef> <!-- optional -->
                                        <ListID >IDTYPE</ListID> <!-- optional -->
                                        <FullName >STRTYPE</FullName> <!-- optional -->
                                </CurrencyRef>
                                <DataExtRet> <!-- optional, may repeat -->
                                        <OwnerID >GUIDTYPE</OwnerID> <!-- optional -->
                                        <DataExtName >STRTYPE</DataExtName> <!-- required -->
                                        <!-- DataExtType may have one of the following values: AMTTYPE, DATETIMETYPE, INTTYPE, PERCENTTYPE, PRICETYPE, QUANTYPE, STR1024TYPE, STR255TYPE -->
                                        <DataExtType >ENUMTYPE</DataExtType> <!-- required -->
                                        <DataExtValue >STRTYPE</DataExtValue> <!-- required -->
                                </DataExtRet>
                        </CustomerRet>
                </CustomerQueryRs>
        </QBXMLMsgsRq>
</QBXML>
```
## CustomerTypeQuery
### XMLOps
```
<?xml version="1.0" encoding="utf-8"?>
<?qbxml version="16.0"?>
<QBXML>
        <QBXMLMsgsRq onError="stopOnError">
                <CustomerTypeQueryRq metaData="ENUMTYPE">
                        <!-- BEGIN OR -->
                                <ListID >IDTYPE</ListID> <!-- optional, may repeat -->
                        <!-- OR -->
                                <FullName >STRTYPE</FullName> <!-- optional, may repeat -->
                        <!-- OR -->
                                <MaxReturned >INTTYPE</MaxReturned> <!-- optional -->
                                <!-- ActiveStatus may have one of the following values: ActiveOnly [DEFAULT], InactiveOnly, All -->
                                <ActiveStatus >ENUMTYPE</ActiveStatus> <!-- optional -->
                                <FromModifiedDate >DATETIMETYPE</FromModifiedDate> <!-- optional -->
                                <ToModifiedDate >DATETIMETYPE</ToModifiedDate> <!-- optional -->
                                <!-- BEGIN OR -->
                                        <NameFilter> <!-- optional -->
                                                <!-- MatchCriterion may have one of the following values: StartsWith, Contains, EndsWith -->
                                                <MatchCriterion >ENUMTYPE</MatchCriterion> <!-- required -->
                                                <Name >STRTYPE</Name> <!-- required -->
                                        </NameFilter>
                                <!-- OR -->
                                        <NameRangeFilter> <!-- optional -->
                                                <FromName >STRTYPE</FromName> <!-- optional -->
                                                <ToName >STRTYPE</ToName> <!-- optional -->
                                        </NameRangeFilter>
                                <!-- END OR -->
                        <!-- END OR -->
                        <IncludeRetElement >STRTYPE</IncludeRetElement> <!-- optional, may repeat -->
                </CustomerTypeQueryRq>

                <CustomerTypeQueryRs statusCode="INTTYPE" statusSeverity="STRTYPE" statusMessage="STRTYPE" retCount="INTTYPE">
                        <CustomerTypeRet> <!-- optional, may repeat -->
                                <ListID >IDTYPE</ListID> <!-- required -->
                                <TimeCreated >DATETIMETYPE</TimeCreated> <!-- required -->
                                <TimeModified >DATETIMETYPE</TimeModified> <!-- required -->
                                <EditSequence >STRTYPE</EditSequence> <!-- required -->
                                <Name >STRTYPE</Name> <!-- required -->
                                <FullName >STRTYPE</FullName> <!-- required -->
                                <IsActive >BOOLTYPE</IsActive> <!-- optional -->
                                <ParentRef> <!-- optional -->
                                        <ListID >IDTYPE</ListID> <!-- optional -->
                                        <FullName >STRTYPE</FullName> <!-- optional -->
                                </ParentRef>
                                <Sublevel >INTTYPE</Sublevel> <!-- required -->
                        </CustomerTypeRet>
                </CustomerTypeQueryRs>
        </QBXMLMsgsRq>
</QBXML>
```

## DepositQuery
### XMLOps
```
<?xml version="1.0" encoding="utf-8"?>
<?qbxml version="16.0"?>
<QBXML>
        <QBXMLMsgsRq onError="stopOnError">
                <DepositQueryRq metaData="ENUMTYPE" iterator="ENUMTYPE" iteratorID="UUIDTYPE">
                        <!-- BEGIN OR -->
                                <TxnID >IDTYPE</TxnID> <!-- optional, may repeat -->
                        <!-- OR -->
                                <MaxReturned >INTTYPE</MaxReturned> <!-- optional -->
                                <!-- BEGIN OR -->
                                        <ModifiedDateRangeFilter> <!-- optional -->
                                                <FromModifiedDate >DATETIMETYPE</FromModifiedDate> <!-- optional -->
                                                <ToModifiedDate >DATETIMETYPE</ToModifiedDate> <!-- optional -->
                                        </ModifiedDateRangeFilter>
                                <!-- OR -->
                                        <TxnDateRangeFilter> <!-- optional -->
                                                <!-- BEGIN OR -->
                                                        <FromTxnDate >DATETYPE</FromTxnDate> <!-- optional -->
                                                        <ToTxnDate >DATETYPE</ToTxnDate> <!-- optional -->
                                                <!-- OR -->
                                                        <!-- DateMacro may have one of the following values: All, Today, ThisWeek, ThisWeekToDate, ThisMonth, ThisMonthToDate, ThisCalendarQuarter, ThisCalendarQuarterToDate, ThisFiscalQuarter, ThisFiscalQuarterToDate, ThisCalendarYear, ThisCalendarYearToDate, ThisFiscalYear, ThisFiscalYearToDate, Yesterday, LastWeek, LastWeekToDate, LastMonth, LastMonthToDate, LastCalendarQuarter, LastCalendarQuarterToDate, LastFiscalQuarter, LastFiscalQuarterToDate, LastCalendarYear, LastCalendarYearToDate, LastFiscalYear, LastFiscalYearToDate, NextWeek, NextFourWeeks, NextMonth, NextCalendarQuarter, NextCalendarYear, NextFiscalQuarter, NextFiscalYear -->
                                                        <DateMacro >ENUMTYPE</DateMacro> <!-- optional -->
                                                <!-- END OR -->
                                        </TxnDateRangeFilter>
                                <!-- END OR -->
                                <EntityFilter> <!-- optional -->
                                        <!-- BEGIN OR -->
                                                <ListID >IDTYPE</ListID> <!-- optional, may repeat -->
                                        <!-- OR -->
                                                <FullName >STRTYPE</FullName> <!-- optional, may repeat -->
                                        <!-- OR -->
                                                <ListIDWithChildren >IDTYPE</ListIDWithChildren> <!-- optional -->
                                        <!-- OR -->
                                                <FullNameWithChildren >STRTYPE</FullNameWithChildren> <!-- optional -->
                                        <!-- END OR -->
                                </EntityFilter>
                                <AccountFilter> <!-- optional -->
                                        <!-- BEGIN OR -->
                                                <ListID >IDTYPE</ListID> <!-- optional, may repeat -->
                                        <!-- OR -->
                                                <FullName >STRTYPE</FullName> <!-- optional, may repeat -->
                                        <!-- OR -->
                                                <ListIDWithChildren >IDTYPE</ListIDWithChildren> <!-- optional -->
                                        <!-- OR -->
                                                <FullNameWithChildren >STRTYPE</FullNameWithChildren> <!-- optional -->
                                        <!-- END OR -->
                                </AccountFilter>
                                <CurrencyFilter> <!-- optional -->
                                        <!-- BEGIN OR -->
                                                <ListID >IDTYPE</ListID> <!-- optional, may repeat -->
                                        <!-- OR -->
                                                <FullName >STRTYPE</FullName> <!-- optional, may repeat -->
                                        <!-- END OR -->
                                </CurrencyFilter>
                        <!-- END OR -->
                        <IncludeLineItems >BOOLTYPE</IncludeLineItems> <!-- optional -->
                        <IncludeRetElement >STRTYPE</IncludeRetElement> <!-- optional, may repeat -->
                        <OwnerID >GUIDTYPE</OwnerID> <!-- optional, may repeat -->
                </DepositQueryRq>

                <DepositQueryRs statusCode="INTTYPE" statusSeverity="STRTYPE" statusMessage="STRTYPE" retCount="INTTYPE" iteratorRemainingCount="INTTYPE" iteratorID="UUIDTYPE">
                        <DepositRet> <!-- optional, may repeat -->
                                <TxnID >IDTYPE</TxnID> <!-- required -->
                                <TimeCreated >DATETIMETYPE</TimeCreated> <!-- required -->
                                <TimeModified >DATETIMETYPE</TimeModified> <!-- required -->
                                <EditSequence >STRTYPE</EditSequence> <!-- required -->
                                <TxnNumber >INTTYPE</TxnNumber> <!-- optional -->
                                <TxnDate >DATETYPE</TxnDate> <!-- required -->
                                <DepositToAccountRef> <!-- required -->
                                        <ListID >IDTYPE</ListID> <!-- optional -->
                                        <FullName >STRTYPE</FullName> <!-- optional -->
                                </DepositToAccountRef>
                                <Memo >STRTYPE</Memo> <!-- optional -->
                                <DepositTotal >AMTTYPE</DepositTotal> <!-- optional -->
                                <CurrencyRef> <!-- optional -->
                                        <ListID >IDTYPE</ListID> <!-- optional -->
                                        <FullName >STRTYPE</FullName> <!-- optional -->
                                </CurrencyRef>
                                <ExchangeRate >FLOATTYPE</ExchangeRate> <!-- optional -->
                                <DepositTotalInHomeCurrency >AMTTYPE</DepositTotalInHomeCurrency> <!-- optional -->
                                <CashBackInfoRet> <!-- optional -->
                                        <TxnLineID >IDTYPE</TxnLineID> <!-- required -->
                                        <AccountRef> <!-- required -->
                                                <ListID >IDTYPE</ListID> <!-- optional -->
                                                <FullName >STRTYPE</FullName> <!-- optional -->
                                        </AccountRef>
                                        <Memo >STRTYPE</Memo> <!-- optional -->
                                        <Amount >AMTTYPE</Amount> <!-- optional -->
                                </CashBackInfoRet>
                                <ExternalGUID >GUIDTYPE</ExternalGUID> <!-- optional -->
                                <DepositLineRet> <!-- optional, may repeat -->
                                        <!-- TxnType may have one of the following values: ARRefundCreditCard, Bill, BillPaymentCheck, BillPaymentCreditCard, BuildAssembly, Charge, Check, CreditCardCharge, CreditCardCredit, CreditMemo, Deposit, Estimate, InventoryAdjustment, Invoice, ItemReceipt, JournalEntry, LiabilityAdjustment, Paycheck, PayrollLiabilityCheck, PurchaseOrder, ReceivePayment, SalesOrder, SalesReceipt, SalesTaxPaymentCheck, Transfer, VendorCredit, YTDAdjustment -->
                                        <TxnType >ENUMTYPE</TxnType> <!-- optional -->
                                        <TxnID >IDTYPE</TxnID> <!-- optional -->
                                        <TxnLineID >IDTYPE</TxnLineID> <!-- required -->
                                        <PaymentTxnLineID >IDTYPE</PaymentTxnLineID> <!-- optional -->
                                        <EntityRef> <!-- optional -->
                                                <ListID >IDTYPE</ListID> <!-- optional -->
                                                <FullName >STRTYPE</FullName> <!-- optional -->
                                        </EntityRef>
                                        <AccountRef> <!-- optional -->
                                                <ListID >IDTYPE</ListID> <!-- optional -->
                                                <FullName >STRTYPE</FullName> <!-- optional -->
                                        </AccountRef>
                                        <Memo >STRTYPE</Memo> <!-- optional -->
                                        <CheckNumber >STRTYPE</CheckNumber> <!-- optional -->
                                        <PaymentMethodRef> <!-- optional -->
                                                <ListID >IDTYPE</ListID> <!-- optional -->
                                                <FullName >STRTYPE</FullName> <!-- optional -->
                                        </PaymentMethodRef>
                                        <ClassRef> <!-- optional -->
                                                <ListID >IDTYPE</ListID> <!-- optional -->
                                                <FullName >STRTYPE</FullName> <!-- optional -->
                                        </ClassRef>
                                        <Amount >AMTTYPE</Amount> <!-- optional -->
                                </DepositLineRet>
                                <DataExtRet> <!-- optional, may repeat -->
                                        <OwnerID >GUIDTYPE</OwnerID> <!-- optional -->
                                        <DataExtName >STRTYPE</DataExtName> <!-- required -->
                                        <!-- DataExtType may have one of the following values: AMTTYPE, DATETIMETYPE, INTTYPE, PERCENTTYPE, PRICETYPE, QUANTYPE, STR1024TYPE, STR255TYPE -->
                                        <DataExtType >ENUMTYPE</DataExtType> <!-- required -->
                                        <DataExtValue >STRTYPE</DataExtValue> <!-- required -->
                                </DataExtRet>
                        </DepositRet>
                </DepositQueryRs>
        </QBXMLMsgsRq>
</QBXML>
```

## EmployeeQuery
### XMLOps
```
<?xml version="1.0" encoding="utf-8"?>
<?qbxml version="16.0"?>
<QBXML>
        <QBXMLMsgsRq onError="stopOnError">
                <EmployeeQueryRq metaData="ENUMTYPE">
                        <!-- BEGIN OR -->
                                <ListID >IDTYPE</ListID> <!-- optional, may repeat -->
                        <!-- OR -->
                                <FullName >STRTYPE</FullName> <!-- optional, may repeat -->
                        <!-- OR -->
                                <MaxReturned >INTTYPE</MaxReturned> <!-- optional -->
                                <!-- ActiveStatus may have one of the following values: ActiveOnly [DEFAULT], InactiveOnly, All -->
                                <ActiveStatus >ENUMTYPE</ActiveStatus> <!-- optional -->
                                <FromModifiedDate >DATETIMETYPE</FromModifiedDate> <!-- optional -->
                                <ToModifiedDate >DATETIMETYPE</ToModifiedDate> <!-- optional -->
                                <!-- BEGIN OR -->
                                        <NameFilter> <!-- optional -->
                                                <!-- MatchCriterion may have one of the following values: StartsWith, Contains, EndsWith -->
                                                <MatchCriterion >ENUMTYPE</MatchCriterion> <!-- required -->
                                                <Name >STRTYPE</Name> <!-- required -->
                                        </NameFilter>
                                <!-- OR -->
                                        <NameRangeFilter> <!-- optional -->
                                                <FromName >STRTYPE</FromName> <!-- optional -->
                                                <ToName >STRTYPE</ToName> <!-- optional -->
                                        </NameRangeFilter>
                                <!-- END OR -->
                        <!-- END OR -->
                        <IncludeRetElement >STRTYPE</IncludeRetElement> <!-- optional, may repeat -->
                        <OwnerID >GUIDTYPE</OwnerID> <!-- optional, may repeat -->
                </EmployeeQueryRq>

                <EmployeeQueryRs statusCode="INTTYPE" statusSeverity="STRTYPE" statusMessage="STRTYPE" retCount="INTTYPE">
                        <EmployeeRet> <!-- optional, may repeat -->
                                <ListID >IDTYPE</ListID> <!-- required -->
                                <TimeCreated >DATETIMETYPE</TimeCreated> <!-- required -->
                                <TimeModified >DATETIMETYPE</TimeModified> <!-- required -->
                                <EditSequence >STRTYPE</EditSequence> <!-- required -->
                                <Name >STRTYPE</Name> <!-- required -->
                                <IsActive >BOOLTYPE</IsActive> <!-- optional -->
                                <Salutation >STRTYPE</Salutation> <!-- optional -->
                                <FirstName >STRTYPE</FirstName> <!-- optional -->
                                <MiddleName >STRTYPE</MiddleName> <!-- optional -->
                                <LastName >STRTYPE</LastName> <!-- optional -->
                                <JobTitle >STRTYPE</JobTitle> <!-- optional -->
                                <SupervisorRef> <!-- optional -->
                                        <ListID >IDTYPE</ListID> <!-- optional -->
                                        <FullName >STRTYPE</FullName> <!-- optional -->
                                </SupervisorRef>
                                <Department >STRTYPE</Department> <!-- optional -->
                                <Description >STRTYPE</Description> <!-- optional -->
                                <TargetBonus >AMTTYPE</TargetBonus> <!-- optional -->
                                <EmployeeAddress> <!-- optional -->
                                        <Addr1 >STRTYPE</Addr1> <!-- optional -->
                                        <Addr2 >STRTYPE</Addr2> <!-- optional -->
                                        <City >STRTYPE</City> <!-- optional -->
                                        <State >STRTYPE</State> <!-- optional -->
                                        <PostalCode >STRTYPE</PostalCode> <!-- optional -->
                                </EmployeeAddress>
                                <PrintAs >STRTYPE</PrintAs> <!-- optional -->
                                <Phone >STRTYPE</Phone> <!-- optional -->
                                <Mobile >STRTYPE</Mobile> <!-- optional -->
                                <Pager >STRTYPE</Pager> <!-- optional -->
                                <PagerPIN >STRTYPE</PagerPIN> <!-- optional -->
                                <AltPhone >STRTYPE</AltPhone> <!-- optional -->
                                <Fax >STRTYPE</Fax> <!-- optional -->
                                <SSN >STRTYPE</SSN> <!-- optional -->
                                <Email >STRTYPE</Email> <!-- optional -->
                                <AdditionalContactRef> <!-- must occur 0 - 8 times -->
                                        <ContactName >STRTYPE</ContactName> <!-- required -->
                                        <ContactValue >STRTYPE</ContactValue> <!-- required -->
                                </AdditionalContactRef>
                                <EmergencyContacts> <!-- optional -->
                                        <PrimaryContact> <!-- optional -->
                                                <ContactName >STRTYPE</ContactName> <!-- required -->
                                                <ContactValue >STRTYPE</ContactValue> <!-- required -->
                                                <!-- Relation may have one of the following values: Spouse, Partner, Mother, Father, Sister, Brother, Son, Daughter, Friend, Other -->
                                                <Relation >ENUMTYPE</Relation> <!-- optional -->
                                        </PrimaryContact>
                                        <SecondaryContact> <!-- optional -->
                                                <ContactName >STRTYPE</ContactName> <!-- required -->
                                                <ContactValue >STRTYPE</ContactValue> <!-- required -->
                                                <!-- Relation may have one of the following values: Spouse, Partner, Mother, Father, Sister, Brother, Son, Daughter, Friend, Other -->
                                                <Relation >ENUMTYPE</Relation> <!-- optional -->
                                        </SecondaryContact>
                                </EmergencyContacts>
                                <!-- EmployeeType may have one of the following values: Officer, Owner, Regular [DEFAULT], Statutory -->
                                <EmployeeType >ENUMTYPE</EmployeeType> <!-- optional -->
                                <!-- PartOrFullTime may have one of the following values: PartTime, FullTime -->
                                <PartOrFullTime >ENUMTYPE</PartOrFullTime> <!-- optional -->
                                <!-- Exempt may have one of the following values: Exempt, NonExempt -->
                                <Exempt >ENUMTYPE</Exempt> <!-- optional -->
                                <!-- KeyEmployee may have one of the following values: Yes, No -->
                                <KeyEmployee >ENUMTYPE</KeyEmployee> <!-- optional -->
                                <!-- Gender may have one of the following values: Male, Female -->
                                <Gender >ENUMTYPE</Gender> <!-- optional -->
                                <HiredDate >DATETYPE</HiredDate> <!-- optional -->
                                <OriginalHireDate >DATETYPE</OriginalHireDate> <!-- optional -->
                                <AdjustedServiceDate >DATETYPE</AdjustedServiceDate> <!-- optional -->
                                <ReleasedDate >DATETYPE</ReleasedDate> <!-- optional -->
                                <BirthDate >DATETYPE</BirthDate> <!-- optional -->
                                <!-- USCitizen may have one of the following values: Yes, No -->
                                <USCitizen >ENUMTYPE</USCitizen> <!-- optional -->
                                <!-- Ethnicity may have one of the following values: AmericianIndian, Asian, Black, Hawaiian, Hispanic, White, TwoOrMoreRaces -->
                                <Ethnicity >ENUMTYPE</Ethnicity> <!-- optional -->
                                <!-- Disabled may have one of the following values: Yes, No -->
                                <Disabled >ENUMTYPE</Disabled> <!-- optional -->
                                <DisabilityDesc >STRTYPE</DisabilityDesc> <!-- optional -->
                                <!-- OnFile may have one of the following values: Yes, No -->
                                <OnFile >ENUMTYPE</OnFile> <!-- optional -->
                                <WorkAuthExpireDate >DATETYPE</WorkAuthExpireDate> <!-- optional -->
                                <!-- USVeteran may have one of the following values: Yes, No -->
                                <USVeteran >ENUMTYPE</USVeteran> <!-- optional -->
                                <!-- MilitaryStatus may have one of the following values: Active, Reserve -->
                                <MilitaryStatus >ENUMTYPE</MilitaryStatus> <!-- optional -->
                                <AccountNumber >STRTYPE</AccountNumber> <!-- optional -->
                                <Notes >STRTYPE</Notes> <!-- optional -->
                                <AdditionalNotesRet> <!-- optional, may repeat -->
                                        <NoteID >INTTYPE</NoteID> <!-- required -->
                                        <Date >DATETYPE</Date> <!-- required -->
                                        <Note >STRTYPE</Note> <!-- required -->
                                </AdditionalNotesRet>
                                <BillingRateRef> <!-- optional -->
                                        <ListID >IDTYPE</ListID> <!-- optional -->
                                        <FullName >STRTYPE</FullName> <!-- optional -->
                                </BillingRateRef>
                                <EmployeePayrollInfo> <!-- optional -->
                                        <!-- PayPeriod may have one of the following values: Daily, Weekly, Biweekly, Semimonthly, Monthly, Quarterly, Yearly -->
                                        <PayPeriod >ENUMTYPE</PayPeriod> <!-- optional -->
                                        <ClassRef> <!-- optional -->
                                                <ListID >IDTYPE</ListID> <!-- optional -->
                                                <FullName >STRTYPE</FullName> <!-- optional -->
                                        </ClassRef>
                                        <!-- BEGIN OR -->
                                                <ClearEarnings >BOOLTYPE</ClearEarnings> <!-- optional -->
                                        <!-- OR -->
                                                <Earnings> <!-- optional, may repeat -->
                                                        <PayrollItemWageRef> <!-- required -->
                                                                <ListID >IDTYPE</ListID> <!-- optional -->
                                                                <FullName >STRTYPE</FullName> <!-- optional -->
                                                        </PayrollItemWageRef>
                                                        <!-- BEGIN OR -->
                                                                <Rate >PRICETYPE</Rate> <!-- optional -->
                                                        <!-- OR -->
                                                                <RatePercent >PERCENTTYPE</RatePercent> <!-- optional -->
                                                        <!-- END OR -->
                                                </Earnings>
                                        <!-- END OR -->
                                        <IsUsingTimeDataToCreatePaychecks >BOOLTYPE</IsUsingTimeDataToCreatePaychecks> <!-- optional -->
                                        <!-- UseTimeDataToCreatePaychecks may have one of the following values: NotSet, UseTimeData, DoNotUseTimeData -->
                                        <UseTimeDataToCreatePaychecks >ENUMTYPE</UseTimeDataToCreatePaychecks> <!-- optional -->
                                        <SickHours> <!-- optional -->
                                                <HoursAvailable >TIMEINTERVALTYPE</HoursAvailable> <!-- optional -->
                                                <!-- AccrualPeriod may have one of the following values: BeginningOfYear, EveryHourOnPaycheck, EveryPaycheck -->
                                                <AccrualPeriod >ENUMTYPE</AccrualPeriod> <!-- optional -->
                                                <HoursAccrued >TIMEINTERVALTYPE</HoursAccrued> <!-- optional -->
                                                <MaximumHours >TIMEINTERVALTYPE</MaximumHours> <!-- optional -->
                                                <IsResettingHoursEachNewYear >BOOLTYPE</IsResettingHoursEachNewYear> <!-- optional -->
                                                <HoursUsed >TIMEINTERVALTYPE</HoursUsed> <!-- optional -->
                                                <AccrualStartDate >DATETYPE</AccrualStartDate> <!-- optional -->
                                        </SickHours>
                                        <VacationHours> <!-- optional -->
                                                <HoursAvailable >TIMEINTERVALTYPE</HoursAvailable> <!-- optional -->
                                                <!-- AccrualPeriod may have one of the following values: BeginningOfYear, EveryHourOnPaycheck, EveryPaycheck -->
                                                <AccrualPeriod >ENUMTYPE</AccrualPeriod> <!-- optional -->
                                                <HoursAccrued >TIMEINTERVALTYPE</HoursAccrued> <!-- optional -->
                                                <MaximumHours >TIMEINTERVALTYPE</MaximumHours> <!-- optional -->
                                                <IsResettingHoursEachNewYear >BOOLTYPE</IsResettingHoursEachNewYear> <!-- optional -->
                                                <HoursUsed >TIMEINTERVALTYPE</HoursUsed> <!-- optional -->
                                                <AccrualStartDate >DATETYPE</AccrualStartDate> <!-- optional -->
                                        </VacationHours>
                                </EmployeePayrollInfo>
                                <ExternalGUID >GUIDTYPE</ExternalGUID> <!-- optional -->
                                <DataExtRet> <!-- optional, may repeat -->
                                        <OwnerID >GUIDTYPE</OwnerID> <!-- optional -->
                                        <DataExtName >STRTYPE</DataExtName> <!-- required -->
                                        <!-- DataExtType may have one of the following values: AMTTYPE, DATETIMETYPE, INTTYPE, PERCENTTYPE, PRICETYPE, QUANTYPE, STR1024TYPE, STR255TYPE -->
                                        <DataExtType >ENUMTYPE</DataExtType> <!-- required -->
                                        <DataExtValue >STRTYPE</DataExtValue> <!-- required -->
                                </DataExtRet>
                        </EmployeeRet>
                </EmployeeQueryRs>
        </QBXMLMsgsRq>
</QBXML>
```
## EntityQuery
### XMLOps
```
<?xml version="1.0" encoding="utf-8"?>
<?qbxml version="16.0"?>
<QBXML>
        <QBXMLMsgsRq onError="stopOnError">
                <EntityQueryRq metaData="ENUMTYPE" iterator="ENUMTYPE" iteratorID="UUIDTYPE">
                        <!-- BEGIN OR -->
                                <ListID >IDTYPE</ListID> <!-- optional, may repeat -->
                        <!-- OR -->
                                <FullName >STRTYPE</FullName> <!-- optional, may repeat -->
                        <!-- OR -->
                                <MaxReturned >INTTYPE</MaxReturned> <!-- optional -->
                                <!-- ActiveStatus may have one of the following values: ActiveOnly [DEFAULT], InactiveOnly, All -->
                                <ActiveStatus >ENUMTYPE</ActiveStatus> <!-- optional -->
                                <FromModifiedDate >DATETIMETYPE</FromModifiedDate> <!-- optional -->
                                <ToModifiedDate >DATETIMETYPE</ToModifiedDate> <!-- optional -->
                                <!-- BEGIN OR -->
                                        <NameFilter> <!-- optional -->
                                                <!-- MatchCriterion may have one of the following values: StartsWith, Contains, EndsWith -->
                                                <MatchCriterion >ENUMTYPE</MatchCriterion> <!-- required -->
                                                <Name >STRTYPE</Name> <!-- required -->
                                        </NameFilter>
                                <!-- OR -->
                                        <NameRangeFilter> <!-- optional -->
                                                <FromName >STRTYPE</FromName> <!-- optional -->
                                                <ToName >STRTYPE</ToName> <!-- optional -->
                                        </NameRangeFilter>
                                <!-- END OR -->
                        <!-- END OR -->
                        <IncludeRetElement >STRTYPE</IncludeRetElement> <!-- optional, may repeat -->
                </EntityQueryRq>

                <EntityQueryRs statusCode="INTTYPE" statusSeverity="STRTYPE" statusMessage="STRTYPE" retCount="INTTYPE" iteratorRemainingCount="INTTYPE" iteratorID="UUIDTYPE">
                        <!-- BEGIN OR -->
                                <CustomerRet> <!-- optional -->
                                        <ListID >IDTYPE</ListID> <!-- required -->
                                        <TimeCreated >DATETIMETYPE</TimeCreated> <!-- required -->
                                        <TimeModified >DATETIMETYPE</TimeModified> <!-- required -->
                                        <EditSequence >STRTYPE</EditSequence> <!-- required -->
                                        <Name >STRTYPE</Name> <!-- required -->
                                        <FullName >STRTYPE</FullName> <!-- required -->
                                        <IsActive >BOOLTYPE</IsActive> <!-- optional -->
                                        <ClassRef> <!-- optional -->
                                                <ListID >IDTYPE</ListID> <!-- optional -->
                                                <FullName >STRTYPE</FullName> <!-- optional -->
                                        </ClassRef>
                                        <ParentRef> <!-- optional -->
                                                <ListID >IDTYPE</ListID> <!-- optional -->
                                                <FullName >STRTYPE</FullName> <!-- optional -->
                                        </ParentRef>
                                        <Sublevel >INTTYPE</Sublevel> <!-- required -->
                                        <CompanyName >STRTYPE</CompanyName> <!-- optional -->
                                        <Salutation >STRTYPE</Salutation> <!-- optional -->
                                        <FirstName >STRTYPE</FirstName> <!-- optional -->
                                        <MiddleName >STRTYPE</MiddleName> <!-- optional -->
                                        <LastName >STRTYPE</LastName> <!-- optional -->
                                        <JobTitle >STRTYPE</JobTitle> <!-- optional -->
                                        <BillAddress> <!-- optional -->
                                                <Addr1 >STRTYPE</Addr1> <!-- optional -->
                                                <Addr2 >STRTYPE</Addr2> <!-- optional -->
                                                <Addr3 >STRTYPE</Addr3> <!-- optional -->
                                                <Addr4 >STRTYPE</Addr4> <!-- optional -->
                                                <Addr5 >STRTYPE</Addr5> <!-- optional -->
                                                <City >STRTYPE</City> <!-- optional -->
                                                <State >STRTYPE</State> <!-- optional -->
                                                <PostalCode >STRTYPE</PostalCode> <!-- optional -->
                                                <Country >STRTYPE</Country> <!-- optional -->
                                                <Note >STRTYPE</Note> <!-- optional -->
                                        </BillAddress>
                                        <BillAddressBlock> <!-- optional -->
                                                <Addr1 >STRTYPE</Addr1> <!-- optional -->
                                                <Addr2 >STRTYPE</Addr2> <!-- optional -->
                                                <Addr3 >STRTYPE</Addr3> <!-- optional -->
                                                <Addr4 >STRTYPE</Addr4> <!-- optional -->
                                                <Addr5 >STRTYPE</Addr5> <!-- optional -->
                                        </BillAddressBlock>
                                        <ShipAddress> <!-- optional -->
                                                <Addr1 >STRTYPE</Addr1> <!-- optional -->
                                                <Addr2 >STRTYPE</Addr2> <!-- optional -->
                                                <Addr3 >STRTYPE</Addr3> <!-- optional -->
                                                <Addr4 >STRTYPE</Addr4> <!-- optional -->
                                                <Addr5 >STRTYPE</Addr5> <!-- optional -->
                                                <City >STRTYPE</City> <!-- optional -->
                                                <State >STRTYPE</State> <!-- optional -->
                                                <PostalCode >STRTYPE</PostalCode> <!-- optional -->
                                                <Country >STRTYPE</Country> <!-- optional -->
                                                <Note >STRTYPE</Note> <!-- optional -->
                                        </ShipAddress>
                                        <ShipAddressBlock> <!-- optional -->
                                                <Addr1 >STRTYPE</Addr1> <!-- optional -->
                                                <Addr2 >STRTYPE</Addr2> <!-- optional -->
                                                <Addr3 >STRTYPE</Addr3> <!-- optional -->
                                                <Addr4 >STRTYPE</Addr4> <!-- optional -->
                                                <Addr5 >STRTYPE</Addr5> <!-- optional -->
                                        </ShipAddressBlock>
                                        <ShipToAddress> <!-- must occur 0 - 50 times -->
                                                <Name >STRTYPE</Name> <!-- required -->
                                                <Addr1 >STRTYPE</Addr1> <!-- optional -->
                                                <Addr2 >STRTYPE</Addr2> <!-- optional -->
                                                <Addr3 >STRTYPE</Addr3> <!-- optional -->
                                                <Addr4 >STRTYPE</Addr4> <!-- optional -->
                                                <Addr5 >STRTYPE</Addr5> <!-- optional -->
                                                <City >STRTYPE</City> <!-- optional -->
                                                <State >STRTYPE</State> <!-- optional -->
                                                <PostalCode >STRTYPE</PostalCode> <!-- optional -->
                                                <Country >STRTYPE</Country> <!-- optional -->
                                                <Note >STRTYPE</Note> <!-- optional -->
                                                <DefaultShipTo >BOOLTYPE</DefaultShipTo> <!-- optional -->
                                        </ShipToAddress>
                                        <Phone >STRTYPE</Phone> <!-- optional -->
                                        <AltPhone >STRTYPE</AltPhone> <!-- optional -->
                                        <Fax >STRTYPE</Fax> <!-- optional -->
                                        <Email >STRTYPE</Email> <!-- optional -->
                                        <Cc >STRTYPE</Cc> <!-- optional -->
                                        <Contact >STRTYPE</Contact> <!-- optional -->
                                        <AltContact >STRTYPE</AltContact> <!-- optional -->
                                        <AdditionalContactRef> <!-- must occur 0 - 8 times -->
                                                <ContactName >STRTYPE</ContactName> <!-- required -->
                                                <ContactValue >STRTYPE</ContactValue> <!-- required -->
                                        </AdditionalContactRef>
                                        <ContactsRet> <!-- optional, may repeat -->
                                                <ListID >IDTYPE</ListID> <!-- required -->
                                                <TimeCreated >DATETIMETYPE</TimeCreated> <!-- required -->
                                                <TimeModified >DATETIMETYPE</TimeModified> <!-- required -->
                                                <EditSequence >STRTYPE</EditSequence> <!-- required -->
                                                <Contact >STRTYPE</Contact> <!-- optional -->
                                                <Salutation >STRTYPE</Salutation> <!-- optional -->
                                                <FirstName >STRTYPE</FirstName> <!-- required -->
                                                <MiddleName >STRTYPE</MiddleName> <!-- optional -->
                                                <LastName >STRTYPE</LastName> <!-- optional -->
                                                <JobTitle >STRTYPE</JobTitle> <!-- optional -->
                                                <AdditionalContactRef> <!-- must occur 0 - 5 times -->
                                                        <ContactName >STRTYPE</ContactName> <!-- required -->
                                                        <ContactValue >STRTYPE</ContactValue> <!-- required -->
                                                </AdditionalContactRef>
                                        </ContactsRet>
                                        <CustomerTypeRef> <!-- optional -->
                                                <ListID >IDTYPE</ListID> <!-- optional -->
                                                <FullName >STRTYPE</FullName> <!-- optional -->
                                        </CustomerTypeRef>
                                        <TermsRef> <!-- optional -->
                                                <ListID >IDTYPE</ListID> <!-- optional -->
                                                <FullName >STRTYPE</FullName> <!-- optional -->
                                        </TermsRef>
                                        <SalesRepRef> <!-- optional -->
                                                <ListID >IDTYPE</ListID> <!-- optional -->
                                                <FullName >STRTYPE</FullName> <!-- optional -->
                                        </SalesRepRef>
                                        <Balance >AMTTYPE</Balance> <!-- optional -->
                                        <TotalBalance >AMTTYPE</TotalBalance> <!-- optional -->
                                        <SalesTaxCodeRef> <!-- optional -->
                                                <ListID >IDTYPE</ListID> <!-- optional -->
                                                <FullName >STRTYPE</FullName> <!-- optional -->
                                        </SalesTaxCodeRef>
                                        <ItemSalesTaxRef> <!-- optional -->
                                                <ListID >IDTYPE</ListID> <!-- optional -->
                                                <FullName >STRTYPE</FullName> <!-- optional -->
                                        </ItemSalesTaxRef>
                                        <!-- SalesTaxCountry may have one of the following values: Australia, Canada [DEFAULT], UK, US -->
                                        <SalesTaxCountry >ENUMTYPE</SalesTaxCountry> <!-- optional -->
                                        <ResaleNumber >STRTYPE</ResaleNumber> <!-- optional -->
                                        <AccountNumber >STRTYPE</AccountNumber> <!-- optional -->
                                        <CreditLimit >AMTTYPE</CreditLimit> <!-- optional -->
                                        <PreferredPaymentMethodRef> <!-- optional -->
                                                <ListID >IDTYPE</ListID> <!-- optional -->
                                                <FullName >STRTYPE</FullName> <!-- optional -->
                                        </PreferredPaymentMethodRef>
                                        <CreditCardInfo> <!-- optional -->
                                                <CreditCardNumber >STRTYPE</CreditCardNumber> <!-- optional -->
                                                <ExpirationMonth >INTTYPE</ExpirationMonth> <!-- optional -->
                                                <ExpirationYear >INTTYPE</ExpirationYear> <!-- optional -->
                                                <NameOnCard >STRTYPE</NameOnCard> <!-- optional -->
                                                <CreditCardAddress >STRTYPE</CreditCardAddress> <!-- optional -->
                                                <CreditCardPostalCode >STRTYPE</CreditCardPostalCode> <!-- optional -->
                                        </CreditCardInfo>
                                        <!-- JobStatus may have one of the following values: Awarded, Closed, InProgress, None [DEFAULT], NotAwarded, Pending -->
                                        <JobStatus >ENUMTYPE</JobStatus> <!-- optional -->
                                        <JobStartDate >DATETYPE</JobStartDate> <!-- optional -->
                                        <JobProjectedEndDate >DATETYPE</JobProjectedEndDate> <!-- optional -->
                                        <JobEndDate >DATETYPE</JobEndDate> <!-- optional -->
                                        <JobDesc >STRTYPE</JobDesc> <!-- optional -->
                                        <JobTypeRef> <!-- optional -->
                                                <ListID >IDTYPE</ListID> <!-- optional -->
                                                <FullName >STRTYPE</FullName> <!-- optional -->
                                        </JobTypeRef>
                                        <Notes >STRTYPE</Notes> <!-- optional -->
                                        <AdditionalNotesRet> <!-- optional, may repeat -->
                                                <NoteID >INTTYPE</NoteID> <!-- required -->
                                                <Date >DATETYPE</Date> <!-- required -->
                                                <Note >STRTYPE</Note> <!-- required -->
                                        </AdditionalNotesRet>
                                        <!-- PreferredDeliveryMethod may have one of the following values: None [Default], Email, Fax -->
                                        <PreferredDeliveryMethod >ENUMTYPE</PreferredDeliveryMethod> <!-- optional -->
                                        <PriceLevelRef> <!-- optional -->
                                                <ListID >IDTYPE</ListID> <!-- optional -->
                                                <FullName >STRTYPE</FullName> <!-- optional -->
                                        </PriceLevelRef>
                                        <ExternalGUID >GUIDTYPE</ExternalGUID> <!-- optional -->
                                        <TaxRegistrationNumber >STRTYPE</TaxRegistrationNumber> <!-- optional -->
                                        <CurrencyRef> <!-- optional -->
                                                <ListID >IDTYPE</ListID> <!-- optional -->
                                                <FullName >STRTYPE</FullName> <!-- optional -->
                                        </CurrencyRef>
                                        <DataExtRet> <!-- optional, may repeat -->
                                                <OwnerID >GUIDTYPE</OwnerID> <!-- optional -->
                                                <DataExtName >STRTYPE</DataExtName> <!-- required -->
                                                <!-- DataExtType may have one of the following values: AMTTYPE, DATETIMETYPE, INTTYPE, PERCENTTYPE, PRICETYPE, QUANTYPE, STR1024TYPE, STR255TYPE -->
                                                <DataExtType >ENUMTYPE</DataExtType> <!-- required -->
                                                <DataExtValue >STRTYPE</DataExtValue> <!-- required -->
                                        </DataExtRet>
                                </CustomerRet>
                        <!-- OR -->
                                <EmployeeRet> <!-- optional -->
                                        <ListID >IDTYPE</ListID> <!-- required -->
                                        <TimeCreated >DATETIMETYPE</TimeCreated> <!-- required -->
                                        <TimeModified >DATETIMETYPE</TimeModified> <!-- required -->
                                        <EditSequence >STRTYPE</EditSequence> <!-- required -->
                                        <Name >STRTYPE</Name> <!-- required -->
                                        <IsActive >BOOLTYPE</IsActive> <!-- optional -->
                                        <Salutation >STRTYPE</Salutation> <!-- optional -->
                                        <FirstName >STRTYPE</FirstName> <!-- optional -->
                                        <MiddleName >STRTYPE</MiddleName> <!-- optional -->
                                        <LastName >STRTYPE</LastName> <!-- optional -->
                                        <JobTitle >STRTYPE</JobTitle> <!-- optional -->
                                        <SupervisorRef> <!-- optional -->
                                                <ListID >IDTYPE</ListID> <!-- optional -->
                                                <FullName >STRTYPE</FullName> <!-- optional -->
                                        </SupervisorRef>
                                        <Department >STRTYPE</Department> <!-- optional -->
                                        <Description >STRTYPE</Description> <!-- optional -->
                                        <TargetBonus >AMTTYPE</TargetBonus> <!-- optional -->
                                        <EmployeeAddress> <!-- optional -->
                                                <Addr1 >STRTYPE</Addr1> <!-- optional -->
                                                <Addr2 >STRTYPE</Addr2> <!-- optional -->
                                                <City >STRTYPE</City> <!-- optional -->
                                                <State >STRTYPE</State> <!-- optional -->
                                                <PostalCode >STRTYPE</PostalCode> <!-- optional -->
                                        </EmployeeAddress>
                                        <PrintAs >STRTYPE</PrintAs> <!-- optional -->
                                        <Phone >STRTYPE</Phone> <!-- optional -->
                                        <Mobile >STRTYPE</Mobile> <!-- optional -->
                                        <Pager >STRTYPE</Pager> <!-- optional -->
                                        <PagerPIN >STRTYPE</PagerPIN> <!-- optional -->
                                        <AltPhone >STRTYPE</AltPhone> <!-- optional -->
                                        <Fax >STRTYPE</Fax> <!-- optional -->
                                        <SSN >STRTYPE</SSN> <!-- optional -->
                                        <Email >STRTYPE</Email> <!-- optional -->
                                        <AdditionalContactRef> <!-- must occur 0 - 8 times -->
                                                <ContactName >STRTYPE</ContactName> <!-- required -->
                                                <ContactValue >STRTYPE</ContactValue> <!-- required -->
                                        </AdditionalContactRef>
                                        <EmergencyContacts> <!-- optional -->
                                                <PrimaryContact> <!-- optional -->
                                                        <ContactName >STRTYPE</ContactName> <!-- required -->
                                                        <ContactValue >STRTYPE</ContactValue> <!-- required -->
                                                        <!-- Relation may have one of the following values: Spouse, Partner, Mother, Father, Sister, Brother, Son, Daughter, Friend, Other -->
                                                        <Relation >ENUMTYPE</Relation> <!-- optional -->
                                                </PrimaryContact>
                                                <SecondaryContact> <!-- optional -->
                                                        <ContactName >STRTYPE</ContactName> <!-- required -->
                                                        <ContactValue >STRTYPE</ContactValue> <!-- required -->
                                                        <!-- Relation may have one of the following values: Spouse, Partner, Mother, Father, Sister, Brother, Son, Daughter, Friend, Other -->
                                                        <Relation >ENUMTYPE</Relation> <!-- optional -->
                                                </SecondaryContact>
                                        </EmergencyContacts>
                                        <!-- EmployeeType may have one of the following values: Officer, Owner, Regular [DEFAULT], Statutory -->
                                        <EmployeeType >ENUMTYPE</EmployeeType> <!-- optional -->
                                        <!-- PartOrFullTime may have one of the following values: PartTime, FullTime -->
                                        <PartOrFullTime >ENUMTYPE</PartOrFullTime> <!-- optional -->
                                        <!-- Exempt may have one of the following values: Exempt, NonExempt -->
                                        <Exempt >ENUMTYPE</Exempt> <!-- optional -->
                                        <!-- KeyEmployee may have one of the following values: Yes, No -->
                                        <KeyEmployee >ENUMTYPE</KeyEmployee> <!-- optional -->
                                        <!-- Gender may have one of the following values: Male, Female -->
                                        <Gender >ENUMTYPE</Gender> <!-- optional -->
                                        <HiredDate >DATETYPE</HiredDate> <!-- optional -->
                                        <OriginalHireDate >DATETYPE</OriginalHireDate> <!-- optional -->
                                        <AdjustedServiceDate >DATETYPE</AdjustedServiceDate> <!-- optional -->
                                        <ReleasedDate >DATETYPE</ReleasedDate> <!-- optional -->
                                        <BirthDate >DATETYPE</BirthDate> <!-- optional -->
                                        <!-- USCitizen may have one of the following values: Yes, No -->
                                        <USCitizen >ENUMTYPE</USCitizen> <!-- optional -->
                                        <!-- Ethnicity may have one of the following values: AmericianIndian, Asian, Black, Hawaiian, Hispanic, White, TwoOrMoreRaces -->
                                        <Ethnicity >ENUMTYPE</Ethnicity> <!-- optional -->
                                        <!-- Disabled may have one of the following values: Yes, No -->
                                        <Disabled >ENUMTYPE</Disabled> <!-- optional -->
                                        <DisabilityDesc >STRTYPE</DisabilityDesc> <!-- optional -->
                                        <!-- OnFile may have one of the following values: Yes, No -->
                                        <OnFile >ENUMTYPE</OnFile> <!-- optional -->
                                        <WorkAuthExpireDate >DATETYPE</WorkAuthExpireDate> <!-- optional -->
                                        <!-- USVeteran may have one of the following values: Yes, No -->
                                        <USVeteran >ENUMTYPE</USVeteran> <!-- optional -->
                                        <!-- MilitaryStatus may have one of the following values: Active, Reserve -->
                                        <MilitaryStatus >ENUMTYPE</MilitaryStatus> <!-- optional -->
                                        <AccountNumber >STRTYPE</AccountNumber> <!-- optional -->
                                        <Notes >STRTYPE</Notes> <!-- optional -->
                                        <AdditionalNotesRet> <!-- optional, may repeat -->
                                                <NoteID >INTTYPE</NoteID> <!-- required -->
                                                <Date >DATETYPE</Date> <!-- required -->
                                                <Note >STRTYPE</Note> <!-- required -->
                                        </AdditionalNotesRet>
                                        <BillingRateRef> <!-- optional -->
                                                <ListID >IDTYPE</ListID> <!-- optional -->
                                                <FullName >STRTYPE</FullName> <!-- optional -->
                                        </BillingRateRef>
                                        <EmployeePayrollInfo> <!-- optional -->
                                                <!-- PayPeriod may have one of the following values: Daily, Weekly, Biweekly, Semimonthly, Monthly, Quarterly, Yearly -->
                                                <PayPeriod >ENUMTYPE</PayPeriod> <!-- optional -->
                                                <ClassRef> <!-- optional -->
                                                        <ListID >IDTYPE</ListID> <!-- optional -->
                                                        <FullName >STRTYPE</FullName> <!-- optional -->
                                                </ClassRef>
                                                <!-- BEGIN OR -->
                                                        <ClearEarnings >BOOLTYPE</ClearEarnings> <!-- optional -->
                                                <!-- OR -->
                                                        <Earnings> <!-- optional, may repeat -->
                                                                <PayrollItemWageRef> <!-- required -->
                                                                        <ListID >IDTYPE</ListID> <!-- optional -->
                                                                        <FullName >STRTYPE</FullName> <!-- optional -->
                                                                </PayrollItemWageRef>
                                                                <!-- BEGIN OR -->
                                                                        <Rate >PRICETYPE</Rate> <!-- optional -->
                                                                <!-- OR -->
                                                                        <RatePercent >PERCENTTYPE</RatePercent> <!-- optional -->
                                                                <!-- END OR -->
                                                        </Earnings>
                                                <!-- END OR -->
                                                <IsUsingTimeDataToCreatePaychecks >BOOLTYPE</IsUsingTimeDataToCreatePaychecks> <!-- optional -->
                                                <!-- UseTimeDataToCreatePaychecks may have one of the following values: NotSet, UseTimeData, DoNotUseTimeData -->
                                                <UseTimeDataToCreatePaychecks >ENUMTYPE</UseTimeDataToCreatePaychecks> <!-- optional -->
                                                <SickHours> <!-- optional -->
                                                        <HoursAvailable >TIMEINTERVALTYPE</HoursAvailable> <!-- optional -->
                                                        <!-- AccrualPeriod may have one of the following values: BeginningOfYear, EveryHourOnPaycheck, EveryPaycheck -->
                                                        <AccrualPeriod >ENUMTYPE</AccrualPeriod> <!-- optional -->
                                                        <HoursAccrued >TIMEINTERVALTYPE</HoursAccrued> <!-- optional -->
                                                        <MaximumHours >TIMEINTERVALTYPE</MaximumHours> <!-- optional -->
                                                        <IsResettingHoursEachNewYear >BOOLTYPE</IsResettingHoursEachNewYear> <!-- optional -->
                                                        <HoursUsed >TIMEINTERVALTYPE</HoursUsed> <!-- optional -->
                                                        <AccrualStartDate >DATETYPE</AccrualStartDate> <!-- optional -->
                                                </SickHours>
                                                <VacationHours> <!-- optional -->
                                                        <HoursAvailable >TIMEINTERVALTYPE</HoursAvailable> <!-- optional -->
                                                        <!-- AccrualPeriod may have one of the following values: BeginningOfYear, EveryHourOnPaycheck, EveryPaycheck -->
                                                        <AccrualPeriod >ENUMTYPE</AccrualPeriod> <!-- optional -->
                                                        <HoursAccrued >TIMEINTERVALTYPE</HoursAccrued> <!-- optional -->
                                                        <MaximumHours >TIMEINTERVALTYPE</MaximumHours> <!-- optional -->
                                                        <IsResettingHoursEachNewYear >BOOLTYPE</IsResettingHoursEachNewYear> <!-- optional -->
                                                        <HoursUsed >TIMEINTERVALTYPE</HoursUsed> <!-- optional -->
                                                        <AccrualStartDate >DATETYPE</AccrualStartDate> <!-- optional -->
                                                </VacationHours>
                                        </EmployeePayrollInfo>
                                        <ExternalGUID >GUIDTYPE</ExternalGUID> <!-- optional -->
                                        <DataExtRet> <!-- optional, may repeat -->
                                                <OwnerID >GUIDTYPE</OwnerID> <!-- optional -->
                                                <DataExtName >STRTYPE</DataExtName> <!-- required -->
                                                <!-- DataExtType may have one of the following values: AMTTYPE, DATETIMETYPE, INTTYPE, PERCENTTYPE, PRICETYPE, QUANTYPE, STR1024TYPE, STR255TYPE -->
                                                <DataExtType >ENUMTYPE</DataExtType> <!-- required -->
                                                <DataExtValue >STRTYPE</DataExtValue> <!-- required -->
                                        </DataExtRet>
                                </EmployeeRet>
                        <!-- OR -->
                                <OtherNameRet> <!-- optional -->
                                        <ListID >IDTYPE</ListID> <!-- required -->
                                        <TimeCreated >DATETIMETYPE</TimeCreated> <!-- required -->
                                        <TimeModified >DATETIMETYPE</TimeModified> <!-- required -->
                                        <EditSequence >STRTYPE</EditSequence> <!-- required -->
                                        <Name >STRTYPE</Name> <!-- required -->
                                        <IsActive >BOOLTYPE</IsActive> <!-- optional -->
                                        <CompanyName >STRTYPE</CompanyName> <!-- optional -->
                                        <Salutation >STRTYPE</Salutation> <!-- optional -->
                                        <FirstName >STRTYPE</FirstName> <!-- optional -->
                                        <MiddleName >STRTYPE</MiddleName> <!-- optional -->
                                        <LastName >STRTYPE</LastName> <!-- optional -->
                                        <OtherNameAddress> <!-- optional -->
                                                <Addr1 >STRTYPE</Addr1> <!-- optional -->
                                                <Addr2 >STRTYPE</Addr2> <!-- optional -->
                                                <Addr3 >STRTYPE</Addr3> <!-- optional -->
                                                <Addr4 >STRTYPE</Addr4> <!-- optional -->
                                                <Addr5 >STRTYPE</Addr5> <!-- optional -->
                                                <City >STRTYPE</City> <!-- optional -->
                                                <State >STRTYPE</State> <!-- optional -->
                                                <PostalCode >STRTYPE</PostalCode> <!-- optional -->
                                                <Country >STRTYPE</Country> <!-- optional -->
                                                <Note >STRTYPE</Note> <!-- optional -->
                                        </OtherNameAddress>
                                        <OtherNameAddressBlock> <!-- optional -->
                                                <Addr1 >STRTYPE</Addr1> <!-- optional -->
                                                <Addr2 >STRTYPE</Addr2> <!-- optional -->
                                                <Addr3 >STRTYPE</Addr3> <!-- optional -->
                                                <Addr4 >STRTYPE</Addr4> <!-- optional -->
                                                <Addr5 >STRTYPE</Addr5> <!-- optional -->
                                        </OtherNameAddressBlock>
                                        <Phone >STRTYPE</Phone> <!-- optional -->
                                        <AltPhone >STRTYPE</AltPhone> <!-- optional -->
                                        <Fax >STRTYPE</Fax> <!-- optional -->
                                        <Email >STRTYPE</Email> <!-- optional -->
                                        <Contact >STRTYPE</Contact> <!-- optional -->
                                        <AltContact >STRTYPE</AltContact> <!-- optional -->
                                        <AccountNumber >STRTYPE</AccountNumber> <!-- optional -->
                                        <Notes >STRTYPE</Notes> <!-- optional -->
                                        <ExternalGUID >GUIDTYPE</ExternalGUID> <!-- optional -->
                                        <DataExtRet> <!-- optional, may repeat -->
                                                <OwnerID >GUIDTYPE</OwnerID> <!-- optional -->
                                                <DataExtName >STRTYPE</DataExtName> <!-- required -->
                                                <!-- DataExtType may have one of the following values: AMTTYPE, DATETIMETYPE, INTTYPE, PERCENTTYPE, PRICETYPE, QUANTYPE, STR1024TYPE, STR255TYPE -->
                                                <DataExtType >ENUMTYPE</DataExtType> <!-- required -->
                                                <DataExtValue >STRTYPE</DataExtValue> <!-- required -->
                                        </DataExtRet>
                                </OtherNameRet>
                        <!-- OR -->
                                <VendorRet> <!-- optional -->
                                        <ListID >IDTYPE</ListID> <!-- required -->
                                        <TimeCreated >DATETIMETYPE</TimeCreated> <!-- required -->
                                        <TimeModified >DATETIMETYPE</TimeModified> <!-- required -->
                                        <EditSequence >STRTYPE</EditSequence> <!-- required -->
                                        <Name >STRTYPE</Name> <!-- required -->
                                        <IsActive >BOOLTYPE</IsActive> <!-- optional -->
                                        <ClassRef> <!-- optional -->
                                                <ListID >IDTYPE</ListID> <!-- optional -->
                                                <FullName >STRTYPE</FullName> <!-- optional -->
                                        </ClassRef>
                                        <IsTaxAgency >BOOLTYPE</IsTaxAgency> <!-- optional -->
                                        <CompanyName >STRTYPE</CompanyName> <!-- optional -->
                                        <Salutation >STRTYPE</Salutation> <!-- optional -->
                                        <FirstName >STRTYPE</FirstName> <!-- optional -->
                                        <MiddleName >STRTYPE</MiddleName> <!-- optional -->
                                        <LastName >STRTYPE</LastName> <!-- optional -->
                                        <JobTitle >STRTYPE</JobTitle> <!-- optional -->
                                        <VendorAddress> <!-- optional -->
                                                <Addr1 >STRTYPE</Addr1> <!-- optional -->
                                                <Addr2 >STRTYPE</Addr2> <!-- optional -->
                                                <Addr3 >STRTYPE</Addr3> <!-- optional -->
                                                <Addr4 >STRTYPE</Addr4> <!-- optional -->
                                                <Addr5 >STRTYPE</Addr5> <!-- optional -->
                                                <City >STRTYPE</City> <!-- optional -->
                                                <State >STRTYPE</State> <!-- optional -->
                                                <PostalCode >STRTYPE</PostalCode> <!-- optional -->
                                                <Country >STRTYPE</Country> <!-- optional -->
                                                <Note >STRTYPE</Note> <!-- optional -->
                                        </VendorAddress>
                                        <VendorAddressBlock> <!-- optional -->
                                                <Addr1 >STRTYPE</Addr1> <!-- optional -->
                                                <Addr2 >STRTYPE</Addr2> <!-- optional -->
                                                <Addr3 >STRTYPE</Addr3> <!-- optional -->
                                                <Addr4 >STRTYPE</Addr4> <!-- optional -->
                                                <Addr5 >STRTYPE</Addr5> <!-- optional -->
                                        </VendorAddressBlock>
                                        <ShipAddress> <!-- optional -->
                                                <Addr1 >STRTYPE</Addr1> <!-- optional -->
                                                <Addr2 >STRTYPE</Addr2> <!-- optional -->
                                                <Addr3 >STRTYPE</Addr3> <!-- optional -->
                                                <Addr4 >STRTYPE</Addr4> <!-- optional -->
                                                <Addr5 >STRTYPE</Addr5> <!-- optional -->
                                                <City >STRTYPE</City> <!-- optional -->
                                                <State >STRTYPE</State> <!-- optional -->
                                                <PostalCode >STRTYPE</PostalCode> <!-- optional -->
                                                <Country >STRTYPE</Country> <!-- optional -->
                                                <Note >STRTYPE</Note> <!-- optional -->
                                        </ShipAddress>
                                        <Phone >STRTYPE</Phone> <!-- optional -->
                                        <AltPhone >STRTYPE</AltPhone> <!-- optional -->
                                        <Fax >STRTYPE</Fax> <!-- optional -->
                                        <Email >STRTYPE</Email> <!-- optional -->
                                        <Cc >STRTYPE</Cc> <!-- optional -->
                                        <Contact >STRTYPE</Contact> <!-- optional -->
                                        <AltContact >STRTYPE</AltContact> <!-- optional -->
                                        <AdditionalContactRef> <!-- must occur 0 - 8 times -->
                                                <ContactName >STRTYPE</ContactName> <!-- required -->
                                                <ContactValue >STRTYPE</ContactValue> <!-- required -->
                                        </AdditionalContactRef>
                                        <ContactsRet> <!-- optional, may repeat -->
                                                <ListID >IDTYPE</ListID> <!-- required -->
                                                <TimeCreated >DATETIMETYPE</TimeCreated> <!-- required -->
                                                <TimeModified >DATETIMETYPE</TimeModified> <!-- required -->
                                                <EditSequence >STRTYPE</EditSequence> <!-- required -->
                                                <Contact >STRTYPE</Contact> <!-- optional -->
                                                <Salutation >STRTYPE</Salutation> <!-- optional -->
                                                <FirstName >STRTYPE</FirstName> <!-- required -->
                                                <MiddleName >STRTYPE</MiddleName> <!-- optional -->
                                                <LastName >STRTYPE</LastName> <!-- optional -->
                                                <JobTitle >STRTYPE</JobTitle> <!-- optional -->
                                                <AdditionalContactRef> <!-- must occur 0 - 5 times -->
                                                        <ContactName >STRTYPE</ContactName> <!-- required -->
                                                        <ContactValue >STRTYPE</ContactValue> <!-- required -->
                                                </AdditionalContactRef>
                                        </ContactsRet>
                                        <NameOnCheck >STRTYPE</NameOnCheck> <!-- optional -->
                                        <AccountNumber >STRTYPE</AccountNumber> <!-- optional -->
                                        <Notes >STRTYPE</Notes> <!-- optional -->
                                        <AdditionalNotesRet> <!-- optional, may repeat -->
                                                <NoteID >INTTYPE</NoteID> <!-- required -->
                                                <Date >DATETYPE</Date> <!-- required -->
                                                <Note >STRTYPE</Note> <!-- required -->
                                        </AdditionalNotesRet>
                                        <VendorTypeRef> <!-- optional -->
                                                <ListID >IDTYPE</ListID> <!-- optional -->
                                                <FullName >STRTYPE</FullName> <!-- optional -->
                                        </VendorTypeRef>
                                        <TermsRef> <!-- optional -->
                                                <ListID >IDTYPE</ListID> <!-- optional -->
                                                <FullName >STRTYPE</FullName> <!-- optional -->
                                        </TermsRef>
                                        <CreditLimit >AMTTYPE</CreditLimit> <!-- optional -->
                                        <VendorTaxIdent >STRTYPE</VendorTaxIdent> <!-- optional -->
                                        <IsVendorEligibleFor1099 >BOOLTYPE</IsVendorEligibleFor1099> <!-- optional -->
                                        <Balance >AMTTYPE</Balance> <!-- optional -->
                                        <BillingRateRef> <!-- optional -->
                                                <ListID >IDTYPE</ListID> <!-- optional -->
                                                <FullName >STRTYPE</FullName> <!-- optional -->
                                        </BillingRateRef>
                                        <ExternalGUID >GUIDTYPE</ExternalGUID> <!-- optional -->
                                        <SalesTaxCodeRef> <!-- optional -->
                                                <ListID >IDTYPE</ListID> <!-- optional -->
                                                <FullName >STRTYPE</FullName> <!-- optional -->
                                        </SalesTaxCodeRef>
                                        <!-- SalesTaxCountry may have one of the following values: Australia, Canada [DEFAULT], UK, US -->
                                        <SalesTaxCountry >ENUMTYPE</SalesTaxCountry> <!-- optional -->
                                        <IsSalesTaxAgency >BOOLTYPE</IsSalesTaxAgency> <!-- optional -->
                                        <SalesTaxReturnRef> <!-- optional -->
                                                <ListID >IDTYPE</ListID> <!-- optional -->
                                                <FullName >STRTYPE</FullName> <!-- optional -->
                                        </SalesTaxReturnRef>
                                        <TaxRegistrationNumber >STRTYPE</TaxRegistrationNumber> <!-- optional -->
                                        <!-- ReportingPeriod may have one of the following values: Monthly, Quarterly [DEFAULT] -->
                                        <ReportingPeriod >ENUMTYPE</ReportingPeriod> <!-- optional -->
                                        <IsTaxTrackedOnPurchases >BOOLTYPE</IsTaxTrackedOnPurchases> <!-- optional -->
                                        <TaxOnPurchasesAccountRef> <!-- optional -->
                                                <ListID >IDTYPE</ListID> <!-- optional -->
                                                <FullName >STRTYPE</FullName> <!-- optional -->
                                        </TaxOnPurchasesAccountRef>
                                        <IsTaxTrackedOnSales >BOOLTYPE</IsTaxTrackedOnSales> <!-- optional -->
                                        <TaxOnSalesAccountRef> <!-- optional -->
                                                <ListID >IDTYPE</ListID> <!-- optional -->
                                                <FullName >STRTYPE</FullName> <!-- optional -->
                                        </TaxOnSalesAccountRef>
                                        <IsTaxOnTax >BOOLTYPE</IsTaxOnTax> <!-- optional -->
                                        <PrefillAccountRef> <!-- must occur 0 - 3 times -->
                                                <ListID >IDTYPE</ListID> <!-- optional -->
                                                <FullName >STRTYPE</FullName> <!-- optional -->
                                        </PrefillAccountRef>
                                        <CurrencyRef> <!-- optional -->
                                                <ListID >IDTYPE</ListID> <!-- optional -->
                                                <FullName >STRTYPE</FullName> <!-- optional -->
                                        </CurrencyRef>
                                        <DataExtRet> <!-- optional, may repeat -->
                                                <OwnerID >GUIDTYPE</OwnerID> <!-- optional -->
                                                <DataExtName >STRTYPE</DataExtName> <!-- required -->
                                                <!-- DataExtType may have one of the following values: AMTTYPE, DATETIMETYPE, INTTYPE, PERCENTTYPE, PRICETYPE, QUANTYPE, STR1024TYPE, STR255TYPE -->
                                                <DataExtType >ENUMTYPE</DataExtType> <!-- required -->
                                                <DataExtValue >STRTYPE</DataExtValue> <!-- required -->
                                        </DataExtRet>
                                </VendorRet>
                        <!-- END OR -->
                </EntityQueryRs>
        </QBXMLMsgsRq>
</QBXML>
```

## EstimateQuery
### XMLOps
```
<?xml version="1.0" encoding="utf-8"?>
<?qbxml version="16.0"?>
<QBXML>
        <QBXMLMsgsRq onError="stopOnError">
                <EntityQueryRq metaData="ENUMTYPE" iterator="ENUMTYPE" iteratorID="UUIDTYPE">
                        <!-- BEGIN OR -->
                                <ListID >IDTYPE</ListID> <!-- optional, may repeat -->
                        <!-- OR -->
                                <FullName >STRTYPE</FullName> <!-- optional, may repeat -->
                        <!-- OR -->
                                <MaxReturned >INTTYPE</MaxReturned> <!-- optional -->
                                <!-- ActiveStatus may have one of the following values: ActiveOnly [DEFAULT], InactiveOnly, All -->
                                <ActiveStatus >ENUMTYPE</ActiveStatus> <!-- optional -->
                                <FromModifiedDate >DATETIMETYPE</FromModifiedDate> <!-- optional -->
                                <ToModifiedDate >DATETIMETYPE</ToModifiedDate> <!-- optional -->
                                <!-- BEGIN OR -->
                                        <NameFilter> <!-- optional -->
                                                <!-- MatchCriterion may have one of the following values: StartsWith, Contains, EndsWith -->
                                                <MatchCriterion >ENUMTYPE</MatchCriterion> <!-- required -->
                                                <Name >STRTYPE</Name> <!-- required -->
                                        </NameFilter>
                                <!-- OR -->
                                        <NameRangeFilter> <!-- optional -->
                                                <FromName >STRTYPE</FromName> <!-- optional -->
                                                <ToName >STRTYPE</ToName> <!-- optional -->
                                        </NameRangeFilter>
                                <!-- END OR -->
                        <!-- END OR -->
                        <IncludeRetElement >STRTYPE</IncludeRetElement> <!-- optional, may repeat -->
                </EntityQueryRq>

                <EntityQueryRs statusCode="INTTYPE" statusSeverity="STRTYPE" statusMessage="STRTYPE" retCount="INTTYPE" iteratorRemainingCount="INTTYPE" iteratorID="UUIDTYPE">
                        <!-- BEGIN OR -->
                                <CustomerRet> <!-- optional -->
                                        <ListID >IDTYPE</ListID> <!-- required -->
                                        <TimeCreated >DATETIMETYPE</TimeCreated> <!-- required -->
                                        <TimeModified >DATETIMETYPE</TimeModified> <!-- required -->
                                        <EditSequence >STRTYPE</EditSequence> <!-- required -->
                                        <Name >STRTYPE</Name> <!-- required -->
                                        <FullName >STRTYPE</FullName> <!-- required -->
                                        <IsActive >BOOLTYPE</IsActive> <!-- optional -->
                                        <ClassRef> <!-- optional -->
                                                <ListID >IDTYPE</ListID> <!-- optional -->
                                                <FullName >STRTYPE</FullName> <!-- optional -->
                                        </ClassRef>
                                        <ParentRef> <!-- optional -->
                                                <ListID >IDTYPE</ListID> <!-- optional -->
                                                <FullName >STRTYPE</FullName> <!-- optional -->
                                        </ParentRef>
                                        <Sublevel >INTTYPE</Sublevel> <!-- required -->
                                        <CompanyName >STRTYPE</CompanyName> <!-- optional -->
                                        <Salutation >STRTYPE</Salutation> <!-- optional -->
                                        <FirstName >STRTYPE</FirstName> <!-- optional -->
                                        <MiddleName >STRTYPE</MiddleName> <!-- optional -->
                                        <LastName >STRTYPE</LastName> <!-- optional -->
                                        <JobTitle >STRTYPE</JobTitle> <!-- optional -->
                                        <BillAddress> <!-- optional -->
                                                <Addr1 >STRTYPE</Addr1> <!-- optional -->
                                                <Addr2 >STRTYPE</Addr2> <!-- optional -->
                                                <Addr3 >STRTYPE</Addr3> <!-- optional -->
                                                <Addr4 >STRTYPE</Addr4> <!-- optional -->
                                                <Addr5 >STRTYPE</Addr5> <!-- optional -->
                                                <City >STRTYPE</City> <!-- optional -->
                                                <State >STRTYPE</State> <!-- optional -->
                                                <PostalCode >STRTYPE</PostalCode> <!-- optional -->
                                                <Country >STRTYPE</Country> <!-- optional -->
                                                <Note >STRTYPE</Note> <!-- optional -->
                                        </BillAddress>
                                        <BillAddressBlock> <!-- optional -->
                                                <Addr1 >STRTYPE</Addr1> <!-- optional -->
                                                <Addr2 >STRTYPE</Addr2> <!-- optional -->
                                                <Addr3 >STRTYPE</Addr3> <!-- optional -->
                                                <Addr4 >STRTYPE</Addr4> <!-- optional -->
                                                <Addr5 >STRTYPE</Addr5> <!-- optional -->
                                        </BillAddressBlock>
                                        <ShipAddress> <!-- optional -->
                                                <Addr1 >STRTYPE</Addr1> <!-- optional -->
                                                <Addr2 >STRTYPE</Addr2> <!-- optional -->
                                                <Addr3 >STRTYPE</Addr3> <!-- optional -->
                                                <Addr4 >STRTYPE</Addr4> <!-- optional -->
                                                <Addr5 >STRTYPE</Addr5> <!-- optional -->
                                                <City >STRTYPE</City> <!-- optional -->
                                                <State >STRTYPE</State> <!-- optional -->
                                                <PostalCode >STRTYPE</PostalCode> <!-- optional -->
                                                <Country >STRTYPE</Country> <!-- optional -->
                                                <Note >STRTYPE</Note> <!-- optional -->
                                        </ShipAddress>
                                        <ShipAddressBlock> <!-- optional -->
                                                <Addr1 >STRTYPE</Addr1> <!-- optional -->
                                                <Addr2 >STRTYPE</Addr2> <!-- optional -->
                                                <Addr3 >STRTYPE</Addr3> <!-- optional -->
                                                <Addr4 >STRTYPE</Addr4> <!-- optional -->
                                                <Addr5 >STRTYPE</Addr5> <!-- optional -->
                                        </ShipAddressBlock>
                                        <ShipToAddress> <!-- must occur 0 - 50 times -->
                                                <Name >STRTYPE</Name> <!-- required -->
                                                <Addr1 >STRTYPE</Addr1> <!-- optional -->
                                                <Addr2 >STRTYPE</Addr2> <!-- optional -->
                                                <Addr3 >STRTYPE</Addr3> <!-- optional -->
                                                <Addr4 >STRTYPE</Addr4> <!-- optional -->
                                                <Addr5 >STRTYPE</Addr5> <!-- optional -->
                                                <City >STRTYPE</City> <!-- optional -->
                                                <State >STRTYPE</State> <!-- optional -->
                                                <PostalCode >STRTYPE</PostalCode> <!-- optional -->
                                                <Country >STRTYPE</Country> <!-- optional -->
                                                <Note >STRTYPE</Note> <!-- optional -->
                                                <DefaultShipTo >BOOLTYPE</DefaultShipTo> <!-- optional -->
                                        </ShipToAddress>
                                        <Phone >STRTYPE</Phone> <!-- optional -->
                                        <AltPhone >STRTYPE</AltPhone> <!-- optional -->
                                        <Fax >STRTYPE</Fax> <!-- optional -->
                                        <Email >STRTYPE</Email> <!-- optional -->
                                        <Cc >STRTYPE</Cc> <!-- optional -->
                                        <Contact >STRTYPE</Contact> <!-- optional -->
                                        <AltContact >STRTYPE</AltContact> <!-- optional -->
                                        <AdditionalContactRef> <!-- must occur 0 - 8 times -->
                                                <ContactName >STRTYPE</ContactName> <!-- required -->
                                                <ContactValue >STRTYPE</ContactValue> <!-- required -->
                                        </AdditionalContactRef>
                                        <ContactsRet> <!-- optional, may repeat -->
                                                <ListID >IDTYPE</ListID> <!-- required -->
                                                <TimeCreated >DATETIMETYPE</TimeCreated> <!-- required -->
                                                <TimeModified >DATETIMETYPE</TimeModified> <!-- required -->
                                                <EditSequence >STRTYPE</EditSequence> <!-- required -->
                                                <Contact >STRTYPE</Contact> <!-- optional -->
                                                <Salutation >STRTYPE</Salutation> <!-- optional -->
                                                <FirstName >STRTYPE</FirstName> <!-- required -->
                                                <MiddleName >STRTYPE</MiddleName> <!-- optional -->
                                                <LastName >STRTYPE</LastName> <!-- optional -->
                                                <JobTitle >STRTYPE</JobTitle> <!-- optional -->
                                                <AdditionalContactRef> <!-- must occur 0 - 5 times -->
                                                        <ContactName >STRTYPE</ContactName> <!-- required -->
                                                        <ContactValue >STRTYPE</ContactValue> <!-- required -->
                                                </AdditionalContactRef>
                                        </ContactsRet>
                                        <CustomerTypeRef> <!-- optional -->
                                                <ListID >IDTYPE</ListID> <!-- optional -->
                                                <FullName >STRTYPE</FullName> <!-- optional -->
                                        </CustomerTypeRef>
                                        <TermsRef> <!-- optional -->
                                                <ListID >IDTYPE</ListID> <!-- optional -->
                                                <FullName >STRTYPE</FullName> <!-- optional -->
                                        </TermsRef>
                                        <SalesRepRef> <!-- optional -->
                                                <ListID >IDTYPE</ListID> <!-- optional -->
                                                <FullName >STRTYPE</FullName> <!-- optional -->
                                        </SalesRepRef>
                                        <Balance >AMTTYPE</Balance> <!-- optional -->
                                        <TotalBalance >AMTTYPE</TotalBalance> <!-- optional -->
                                        <SalesTaxCodeRef> <!-- optional -->
                                                <ListID >IDTYPE</ListID> <!-- optional -->
                                                <FullName >STRTYPE</FullName> <!-- optional -->
                                        </SalesTaxCodeRef>
                                        <ItemSalesTaxRef> <!-- optional -->
                                                <ListID >IDTYPE</ListID> <!-- optional -->
                                                <FullName >STRTYPE</FullName> <!-- optional -->
                                        </ItemSalesTaxRef>
                                        <!-- SalesTaxCountry may have one of the following values: Australia, Canada [DEFAULT], UK, US -->
                                        <SalesTaxCountry >ENUMTYPE</SalesTaxCountry> <!-- optional -->
                                        <ResaleNumber >STRTYPE</ResaleNumber> <!-- optional -->
                                        <AccountNumber >STRTYPE</AccountNumber> <!-- optional -->
                                        <CreditLimit >AMTTYPE</CreditLimit> <!-- optional -->
                                        <PreferredPaymentMethodRef> <!-- optional -->
                                                <ListID >IDTYPE</ListID> <!-- optional -->
                                                <FullName >STRTYPE</FullName> <!-- optional -->
                                        </PreferredPaymentMethodRef>
                                        <CreditCardInfo> <!-- optional -->
                                                <CreditCardNumber >STRTYPE</CreditCardNumber> <!-- optional -->
                                                <ExpirationMonth >INTTYPE</ExpirationMonth> <!-- optional -->
                                                <ExpirationYear >INTTYPE</ExpirationYear> <!-- optional -->
                                                <NameOnCard >STRTYPE</NameOnCard> <!-- optional -->
                                                <CreditCardAddress >STRTYPE</CreditCardAddress> <!-- optional -->
                                                <CreditCardPostalCode >STRTYPE</CreditCardPostalCode> <!-- optional -->
                                        </CreditCardInfo>
                                        <!-- JobStatus may have one of the following values: Awarded, Closed, InProgress, None [DEFAULT], NotAwarded, Pending -->
                                        <JobStatus >ENUMTYPE</JobStatus> <!-- optional -->
                                        <JobStartDate >DATETYPE</JobStartDate> <!-- optional -->
                                        <JobProjectedEndDate >DATETYPE</JobProjectedEndDate> <!-- optional -->
                                        <JobEndDate >DATETYPE</JobEndDate> <!-- optional -->
                                        <JobDesc >STRTYPE</JobDesc> <!-- optional -->
                                        <JobTypeRef> <!-- optional -->
                                                <ListID >IDTYPE</ListID> <!-- optional -->
                                                <FullName >STRTYPE</FullName> <!-- optional -->
                                        </JobTypeRef>
                                        <Notes >STRTYPE</Notes> <!-- optional -->
                                        <AdditionalNotesRet> <!-- optional, may repeat -->
                                                <NoteID >INTTYPE</NoteID> <!-- required -->
                                                <Date >DATETYPE</Date> <!-- required -->
                                                <Note >STRTYPE</Note> <!-- required -->
                                        </AdditionalNotesRet>
                                        <!-- PreferredDeliveryMethod may have one of the following values: None [Default], Email, Fax -->
                                        <PreferredDeliveryMethod >ENUMTYPE</PreferredDeliveryMethod> <!-- optional -->
                                        <PriceLevelRef> <!-- optional -->
                                                <ListID >IDTYPE</ListID> <!-- optional -->
                                                <FullName >STRTYPE</FullName> <!-- optional -->
                                        </PriceLevelRef>
                                        <ExternalGUID >GUIDTYPE</ExternalGUID> <!-- optional -->
                                        <TaxRegistrationNumber >STRTYPE</TaxRegistrationNumber> <!-- optional -->
                                        <CurrencyRef> <!-- optional -->
                                                <ListID >IDTYPE</ListID> <!-- optional -->
                                                <FullName >STRTYPE</FullName> <!-- optional -->
                                        </CurrencyRef>
                                        <DataExtRet> <!-- optional, may repeat -->
                                                <OwnerID >GUIDTYPE</OwnerID> <!-- optional -->
                                                <DataExtName >STRTYPE</DataExtName> <!-- required -->
                                                <!-- DataExtType may have one of the following values: AMTTYPE, DATETIMETYPE, INTTYPE, PERCENTTYPE, PRICETYPE, QUANTYPE, STR1024TYPE, STR255TYPE -->
                                                <DataExtType >ENUMTYPE</DataExtType> <!-- required -->
                                                <DataExtValue >STRTYPE</DataExtValue> <!-- required -->
                                        </DataExtRet>
                                </CustomerRet>
                        <!-- OR -->
                                <EmployeeRet> <!-- optional -->
                                        <ListID >IDTYPE</ListID> <!-- required -->
                                        <TimeCreated >DATETIMETYPE</TimeCreated> <!-- required -->
                                        <TimeModified >DATETIMETYPE</TimeModified> <!-- required -->
                                        <EditSequence >STRTYPE</EditSequence> <!-- required -->
                                        <Name >STRTYPE</Name> <!-- required -->
                                        <IsActive >BOOLTYPE</IsActive> <!-- optional -->
                                        <Salutation >STRTYPE</Salutation> <!-- optional -->
                                        <FirstName >STRTYPE</FirstName> <!-- optional -->
                                        <MiddleName >STRTYPE</MiddleName> <!-- optional -->
                                        <LastName >STRTYPE</LastName> <!-- optional -->
                                        <JobTitle >STRTYPE</JobTitle> <!-- optional -->
                                        <SupervisorRef> <!-- optional -->
                                                <ListID >IDTYPE</ListID> <!-- optional -->
                                                <FullName >STRTYPE</FullName> <!-- optional -->
                                        </SupervisorRef>
                                        <Department >STRTYPE</Department> <!-- optional -->
                                        <Description >STRTYPE</Description> <!-- optional -->
                                        <TargetBonus >AMTTYPE</TargetBonus> <!-- optional -->
                                        <EmployeeAddress> <!-- optional -->
                                                <Addr1 >STRTYPE</Addr1> <!-- optional -->
                                                <Addr2 >STRTYPE</Addr2> <!-- optional -->
                                                <City >STRTYPE</City> <!-- optional -->
                                                <State >STRTYPE</State> <!-- optional -->
                                                <PostalCode >STRTYPE</PostalCode> <!-- optional -->
                                        </EmployeeAddress>
                                        <PrintAs >STRTYPE</PrintAs> <!-- optional -->
                                        <Phone >STRTYPE</Phone> <!-- optional -->
                                        <Mobile >STRTYPE</Mobile> <!-- optional -->
                                        <Pager >STRTYPE</Pager> <!-- optional -->
                                        <PagerPIN >STRTYPE</PagerPIN> <!-- optional -->
                                        <AltPhone >STRTYPE</AltPhone> <!-- optional -->
                                        <Fax >STRTYPE</Fax> <!-- optional -->
                                        <SSN >STRTYPE</SSN> <!-- optional -->
                                        <Email >STRTYPE</Email> <!-- optional -->
                                        <AdditionalContactRef> <!-- must occur 0 - 8 times -->
                                                <ContactName >STRTYPE</ContactName> <!-- required -->
                                                <ContactValue >STRTYPE</ContactValue> <!-- required -->
                                        </AdditionalContactRef>
                                        <EmergencyContacts> <!-- optional -->
                                                <PrimaryContact> <!-- optional -->
                                                        <ContactName >STRTYPE</ContactName> <!-- required -->
                                                        <ContactValue >STRTYPE</ContactValue> <!-- required -->
                                                        <!-- Relation may have one of the following values: Spouse, Partner, Mother, Father, Sister, Brother, Son, Daughter, Friend, Other -->
                                                        <Relation >ENUMTYPE</Relation> <!-- optional -->
                                                </PrimaryContact>
                                                <SecondaryContact> <!-- optional -->
                                                        <ContactName >STRTYPE</ContactName> <!-- required -->
                                                        <ContactValue >STRTYPE</ContactValue> <!-- required -->
                                                        <!-- Relation may have one of the following values: Spouse, Partner, Mother, Father, Sister, Brother, Son, Daughter, Friend, Other -->
                                                        <Relation >ENUMTYPE</Relation> <!-- optional -->
                                                </SecondaryContact>
                                        </EmergencyContacts>
                                        <!-- EmployeeType may have one of the following values: Officer, Owner, Regular [DEFAULT], Statutory -->
                                        <EmployeeType >ENUMTYPE</EmployeeType> <!-- optional -->
                                        <!-- PartOrFullTime may have one of the following values: PartTime, FullTime -->
                                        <PartOrFullTime >ENUMTYPE</PartOrFullTime> <!-- optional -->
                                        <!-- Exempt may have one of the following values: Exempt, NonExempt -->
                                        <Exempt >ENUMTYPE</Exempt> <!-- optional -->
                                        <!-- KeyEmployee may have one of the following values: Yes, No -->
                                        <KeyEmployee >ENUMTYPE</KeyEmployee> <!-- optional -->
                                        <!-- Gender may have one of the following values: Male, Female -->
                                        <Gender >ENUMTYPE</Gender> <!-- optional -->
                                        <HiredDate >DATETYPE</HiredDate> <!-- optional -->
                                        <OriginalHireDate >DATETYPE</OriginalHireDate> <!-- optional -->
                                        <AdjustedServiceDate >DATETYPE</AdjustedServiceDate> <!-- optional -->
                                        <ReleasedDate >DATETYPE</ReleasedDate> <!-- optional -->
                                        <BirthDate >DATETYPE</BirthDate> <!-- optional -->
                                        <!-- USCitizen may have one of the following values: Yes, No -->
                                        <USCitizen >ENUMTYPE</USCitizen> <!-- optional -->
                                        <!-- Ethnicity may have one of the following values: AmericianIndian, Asian, Black, Hawaiian, Hispanic, White, TwoOrMoreRaces -->
                                        <Ethnicity >ENUMTYPE</Ethnicity> <!-- optional -->
                                        <!-- Disabled may have one of the following values: Yes, No -->
                                        <Disabled >ENUMTYPE</Disabled> <!-- optional -->
                                        <DisabilityDesc >STRTYPE</DisabilityDesc> <!-- optional -->
                                        <!-- OnFile may have one of the following values: Yes, No -->
                                        <OnFile >ENUMTYPE</OnFile> <!-- optional -->
                                        <WorkAuthExpireDate >DATETYPE</WorkAuthExpireDate> <!-- optional -->
                                        <!-- USVeteran may have one of the following values: Yes, No -->
                                        <USVeteran >ENUMTYPE</USVeteran> <!-- optional -->
                                        <!-- MilitaryStatus may have one of the following values: Active, Reserve -->
                                        <MilitaryStatus >ENUMTYPE</MilitaryStatus> <!-- optional -->
                                        <AccountNumber >STRTYPE</AccountNumber> <!-- optional -->
                                        <Notes >STRTYPE</Notes> <!-- optional -->
                                        <AdditionalNotesRet> <!-- optional, may repeat -->
                                                <NoteID >INTTYPE</NoteID> <!-- required -->
                                                <Date >DATETYPE</Date> <!-- required -->
                                                <Note >STRTYPE</Note> <!-- required -->
                                        </AdditionalNotesRet>
                                        <BillingRateRef> <!-- optional -->
                                                <ListID >IDTYPE</ListID> <!-- optional -->
                                                <FullName >STRTYPE</FullName> <!-- optional -->
                                        </BillingRateRef>
                                        <EmployeePayrollInfo> <!-- optional -->
                                                <!-- PayPeriod may have one of the following values: Daily, Weekly, Biweekly, Semimonthly, Monthly, Quarterly, Yearly -->
                                                <PayPeriod >ENUMTYPE</PayPeriod> <!-- optional -->
                                                <ClassRef> <!-- optional -->
                                                        <ListID >IDTYPE</ListID> <!-- optional -->
                                                        <FullName >STRTYPE</FullName> <!-- optional -->
                                                </ClassRef>
                                                <!-- BEGIN OR -->
                                                        <ClearEarnings >BOOLTYPE</ClearEarnings> <!-- optional -->
                                                <!-- OR -->
                                                        <Earnings> <!-- optional, may repeat -->
                                                                <PayrollItemWageRef> <!-- required -->
                                                                        <ListID >IDTYPE</ListID> <!-- optional -->
                                                                        <FullName >STRTYPE</FullName> <!-- optional -->
                                                                </PayrollItemWageRef>
                                                                <!-- BEGIN OR -->
                                                                        <Rate >PRICETYPE</Rate> <!-- optional -->
                                                                <!-- OR -->
                                                                        <RatePercent >PERCENTTYPE</RatePercent> <!-- optional -->
                                                                <!-- END OR -->
                                                        </Earnings>
                                                <!-- END OR -->
                                                <IsUsingTimeDataToCreatePaychecks >BOOLTYPE</IsUsingTimeDataToCreatePaychecks> <!-- optional -->
                                                <!-- UseTimeDataToCreatePaychecks may have one of the following values: NotSet, UseTimeData, DoNotUseTimeData -->
                                                <UseTimeDataToCreatePaychecks >ENUMTYPE</UseTimeDataToCreatePaychecks> <!-- optional -->
                                                <SickHours> <!-- optional -->
                                                        <HoursAvailable >TIMEINTERVALTYPE</HoursAvailable> <!-- optional -->
                                                        <!-- AccrualPeriod may have one of the following values: BeginningOfYear, EveryHourOnPaycheck, EveryPaycheck -->
                                                        <AccrualPeriod >ENUMTYPE</AccrualPeriod> <!-- optional -->
                                                        <HoursAccrued >TIMEINTERVALTYPE</HoursAccrued> <!-- optional -->
                                                        <MaximumHours >TIMEINTERVALTYPE</MaximumHours> <!-- optional -->
                                                        <IsResettingHoursEachNewYear >BOOLTYPE</IsResettingHoursEachNewYear> <!-- optional -->
                                                        <HoursUsed >TIMEINTERVALTYPE</HoursUsed> <!-- optional -->
                                                        <AccrualStartDate >DATETYPE</AccrualStartDate> <!-- optional -->
                                                </SickHours>
                                                <VacationHours> <!-- optional -->
                                                        <HoursAvailable >TIMEINTERVALTYPE</HoursAvailable> <!-- optional -->
                                                        <!-- AccrualPeriod may have one of the following values: BeginningOfYear, EveryHourOnPaycheck, EveryPaycheck -->
                                                        <AccrualPeriod >ENUMTYPE</AccrualPeriod> <!-- optional -->
                                                        <HoursAccrued >TIMEINTERVALTYPE</HoursAccrued> <!-- optional -->
                                                        <MaximumHours >TIMEINTERVALTYPE</MaximumHours> <!-- optional -->
                                                        <IsResettingHoursEachNewYear >BOOLTYPE</IsResettingHoursEachNewYear> <!-- optional -->
                                                        <HoursUsed >TIMEINTERVALTYPE</HoursUsed> <!-- optional -->
                                                        <AccrualStartDate >DATETYPE</AccrualStartDate> <!-- optional -->
                                                </VacationHours>
                                        </EmployeePayrollInfo>
                                        <ExternalGUID >GUIDTYPE</ExternalGUID> <!-- optional -->
                                        <DataExtRet> <!-- optional, may repeat -->
                                                <OwnerID >GUIDTYPE</OwnerID> <!-- optional -->
                                                <DataExtName >STRTYPE</DataExtName> <!-- required -->
                                                <!-- DataExtType may have one of the following values: AMTTYPE, DATETIMETYPE, INTTYPE, PERCENTTYPE, PRICETYPE, QUANTYPE, STR1024TYPE, STR255TYPE -->
                                                <DataExtType >ENUMTYPE</DataExtType> <!-- required -->
                                                <DataExtValue >STRTYPE</DataExtValue> <!-- required -->
                                        </DataExtRet>
                                </EmployeeRet>
                        <!-- OR -->
                                <OtherNameRet> <!-- optional -->
                                        <ListID >IDTYPE</ListID> <!-- required -->
                                        <TimeCreated >DATETIMETYPE</TimeCreated> <!-- required -->
                                        <TimeModified >DATETIMETYPE</TimeModified> <!-- required -->
                                        <EditSequence >STRTYPE</EditSequence> <!-- required -->
                                        <Name >STRTYPE</Name> <!-- required -->
                                        <IsActive >BOOLTYPE</IsActive> <!-- optional -->
                                        <CompanyName >STRTYPE</CompanyName> <!-- optional -->
                                        <Salutation >STRTYPE</Salutation> <!-- optional -->
                                        <FirstName >STRTYPE</FirstName> <!-- optional -->
                                        <MiddleName >STRTYPE</MiddleName> <!-- optional -->
                                        <LastName >STRTYPE</LastName> <!-- optional -->
                                        <OtherNameAddress> <!-- optional -->
                                                <Addr1 >STRTYPE</Addr1> <!-- optional -->
                                                <Addr2 >STRTYPE</Addr2> <!-- optional -->
                                                <Addr3 >STRTYPE</Addr3> <!-- optional -->
                                                <Addr4 >STRTYPE</Addr4> <!-- optional -->
                                                <Addr5 >STRTYPE</Addr5> <!-- optional -->
                                                <City >STRTYPE</City> <!-- optional -->
                                                <State >STRTYPE</State> <!-- optional -->
                                                <PostalCode >STRTYPE</PostalCode> <!-- optional -->
                                                <Country >STRTYPE</Country> <!-- optional -->
                                                <Note >STRTYPE</Note> <!-- optional -->
                                        </OtherNameAddress>
                                        <OtherNameAddressBlock> <!-- optional -->
                                                <Addr1 >STRTYPE</Addr1> <!-- optional -->
                                                <Addr2 >STRTYPE</Addr2> <!-- optional -->
                                                <Addr3 >STRTYPE</Addr3> <!-- optional -->
                                                <Addr4 >STRTYPE</Addr4> <!-- optional -->
                                                <Addr5 >STRTYPE</Addr5> <!-- optional -->
                                        </OtherNameAddressBlock>
                                        <Phone >STRTYPE</Phone> <!-- optional -->
                                        <AltPhone >STRTYPE</AltPhone> <!-- optional -->
                                        <Fax >STRTYPE</Fax> <!-- optional -->
                                        <Email >STRTYPE</Email> <!-- optional -->
                                        <Contact >STRTYPE</Contact> <!-- optional -->
                                        <AltContact >STRTYPE</AltContact> <!-- optional -->
                                        <AccountNumber >STRTYPE</AccountNumber> <!-- optional -->
                                        <Notes >STRTYPE</Notes> <!-- optional -->
                                        <ExternalGUID >GUIDTYPE</ExternalGUID> <!-- optional -->
                                        <DataExtRet> <!-- optional, may repeat -->
                                                <OwnerID >GUIDTYPE</OwnerID> <!-- optional -->
                                                <DataExtName >STRTYPE</DataExtName> <!-- required -->
                                                <!-- DataExtType may have one of the following values: AMTTYPE, DATETIMETYPE, INTTYPE, PERCENTTYPE, PRICETYPE, QUANTYPE, STR1024TYPE, STR255TYPE -->
                                                <DataExtType >ENUMTYPE</DataExtType> <!-- required -->
                                                <DataExtValue >STRTYPE</DataExtValue> <!-- required -->
                                        </DataExtRet>
                                </OtherNameRet>
                        <!-- OR -->
                                <VendorRet> <!-- optional -->
                                        <ListID >IDTYPE</ListID> <!-- required -->
                                        <TimeCreated >DATETIMETYPE</TimeCreated> <!-- required -->
                                        <TimeModified >DATETIMETYPE</TimeModified> <!-- required -->
                                        <EditSequence >STRTYPE</EditSequence> <!-- required -->
                                        <Name >STRTYPE</Name> <!-- required -->
                                        <IsActive >BOOLTYPE</IsActive> <!-- optional -->
                                        <ClassRef> <!-- optional -->
                                                <ListID >IDTYPE</ListID> <!-- optional -->
                                                <FullName >STRTYPE</FullName> <!-- optional -->
                                        </ClassRef>
                                        <IsTaxAgency >BOOLTYPE</IsTaxAgency> <!-- optional -->
                                        <CompanyName >STRTYPE</CompanyName> <!-- optional -->
                                        <Salutation >STRTYPE</Salutation> <!-- optional -->
                                        <FirstName >STRTYPE</FirstName> <!-- optional -->
                                        <MiddleName >STRTYPE</MiddleName> <!-- optional -->
                                        <LastName >STRTYPE</LastName> <!-- optional -->
                                        <JobTitle >STRTYPE</JobTitle> <!-- optional -->
                                        <VendorAddress> <!-- optional -->
                                                <Addr1 >STRTYPE</Addr1> <!-- optional -->
                                                <Addr2 >STRTYPE</Addr2> <!-- optional -->
                                                <Addr3 >STRTYPE</Addr3> <!-- optional -->
                                                <Addr4 >STRTYPE</Addr4> <!-- optional -->
                                                <Addr5 >STRTYPE</Addr5> <!-- optional -->
                                                <City >STRTYPE</City> <!-- optional -->
                                                <State >STRTYPE</State> <!-- optional -->
                                                <PostalCode >STRTYPE</PostalCode> <!-- optional -->
                                                <Country >STRTYPE</Country> <!-- optional -->
                                                <Note >STRTYPE</Note> <!-- optional -->
                                        </VendorAddress>
                                        <VendorAddressBlock> <!-- optional -->
                                                <Addr1 >STRTYPE</Addr1> <!-- optional -->
                                                <Addr2 >STRTYPE</Addr2> <!-- optional -->
                                                <Addr3 >STRTYPE</Addr3> <!-- optional -->
                                                <Addr4 >STRTYPE</Addr4> <!-- optional -->
                                                <Addr5 >STRTYPE</Addr5> <!-- optional -->
                                        </VendorAddressBlock>
                                        <ShipAddress> <!-- optional -->
                                                <Addr1 >STRTYPE</Addr1> <!-- optional -->
                                                <Addr2 >STRTYPE</Addr2> <!-- optional -->
                                                <Addr3 >STRTYPE</Addr3> <!-- optional -->
                                                <Addr4 >STRTYPE</Addr4> <!-- optional -->
                                                <Addr5 >STRTYPE</Addr5> <!-- optional -->
                                                <City >STRTYPE</City> <!-- optional -->
                                                <State >STRTYPE</State> <!-- optional -->
                                                <PostalCode >STRTYPE</PostalCode> <!-- optional -->
                                                <Country >STRTYPE</Country> <!-- optional -->
                                                <Note >STRTYPE</Note> <!-- optional -->
                                        </ShipAddress>
                                        <Phone >STRTYPE</Phone> <!-- optional -->
                                        <AltPhone >STRTYPE</AltPhone> <!-- optional -->
                                        <Fax >STRTYPE</Fax> <!-- optional -->
                                        <Email >STRTYPE</Email> <!-- optional -->
                                        <Cc >STRTYPE</Cc> <!-- optional -->
                                        <Contact >STRTYPE</Contact> <!-- optional -->
                                        <AltContact >STRTYPE</AltContact> <!-- optional -->
                                        <AdditionalContactRef> <!-- must occur 0 - 8 times -->
                                                <ContactName >STRTYPE</ContactName> <!-- required -->
                                                <ContactValue >STRTYPE</ContactValue> <!-- required -->
                                        </AdditionalContactRef>
                                        <ContactsRet> <!-- optional, may repeat -->
                                                <ListID >IDTYPE</ListID> <!-- required -->
                                                <TimeCreated >DATETIMETYPE</TimeCreated> <!-- required -->
                                                <TimeModified >DATETIMETYPE</TimeModified> <!-- required -->
                                                <EditSequence >STRTYPE</EditSequence> <!-- required -->
                                                <Contact >STRTYPE</Contact> <!-- optional -->
                                                <Salutation >STRTYPE</Salutation> <!-- optional -->
                                                <FirstName >STRTYPE</FirstName> <!-- required -->
                                                <MiddleName >STRTYPE</MiddleName> <!-- optional -->
                                                <LastName >STRTYPE</LastName> <!-- optional -->
                                                <JobTitle >STRTYPE</JobTitle> <!-- optional -->
                                                <AdditionalContactRef> <!-- must occur 0 - 5 times -->
                                                        <ContactName >STRTYPE</ContactName> <!-- required -->
                                                        <ContactValue >STRTYPE</ContactValue> <!-- required -->
                                                </AdditionalContactRef>
                                        </ContactsRet>
                                        <NameOnCheck >STRTYPE</NameOnCheck> <!-- optional -->
                                        <AccountNumber >STRTYPE</AccountNumber> <!-- optional -->
                                        <Notes >STRTYPE</Notes> <!-- optional -->
                                        <AdditionalNotesRet> <!-- optional, may repeat -->
                                                <NoteID >INTTYPE</NoteID> <!-- required -->
                                                <Date >DATETYPE</Date> <!-- required -->
                                                <Note >STRTYPE</Note> <!-- required -->
                                        </AdditionalNotesRet>
                                        <VendorTypeRef> <!-- optional -->
                                                <ListID >IDTYPE</ListID> <!-- optional -->
                                                <FullName >STRTYPE</FullName> <!-- optional -->
                                        </VendorTypeRef>
                                        <TermsRef> <!-- optional -->
                                                <ListID >IDTYPE</ListID> <!-- optional -->
                                                <FullName >STRTYPE</FullName> <!-- optional -->
                                        </TermsRef>
                                        <CreditLimit >AMTTYPE</CreditLimit> <!-- optional -->
                                        <VendorTaxIdent >STRTYPE</VendorTaxIdent> <!-- optional -->
                                        <IsVendorEligibleFor1099 >BOOLTYPE</IsVendorEligibleFor1099> <!-- optional -->
                                        <Balance >AMTTYPE</Balance> <!-- optional -->
                                        <BillingRateRef> <!-- optional -->
                                                <ListID >IDTYPE</ListID> <!-- optional -->
                                                <FullName >STRTYPE</FullName> <!-- optional -->
                                        </BillingRateRef>
                                        <ExternalGUID >GUIDTYPE</ExternalGUID> <!-- optional -->
                                        <SalesTaxCodeRef> <!-- optional -->
                                                <ListID >IDTYPE</ListID> <!-- optional -->
                                                <FullName >STRTYPE</FullName> <!-- optional -->
                                        </SalesTaxCodeRef>
                                        <!-- SalesTaxCountry may have one of the following values: Australia, Canada [DEFAULT], UK, US -->
                                        <SalesTaxCountry >ENUMTYPE</SalesTaxCountry> <!-- optional -->
                                        <IsSalesTaxAgency >BOOLTYPE</IsSalesTaxAgency> <!-- optional -->
                                        <SalesTaxReturnRef> <!-- optional -->
                                                <ListID >IDTYPE</ListID> <!-- optional -->
                                                <FullName >STRTYPE</FullName> <!-- optional -->
                                        </SalesTaxReturnRef>
                                        <TaxRegistrationNumber >STRTYPE</TaxRegistrationNumber> <!-- optional -->
                                        <!-- ReportingPeriod may have one of the following values: Monthly, Quarterly [DEFAULT] -->
                                        <ReportingPeriod >ENUMTYPE</ReportingPeriod> <!-- optional -->
                                        <IsTaxTrackedOnPurchases >BOOLTYPE</IsTaxTrackedOnPurchases> <!-- optional -->
                                        <TaxOnPurchasesAccountRef> <!-- optional -->
                                                <ListID >IDTYPE</ListID> <!-- optional -->
                                                <FullName >STRTYPE</FullName> <!-- optional -->
                                        </TaxOnPurchasesAccountRef>
                                        <IsTaxTrackedOnSales >BOOLTYPE</IsTaxTrackedOnSales> <!-- optional -->
                                        <TaxOnSalesAccountRef> <!-- optional -->
                                                <ListID >IDTYPE</ListID> <!-- optional -->
                                                <FullName >STRTYPE</FullName> <!-- optional -->
                                        </TaxOnSalesAccountRef>
                                        <IsTaxOnTax >BOOLTYPE</IsTaxOnTax> <!-- optional -->
                                        <PrefillAccountRef> <!-- must occur 0 - 3 times -->
                                                <ListID >IDTYPE</ListID> <!-- optional -->
                                                <FullName >STRTYPE</FullName> <!-- optional -->
                                        </PrefillAccountRef>
                                        <CurrencyRef> <!-- optional -->
                                                <ListID >IDTYPE</ListID> <!-- optional -->
                                                <FullName >STRTYPE</FullName> <!-- optional -->
                                        </CurrencyRef>
                                        <DataExtRet> <!-- optional, may repeat -->
                                                <OwnerID >GUIDTYPE</OwnerID> <!-- optional -->
                                                <DataExtName >STRTYPE</DataExtName> <!-- required -->
                                                <!-- DataExtType may have one of the following values: AMTTYPE, DATETIMETYPE, INTTYPE, PERCENTTYPE, PRICETYPE, QUANTYPE, STR1024TYPE, STR255TYPE -->
                                                <DataExtType >ENUMTYPE</DataExtType> <!-- required -->
                                                <DataExtValue >STRTYPE</DataExtValue> <!-- required -->
                                        </DataExtRet>
                                </VendorRet>
                        <!-- END OR -->
                </EntityQueryRs>
        </QBXMLMsgsRq>
</QBXML>
```
## EstimateQuery
### XMLOps
```
<?xml version="1.0" encoding="utf-8"?>
<?qbxml version="16.0"?>
<QBXML>
        <QBXMLMsgsRq onError="stopOnError">
                <EstimateQueryRq metaData="ENUMTYPE" iterator="ENUMTYPE" iteratorID="UUIDTYPE">
                        <!-- BEGIN OR -->
                                <TxnID >IDTYPE</TxnID> <!-- optional, may repeat -->
                        <!-- OR -->
                                <RefNumber >STRTYPE</RefNumber> <!-- optional, may repeat -->
                        <!-- OR -->
                                <RefNumberCaseSensitive >STRTYPE</RefNumberCaseSensitive> <!-- optional, may repeat -->
                        <!-- OR -->
                                <MaxReturned >INTTYPE</MaxReturned> <!-- optional -->
                                <!-- BEGIN OR -->
                                        <ModifiedDateRangeFilter> <!-- optional -->
                                                <FromModifiedDate >DATETIMETYPE</FromModifiedDate> <!-- optional -->
                                                <ToModifiedDate >DATETIMETYPE</ToModifiedDate> <!-- optional -->
                                        </ModifiedDateRangeFilter>
                                <!-- OR -->
                                        <TxnDateRangeFilter> <!-- optional -->
                                                <!-- BEGIN OR -->
                                                        <FromTxnDate >DATETYPE</FromTxnDate> <!-- optional -->
                                                        <ToTxnDate >DATETYPE</ToTxnDate> <!-- optional -->
                                                <!-- OR -->
                                                        <!-- DateMacro may have one of the following values: All, Today, ThisWeek, ThisWeekToDate, ThisMonth, ThisMonthToDate, ThisCalendarQuarter, ThisCalendarQuarterToDate, ThisFiscalQuarter, ThisFiscalQuarterToDate, ThisCalendarYear, ThisCalendarYearToDate, ThisFiscalYear, ThisFiscalYearToDate, Yesterday, LastWeek, LastWeekToDate, LastMonth, LastMonthToDate, LastCalendarQuarter, LastCalendarQuarterToDate, LastFiscalQuarter, LastFiscalQuarterToDate, LastCalendarYear, LastCalendarYearToDate, LastFiscalYear, LastFiscalYearToDate, NextWeek, NextFourWeeks, NextMonth, NextCalendarQuarter, NextCalendarYear, NextFiscalQuarter, NextFiscalYear -->
                                                        <DateMacro >ENUMTYPE</DateMacro> <!-- optional -->
                                                <!-- END OR -->
                                        </TxnDateRangeFilter>
                                <!-- END OR -->
                                <EntityFilter> <!-- optional -->
                                        <!-- BEGIN OR -->
                                                <ListID >IDTYPE</ListID> <!-- optional, may repeat -->
                                        <!-- OR -->
                                                <FullName >STRTYPE</FullName> <!-- optional, may repeat -->
                                        <!-- OR -->
                                                <ListIDWithChildren >IDTYPE</ListIDWithChildren> <!-- optional -->
                                        <!-- OR -->
                                                <FullNameWithChildren >STRTYPE</FullNameWithChildren> <!-- optional -->
                                        <!-- END OR -->
                                </EntityFilter>
                                <AccountFilter> <!-- optional -->
                                        <!-- BEGIN OR -->
                                                <ListID >IDTYPE</ListID> <!-- optional, may repeat -->
                                        <!-- OR -->
                                                <FullName >STRTYPE</FullName> <!-- optional, may repeat -->
                                        <!-- OR -->
                                                <ListIDWithChildren >IDTYPE</ListIDWithChildren> <!-- optional -->
                                        <!-- OR -->
                                                <FullNameWithChildren >STRTYPE</FullNameWithChildren> <!-- optional -->
                                        <!-- END OR -->
                                </AccountFilter>
                                <!-- BEGIN OR -->
                                        <RefNumberFilter> <!-- optional -->
                                                <!-- MatchCriterion may have one of the following values: StartsWith, Contains, EndsWith -->
                                                <MatchCriterion >ENUMTYPE</MatchCriterion> <!-- required -->
                                                <RefNumber >STRTYPE</RefNumber> <!-- required -->
                                        </RefNumberFilter>
                                <!-- OR -->
                                        <RefNumberRangeFilter> <!-- optional -->
                                                <FromRefNumber >STRTYPE</FromRefNumber> <!-- optional -->
                                                <ToRefNumber >STRTYPE</ToRefNumber> <!-- optional -->
                                        </RefNumberRangeFilter>
                                <!-- END OR -->
                                <CurrencyFilter> <!-- optional -->
                                        <!-- BEGIN OR -->
                                                <ListID >IDTYPE</ListID> <!-- optional, may repeat -->
                                        <!-- OR -->
                                                <FullName >STRTYPE</FullName> <!-- optional, may repeat -->
                                        <!-- END OR -->
                                </CurrencyFilter>
                        <!-- END OR -->
                        <IncludeLineItems >BOOLTYPE</IncludeLineItems> <!-- optional -->
                        <IncludeLinkedTxns >BOOLTYPE</IncludeLinkedTxns> <!-- optional -->
                        <IncludeRetElement >STRTYPE</IncludeRetElement> <!-- optional, may repeat -->
                        <OwnerID >GUIDTYPE</OwnerID> <!-- optional, may repeat -->
                </EstimateQueryRq>

                <EstimateQueryRs statusCode="INTTYPE" statusSeverity="STRTYPE" statusMessage="STRTYPE" retCount="INTTYPE" iteratorRemainingCount="INTTYPE" iteratorID="UUIDTYPE">
                        <EstimateRet> <!-- optional, may repeat -->
                                <TxnID >IDTYPE</TxnID> <!-- required -->
                                <TimeCreated >DATETIMETYPE</TimeCreated> <!-- required -->
                                <TimeModified >DATETIMETYPE</TimeModified> <!-- required -->
                                <EditSequence >STRTYPE</EditSequence> <!-- required -->
                                <TxnNumber >INTTYPE</TxnNumber> <!-- optional -->
                                <CustomerRef> <!-- required -->
                                        <ListID >IDTYPE</ListID> <!-- optional -->
                                        <FullName >STRTYPE</FullName> <!-- optional -->
                                </CustomerRef>
                                <ClassRef> <!-- optional -->
                                        <ListID >IDTYPE</ListID> <!-- optional -->
                                        <FullName >STRTYPE</FullName> <!-- optional -->
                                </ClassRef>
                                <TemplateRef> <!-- optional -->
                                        <ListID >IDTYPE</ListID> <!-- optional -->
                                        <FullName >STRTYPE</FullName> <!-- optional -->
                                </TemplateRef>
                                <TxnDate >DATETYPE</TxnDate> <!-- required -->
                                <RefNumber >STRTYPE</RefNumber> <!-- optional -->
                                <BillAddress> <!-- optional -->
                                        <Addr1 >STRTYPE</Addr1> <!-- optional -->
                                        <Addr2 >STRTYPE</Addr2> <!-- optional -->
                                        <Addr3 >STRTYPE</Addr3> <!-- optional -->
                                        <Addr4 >STRTYPE</Addr4> <!-- optional -->
                                        <Addr5 >STRTYPE</Addr5> <!-- optional -->
                                        <City >STRTYPE</City> <!-- optional -->
                                        <State >STRTYPE</State> <!-- optional -->
                                        <PostalCode >STRTYPE</PostalCode> <!-- optional -->
                                        <Country >STRTYPE</Country> <!-- optional -->
                                        <Note >STRTYPE</Note> <!-- optional -->
                                </BillAddress>
                                <BillAddressBlock> <!-- optional -->
                                        <Addr1 >STRTYPE</Addr1> <!-- optional -->
                                        <Addr2 >STRTYPE</Addr2> <!-- optional -->
                                        <Addr3 >STRTYPE</Addr3> <!-- optional -->
                                        <Addr4 >STRTYPE</Addr4> <!-- optional -->
                                        <Addr5 >STRTYPE</Addr5> <!-- optional -->
                                </BillAddressBlock>
                                <ShipAddress> <!-- optional -->
                                        <Addr1 >STRTYPE</Addr1> <!-- optional -->
                                        <Addr2 >STRTYPE</Addr2> <!-- optional -->
                                        <Addr3 >STRTYPE</Addr3> <!-- optional -->
                                        <Addr4 >STRTYPE</Addr4> <!-- optional -->
                                        <Addr5 >STRTYPE</Addr5> <!-- optional -->
                                        <City >STRTYPE</City> <!-- optional -->
                                        <State >STRTYPE</State> <!-- optional -->
                                        <PostalCode >STRTYPE</PostalCode> <!-- optional -->
                                        <Country >STRTYPE</Country> <!-- optional -->
                                        <Note >STRTYPE</Note> <!-- optional -->
                                </ShipAddress>
                                <ShipAddressBlock> <!-- optional -->
                                        <Addr1 >STRTYPE</Addr1> <!-- optional -->
                                        <Addr2 >STRTYPE</Addr2> <!-- optional -->
                                        <Addr3 >STRTYPE</Addr3> <!-- optional -->
                                        <Addr4 >STRTYPE</Addr4> <!-- optional -->
                                        <Addr5 >STRTYPE</Addr5> <!-- optional -->
                                </ShipAddressBlock>
                                <IsActive >BOOLTYPE</IsActive> <!-- optional -->
                                <PONumber >STRTYPE</PONumber> <!-- optional -->
                                <TermsRef> <!-- optional -->
                                        <ListID >IDTYPE</ListID> <!-- optional -->
                                        <FullName >STRTYPE</FullName> <!-- optional -->
                                </TermsRef>
                                <DueDate >DATETYPE</DueDate> <!-- optional -->
                                <SalesRepRef> <!-- optional -->
                                        <ListID >IDTYPE</ListID> <!-- optional -->
                                        <FullName >STRTYPE</FullName> <!-- optional -->
                                </SalesRepRef>
                                <FOB >STRTYPE</FOB> <!-- optional -->
                                <Subtotal >AMTTYPE</Subtotal> <!-- optional -->
                                <ItemSalesTaxRef> <!-- optional -->
                                        <ListID >IDTYPE</ListID> <!-- optional -->
                                        <FullName >STRTYPE</FullName> <!-- optional -->
                                </ItemSalesTaxRef>
                                <SalesTaxPercentage >PERCENTTYPE</SalesTaxPercentage> <!-- optional -->
                                <SalesTaxTotal >AMTTYPE</SalesTaxTotal> <!-- optional -->
                                <TotalAmount >AMTTYPE</TotalAmount> <!-- optional -->
                                <CurrencyRef> <!-- optional -->
                                        <ListID >IDTYPE</ListID> <!-- optional -->
                                        <FullName >STRTYPE</FullName> <!-- optional -->
                                </CurrencyRef>
                                <ExchangeRate >FLOATTYPE</ExchangeRate> <!-- optional -->
                                <TotalAmountInHomeCurrency >AMTTYPE</TotalAmountInHomeCurrency> <!-- optional -->
                                <Memo >STRTYPE</Memo> <!-- optional -->
                                <CustomerMsgRef> <!-- optional -->
                                        <ListID >IDTYPE</ListID> <!-- optional -->
                                        <FullName >STRTYPE</FullName> <!-- optional -->
                                </CustomerMsgRef>
                                <IsToBeEmailed >BOOLTYPE</IsToBeEmailed> <!-- optional -->
                                <IsTaxIncluded >BOOLTYPE</IsTaxIncluded> <!-- optional -->
                                <CustomerSalesTaxCodeRef> <!-- optional -->
                                        <ListID >IDTYPE</ListID> <!-- optional -->
                                        <FullName >STRTYPE</FullName> <!-- optional -->
                                </CustomerSalesTaxCodeRef>
                                <Other >STRTYPE</Other> <!-- optional -->
                                <ExternalGUID >GUIDTYPE</ExternalGUID> <!-- optional -->
                                <LinkedTxn> <!-- optional, may repeat -->
                                        <TxnID >IDTYPE</TxnID> <!-- required -->
                                        <!-- TxnType may have one of the following values: ARRefundCreditCard, Bill, BillPaymentCheck, BillPaymentCreditCard, BuildAssembly, Charge, Check, CreditCardCharge, CreditCardCredit, CreditMemo, Deposit, Estimate, InventoryAdjustment, Invoice, ItemReceipt, JournalEntry, LiabilityAdjustment, Paycheck, PayrollLiabilityCheck, PurchaseOrder, ReceivePayment, SalesOrder, SalesReceipt, SalesTaxPaymentCheck, Transfer, VendorCredit, YTDAdjustment -->
                                        <TxnType >ENUMTYPE</TxnType> <!-- required -->
                                        <TxnDate >DATETYPE</TxnDate> <!-- required -->
                                        <RefNumber >STRTYPE</RefNumber> <!-- optional -->
                                        <!-- LinkType may have one of the following values: AMTTYPE, QUANTYPE -->
                                        <LinkType >ENUMTYPE</LinkType> <!-- optional -->
                                        <Amount >AMTTYPE</Amount> <!-- required -->
                                </LinkedTxn>
                                <!-- BEGIN OR -->
                                        <EstimateLineRet> <!-- optional -->
                                                <TxnLineID >IDTYPE</TxnLineID> <!-- required -->
                                                <ItemRef> <!-- optional -->
                                                        <ListID >IDTYPE</ListID> <!-- optional -->
                                                        <FullName >STRTYPE</FullName> <!-- optional -->
                                                </ItemRef>
                                                <Desc >STRTYPE</Desc> <!-- optional -->
                                                <Quantity >QUANTYPE</Quantity> <!-- optional -->
                                                <UnitOfMeasure >STRTYPE</UnitOfMeasure> <!-- optional -->
                                                <OverrideUOMSetRef> <!-- optional -->
                                                        <ListID >IDTYPE</ListID> <!-- optional -->
                                                        <FullName >STRTYPE</FullName> <!-- optional -->
                                                </OverrideUOMSetRef>
                                                <!-- BEGIN OR -->
                                                        <Rate >PRICETYPE</Rate> <!-- optional -->
                                                <!-- OR -->
                                                        <RatePercent >PERCENTTYPE</RatePercent> <!-- optional -->
                                                <!-- END OR -->
                                                <ClassRef> <!-- optional -->
                                                        <ListID >IDTYPE</ListID> <!-- optional -->
                                                        <FullName >STRTYPE</FullName> <!-- optional -->
                                                </ClassRef>
                                                <Amount >AMTTYPE</Amount> <!-- optional -->
                                                <InventorySiteRef> <!-- optional -->
                                                        <ListID >IDTYPE</ListID> <!-- optional -->
                                                        <FullName >STRTYPE</FullName> <!-- optional -->
                                                </InventorySiteRef>
                                                <InventorySiteLocationRef> <!-- optional -->
                                                        <ListID >IDTYPE</ListID> <!-- optional -->
                                                        <FullName >STRTYPE</FullName> <!-- optional -->
                                                </InventorySiteLocationRef>
                                                <SalesTaxCodeRef> <!-- optional -->
                                                        <ListID >IDTYPE</ListID> <!-- optional -->
                                                        <FullName >STRTYPE</FullName> <!-- optional -->
                                                </SalesTaxCodeRef>
                                                <!-- BEGIN OR -->
                                                        <MarkupRate >PRICETYPE</MarkupRate> <!-- optional -->
                                                <!-- OR -->
                                                        <MarkupRatePercent >PERCENTTYPE</MarkupRatePercent> <!-- optional -->
                                                <!-- END OR -->
                                                <Other1 >STRTYPE</Other1> <!-- optional -->
                                                <Other2 >STRTYPE</Other2> <!-- optional -->
                                                <DataExtRet> <!-- optional, may repeat -->
                                                        <OwnerID >GUIDTYPE</OwnerID> <!-- optional -->
                                                        <DataExtName >STRTYPE</DataExtName> <!-- required -->
                                                        <!-- DataExtType may have one of the following values: AMTTYPE, DATETIMETYPE, INTTYPE, PERCENTTYPE, PRICETYPE, QUANTYPE, STR1024TYPE, STR255TYPE -->
                                                        <DataExtType >ENUMTYPE</DataExtType> <!-- required -->
                                                        <DataExtValue >STRTYPE</DataExtValue> <!-- required -->
                                                </DataExtRet>
                                        </EstimateLineRet>
                                <!-- OR -->
                                        <EstimateLineGroupRet> <!-- optional -->
                                                <TxnLineID >IDTYPE</TxnLineID> <!-- required -->
                                                <ItemGroupRef> <!-- required -->
                                                        <ListID >IDTYPE</ListID> <!-- optional -->
                                                        <FullName >STRTYPE</FullName> <!-- optional -->
                                                </ItemGroupRef>
                                                <Desc >STRTYPE</Desc> <!-- optional -->
                                                <Quantity >QUANTYPE</Quantity> <!-- optional -->
                                                <UnitOfMeasure >STRTYPE</UnitOfMeasure> <!-- optional -->
                                                <OverrideUOMSetRef> <!-- optional -->
                                                        <ListID >IDTYPE</ListID> <!-- optional -->
                                                        <FullName >STRTYPE</FullName> <!-- optional -->
                                                </OverrideUOMSetRef>
                                                <IsPrintItemsInGroup >BOOLTYPE</IsPrintItemsInGroup> <!-- required -->
                                                <TotalAmount >AMTTYPE</TotalAmount> <!-- required -->
                                                <EstimateLineRet> <!-- optional, may repeat -->
                                                        <TxnLineID >IDTYPE</TxnLineID> <!-- required -->
                                                        <ItemRef> <!-- optional -->
                                                                <ListID >IDTYPE</ListID> <!-- optional -->
                                                                <FullName >STRTYPE</FullName> <!-- optional -->
                                                        </ItemRef>
                                                        <Desc >STRTYPE</Desc> <!-- optional -->
                                                        <Quantity >QUANTYPE</Quantity> <!-- optional -->
                                                        <UnitOfMeasure >STRTYPE</UnitOfMeasure> <!-- optional -->
                                                        <OverrideUOMSetRef> <!-- optional -->
                                                                <ListID >IDTYPE</ListID> <!-- optional -->
                                                                <FullName >STRTYPE</FullName> <!-- optional -->
                                                        </OverrideUOMSetRef>
                                                        <!-- BEGIN OR -->
                                                                <Rate >PRICETYPE</Rate> <!-- optional -->
                                                        <!-- OR -->
                                                                <RatePercent >PERCENTTYPE</RatePercent> <!-- optional -->
                                                        <!-- END OR -->
                                                        <ClassRef> <!-- optional -->
                                                                <ListID >IDTYPE</ListID> <!-- optional -->
                                                                <FullName >STRTYPE</FullName> <!-- optional -->
                                                        </ClassRef>
                                                        <Amount >AMTTYPE</Amount> <!-- optional -->
                                                        <InventorySiteRef> <!-- optional -->
                                                                <ListID >IDTYPE</ListID> <!-- optional -->
                                                                <FullName >STRTYPE</FullName> <!-- optional -->
                                                        </InventorySiteRef>
                                                        <InventorySiteLocationRef> <!-- optional -->
                                                                <ListID >IDTYPE</ListID> <!-- optional -->
                                                                <FullName >STRTYPE</FullName> <!-- optional -->
                                                        </InventorySiteLocationRef>
                                                        <SalesTaxCodeRef> <!-- optional -->
                                                                <ListID >IDTYPE</ListID> <!-- optional -->
                                                                <FullName >STRTYPE</FullName> <!-- optional -->
                                                        </SalesTaxCodeRef>
                                                        <!-- BEGIN OR -->
                                                                <MarkupRate >PRICETYPE</MarkupRate> <!-- optional -->
                                                        <!-- OR -->
                                                                <MarkupRatePercent >PERCENTTYPE</MarkupRatePercent> <!-- optional -->
                                                        <!-- END OR -->
                                                        <Other1 >STRTYPE</Other1> <!-- optional -->
                                                        <Other2 >STRTYPE</Other2> <!-- optional -->
                                                        <DataExtRet> <!-- optional, may repeat -->
                                                                <OwnerID >GUIDTYPE</OwnerID> <!-- optional -->
                                                                <DataExtName >STRTYPE</DataExtName> <!-- required -->
                                                                <!-- DataExtType may have one of the following values: AMTTYPE, DATETIMETYPE, INTTYPE, PERCENTTYPE, PRICETYPE, QUANTYPE, STR1024TYPE, STR255TYPE -->
                                                                <DataExtType >ENUMTYPE</DataExtType> <!-- required -->
                                                                <DataExtValue >STRTYPE</DataExtValue> <!-- required -->
                                                        </DataExtRet>
                                                </EstimateLineRet>
                                                <DataExtRet> <!-- optional, may repeat -->
                                                        <OwnerID >GUIDTYPE</OwnerID> <!-- optional -->
                                                        <DataExtName >STRTYPE</DataExtName> <!-- required -->
                                                        <!-- DataExtType may have one of the following values: AMTTYPE, DATETIMETYPE, INTTYPE, PERCENTTYPE, PRICETYPE, QUANTYPE, STR1024TYPE, STR255TYPE -->
                                                        <DataExtType >ENUMTYPE</DataExtType> <!-- required -->
                                                        <DataExtValue >STRTYPE</DataExtValue> <!-- required -->
                                                </DataExtRet>
                                        </EstimateLineGroupRet>
                                <!-- END OR -->
                                <DataExtRet> <!-- optional, may repeat -->
                                        <OwnerID >GUIDTYPE</OwnerID> <!-- optional -->
                                        <DataExtName >STRTYPE</DataExtName> <!-- required -->
                                        <!-- DataExtType may have one of the following values: AMTTYPE, DATETIMETYPE, INTTYPE, PERCENTTYPE, PRICETYPE, QUANTYPE, STR1024TYPE, STR255TYPE -->
                                        <DataExtType >ENUMTYPE</DataExtType> <!-- required -->
                                        <DataExtValue >STRTYPE</DataExtValue> <!-- required -->
                                </DataExtRet>
                        </EstimateRet>
                </EstimateQueryRs>
        </QBXMLMsgsRq>
</QBXML>
```

## HostQuery
### XMLOps
```
<?xml version="1.0" encoding="utf-8"?>
<?qbxml version="16.0"?>
<QBXML>
        <QBXMLMsgsRq onError="stopOnError">
                <HostQueryRq>
                        <IncludeListMetaData> <!-- optional -->
                                <IncludeMaxCapacity >BOOLTYPE</IncludeMaxCapacity> <!-- required -->
                        </IncludeListMetaData>
                        <IncludeRetElement >STRTYPE</IncludeRetElement> <!-- optional, may repeat -->
                </HostQueryRq>

                <HostQueryRs statusCode="INTTYPE" statusSeverity="STRTYPE" statusMessage="STRTYPE">
                        <HostRet> <!-- optional -->
                                <ProductName >STRTYPE</ProductName> <!-- required -->
                                <MajorVersion >STRTYPE</MajorVersion> <!-- required -->
                                <MinorVersion >STRTYPE</MinorVersion> <!-- required -->
                                <Country >STRTYPE</Country> <!-- optional -->
                                <SupportedQBXMLVersion >STRTYPE</SupportedQBXMLVersion> <!-- required, may repeat -->
                                <IsAutomaticLogin >BOOLTYPE</IsAutomaticLogin> <!-- optional -->
                                <!-- QBFileMode may have one of the following values: MultiUser, SingleUser -->
                                <QBFileMode >ENUMTYPE</QBFileMode> <!-- required -->
                                <ListMetaData> <!-- optional -->
                                        <AccountMetaData> <!-- required -->
                                                <MaxCapacity >INTTYPE</MaxCapacity> <!-- required -->
                                        </AccountMetaData>
                                        <BillingRateMetaData> <!-- required -->
                                                <MaxCapacity >INTTYPE</MaxCapacity> <!-- required -->
                                        </BillingRateMetaData>
                                        <ClassMetaData> <!-- required -->
                                                <MaxCapacity >INTTYPE</MaxCapacity> <!-- required -->
                                        </ClassMetaData>
                                        <CustomerMsgMetaData> <!-- required -->
                                                <MaxCapacity >INTTYPE</MaxCapacity> <!-- required -->
                                        </CustomerMsgMetaData>
                                        <CustomerTypeMetaData> <!-- required -->
                                                <MaxCapacity >INTTYPE</MaxCapacity> <!-- required -->
                                        </CustomerTypeMetaData>
                                        <EntityMetaData> <!-- required -->
                                                <MaxCapacity >INTTYPE</MaxCapacity> <!-- required -->
                                        </EntityMetaData>
                                        <ItemMetaData> <!-- required -->
                                                <MaxCapacity >INTTYPE</MaxCapacity> <!-- required -->
                                        </ItemMetaData>
                                        <JobTypeMetaData> <!-- required -->
                                                <MaxCapacity >INTTYPE</MaxCapacity> <!-- required -->
                                        </JobTypeMetaData>
                                        <PaymentMethodMetaData> <!-- required -->
                                                <MaxCapacity >INTTYPE</MaxCapacity> <!-- required -->
                                        </PaymentMethodMetaData>
                                        <PayrollItemMetaData> <!-- required -->
                                                <MaxCapacity >INTTYPE</MaxCapacity> <!-- required -->
                                        </PayrollItemMetaData>
                                        <PriceLevelMetaData> <!-- required -->
                                                <MaxCapacity >INTTYPE</MaxCapacity> <!-- required -->
                                        </PriceLevelMetaData>
                                        <SalesRepMetaData> <!-- required -->
                                                <MaxCapacity >INTTYPE</MaxCapacity> <!-- required -->
                                        </SalesRepMetaData>
                                        <SalesTaxCodeMetaData> <!-- required -->
                                                <MaxCapacity >INTTYPE</MaxCapacity> <!-- required -->
                                        </SalesTaxCodeMetaData>
                                        <ShipMethodMetaData> <!-- required -->
                                                <MaxCapacity >INTTYPE</MaxCapacity> <!-- required -->
                                        </ShipMethodMetaData>
                                        <TemplateMetaData> <!-- required -->
                                                <MaxCapacity >INTTYPE</MaxCapacity> <!-- required -->
                                        </TemplateMetaData>
                                        <TermsMetaData> <!-- required -->
                                                <MaxCapacity >INTTYPE</MaxCapacity> <!-- required -->
                                        </TermsMetaData>
                                        <ToDoMetaData> <!-- required -->
                                                <MaxCapacity >INTTYPE</MaxCapacity> <!-- required -->
                                        </ToDoMetaData>
                                        <VehicleMetaData> <!-- required -->
                                                <MaxCapacity >INTTYPE</MaxCapacity> <!-- required -->
                                        </VehicleMetaData>
                                        <VendorTypeMetaData> <!-- required -->
                                                <MaxCapacity >INTTYPE</MaxCapacity> <!-- required -->
                                        </VendorTypeMetaData>
                                </ListMetaData>
                        </HostRet>
                </HostQueryRs>
        </QBXMLMsgsRq>
</QBXML>
```
## InventorySiteQuery
### XMLOps
```
<?xml version="1.0" encoding="utf-8"?>
<?qbxml version="16.0"?>
<QBXML>
        <QBXMLMsgsRq onError="stopOnError">
                <InventorySiteQueryRq metaData="ENUMTYPE">
                        <!-- BEGIN OR -->
                                <ListID >IDTYPE</ListID> <!-- optional, may repeat -->
                        <!-- OR -->
                                <FullName >STRTYPE</FullName> <!-- optional, may repeat -->
                        <!-- OR -->
                                <!-- ActiveStatus may have one of the following values: ActiveOnly [DEFAULT], InactiveOnly, All -->
                                <ActiveStatus >ENUMTYPE</ActiveStatus> <!-- optional -->
                                <FromModifiedDate >DATETIMETYPE</FromModifiedDate> <!-- optional -->
                                <ToModifiedDate >DATETIMETYPE</ToModifiedDate> <!-- optional -->
                                <!-- BEGIN OR -->
                                        <NameFilter> <!-- optional -->
                                                <!-- MatchCriterion may have one of the following values: StartsWith, Contains, EndsWith -->
                                                <MatchCriterion >ENUMTYPE</MatchCriterion> <!-- required -->
                                                <Name >STRTYPE</Name> <!-- required -->
                                        </NameFilter>
                                <!-- OR -->
                                        <NameRangeFilter> <!-- optional -->
                                                <FromName >STRTYPE</FromName> <!-- optional -->
                                                <ToName >STRTYPE</ToName> <!-- optional -->
                                        </NameRangeFilter>
                                <!-- END OR -->
                        <!-- END OR -->
                        <IncludeRetElement >STRTYPE</IncludeRetElement> <!-- optional, may repeat -->
                </InventorySiteQueryRq>

                <InventorySiteQueryRs statusCode="INTTYPE" statusSeverity="STRTYPE" statusMessage="STRTYPE" retCount="INTTYPE">
                        <InventorySiteRet> <!-- optional, may repeat -->
                                <ListID >IDTYPE</ListID> <!-- required -->
                                <TimeCreated >DATETIMETYPE</TimeCreated> <!-- required -->
                                <TimeModified >DATETIMETYPE</TimeModified> <!-- required -->
                                <EditSequence >STRTYPE</EditSequence> <!-- required -->
                                <Name >STRTYPE</Name> <!-- optional -->
                                <IsActive >BOOLTYPE</IsActive> <!-- optional -->
                                <ParentSiteRef> <!-- optional -->
                                        <ListID >IDTYPE</ListID> <!-- optional -->
                                        <FullName >STRTYPE</FullName> <!-- optional -->
                                </ParentSiteRef>
                                <IsDefaultSite >BOOLTYPE</IsDefaultSite> <!-- optional -->
                                <SiteDesc >STRTYPE</SiteDesc> <!-- optional -->
                                <Contact >STRTYPE</Contact> <!-- optional -->
                                <Phone >STRTYPE</Phone> <!-- optional -->
                                <Fax >STRTYPE</Fax> <!-- optional -->
                                <Email >STRTYPE</Email> <!-- optional -->
                                <SiteAddress> <!-- optional -->
                                        <Addr1 >STRTYPE</Addr1> <!-- optional -->
                                        <Addr2 >STRTYPE</Addr2> <!-- optional -->
                                        <Addr3 >STRTYPE</Addr3> <!-- optional -->
                                        <Addr4 >STRTYPE</Addr4> <!-- optional -->
                                        <Addr5 >STRTYPE</Addr5> <!-- optional -->
                                        <City >STRTYPE</City> <!-- optional -->
                                        <State >STRTYPE</State> <!-- optional -->
                                        <PostalCode >STRTYPE</PostalCode> <!-- optional -->
                                        <Country >STRTYPE</Country> <!-- optional -->
                                </SiteAddress>
                                <SiteAddressBlock> <!-- optional -->
                                        <Addr1 >STRTYPE</Addr1> <!-- optional -->
                                        <Addr2 >STRTYPE</Addr2> <!-- optional -->
                                        <Addr3 >STRTYPE</Addr3> <!-- optional -->
                                        <Addr4 >STRTYPE</Addr4> <!-- optional -->
                                        <Addr5 >STRTYPE</Addr5> <!-- optional -->
                                </SiteAddressBlock>
                        </InventorySiteRet>
                </InventorySiteQueryRs>
        </QBXMLMsgsRq>
</QBXML>
```
## InvoiceQuery
### XMLOps
```
<?xml version="1.0" encoding="utf-8"?>
<?qbxml version="16.0"?>
<QBXML>
        <QBXMLMsgsRq onError="stopOnError">
                <InvoiceQueryRq metaData="ENUMTYPE" iterator="ENUMTYPE" iteratorID="UUIDTYPE">
                        <!-- BEGIN OR -->
                                <TxnID >IDTYPE</TxnID> <!-- optional, may repeat -->
                        <!-- OR -->
                                <RefNumber >STRTYPE</RefNumber> <!-- optional, may repeat -->
                        <!-- OR -->
                                <RefNumberCaseSensitive >STRTYPE</RefNumberCaseSensitive> <!-- optional, may repeat -->
                        <!-- OR -->
                                <MaxReturned >INTTYPE</MaxReturned> <!-- optional -->
                                <!-- BEGIN OR -->
                                        <ModifiedDateRangeFilter> <!-- optional -->
                                                <FromModifiedDate >DATETIMETYPE</FromModifiedDate> <!-- optional -->
                                                <ToModifiedDate >DATETIMETYPE</ToModifiedDate> <!-- optional -->
                                        </ModifiedDateRangeFilter>
                                <!-- OR -->
                                        <TxnDateRangeFilter> <!-- optional -->
                                                <!-- BEGIN OR -->
                                                        <FromTxnDate >DATETYPE</FromTxnDate> <!-- optional -->
                                                        <ToTxnDate >DATETYPE</ToTxnDate> <!-- optional -->
                                                <!-- OR -->
                                                        <!-- DateMacro may have one of the following values: All, Today, ThisWeek, ThisWeekToDate, ThisMonth, ThisMonthToDate, ThisCalendarQuarter, ThisCalendarQuarterToDate, ThisFiscalQuarter, ThisFiscalQuarterToDate, ThisCalendarYear, ThisCalendarYearToDate, ThisFiscalYear, ThisFiscalYearToDate, Yesterday, LastWeek, LastWeekToDate, LastMonth, LastMonthToDate, LastCalendarQuarter, LastCalendarQuarterToDate, LastFiscalQuarter, LastFiscalQuarterToDate, LastCalendarYear, LastCalendarYearToDate, LastFiscalYear, LastFiscalYearToDate, NextWeek, NextFourWeeks, NextMonth, NextCalendarQuarter, NextCalendarYear, NextFiscalQuarter, NextFiscalYear -->
                                                        <DateMacro >ENUMTYPE</DateMacro> <!-- optional -->
                                                <!-- END OR -->
                                        </TxnDateRangeFilter>
                                <!-- END OR -->
                                <EntityFilter> <!-- optional -->
                                        <!-- BEGIN OR -->
                                                <ListID >IDTYPE</ListID> <!-- optional, may repeat -->
                                        <!-- OR -->
                                                <FullName >STRTYPE</FullName> <!-- optional, may repeat -->
                                        <!-- OR -->
                                                <ListIDWithChildren >IDTYPE</ListIDWithChildren> <!-- optional -->
                                        <!-- OR -->
                                                <FullNameWithChildren >STRTYPE</FullNameWithChildren> <!-- optional -->
                                        <!-- END OR -->
                                </EntityFilter>
                                <AccountFilter> <!-- optional -->
                                        <!-- BEGIN OR -->
                                                <ListID >IDTYPE</ListID> <!-- optional, may repeat -->
                                        <!-- OR -->
                                                <FullName >STRTYPE</FullName> <!-- optional, may repeat -->
                                        <!-- OR -->
                                                <ListIDWithChildren >IDTYPE</ListIDWithChildren> <!-- optional -->
                                        <!-- OR -->
                                                <FullNameWithChildren >STRTYPE</FullNameWithChildren> <!-- optional -->
                                        <!-- END OR -->
                                </AccountFilter>
                                <!-- BEGIN OR -->
                                        <RefNumberFilter> <!-- optional -->
                                                <!-- MatchCriterion may have one of the following values: StartsWith, Contains, EndsWith -->
                                                <MatchCriterion >ENUMTYPE</MatchCriterion> <!-- required -->
                                                <RefNumber >STRTYPE</RefNumber> <!-- required -->
                                        </RefNumberFilter>
                                <!-- OR -->
                                        <RefNumberRangeFilter> <!-- optional -->
                                                <FromRefNumber >STRTYPE</FromRefNumber> <!-- optional -->
                                                <ToRefNumber >STRTYPE</ToRefNumber> <!-- optional -->
                                        </RefNumberRangeFilter>
                                <!-- END OR -->
                                <CurrencyFilter> <!-- optional -->
                                        <!-- BEGIN OR -->
                                                <ListID >IDTYPE</ListID> <!-- optional, may repeat -->
                                        <!-- OR -->
                                                <FullName >STRTYPE</FullName> <!-- optional, may repeat -->
                                        <!-- END OR -->
                                </CurrencyFilter>
                                <!-- PaidStatus may have one of the following values: All [DEFAULT], PaidOnly, NotPaidOnly -->
                                <PaidStatus >ENUMTYPE</PaidStatus> <!-- optional -->
                        <!-- END OR -->
                        <IncludeLineItems >BOOLTYPE</IncludeLineItems> <!-- optional -->
                        <IncludeLinkedTxns >BOOLTYPE</IncludeLinkedTxns> <!-- optional -->
                        <IncludeRetElement >STRTYPE</IncludeRetElement> <!-- optional, may repeat -->
                        <OwnerID >GUIDTYPE</OwnerID> <!-- optional, may repeat -->
                </InvoiceQueryRq>

                <InvoiceQueryRs statusCode="INTTYPE" statusSeverity="STRTYPE" statusMessage="STRTYPE" retCount="INTTYPE" iteratorRemainingCount="INTTYPE" iteratorID="UUIDTYPE">
                        <InvoiceRet> <!-- optional, may repeat -->
                                <TxnID >IDTYPE</TxnID> <!-- required -->
                                <TimeCreated >DATETIMETYPE</TimeCreated> <!-- required -->
                                <TimeModified >DATETIMETYPE</TimeModified> <!-- required -->
                                <EditSequence >STRTYPE</EditSequence> <!-- required -->
                                <TxnNumber >INTTYPE</TxnNumber> <!-- optional -->
                                <CustomerRef> <!-- required -->
                                        <ListID >IDTYPE</ListID> <!-- optional -->
                                        <FullName >STRTYPE</FullName> <!-- optional -->
                                </CustomerRef>
                                <ClassRef> <!-- optional -->
                                        <ListID >IDTYPE</ListID> <!-- optional -->
                                        <FullName >STRTYPE</FullName> <!-- optional -->
                                </ClassRef>
                                <ARAccountRef> <!-- optional -->
                                        <ListID >IDTYPE</ListID> <!-- optional -->
                                        <FullName >STRTYPE</FullName> <!-- optional -->
                                </ARAccountRef>
                                <TemplateRef> <!-- optional -->
                                        <ListID >IDTYPE</ListID> <!-- optional -->
                                        <FullName >STRTYPE</FullName> <!-- optional -->
                                </TemplateRef>
                                <TxnDate >DATETYPE</TxnDate> <!-- required -->
                                <RefNumber >STRTYPE</RefNumber> <!-- optional -->
                                <BillAddress> <!-- optional -->
                                        <Addr1 >STRTYPE</Addr1> <!-- optional -->
                                        <Addr2 >STRTYPE</Addr2> <!-- optional -->
                                        <Addr3 >STRTYPE</Addr3> <!-- optional -->
                                        <Addr4 >STRTYPE</Addr4> <!-- optional -->
                                        <Addr5 >STRTYPE</Addr5> <!-- optional -->
                                        <City >STRTYPE</City> <!-- optional -->
                                        <State >STRTYPE</State> <!-- optional -->
                                        <PostalCode >STRTYPE</PostalCode> <!-- optional -->
                                        <Country >STRTYPE</Country> <!-- optional -->
                                        <Note >STRTYPE</Note> <!-- optional -->
                                </BillAddress>
                                <BillAddressBlock> <!-- optional -->
                                        <Addr1 >STRTYPE</Addr1> <!-- optional -->
                                        <Addr2 >STRTYPE</Addr2> <!-- optional -->
                                        <Addr3 >STRTYPE</Addr3> <!-- optional -->
                                        <Addr4 >STRTYPE</Addr4> <!-- optional -->
                                        <Addr5 >STRTYPE</Addr5> <!-- optional -->
                                </BillAddressBlock>
                                <ShipAddress> <!-- optional -->
                                        <Addr1 >STRTYPE</Addr1> <!-- optional -->
                                        <Addr2 >STRTYPE</Addr2> <!-- optional -->
                                        <Addr3 >STRTYPE</Addr3> <!-- optional -->
                                        <Addr4 >STRTYPE</Addr4> <!-- optional -->
                                        <Addr5 >STRTYPE</Addr5> <!-- optional -->
                                        <City >STRTYPE</City> <!-- optional -->
                                        <State >STRTYPE</State> <!-- optional -->
                                        <PostalCode >STRTYPE</PostalCode> <!-- optional -->
                                        <Country >STRTYPE</Country> <!-- optional -->
                                        <Note >STRTYPE</Note> <!-- optional -->
                                </ShipAddress>
                                <ShipAddressBlock> <!-- optional -->
                                        <Addr1 >STRTYPE</Addr1> <!-- optional -->
                                        <Addr2 >STRTYPE</Addr2> <!-- optional -->
                                        <Addr3 >STRTYPE</Addr3> <!-- optional -->
                                        <Addr4 >STRTYPE</Addr4> <!-- optional -->
                                        <Addr5 >STRTYPE</Addr5> <!-- optional -->
                                </ShipAddressBlock>
                                <IsPending >BOOLTYPE</IsPending> <!-- optional -->
                                <IsFinanceCharge >BOOLTYPE</IsFinanceCharge> <!-- optional -->
                                <PONumber >STRTYPE</PONumber> <!-- optional -->
                                <TermsRef> <!-- optional -->
                                        <ListID >IDTYPE</ListID> <!-- optional -->
                                        <FullName >STRTYPE</FullName> <!-- optional -->
                                </TermsRef>
                                <DueDate >DATETYPE</DueDate> <!-- optional -->
                                <SalesRepRef> <!-- optional -->
                                        <ListID >IDTYPE</ListID> <!-- optional -->
                                        <FullName >STRTYPE</FullName> <!-- optional -->
                                </SalesRepRef>
                                <FOB >STRTYPE</FOB> <!-- optional -->
                                <ShipDate >DATETYPE</ShipDate> <!-- optional -->
                                <ShipMethodRef> <!-- optional -->
                                        <ListID >IDTYPE</ListID> <!-- optional -->
                                        <FullName >STRTYPE</FullName> <!-- optional -->
                                </ShipMethodRef>
                                <Subtotal >AMTTYPE</Subtotal> <!-- optional -->
                                <ItemSalesTaxRef> <!-- optional -->
                                        <ListID >IDTYPE</ListID> <!-- optional -->
                                        <FullName >STRTYPE</FullName> <!-- optional -->
                                </ItemSalesTaxRef>
                                <SalesTaxPercentage >PERCENTTYPE</SalesTaxPercentage> <!-- optional -->
                                <SalesTaxTotal >AMTTYPE</SalesTaxTotal> <!-- optional -->
                                <AppliedAmount >AMTTYPE</AppliedAmount> <!-- optional -->
                                <BalanceRemaining >AMTTYPE</BalanceRemaining> <!-- optional -->
                                <CurrencyRef> <!-- optional -->
                                        <ListID >IDTYPE</ListID> <!-- optional -->
                                        <FullName >STRTYPE</FullName> <!-- optional -->
                                </CurrencyRef>
                                <ExchangeRate >FLOATTYPE</ExchangeRate> <!-- optional -->
                                <BalanceRemainingInHomeCurrency >AMTTYPE</BalanceRemainingInHomeCurrency> <!-- optional -->
                                <Memo >STRTYPE</Memo> <!-- optional -->
                                <IsPaid >BOOLTYPE</IsPaid> <!-- optional -->
                                <CustomerMsgRef> <!-- optional -->
                                        <ListID >IDTYPE</ListID> <!-- optional -->
                                        <FullName >STRTYPE</FullName> <!-- optional -->
                                </CustomerMsgRef>
                                <IsToBePrinted >BOOLTYPE</IsToBePrinted> <!-- optional -->
                                <IsToBeEmailed >BOOLTYPE</IsToBeEmailed> <!-- optional -->
                                <IsTaxIncluded >BOOLTYPE</IsTaxIncluded> <!-- optional -->
                                <CustomerSalesTaxCodeRef> <!-- optional -->
                                        <ListID >IDTYPE</ListID> <!-- optional -->
                                        <FullName >STRTYPE</FullName> <!-- optional -->
                                </CustomerSalesTaxCodeRef>
                                <SuggestedDiscountAmount >AMTTYPE</SuggestedDiscountAmount> <!-- optional -->
                                <SuggestedDiscountDate >DATETYPE</SuggestedDiscountDate> <!-- optional -->
                                <Other >STRTYPE</Other> <!-- optional -->
                                <ExternalGUID >GUIDTYPE</ExternalGUID> <!-- optional -->
                                <LinkedTxn> <!-- optional, may repeat -->
                                        <TxnID >IDTYPE</TxnID> <!-- required -->
                                        <!-- TxnType may have one of the following values: ARRefundCreditCard, Bill, BillPaymentCheck, BillPaymentCreditCard, BuildAssembly, Charge, Check, CreditCardCharge, CreditCardCredit, CreditMemo, Deposit, Estimate, InventoryAdjustment, Invoice, ItemReceipt, JournalEntry, LiabilityAdjustment, Paycheck, PayrollLiabilityCheck, PurchaseOrder, ReceivePayment, SalesOrder, SalesReceipt, SalesTaxPaymentCheck, Transfer, VendorCredit, YTDAdjustment -->
                                        <TxnType >ENUMTYPE</TxnType> <!-- required -->
                                        <TxnDate >DATETYPE</TxnDate> <!-- required -->
                                        <RefNumber >STRTYPE</RefNumber> <!-- optional -->
                                        <!-- LinkType may have one of the following values: AMTTYPE, QUANTYPE -->
                                        <LinkType >ENUMTYPE</LinkType> <!-- optional -->
                                        <Amount >AMTTYPE</Amount> <!-- required -->
                                </LinkedTxn>
                                <!-- BEGIN OR -->
                                        <InvoiceLineRet> <!-- optional -->
                                                <TxnLineID >IDTYPE</TxnLineID> <!-- required -->
                                                <ItemRef> <!-- optional -->
                                                        <ListID >IDTYPE</ListID> <!-- optional -->
                                                        <FullName >STRTYPE</FullName> <!-- optional -->
                                                </ItemRef>
                                                <Desc >STRTYPE</Desc> <!-- optional -->
                                                <Quantity >QUANTYPE</Quantity> <!-- optional -->
                                                <UnitOfMeasure >STRTYPE</UnitOfMeasure> <!-- optional -->
                                                <OverrideUOMSetRef> <!-- optional -->
                                                        <ListID >IDTYPE</ListID> <!-- optional -->
                                                        <FullName >STRTYPE</FullName> <!-- optional -->
                                                </OverrideUOMSetRef>
                                                <!-- BEGIN OR -->
                                                        <Rate >PRICETYPE</Rate> <!-- optional -->
                                                <!-- OR -->
                                                        <RatePercent >PERCENTTYPE</RatePercent> <!-- optional -->
                                                <!-- END OR -->
                                                <ClassRef> <!-- optional -->
                                                        <ListID >IDTYPE</ListID> <!-- optional -->
                                                        <FullName >STRTYPE</FullName> <!-- optional -->
                                                </ClassRef>
                                                <Amount >AMTTYPE</Amount> <!-- optional -->
                                                <InventorySiteRef> <!-- optional -->
                                                        <ListID >IDTYPE</ListID> <!-- optional -->
                                                        <FullName >STRTYPE</FullName> <!-- optional -->
                                                </InventorySiteRef>
                                                <InventorySiteLocationRef> <!-- optional -->
                                                        <ListID >IDTYPE</ListID> <!-- optional -->
                                                        <FullName >STRTYPE</FullName> <!-- optional -->
                                                </InventorySiteLocationRef>
                                                <!-- BEGIN OR -->
                                                        <SerialNumber >STRTYPE</SerialNumber> <!-- optional -->
                                                <!-- OR -->
                                                        <LotNumber >STRTYPE</LotNumber> <!-- optional -->
                                                <!-- END OR -->
                                                <ExpirationDateForSerialLotNumber>STRTYPE</ExpirationDateForSerialLotNumber> <!-- optional -->
                                                <ServiceDate >DATETYPE</ServiceDate> <!-- optional -->
                                                <SalesTaxCodeRef> <!-- optional -->
                                                        <ListID >IDTYPE</ListID> <!-- optional -->
                                                        <FullName >STRTYPE</FullName> <!-- optional -->
                                                </SalesTaxCodeRef>
                                                <Other1 >STRTYPE</Other1> <!-- optional -->
                                                <Other2 >STRTYPE</Other2> <!-- optional -->
                                                <DataExtRet> <!-- optional, may repeat -->
                                                        <OwnerID >GUIDTYPE</OwnerID> <!-- optional -->
                                                        <DataExtName >STRTYPE</DataExtName> <!-- required -->
                                                        <!-- DataExtType may have one of the following values: AMTTYPE, DATETIMETYPE, INTTYPE, PERCENTTYPE, PRICETYPE, QUANTYPE, STR1024TYPE, STR255TYPE -->
                                                        <DataExtType >ENUMTYPE</DataExtType> <!-- required -->
                                                        <DataExtValue >STRTYPE</DataExtValue> <!-- required -->
                                                </DataExtRet>
                                        </InvoiceLineRet>
                                <!-- OR -->
                                        <InvoiceLineGroupRet> <!-- optional -->
                                                <TxnLineID >IDTYPE</TxnLineID> <!-- required -->
                                                <ItemGroupRef> <!-- required -->
                                                        <ListID >IDTYPE</ListID> <!-- optional -->
                                                        <FullName >STRTYPE</FullName> <!-- optional -->
                                                </ItemGroupRef>
                                                <Desc >STRTYPE</Desc> <!-- optional -->
                                                <Quantity >QUANTYPE</Quantity> <!-- optional -->
                                                <UnitOfMeasure >STRTYPE</UnitOfMeasure> <!-- optional -->
                                                <OverrideUOMSetRef> <!-- optional -->
                                                        <ListID >IDTYPE</ListID> <!-- optional -->
                                                        <FullName >STRTYPE</FullName> <!-- optional -->
                                                </OverrideUOMSetRef>
                                                <IsPrintItemsInGroup >BOOLTYPE</IsPrintItemsInGroup> <!-- required -->
                                                <TotalAmount >AMTTYPE</TotalAmount> <!-- required -->
                                                <InvoiceLineRet> <!-- optional, may repeat -->
                                                        <TxnLineID >IDTYPE</TxnLineID> <!-- required -->
                                                        <ItemRef> <!-- optional -->
                                                                <ListID >IDTYPE</ListID> <!-- optional -->
                                                                <FullName >STRTYPE</FullName> <!-- optional -->
                                                        </ItemRef>
                                                        <Desc >STRTYPE</Desc> <!-- optional -->
                                                        <Quantity >QUANTYPE</Quantity> <!-- optional -->
                                                        <UnitOfMeasure >STRTYPE</UnitOfMeasure> <!-- optional -->
                                                        <OverrideUOMSetRef> <!-- optional -->
                                                                <ListID >IDTYPE</ListID> <!-- optional -->
                                                                <FullName >STRTYPE</FullName> <!-- optional -->
                                                        </OverrideUOMSetRef>
                                                        <!-- BEGIN OR -->
                                                                <Rate >PRICETYPE</Rate> <!-- optional -->
                                                        <!-- OR -->
                                                                <RatePercent >PERCENTTYPE</RatePercent> <!-- optional -->
                                                        <!-- END OR -->
                                                        <ClassRef> <!-- optional -->
                                                                <ListID >IDTYPE</ListID> <!-- optional -->
                                                                <FullName >STRTYPE</FullName> <!-- optional -->
                                                        </ClassRef>
                                                        <Amount >AMTTYPE</Amount> <!-- optional -->
                                                        <InventorySiteRef> <!-- optional -->
                                                                <ListID >IDTYPE</ListID> <!-- optional -->
                                                                <FullName >STRTYPE</FullName> <!-- optional -->
                                                        </InventorySiteRef>
                                                        <InventorySiteLocationRef> <!-- optional -->
                                                                <ListID >IDTYPE</ListID> <!-- optional -->
                                                                <FullName >STRTYPE</FullName> <!-- optional -->
                                                        </InventorySiteLocationRef>
                                                        <!-- BEGIN OR -->
                                                                <SerialNumber >STRTYPE</SerialNumber> <!-- optional -->
                                                        <!-- OR -->
                                                                <LotNumber >STRTYPE</LotNumber> <!-- optional -->
                                                        <!-- END OR -->
                                                        <ExpirationDateForSerialLotNumber>STRTYPE</ExpirationDateForSerialLotNumber> <!-- optional -->
                                                        <ServiceDate >DATETYPE</ServiceDate> <!-- optional -->
                                                        <SalesTaxCodeRef> <!-- optional -->
                                                                <ListID >IDTYPE</ListID> <!-- optional -->
                                                                <FullName >STRTYPE</FullName> <!-- optional -->
                                                        </SalesTaxCodeRef>
                                                        <Other1 >STRTYPE</Other1> <!-- optional -->
                                                        <Other2 >STRTYPE</Other2> <!-- optional -->
                                                        <DataExtRet> <!-- optional, may repeat -->
                                                                <OwnerID >GUIDTYPE</OwnerID> <!-- optional -->
                                                                <DataExtName >STRTYPE</DataExtName> <!-- required -->
                                                                <!-- DataExtType may have one of the following values: AMTTYPE, DATETIMETYPE, INTTYPE, PERCENTTYPE, PRICETYPE, QUANTYPE, STR1024TYPE, STR255TYPE -->
                                                                <DataExtType >ENUMTYPE</DataExtType> <!-- required -->
                                                                <DataExtValue >STRTYPE</DataExtValue> <!-- required -->
                                                        </DataExtRet>
                                                </InvoiceLineRet>
                                                <DataExtRet> <!-- optional, may repeat -->
                                                        <OwnerID >GUIDTYPE</OwnerID> <!-- optional -->
                                                        <DataExtName >STRTYPE</DataExtName> <!-- required -->
                                                        <!-- DataExtType may have one of the following values: AMTTYPE, DATETIMETYPE, INTTYPE, PERCENTTYPE, PRICETYPE, QUANTYPE, STR1024TYPE, STR255TYPE -->
                                                        <DataExtType >ENUMTYPE</DataExtType> <!-- required -->
                                                        <DataExtValue >STRTYPE</DataExtValue> <!-- required -->
                                                </DataExtRet>
                                        </InvoiceLineGroupRet>
                                <!-- END OR -->
                                <DataExtRet> <!-- optional, may repeat -->
                                        <OwnerID >GUIDTYPE</OwnerID> <!-- optional -->
                                        <DataExtName >STRTYPE</DataExtName> <!-- required -->
                                        <!-- DataExtType may have one of the following values: AMTTYPE, DATETIMETYPE, INTTYPE, PERCENTTYPE, PRICETYPE, QUANTYPE, STR1024TYPE, STR255TYPE -->
                                        <DataExtType >ENUMTYPE</DataExtType> <!-- required -->
                                        <DataExtValue >STRTYPE</DataExtValue> <!-- required -->
                                </DataExtRet>
                        </InvoiceRet>
                </InvoiceQueryRs>
        </QBXMLMsgsRq>
</QBXML>
```
## ItemDiscountQuery
### XMLOps
```
<?xml version="1.0" encoding="utf-8"?>
<?qbxml version="16.0"?>
<QBXML>
        <QBXMLMsgsRq onError="stopOnError">
                <ItemDiscountQueryRq metaData="ENUMTYPE" iterator="ENUMTYPE" iteratorID="UUIDTYPE">
                        <!-- BEGIN OR -->
                                <ListID >IDTYPE</ListID> <!-- optional, may repeat -->
                        <!-- OR -->
                                <FullName >STRTYPE</FullName> <!-- optional, may repeat -->
                        <!-- OR -->
                                <MaxReturned >INTTYPE</MaxReturned> <!-- optional -->
                                <!-- ActiveStatus may have one of the following values: ActiveOnly [DEFAULT], InactiveOnly, All -->
                                <ActiveStatus >ENUMTYPE</ActiveStatus> <!-- optional -->
                                <FromModifiedDate >DATETIMETYPE</FromModifiedDate> <!-- optional -->
                                <ToModifiedDate >DATETIMETYPE</ToModifiedDate> <!-- optional -->
                                <!-- BEGIN OR -->
                                        <NameFilter> <!-- optional -->
                                                <!-- MatchCriterion may have one of the following values: StartsWith, Contains, EndsWith -->
                                                <MatchCriterion >ENUMTYPE</MatchCriterion> <!-- required -->
                                                <Name >STRTYPE</Name> <!-- required -->
                                        </NameFilter>
                                <!-- OR -->
                                        <NameRangeFilter> <!-- optional -->
                                                <FromName >STRTYPE</FromName> <!-- optional -->
                                                <ToName >STRTYPE</ToName> <!-- optional -->
                                        </NameRangeFilter>
                                <!-- END OR -->
                                <ClassFilter> <!-- optional -->
                                        <!-- BEGIN OR -->
                                                <ListID >IDTYPE</ListID> <!-- optional, may repeat -->
                                        <!-- OR -->
                                                <FullName >STRTYPE</FullName> <!-- optional, may repeat -->
                                        <!-- OR -->
                                                <ListIDWithChildren >IDTYPE</ListIDWithChildren> <!-- optional -->
                                        <!-- OR -->
                                                <FullNameWithChildren >STRTYPE</FullNameWithChildren> <!-- optional -->
                                        <!-- END OR -->
                                </ClassFilter>
                        <!-- END OR -->
                        <IncludeRetElement >STRTYPE</IncludeRetElement> <!-- optional, may repeat -->
                        <OwnerID >GUIDTYPE</OwnerID> <!-- optional, may repeat -->
                </ItemDiscountQueryRq>

                <ItemDiscountQueryRs statusCode="INTTYPE" statusSeverity="STRTYPE" statusMessage="STRTYPE" retCount="INTTYPE" iteratorRemainingCount="INTTYPE" iteratorID="UUIDTYPE">
                        <ItemDiscountRet> <!-- optional, may repeat -->
                                <ListID >IDTYPE</ListID> <!-- required -->
                                <TimeCreated >DATETIMETYPE</TimeCreated> <!-- required -->
                                <TimeModified >DATETIMETYPE</TimeModified> <!-- required -->
                                <EditSequence >STRTYPE</EditSequence> <!-- required -->
                                <Name >STRTYPE</Name> <!-- required -->
                                <FullName >STRTYPE</FullName> <!-- required -->
                                <BarCodeValue >STRTYPE</BarCodeValue> <!-- optional -->
                                <IsActive >BOOLTYPE</IsActive> <!-- optional -->
                                <ClassRef> <!-- optional -->
                                        <ListID >IDTYPE</ListID> <!-- optional -->
                                        <FullName >STRTYPE</FullName> <!-- optional -->
                                </ClassRef>
                                <ParentRef> <!-- optional -->
                                        <ListID >IDTYPE</ListID> <!-- optional -->
                                        <FullName >STRTYPE</FullName> <!-- optional -->
                                </ParentRef>
                                <Sublevel >INTTYPE</Sublevel> <!-- required -->
                                <ItemDesc >STRTYPE</ItemDesc> <!-- optional -->
                                <SalesTaxCodeRef> <!-- optional -->
                                        <ListID >IDTYPE</ListID> <!-- optional -->
                                        <FullName >STRTYPE</FullName> <!-- optional -->
                                </SalesTaxCodeRef>
                                <!-- BEGIN OR -->
                                        <DiscountRate >PRICETYPE</DiscountRate> <!-- optional -->
                                <!-- OR -->
                                        <DiscountRatePercent >PERCENTTYPE</DiscountRatePercent> <!-- optional -->
                                <!-- END OR -->
                                <AccountRef> <!-- optional -->
                                        <ListID >IDTYPE</ListID> <!-- optional -->
                                        <FullName >STRTYPE</FullName> <!-- optional -->
                                </AccountRef>
                                <ExternalGUID >GUIDTYPE</ExternalGUID> <!-- optional -->
                                <DataExtRet> <!-- optional, may repeat -->
                                        <OwnerID >GUIDTYPE</OwnerID> <!-- optional -->
                                        <DataExtName >STRTYPE</DataExtName> <!-- required -->
                                        <!-- DataExtType may have one of the following values: AMTTYPE, DATETIMETYPE, INTTYPE, PERCENTTYPE, PRICETYPE, QUANTYPE, STR1024TYPE, STR255TYPE -->
                                        <DataExtType >ENUMTYPE</DataExtType> <!-- required -->
                                        <DataExtValue >STRTYPE</DataExtValue> <!-- required -->
                                </DataExtRet>
                        </ItemDiscountRet>
                </ItemDiscountQueryRs>
        </QBXMLMsgsRq>
</QBXML>
```
## ItemGroupQuery
### XMLOps
```
<?xml version="1.0" encoding="utf-8"?>
<?qbxml version="16.0"?>
<QBXML>
        <QBXMLMsgsRq onError="stopOnError">
                <ItemGroupQueryRq metaData="ENUMTYPE" iterator="ENUMTYPE" iteratorID="UUIDTYPE">
                        <!-- BEGIN OR -->
                                <ListID >IDTYPE</ListID> <!-- optional, may repeat -->
                        <!-- OR -->
                                <FullName >STRTYPE</FullName> <!-- optional, may repeat -->
                        <!-- OR -->
                                <MaxReturned >INTTYPE</MaxReturned> <!-- optional -->
                                <!-- ActiveStatus may have one of the following values: ActiveOnly [DEFAULT], InactiveOnly, All -->
                                <ActiveStatus >ENUMTYPE</ActiveStatus> <!-- optional -->
                                <FromModifiedDate >DATETIMETYPE</FromModifiedDate> <!-- optional -->
                                <ToModifiedDate >DATETIMETYPE</ToModifiedDate> <!-- optional -->
                                <!-- BEGIN OR -->
                                        <NameFilter> <!-- optional -->
                                                <!-- MatchCriterion may have one of the following values: StartsWith, Contains, EndsWith -->
                                                <MatchCriterion >ENUMTYPE</MatchCriterion> <!-- required -->
                                                <Name >STRTYPE</Name> <!-- required -->
                                        </NameFilter>
                                <!-- OR -->
                                        <NameRangeFilter> <!-- optional -->
                                                <FromName >STRTYPE</FromName> <!-- optional -->
                                                <ToName >STRTYPE</ToName> <!-- optional -->
                                        </NameRangeFilter>
                                <!-- END OR -->
                        <!-- END OR -->
                        <IncludeRetElement >STRTYPE</IncludeRetElement> <!-- optional, may repeat -->
                        <OwnerID >GUIDTYPE</OwnerID> <!-- optional, may repeat -->
                </ItemGroupQueryRq>

                <ItemGroupQueryRs statusCode="INTTYPE" statusSeverity="STRTYPE" statusMessage="STRTYPE" retCount="INTTYPE" iteratorRemainingCount="INTTYPE" iteratorID="UUIDTYPE">
                        <ItemGroupRet> <!-- optional, may repeat -->
                                <ListID >IDTYPE</ListID> <!-- required -->
                                <TimeCreated >DATETIMETYPE</TimeCreated> <!-- required -->
                                <TimeModified >DATETIMETYPE</TimeModified> <!-- required -->
                                <EditSequence >STRTYPE</EditSequence> <!-- required -->
                                <Name >STRTYPE</Name> <!-- required -->
                                <BarCodeValue >STRTYPE</BarCodeValue> <!-- optional -->
                                <IsActive >BOOLTYPE</IsActive> <!-- optional -->
                                <ItemDesc >STRTYPE</ItemDesc> <!-- optional -->
                                <UnitOfMeasureSetRef> <!-- optional -->
                                        <ListID >IDTYPE</ListID> <!-- optional -->
                                        <FullName >STRTYPE</FullName> <!-- optional -->
                                </UnitOfMeasureSetRef>
                                <IsPrintItemsInGroup >BOOLTYPE</IsPrintItemsInGroup> <!-- optional -->
                                <!-- SpecialItemType may have one of the following values: FinanceCharge, ReimbursableExpenseGroup, ReimbursableExpenseSubtotal -->
                                <SpecialItemType >ENUMTYPE</SpecialItemType> <!-- optional -->
                                <ExternalGUID >GUIDTYPE</ExternalGUID> <!-- optional -->
                                <ItemGroupLine> <!-- optional, may repeat -->
                                        <ItemRef> <!-- optional -->
                                                <ListID >IDTYPE</ListID> <!-- optional -->
                                                <FullName >STRTYPE</FullName> <!-- optional -->
                                        </ItemRef>
                                        <Quantity >QUANTYPE</Quantity> <!-- optional -->
                                        <UnitOfMeasure >STRTYPE</UnitOfMeasure> <!-- optional -->
                                </ItemGroupLine>
                                <DataExtRet> <!-- optional, may repeat -->
                                        <OwnerID >GUIDTYPE</OwnerID> <!-- optional -->
                                        <DataExtName >STRTYPE</DataExtName> <!-- required -->
                                        <!-- DataExtType may have one of the following values: AMTTYPE, DATETIMETYPE, INTTYPE, PERCENTTYPE, PRICETYPE, QUANTYPE, STR1024TYPE, STR255TYPE -->
                                        <DataExtType >ENUMTYPE</DataExtType> <!-- required -->
                                        <DataExtValue >STRTYPE</DataExtValue> <!-- required -->
                                </DataExtRet>
                        </ItemGroupRet>
                </ItemGroupQueryRs>
        </QBXMLMsgsRq>
</QBXML>
```
## ItemInventoryQuery
### XMLOps
```
<?xml version="1.0" encoding="utf-8"?>
<?qbxml version="16.0"?>
<QBXML>
        <QBXMLMsgsRq onError="stopOnError">
                <ItemInventoryQueryRq metaData="ENUMTYPE" iterator="ENUMTYPE" iteratorID="UUIDTYPE">
                        <!-- BEGIN OR -->
                                <ListID >IDTYPE</ListID> <!-- optional, may repeat -->
                        <!-- OR -->
                                <FullName >STRTYPE</FullName> <!-- optional, may repeat -->
                        <!-- OR -->
                                <MaxReturned >INTTYPE</MaxReturned> <!-- optional -->
                                <!-- ActiveStatus may have one of the following values: ActiveOnly [DEFAULT], InactiveOnly, All -->
                                <ActiveStatus >ENUMTYPE</ActiveStatus> <!-- optional -->
                                <FromModifiedDate >DATETIMETYPE</FromModifiedDate> <!-- optional -->
                                <ToModifiedDate >DATETIMETYPE</ToModifiedDate> <!-- optional -->
                                <!-- BEGIN OR -->
                                        <NameFilter> <!-- optional -->
                                                <!-- MatchCriterion may have one of the following values: StartsWith, Contains, EndsWith -->
                                                <MatchCriterion >ENUMTYPE</MatchCriterion> <!-- required -->
                                                <Name >STRTYPE</Name> <!-- required -->
                                        </NameFilter>
                                <!-- OR -->
                                        <NameRangeFilter> <!-- optional -->
                                                <FromName >STRTYPE</FromName> <!-- optional -->
                                                <ToName >STRTYPE</ToName> <!-- optional -->
                                        </NameRangeFilter>
                                <!-- END OR -->
                                <ClassFilter> <!-- optional -->
                                        <!-- BEGIN OR -->
                                                <ListID >IDTYPE</ListID> <!-- optional, may repeat -->
                                        <!-- OR -->
                                                <FullName >STRTYPE</FullName> <!-- optional, may repeat -->
                                        <!-- OR -->
                                                <ListIDWithChildren >IDTYPE</ListIDWithChildren> <!-- optional -->
                                        <!-- OR -->
                                                <FullNameWithChildren >STRTYPE</FullNameWithChildren> <!-- optional -->
                                        <!-- END OR -->
                                </ClassFilter>
                        <!-- END OR -->
                        <IncludeRetElement >STRTYPE</IncludeRetElement> <!-- optional, may repeat -->
                        <OwnerID >GUIDTYPE</OwnerID> <!-- optional, may repeat -->
                </ItemInventoryQueryRq>

                <ItemInventoryQueryRs statusCode="INTTYPE" statusSeverity="STRTYPE" statusMessage="STRTYPE" retCount="INTTYPE" iteratorRemainingCount="INTTYPE" iteratorID="UUIDTYPE">
                        <ItemInventoryRet> <!-- optional, may repeat -->
                                <ListID >IDTYPE</ListID> <!-- required -->
                                <TimeCreated >DATETIMETYPE</TimeCreated> <!-- required -->
                                <TimeModified >DATETIMETYPE</TimeModified> <!-- required -->
                                <EditSequence >STRTYPE</EditSequence> <!-- required -->
                                <Name >STRTYPE</Name> <!-- required -->
                                <FullName >STRTYPE</FullName> <!-- required -->
                                <BarCodeValue >STRTYPE</BarCodeValue> <!-- optional -->
                                <IsActive >BOOLTYPE</IsActive> <!-- optional -->
                                <ClassRef> <!-- optional -->
                                        <ListID >IDTYPE</ListID> <!-- optional -->
                                        <FullName >STRTYPE</FullName> <!-- optional -->
                                </ClassRef>
                                <ParentRef> <!-- optional -->
                                        <ListID >IDTYPE</ListID> <!-- optional -->
                                        <FullName >STRTYPE</FullName> <!-- optional -->
                                </ParentRef>
                                <Sublevel >INTTYPE</Sublevel> <!-- required -->
                                <ManufacturerPartNumber >STRTYPE</ManufacturerPartNumber> <!-- optional -->
                                <UnitOfMeasureSetRef> <!-- optional -->
                                        <ListID >IDTYPE</ListID> <!-- optional -->
                                        <FullName >STRTYPE</FullName> <!-- optional -->
                                </UnitOfMeasureSetRef>
                                <IsTaxIncluded >BOOLTYPE</IsTaxIncluded> <!-- optional -->
                                <SalesTaxCodeRef> <!-- optional -->
                                        <ListID >IDTYPE</ListID> <!-- optional -->
                                        <FullName >STRTYPE</FullName> <!-- optional -->
                                </SalesTaxCodeRef>
                                <SalesDesc >STRTYPE</SalesDesc> <!-- optional -->
                                <SalesPrice >PRICETYPE</SalesPrice> <!-- optional -->
                                <IncomeAccountRef> <!-- optional -->
                                        <ListID >IDTYPE</ListID> <!-- optional -->
                                        <FullName >STRTYPE</FullName> <!-- optional -->
                                </IncomeAccountRef>
                                <PurchaseDesc >STRTYPE</PurchaseDesc> <!-- optional -->
                                <PurchaseCost >PRICETYPE</PurchaseCost> <!-- optional -->
                                <PurchaseTaxCodeRef> <!-- optional -->
                                        <ListID >IDTYPE</ListID> <!-- optional -->
                                        <FullName >STRTYPE</FullName> <!-- optional -->
                                </PurchaseTaxCodeRef>
                                <COGSAccountRef> <!-- optional -->
                                        <ListID >IDTYPE</ListID> <!-- optional -->
                                        <FullName >STRTYPE</FullName> <!-- optional -->
                                </COGSAccountRef>
                                <PrefVendorRef> <!-- optional -->
                                        <ListID >IDTYPE</ListID> <!-- optional -->
                                        <FullName >STRTYPE</FullName> <!-- optional -->
                                </PrefVendorRef>
                                <AssetAccountRef> <!-- optional -->
                                        <ListID >IDTYPE</ListID> <!-- optional -->
                                        <FullName >STRTYPE</FullName> <!-- optional -->
                                </AssetAccountRef>
                                <ReorderPoint >QUANTYPE</ReorderPoint> <!-- optional -->
                                <Max >QUANTYPE</Max> <!-- optional -->
                                <QuantityOnHand >QUANTYPE</QuantityOnHand> <!-- optional -->
                                <AverageCost >PRICETYPE</AverageCost> <!-- optional -->
                                <QuantityOnOrder >QUANTYPE</QuantityOnOrder> <!-- optional -->
                                <QuantityOnSalesOrder >QUANTYPE</QuantityOnSalesOrder> <!-- optional -->
                                <ExternalGUID >GUIDTYPE</ExternalGUID> <!-- optional -->
                                <DataExtRet> <!-- optional, may repeat -->
                                        <OwnerID >GUIDTYPE</OwnerID> <!-- optional -->
                                        <DataExtName >STRTYPE</DataExtName> <!-- required -->
                                        <!-- DataExtType may have one of the following values: AMTTYPE, DATETIMETYPE, INTTYPE, PERCENTTYPE, PRICETYPE, QUANTYPE, STR1024TYPE, STR255TYPE -->
                                        <DataExtType >ENUMTYPE</DataExtType> <!-- required -->
                                        <DataExtValue >STRTYPE</DataExtValue> <!-- required -->
                                </DataExtRet>
                        </ItemInventoryRet>
                </ItemInventoryQueryRs>
        </QBXMLMsgsRq>
</QBXML>
```
## ItemNonInventoryQuery
### XMLOps
```
<?xml version="1.0" encoding="utf-8"?>
<?qbxml version="16.0"?>
<QBXML>
        <QBXMLMsgsRq onError="stopOnError">
                <ItemNonInventoryQueryRq metaData="ENUMTYPE" iterator="ENUMTYPE" iteratorID="UUIDTYPE">
                        <!-- BEGIN OR -->
                                <ListID >IDTYPE</ListID> <!-- optional, may repeat -->
                        <!-- OR -->
                                <FullName >STRTYPE</FullName> <!-- optional, may repeat -->
                        <!-- OR -->
                                <MaxReturned >INTTYPE</MaxReturned> <!-- optional -->
                                <!-- ActiveStatus may have one of the following values: ActiveOnly [DEFAULT], InactiveOnly, All -->
                                <ActiveStatus >ENUMTYPE</ActiveStatus> <!-- optional -->
                                <FromModifiedDate >DATETIMETYPE</FromModifiedDate> <!-- optional -->
                                <ToModifiedDate >DATETIMETYPE</ToModifiedDate> <!-- optional -->
                                <!-- BEGIN OR -->
                                        <NameFilter> <!-- optional -->
                                                <!-- MatchCriterion may have one of the following values: StartsWith, Contains, EndsWith -->
                                                <MatchCriterion >ENUMTYPE</MatchCriterion> <!-- required -->
                                                <Name >STRTYPE</Name> <!-- required -->
                                        </NameFilter>
                                <!-- OR -->
                                        <NameRangeFilter> <!-- optional -->
                                                <FromName >STRTYPE</FromName> <!-- optional -->
                                                <ToName >STRTYPE</ToName> <!-- optional -->
                                        </NameRangeFilter>
                                <!-- END OR -->
                                <ClassFilter> <!-- optional -->
                                        <!-- BEGIN OR -->
                                                <ListID >IDTYPE</ListID> <!-- optional, may repeat -->
                                        <!-- OR -->
                                                <FullName >STRTYPE</FullName> <!-- optional, may repeat -->
                                        <!-- OR -->
                                                <ListIDWithChildren >IDTYPE</ListIDWithChildren> <!-- optional -->
                                        <!-- OR -->
                                                <FullNameWithChildren >STRTYPE</FullNameWithChildren> <!-- optional -->
                                        <!-- END OR -->
                                </ClassFilter>
                        <!-- END OR -->
                        <IncludeRetElement >STRTYPE</IncludeRetElement> <!-- optional, may repeat -->
                        <OwnerID >GUIDTYPE</OwnerID> <!-- optional, may repeat -->
                </ItemNonInventoryQueryRq>

                <ItemNonInventoryQueryRs statusCode="INTTYPE" statusSeverity="STRTYPE" statusMessage="STRTYPE" retCount="INTTYPE" iteratorRemainingCount="INTTYPE" iteratorID="UUIDTYPE">
                        <ItemNonInventoryRet> <!-- optional, may repeat -->
                                <ListID >IDTYPE</ListID> <!-- required -->
                                <TimeCreated >DATETIMETYPE</TimeCreated> <!-- required -->
                                <TimeModified >DATETIMETYPE</TimeModified> <!-- required -->
                                <EditSequence >STRTYPE</EditSequence> <!-- required -->
                                <Name >STRTYPE</Name> <!-- required -->
                                <FullName >STRTYPE</FullName> <!-- required -->
                                <BarCodeValue >STRTYPE</BarCodeValue> <!-- optional -->
                                <IsActive >BOOLTYPE</IsActive> <!-- optional -->
                                <ClassRef> <!-- optional -->
                                        <ListID >IDTYPE</ListID> <!-- optional -->
                                        <FullName >STRTYPE</FullName> <!-- optional -->
                                </ClassRef>
                                <ParentRef> <!-- optional -->
                                        <ListID >IDTYPE</ListID> <!-- optional -->
                                        <FullName >STRTYPE</FullName> <!-- optional -->
                                </ParentRef>
                                <Sublevel >INTTYPE</Sublevel> <!-- required -->
                                <ManufacturerPartNumber >STRTYPE</ManufacturerPartNumber> <!-- optional -->
                                <UnitOfMeasureSetRef> <!-- optional -->
                                        <ListID >IDTYPE</ListID> <!-- optional -->
                                        <FullName >STRTYPE</FullName> <!-- optional -->
                                </UnitOfMeasureSetRef>
                                <IsTaxIncluded >BOOLTYPE</IsTaxIncluded> <!-- optional -->
                                <SalesTaxCodeRef> <!-- optional -->
                                        <ListID >IDTYPE</ListID> <!-- optional -->
                                        <FullName >STRTYPE</FullName> <!-- optional -->
                                </SalesTaxCodeRef>
                                <!-- BEGIN OR -->
                                        <SalesOrPurchase> <!-- optional -->
                                                <Desc >STRTYPE</Desc> <!-- optional -->
                                                <!-- BEGIN OR -->
                                                        <Price >PRICETYPE</Price> <!-- optional -->
                                                <!-- OR -->
                                                        <PricePercent >PERCENTTYPE</PricePercent> <!-- optional -->
                                                <!-- END OR -->
                                                <AccountRef> <!-- optional -->
                                                        <ListID >IDTYPE</ListID> <!-- optional -->
                                                        <FullName >STRTYPE</FullName> <!-- optional -->
                                                </AccountRef>
                                        </SalesOrPurchase>
                                <!-- OR -->
                                        <SalesAndPurchase> <!-- optional -->
                                                <SalesDesc >STRTYPE</SalesDesc> <!-- optional -->
                                                <SalesPrice >PRICETYPE</SalesPrice> <!-- optional -->
                                                <IncomeAccountRef> <!-- optional -->
                                                        <ListID >IDTYPE</ListID> <!-- optional -->
                                                        <FullName >STRTYPE</FullName> <!-- optional -->
                                                </IncomeAccountRef>
                                                <PurchaseDesc >STRTYPE</PurchaseDesc> <!-- optional -->
                                                <PurchaseCost >PRICETYPE</PurchaseCost> <!-- optional -->
                                                <PurchaseTaxCodeRef> <!-- optional -->
                                                        <ListID >IDTYPE</ListID> <!-- optional -->
                                                        <FullName >STRTYPE</FullName> <!-- optional -->
                                                </PurchaseTaxCodeRef>
                                                <ExpenseAccountRef> <!-- optional -->
                                                        <ListID >IDTYPE</ListID> <!-- optional -->
                                                        <FullName >STRTYPE</FullName> <!-- optional -->
                                                </ExpenseAccountRef>
                                                <PrefVendorRef> <!-- optional -->
                                                        <ListID >IDTYPE</ListID> <!-- optional -->
                                                        <FullName >STRTYPE</FullName> <!-- optional -->
                                                </PrefVendorRef>
                                        </SalesAndPurchase>
                                <!-- END OR -->
                                <ExternalGUID >GUIDTYPE</ExternalGUID> <!-- optional -->
                                <DataExtRet> <!-- optional, may repeat -->
                                        <OwnerID >GUIDTYPE</OwnerID> <!-- optional -->
                                        <DataExtName >STRTYPE</DataExtName> <!-- required -->
                                        <!-- DataExtType may have one of the following values: AMTTYPE, DATETIMETYPE, INTTYPE, PERCENTTYPE, PRICETYPE, QUANTYPE, STR1024TYPE, STR255TYPE -->
                                        <DataExtType >ENUMTYPE</DataExtType> <!-- required -->
                                        <DataExtValue >STRTYPE</DataExtValue> <!-- required -->
                                </DataExtRet>
                        </ItemNonInventoryRet>
                </ItemNonInventoryQueryRs>
        </QBXMLMsgsRq>
</QBXML>
```
## ItemOtherChargeQuery
### XMLOps
```
<?xml version="1.0" encoding="utf-8"?>
<?qbxml version="16.0"?>
<QBXML>
        <QBXMLMsgsRq onError="stopOnError">
                <ItemOtherChargeQueryRq metaData="ENUMTYPE" iterator="ENUMTYPE" iteratorID="UUIDTYPE">
                        <!-- BEGIN OR -->
                                <ListID >IDTYPE</ListID> <!-- optional, may repeat -->
                        <!-- OR -->
                                <FullName >STRTYPE</FullName> <!-- optional, may repeat -->
                        <!-- OR -->
                                <MaxReturned >INTTYPE</MaxReturned> <!-- optional -->
                                <!-- ActiveStatus may have one of the following values: ActiveOnly [DEFAULT], InactiveOnly, All -->
                                <ActiveStatus >ENUMTYPE</ActiveStatus> <!-- optional -->
                                <FromModifiedDate >DATETIMETYPE</FromModifiedDate> <!-- optional -->
                                <ToModifiedDate >DATETIMETYPE</ToModifiedDate> <!-- optional -->
                                <!-- BEGIN OR -->
                                        <NameFilter> <!-- optional -->
                                                <!-- MatchCriterion may have one of the following values: StartsWith, Contains, EndsWith -->
                                                <MatchCriterion >ENUMTYPE</MatchCriterion> <!-- required -->
                                                <Name >STRTYPE</Name> <!-- required -->
                                        </NameFilter>
                                <!-- OR -->
                                        <NameRangeFilter> <!-- optional -->
                                                <FromName >STRTYPE</FromName> <!-- optional -->
                                                <ToName >STRTYPE</ToName> <!-- optional -->
                                        </NameRangeFilter>
                                <!-- END OR -->
                                <ClassFilter> <!-- optional -->
                                        <!-- BEGIN OR -->
                                                <ListID >IDTYPE</ListID> <!-- optional, may repeat -->
                                        <!-- OR -->
                                                <FullName >STRTYPE</FullName> <!-- optional, may repeat -->
                                        <!-- OR -->
                                                <ListIDWithChildren >IDTYPE</ListIDWithChildren> <!-- optional -->
                                        <!-- OR -->
                                                <FullNameWithChildren >STRTYPE</FullNameWithChildren> <!-- optional -->
                                        <!-- END OR -->
                                </ClassFilter>
                        <!-- END OR -->
                        <IncludeRetElement >STRTYPE</IncludeRetElement> <!-- optional, may repeat -->
                        <OwnerID >GUIDTYPE</OwnerID> <!-- optional, may repeat -->
                </ItemOtherChargeQueryRq>

                <ItemOtherChargeQueryRs statusCode="INTTYPE" statusSeverity="STRTYPE" statusMessage="STRTYPE" retCount="INTTYPE" iteratorRemainingCount="INTTYPE" iteratorID="UUIDTYPE">
                        <ItemOtherChargeRet> <!-- optional, may repeat -->
                                <ListID >IDTYPE</ListID> <!-- required -->
                                <TimeCreated >DATETIMETYPE</TimeCreated> <!-- required -->
                                <TimeModified >DATETIMETYPE</TimeModified> <!-- required -->
                                <EditSequence >STRTYPE</EditSequence> <!-- required -->
                                <Name >STRTYPE</Name> <!-- required -->
                                <FullName >STRTYPE</FullName> <!-- required -->
                                <BarCodeValue >STRTYPE</BarCodeValue> <!-- optional -->
                                <IsActive >BOOLTYPE</IsActive> <!-- optional -->
                                <ClassRef> <!-- optional -->
                                        <ListID >IDTYPE</ListID> <!-- optional -->
                                        <FullName >STRTYPE</FullName> <!-- optional -->
                                </ClassRef>
                                <ParentRef> <!-- optional -->
                                        <ListID >IDTYPE</ListID> <!-- optional -->
                                        <FullName >STRTYPE</FullName> <!-- optional -->
                                </ParentRef>
                                <Sublevel >INTTYPE</Sublevel> <!-- required -->
                                <IsTaxIncluded >BOOLTYPE</IsTaxIncluded> <!-- optional -->
                                <SalesTaxCodeRef> <!-- optional -->
                                        <ListID >IDTYPE</ListID> <!-- optional -->
                                        <FullName >STRTYPE</FullName> <!-- optional -->
                                </SalesTaxCodeRef>
                                <!-- BEGIN OR -->
                                        <SalesOrPurchase> <!-- optional -->
                                                <Desc >STRTYPE</Desc> <!-- optional -->
                                                <!-- BEGIN OR -->
                                                        <Price >PRICETYPE</Price> <!-- optional -->
                                                <!-- OR -->
                                                        <PricePercent >PERCENTTYPE</PricePercent> <!-- optional -->
                                                <!-- END OR -->
                                                <AccountRef> <!-- optional -->
                                                        <ListID >IDTYPE</ListID> <!-- optional -->
                                                        <FullName >STRTYPE</FullName> <!-- optional -->
                                                </AccountRef>
                                        </SalesOrPurchase>
                                <!-- OR -->
                                        <SalesAndPurchase> <!-- optional -->
                                                <SalesDesc >STRTYPE</SalesDesc> <!-- optional -->
                                                <SalesPrice >PRICETYPE</SalesPrice> <!-- optional -->
                                                <IncomeAccountRef> <!-- optional -->
                                                        <ListID >IDTYPE</ListID> <!-- optional -->
                                                        <FullName >STRTYPE</FullName> <!-- optional -->
                                                </IncomeAccountRef>
                                                <PurchaseDesc >STRTYPE</PurchaseDesc> <!-- optional -->
                                                <PurchaseCost >PRICETYPE</PurchaseCost> <!-- optional -->
                                                <PurchaseTaxCodeRef> <!-- optional -->
                                                        <ListID >IDTYPE</ListID> <!-- optional -->
                                                        <FullName >STRTYPE</FullName> <!-- optional -->
                                                </PurchaseTaxCodeRef>
                                                <ExpenseAccountRef> <!-- optional -->
                                                        <ListID >IDTYPE</ListID> <!-- optional -->
                                                        <FullName >STRTYPE</FullName> <!-- optional -->
                                                </ExpenseAccountRef>
                                                <PrefVendorRef> <!-- optional -->
                                                        <ListID >IDTYPE</ListID> <!-- optional -->
                                                        <FullName >STRTYPE</FullName> <!-- optional -->
                                                </PrefVendorRef>
                                        </SalesAndPurchase>
                                <!-- END OR -->
                                <!-- SpecialItemType may have one of the following values: FinanceCharge, ReimbursableExpenseGroup, ReimbursableExpenseSubtotal -->
                                <SpecialItemType >ENUMTYPE</SpecialItemType> <!-- optional -->
                                <ExternalGUID >GUIDTYPE</ExternalGUID> <!-- optional -->
                                <DataExtRet> <!-- optional, may repeat -->
                                        <OwnerID >GUIDTYPE</OwnerID> <!-- optional -->
                                        <DataExtName >STRTYPE</DataExtName> <!-- required -->
                                        <!-- DataExtType may have one of the following values: AMTTYPE, DATETIMETYPE, INTTYPE, PERCENTTYPE, PRICETYPE, QUANTYPE, STR1024TYPE, STR255TYPE -->
                                        <DataExtType >ENUMTYPE</DataExtType> <!-- required -->
                                        <DataExtValue >STRTYPE</DataExtValue> <!-- required -->
                                </DataExtRet>
                        </ItemOtherChargeRet>
                </ItemOtherChargeQueryRs>
        </QBXMLMsgsRq>
</QBXML>
```
## ItemPaymentQuery
### XMLOps
```
<?xml version="1.0" encoding="utf-8"?>
<?qbxml version="16.0"?>
<QBXML>
        <QBXMLMsgsRq onError="stopOnError">
                <ItemPaymentQueryRq metaData="ENUMTYPE" iterator="ENUMTYPE" iteratorID="UUIDTYPE">
                        <!-- BEGIN OR -->
                                <ListID >IDTYPE</ListID> <!-- optional, may repeat -->
                        <!-- OR -->
                                <FullName >STRTYPE</FullName> <!-- optional, may repeat -->
                        <!-- OR -->
                                <MaxReturned >INTTYPE</MaxReturned> <!-- optional -->
                                <!-- ActiveStatus may have one of the following values: ActiveOnly [DEFAULT], InactiveOnly, All -->
                                <ActiveStatus >ENUMTYPE</ActiveStatus> <!-- optional -->
                                <FromModifiedDate >DATETIMETYPE</FromModifiedDate> <!-- optional -->
                                <ToModifiedDate >DATETIMETYPE</ToModifiedDate> <!-- optional -->
                                <!-- BEGIN OR -->
                                        <NameFilter> <!-- optional -->
                                                <!-- MatchCriterion may have one of the following values: StartsWith, Contains, EndsWith -->
                                                <MatchCriterion >ENUMTYPE</MatchCriterion> <!-- required -->
                                                <Name >STRTYPE</Name> <!-- required -->
                                        </NameFilter>
                                <!-- OR -->
                                        <NameRangeFilter> <!-- optional -->
                                                <FromName >STRTYPE</FromName> <!-- optional -->
                                                <ToName >STRTYPE</ToName> <!-- optional -->
                                        </NameRangeFilter>
                                <!-- END OR -->
                                <ClassFilter> <!-- optional -->
                                        <!-- BEGIN OR -->
                                                <ListID >IDTYPE</ListID> <!-- optional, may repeat -->
                                        <!-- OR -->
                                                <FullName >STRTYPE</FullName> <!-- optional, may repeat -->
                                        <!-- OR -->
                                                <ListIDWithChildren >IDTYPE</ListIDWithChildren> <!-- optional -->
                                        <!-- OR -->
                                                <FullNameWithChildren >STRTYPE</FullNameWithChildren> <!-- optional -->
                                        <!-- END OR -->
                                </ClassFilter>
                        <!-- END OR -->
                        <IncludeRetElement >STRTYPE</IncludeRetElement> <!-- optional, may repeat -->
                        <OwnerID >GUIDTYPE</OwnerID> <!-- optional, may repeat -->
                </ItemPaymentQueryRq>

                <ItemPaymentQueryRs statusCode="INTTYPE" statusSeverity="STRTYPE" statusMessage="STRTYPE" retCount="INTTYPE" iteratorRemainingCount="INTTYPE" iteratorID="UUIDTYPE">
                        <ItemPaymentRet> <!-- optional, may repeat -->
                                <ListID >IDTYPE</ListID> <!-- required -->
                                <TimeCreated >DATETIMETYPE</TimeCreated> <!-- required -->
                                <TimeModified >DATETIMETYPE</TimeModified> <!-- required -->
                                <EditSequence >STRTYPE</EditSequence> <!-- required -->
                                <Name >STRTYPE</Name> <!-- required -->
                                <BarCodeValue >STRTYPE</BarCodeValue> <!-- optional -->
                                <IsActive >BOOLTYPE</IsActive> <!-- optional -->
                                <ClassRef> <!-- optional -->
                                        <ListID >IDTYPE</ListID> <!-- optional -->
                                        <FullName >STRTYPE</FullName> <!-- optional -->
                                </ClassRef>
                                <ItemDesc >STRTYPE</ItemDesc> <!-- optional -->
                                <DepositToAccountRef> <!-- optional -->
                                        <ListID >IDTYPE</ListID> <!-- optional -->
                                        <FullName >STRTYPE</FullName> <!-- optional -->
                                </DepositToAccountRef>
                                <PaymentMethodRef> <!-- optional -->
                                        <ListID >IDTYPE</ListID> <!-- optional -->
                                        <FullName >STRTYPE</FullName> <!-- optional -->
                                </PaymentMethodRef>
                                <ExternalGUID >GUIDTYPE</ExternalGUID> <!-- optional -->
                                <DataExtRet> <!-- optional, may repeat -->
                                        <OwnerID >GUIDTYPE</OwnerID> <!-- optional -->
                                        <DataExtName >STRTYPE</DataExtName> <!-- required -->
                                        <!-- DataExtType may have one of the following values: AMTTYPE, DATETIMETYPE, INTTYPE, PERCENTTYPE, PRICETYPE, QUANTYPE, STR1024TYPE, STR255TYPE -->
                                        <DataExtType >ENUMTYPE</DataExtType> <!-- required -->
                                        <DataExtValue >STRTYPE</DataExtValue> <!-- required -->
                                </DataExtRet>
                        </ItemPaymentRet>
                </ItemPaymentQueryRs>
        </QBXMLMsgsRq>
</QBXML>
```
## ItemQuery
### XMLOps
```
<?xml version="1.0" encoding="utf-8"?>
<?qbxml version="16.0"?>
<QBXML>
        <QBXMLMsgsRq onError="stopOnError">
                <ItemQueryRq metaData="ENUMTYPE" iterator="ENUMTYPE" iteratorID="UUIDTYPE">
                        <!-- BEGIN OR -->
                                <ListID >IDTYPE</ListID> <!-- optional, may repeat -->
                        <!-- OR -->
                                <FullName >STRTYPE</FullName> <!-- optional, may repeat -->
                        <!-- OR -->
                                <MaxReturned >INTTYPE</MaxReturned> <!-- optional -->
                                <!-- ActiveStatus may have one of the following values: ActiveOnly [DEFAULT], InactiveOnly, All -->
                                <ActiveStatus >ENUMTYPE</ActiveStatus> <!-- optional -->
                                <FromModifiedDate >DATETIMETYPE</FromModifiedDate> <!-- optional -->
                                <ToModifiedDate >DATETIMETYPE</ToModifiedDate> <!-- optional -->
                                <!-- BEGIN OR -->
                                        <NameFilter> <!-- optional -->
                                                <!-- MatchCriterion may have one of the following values: StartsWith, Contains, EndsWith -->
                                                <MatchCriterion >ENUMTYPE</MatchCriterion> <!-- required -->
                                                <Name >STRTYPE</Name> <!-- required -->
                                        </NameFilter>
                                <!-- OR -->
                                        <NameRangeFilter> <!-- optional -->
                                                <FromName >STRTYPE</FromName> <!-- optional -->
                                                <ToName >STRTYPE</ToName> <!-- optional -->
                                        </NameRangeFilter>
                                <!-- END OR -->
                        <!-- END OR -->
                        <IncludeRetElement >STRTYPE</IncludeRetElement> <!-- optional, may repeat -->
                        <OwnerID >GUIDTYPE</OwnerID> <!-- optional, may repeat -->
                </ItemQueryRq>

                <ItemQueryRs statusCode="INTTYPE" statusSeverity="STRTYPE" statusMessage="STRTYPE" retCount="INTTYPE" iteratorRemainingCount="INTTYPE" iteratorID="UUIDTYPE">
                        <!-- BEGIN OR -->
                                <ItemServiceRet> <!-- optional -->
                                        <ListID >IDTYPE</ListID> <!-- required -->
                                        <TimeCreated >DATETIMETYPE</TimeCreated> <!-- required -->
                                        <TimeModified >DATETIMETYPE</TimeModified> <!-- required -->
                                        <EditSequence >STRTYPE</EditSequence> <!-- required -->
                                        <Name >STRTYPE</Name> <!-- required -->
                                        <FullName >STRTYPE</FullName> <!-- required -->
                                        <BarCodeValue >STRTYPE</BarCodeValue> <!-- optional -->
                                        <IsActive >BOOLTYPE</IsActive> <!-- optional -->
                                        <ClassRef> <!-- optional -->
                                                <ListID >IDTYPE</ListID> <!-- optional -->
                                                <FullName >STRTYPE</FullName> <!-- optional -->
                                        </ClassRef>
                                        <ParentRef> <!-- optional -->
                                                <ListID >IDTYPE</ListID> <!-- optional -->
                                                <FullName >STRTYPE</FullName> <!-- optional -->
                                        </ParentRef>
                                        <Sublevel >INTTYPE</Sublevel> <!-- required -->
                                        <UnitOfMeasureSetRef> <!-- optional -->
                                                <ListID >IDTYPE</ListID> <!-- optional -->
                                                <FullName >STRTYPE</FullName> <!-- optional -->
                                        </UnitOfMeasureSetRef>
                                        <IsTaxIncluded >BOOLTYPE</IsTaxIncluded> <!-- optional -->
                                        <SalesTaxCodeRef> <!-- optional -->
                                                <ListID >IDTYPE</ListID> <!-- optional -->
                                                <FullName >STRTYPE</FullName> <!-- optional -->
                                        </SalesTaxCodeRef>
                                        <!-- BEGIN OR -->
                                                <SalesOrPurchase> <!-- optional -->
                                                        <Desc >STRTYPE</Desc> <!-- optional -->
                                                        <!-- BEGIN OR -->
                                                                <Price >PRICETYPE</Price> <!-- optional -->
                                                        <!-- OR -->
                                                                <PricePercent >PERCENTTYPE</PricePercent> <!-- optional -->
                                                        <!-- END OR -->
                                                        <AccountRef> <!-- optional -->
                                                                <ListID >IDTYPE</ListID> <!-- optional -->
                                                                <FullName >STRTYPE</FullName> <!-- optional -->
                                                        </AccountRef>
                                                </SalesOrPurchase>
                                        <!-- OR -->
                                                <SalesAndPurchase> <!-- optional -->
                                                        <SalesDesc >STRTYPE</SalesDesc> <!-- optional -->
                                                        <SalesPrice >PRICETYPE</SalesPrice> <!-- optional -->
                                                        <IncomeAccountRef> <!-- optional -->
                                                                <ListID >IDTYPE</ListID> <!-- optional -->
                                                                <FullName >STRTYPE</FullName> <!-- optional -->
                                                        </IncomeAccountRef>
                                                        <PurchaseDesc >STRTYPE</PurchaseDesc> <!-- optional -->
                                                        <PurchaseCost >PRICETYPE</PurchaseCost> <!-- optional -->
                                                        <PurchaseTaxCodeRef> <!-- optional -->
                                                                <ListID >IDTYPE</ListID> <!-- optional -->
                                                                <FullName >STRTYPE</FullName> <!-- optional -->
                                                        </PurchaseTaxCodeRef>
                                                        <ExpenseAccountRef> <!-- optional -->
                                                                <ListID >IDTYPE</ListID> <!-- optional -->
                                                                <FullName >STRTYPE</FullName> <!-- optional -->
                                                        </ExpenseAccountRef>
                                                        <PrefVendorRef> <!-- optional -->
                                                                <ListID >IDTYPE</ListID> <!-- optional -->
                                                                <FullName >STRTYPE</FullName> <!-- optional -->
                                                        </PrefVendorRef>
                                                </SalesAndPurchase>
                                        <!-- END OR -->
                                        <ExternalGUID >GUIDTYPE</ExternalGUID> <!-- optional -->
                                        <DataExtRet> <!-- optional, may repeat -->
                                                <OwnerID >GUIDTYPE</OwnerID> <!-- optional -->
                                                <DataExtName >STRTYPE</DataExtName> <!-- required -->
                                                <!-- DataExtType may have one of the following values: AMTTYPE, DATETIMETYPE, INTTYPE, PERCENTTYPE, PRICETYPE, QUANTYPE, STR1024TYPE, STR255TYPE -->
                                                <DataExtType >ENUMTYPE</DataExtType> <!-- required -->
                                                <DataExtValue >STRTYPE</DataExtValue> <!-- required -->
                                        </DataExtRet>
                                </ItemServiceRet>
                        <!-- OR -->
                                <ItemNonInventoryRet> <!-- optional -->
                                        <ListID >IDTYPE</ListID> <!-- required -->
                                        <TimeCreated >DATETIMETYPE</TimeCreated> <!-- required -->
                                        <TimeModified >DATETIMETYPE</TimeModified> <!-- required -->
                                        <EditSequence >STRTYPE</EditSequence> <!-- required -->
                                        <Name >STRTYPE</Name> <!-- required -->
                                        <FullName >STRTYPE</FullName> <!-- required -->
                                        <BarCodeValue >STRTYPE</BarCodeValue> <!-- optional -->
                                        <IsActive >BOOLTYPE</IsActive> <!-- optional -->
                                        <ClassRef> <!-- optional -->
                                                <ListID >IDTYPE</ListID> <!-- optional -->
                                                <FullName >STRTYPE</FullName> <!-- optional -->
                                        </ClassRef>
                                        <ParentRef> <!-- optional -->
                                                <ListID >IDTYPE</ListID> <!-- optional -->
                                                <FullName >STRTYPE</FullName> <!-- optional -->
                                        </ParentRef>
                                        <Sublevel >INTTYPE</Sublevel> <!-- required -->
                                        <ManufacturerPartNumber >STRTYPE</ManufacturerPartNumber> <!-- optional -->
                                        <UnitOfMeasureSetRef> <!-- optional -->
                                                <ListID >IDTYPE</ListID> <!-- optional -->
                                                <FullName >STRTYPE</FullName> <!-- optional -->
                                        </UnitOfMeasureSetRef>
                                        <IsTaxIncluded >BOOLTYPE</IsTaxIncluded> <!-- optional -->
                                        <SalesTaxCodeRef> <!-- optional -->
                                                <ListID >IDTYPE</ListID> <!-- optional -->
                                                <FullName >STRTYPE</FullName> <!-- optional -->
                                        </SalesTaxCodeRef>
                                        <!-- BEGIN OR -->
                                                <SalesOrPurchase> <!-- optional -->
                                                        <Desc >STRTYPE</Desc> <!-- optional -->
                                                        <!-- BEGIN OR -->
                                                                <Price >PRICETYPE</Price> <!-- optional -->
                                                        <!-- OR -->
                                                                <PricePercent >PERCENTTYPE</PricePercent> <!-- optional -->
                                                        <!-- END OR -->
                                                        <AccountRef> <!-- optional -->
                                                                <ListID >IDTYPE</ListID> <!-- optional -->
                                                                <FullName >STRTYPE</FullName> <!-- optional -->
                                                        </AccountRef>
                                                </SalesOrPurchase>
                                        <!-- OR -->
                                                <SalesAndPurchase> <!-- optional -->
                                                        <SalesDesc >STRTYPE</SalesDesc> <!-- optional -->
                                                        <SalesPrice >PRICETYPE</SalesPrice> <!-- optional -->
                                                        <IncomeAccountRef> <!-- optional -->
                                                                <ListID >IDTYPE</ListID> <!-- optional -->
                                                                <FullName >STRTYPE</FullName> <!-- optional -->
                                                        </IncomeAccountRef>
                                                        <PurchaseDesc >STRTYPE</PurchaseDesc> <!-- optional -->
                                                        <PurchaseCost >PRICETYPE</PurchaseCost> <!-- optional -->
                                                        <PurchaseTaxCodeRef> <!-- optional -->
                                                                <ListID >IDTYPE</ListID> <!-- optional -->
                                                                <FullName >STRTYPE</FullName> <!-- optional -->
                                                        </PurchaseTaxCodeRef>
                                                        <ExpenseAccountRef> <!-- optional -->
                                                                <ListID >IDTYPE</ListID> <!-- optional -->
                                                                <FullName >STRTYPE</FullName> <!-- optional -->
                                                        </ExpenseAccountRef>
                                                        <PrefVendorRef> <!-- optional -->
                                                                <ListID >IDTYPE</ListID> <!-- optional -->
                                                                <FullName >STRTYPE</FullName> <!-- optional -->
                                                        </PrefVendorRef>
                                                </SalesAndPurchase>
                                        <!-- END OR -->
                                        <ExternalGUID >GUIDTYPE</ExternalGUID> <!-- optional -->
                                        <DataExtRet> <!-- optional, may repeat -->
                                                <OwnerID >GUIDTYPE</OwnerID> <!-- optional -->
                                                <DataExtName >STRTYPE</DataExtName> <!-- required -->
                                                <!-- DataExtType may have one of the following values: AMTTYPE, DATETIMETYPE, INTTYPE, PERCENTTYPE, PRICETYPE, QUANTYPE, STR1024TYPE, STR255TYPE -->
                                                <DataExtType >ENUMTYPE</DataExtType> <!-- required -->
                                                <DataExtValue >STRTYPE</DataExtValue> <!-- required -->
                                        </DataExtRet>
                                </ItemNonInventoryRet>
                        <!-- OR -->
                                <ItemOtherChargeRet> <!-- optional -->
                                        <ListID >IDTYPE</ListID> <!-- required -->
                                        <TimeCreated >DATETIMETYPE</TimeCreated> <!-- required -->
                                        <TimeModified >DATETIMETYPE</TimeModified> <!-- required -->
                                        <EditSequence >STRTYPE</EditSequence> <!-- required -->
                                        <Name >STRTYPE</Name> <!-- required -->
                                        <FullName >STRTYPE</FullName> <!-- required -->
                                        <BarCodeValue >STRTYPE</BarCodeValue> <!-- optional -->
                                        <IsActive >BOOLTYPE</IsActive> <!-- optional -->
                                        <ClassRef> <!-- optional -->
                                                <ListID >IDTYPE</ListID> <!-- optional -->
                                                <FullName >STRTYPE</FullName> <!-- optional -->
                                        </ClassRef>
                                        <ParentRef> <!-- optional -->
                                                <ListID >IDTYPE</ListID> <!-- optional -->
                                                <FullName >STRTYPE</FullName> <!-- optional -->
                                        </ParentRef>
                                        <Sublevel >INTTYPE</Sublevel> <!-- required -->
                                        <IsTaxIncluded >BOOLTYPE</IsTaxIncluded> <!-- optional -->
                                        <SalesTaxCodeRef> <!-- optional -->
                                                <ListID >IDTYPE</ListID> <!-- optional -->
                                                <FullName >STRTYPE</FullName> <!-- optional -->
                                        </SalesTaxCodeRef>
                                        <!-- BEGIN OR -->
                                                <SalesOrPurchase> <!-- optional -->
                                                        <Desc >STRTYPE</Desc> <!-- optional -->
                                                        <!-- BEGIN OR -->
                                                                <Price >PRICETYPE</Price> <!-- optional -->
                                                        <!-- OR -->
                                                                <PricePercent >PERCENTTYPE</PricePercent> <!-- optional -->
                                                        <!-- END OR -->
                                                        <AccountRef> <!-- optional -->
                                                                <ListID >IDTYPE</ListID> <!-- optional -->
                                                                <FullName >STRTYPE</FullName> <!-- optional -->
                                                        </AccountRef>
                                                </SalesOrPurchase>
                                        <!-- OR -->
                                                <SalesAndPurchase> <!-- optional -->
                                                        <SalesDesc >STRTYPE</SalesDesc> <!-- optional -->
                                                        <SalesPrice >PRICETYPE</SalesPrice> <!-- optional -->
                                                        <IncomeAccountRef> <!-- optional -->
                                                                <ListID >IDTYPE</ListID> <!-- optional -->
                                                                <FullName >STRTYPE</FullName> <!-- optional -->
                                                        </IncomeAccountRef>
                                                        <PurchaseDesc >STRTYPE</PurchaseDesc> <!-- optional -->
                                                        <PurchaseCost >PRICETYPE</PurchaseCost> <!-- optional -->
                                                        <PurchaseTaxCodeRef> <!-- optional -->
                                                                <ListID >IDTYPE</ListID> <!-- optional -->
                                                                <FullName >STRTYPE</FullName> <!-- optional -->
                                                        </PurchaseTaxCodeRef>
                                                        <ExpenseAccountRef> <!-- optional -->
                                                                <ListID >IDTYPE</ListID> <!-- optional -->
                                                                <FullName >STRTYPE</FullName> <!-- optional -->
                                                        </ExpenseAccountRef>
                                                        <PrefVendorRef> <!-- optional -->
                                                                <ListID >IDTYPE</ListID> <!-- optional -->
                                                                <FullName >STRTYPE</FullName> <!-- optional -->
                                                        </PrefVendorRef>
                                                </SalesAndPurchase>
                                        <!-- END OR -->
                                        <!-- SpecialItemType may have one of the following values: FinanceCharge, ReimbursableExpenseGroup, ReimbursableExpenseSubtotal -->
                                        <SpecialItemType >ENUMTYPE</SpecialItemType> <!-- optional -->
                                        <ExternalGUID >GUIDTYPE</ExternalGUID> <!-- optional -->
                                        <DataExtRet> <!-- optional, may repeat -->
                                                <OwnerID >GUIDTYPE</OwnerID> <!-- optional -->
                                                <DataExtName >STRTYPE</DataExtName> <!-- required -->
                                                <!-- DataExtType may have one of the following values: AMTTYPE, DATETIMETYPE, INTTYPE, PERCENTTYPE, PRICETYPE, QUANTYPE, STR1024TYPE, STR255TYPE -->
                                                <DataExtType >ENUMTYPE</DataExtType> <!-- required -->
                                                <DataExtValue >STRTYPE</DataExtValue> <!-- required -->
                                        </DataExtRet>
                                </ItemOtherChargeRet>
                        <!-- OR -->
                                <ItemInventoryRet> <!-- optional -->
                                        <ListID >IDTYPE</ListID> <!-- required -->
                                        <TimeCreated >DATETIMETYPE</TimeCreated> <!-- required -->
                                        <TimeModified >DATETIMETYPE</TimeModified> <!-- required -->
                                        <EditSequence >STRTYPE</EditSequence> <!-- required -->
                                        <Name >STRTYPE</Name> <!-- required -->
                                        <FullName >STRTYPE</FullName> <!-- required -->
                                        <BarCodeValue >STRTYPE</BarCodeValue> <!-- optional -->
                                        <IsActive >BOOLTYPE</IsActive> <!-- optional -->
                                        <ClassRef> <!-- optional -->
                                                <ListID >IDTYPE</ListID> <!-- optional -->
                                                <FullName >STRTYPE</FullName> <!-- optional -->
                                        </ClassRef>
                                        <ParentRef> <!-- optional -->
                                                <ListID >IDTYPE</ListID> <!-- optional -->
                                                <FullName >STRTYPE</FullName> <!-- optional -->
                                        </ParentRef>
                                        <Sublevel >INTTYPE</Sublevel> <!-- required -->
                                        <ManufacturerPartNumber >STRTYPE</ManufacturerPartNumber> <!-- optional -->
                                        <UnitOfMeasureSetRef> <!-- optional -->
                                                <ListID >IDTYPE</ListID> <!-- optional -->
                                                <FullName >STRTYPE</FullName> <!-- optional -->
                                        </UnitOfMeasureSetRef>
                                        <IsTaxIncluded >BOOLTYPE</IsTaxIncluded> <!-- optional -->
                                        <SalesTaxCodeRef> <!-- optional -->
                                                <ListID >IDTYPE</ListID> <!-- optional -->
                                                <FullName >STRTYPE</FullName> <!-- optional -->
                                        </SalesTaxCodeRef>
                                        <SalesDesc >STRTYPE</SalesDesc> <!-- optional -->
                                        <SalesPrice >PRICETYPE</SalesPrice> <!-- optional -->
                                        <IncomeAccountRef> <!-- optional -->
                                                <ListID >IDTYPE</ListID> <!-- optional -->
                                                <FullName >STRTYPE</FullName> <!-- optional -->
                                        </IncomeAccountRef>
                                        <PurchaseDesc >STRTYPE</PurchaseDesc> <!-- optional -->
                                        <PurchaseCost >PRICETYPE</PurchaseCost> <!-- optional -->
                                        <PurchaseTaxCodeRef> <!-- optional -->
                                                <ListID >IDTYPE</ListID> <!-- optional -->
                                                <FullName >STRTYPE</FullName> <!-- optional -->
                                        </PurchaseTaxCodeRef>
                                        <COGSAccountRef> <!-- optional -->
                                                <ListID >IDTYPE</ListID> <!-- optional -->
                                                <FullName >STRTYPE</FullName> <!-- optional -->
                                        </COGSAccountRef>
                                        <PrefVendorRef> <!-- optional -->
                                                <ListID >IDTYPE</ListID> <!-- optional -->
                                                <FullName >STRTYPE</FullName> <!-- optional -->
                                        </PrefVendorRef>
                                        <AssetAccountRef> <!-- optional -->
                                                <ListID >IDTYPE</ListID> <!-- optional -->
                                                <FullName >STRTYPE</FullName> <!-- optional -->
                                        </AssetAccountRef>
                                        <ReorderPoint >QUANTYPE</ReorderPoint> <!-- optional -->
                                        <Max >QUANTYPE</Max> <!-- optional -->
                                        <QuantityOnHand >QUANTYPE</QuantityOnHand> <!-- optional -->
                                        <AverageCost >PRICETYPE</AverageCost> <!-- optional -->
                                        <QuantityOnOrder >QUANTYPE</QuantityOnOrder> <!-- optional -->
                                        <QuantityOnSalesOrder >QUANTYPE</QuantityOnSalesOrder> <!-- optional -->
                                        <ExternalGUID >GUIDTYPE</ExternalGUID> <!-- optional -->
                                        <DataExtRet> <!-- optional, may repeat -->
                                                <OwnerID >GUIDTYPE</OwnerID> <!-- optional -->
                                                <DataExtName >STRTYPE</DataExtName> <!-- required -->
                                                <!-- DataExtType may have one of the following values: AMTTYPE, DATETIMETYPE, INTTYPE, PERCENTTYPE, PRICETYPE, QUANTYPE, STR1024TYPE, STR255TYPE -->
                                                <DataExtType >ENUMTYPE</DataExtType> <!-- required -->
                                                <DataExtValue >STRTYPE</DataExtValue> <!-- required -->
                                        </DataExtRet>
                                </ItemInventoryRet>
                        <!-- OR -->
                                <ItemInventoryAssemblyRet> <!-- optional -->
                                        <ListID >IDTYPE</ListID> <!-- required -->
                                        <TimeCreated >DATETIMETYPE</TimeCreated> <!-- required -->
                                        <TimeModified >DATETIMETYPE</TimeModified> <!-- required -->
                                        <EditSequence >STRTYPE</EditSequence> <!-- required -->
                                        <Name >STRTYPE</Name> <!-- required -->
                                        <FullName >STRTYPE</FullName> <!-- required -->
                                        <BarCodeValue >STRTYPE</BarCodeValue> <!-- optional -->
                                        <IsActive >BOOLTYPE</IsActive> <!-- optional -->
                                        <ClassRef> <!-- optional -->
                                                <ListID >IDTYPE</ListID> <!-- optional -->
                                                <FullName >STRTYPE</FullName> <!-- optional -->
                                        </ClassRef>
                                        <ParentRef> <!-- optional -->
                                                <ListID >IDTYPE</ListID> <!-- optional -->
                                                <FullName >STRTYPE</FullName> <!-- optional -->
                                        </ParentRef>
                                        <Sublevel >INTTYPE</Sublevel> <!-- required -->
                                        <ManufacturerPartNumber >STRTYPE</ManufacturerPartNumber> <!-- optional -->
                                        <UnitOfMeasureSetRef> <!-- optional -->
                                                <ListID >IDTYPE</ListID> <!-- optional -->
                                                <FullName >STRTYPE</FullName> <!-- optional -->
                                        </UnitOfMeasureSetRef>
                                        <IsTaxIncluded >BOOLTYPE</IsTaxIncluded> <!-- optional -->
                                        <SalesTaxCodeRef> <!-- optional -->
                                                <ListID >IDTYPE</ListID> <!-- optional -->
                                                <FullName >STRTYPE</FullName> <!-- optional -->
                                        </SalesTaxCodeRef>
                                        <SalesDesc >STRTYPE</SalesDesc> <!-- optional -->
                                        <SalesPrice >PRICETYPE</SalesPrice> <!-- optional -->
                                        <IncomeAccountRef> <!-- optional -->
                                                <ListID >IDTYPE</ListID> <!-- optional -->
                                                <FullName >STRTYPE</FullName> <!-- optional -->
                                        </IncomeAccountRef>
                                        <PurchaseDesc >STRTYPE</PurchaseDesc> <!-- optional -->
                                        <PurchaseCost >PRICETYPE</PurchaseCost> <!-- optional -->
                                        <PurchaseTaxCodeRef> <!-- optional -->
                                                <ListID >IDTYPE</ListID> <!-- optional -->
                                                <FullName >STRTYPE</FullName> <!-- optional -->
                                        </PurchaseTaxCodeRef>
                                        <COGSAccountRef> <!-- optional -->
                                                <ListID >IDTYPE</ListID> <!-- optional -->
                                                <FullName >STRTYPE</FullName> <!-- optional -->
                                        </COGSAccountRef>
                                        <PrefVendorRef> <!-- optional -->
                                                <ListID >IDTYPE</ListID> <!-- optional -->
                                                <FullName >STRTYPE</FullName> <!-- optional -->
                                        </PrefVendorRef>
                                        <AssetAccountRef> <!-- optional -->
                                                <ListID >IDTYPE</ListID> <!-- optional -->
                                                <FullName >STRTYPE</FullName> <!-- optional -->
                                        </AssetAccountRef>
                                        <BuildPoint >QUANTYPE</BuildPoint> <!-- optional -->
                                        <Max >QUANTYPE</Max> <!-- optional -->
                                        <QuantityOnHand >QUANTYPE</QuantityOnHand> <!-- optional -->
                                        <AverageCost >PRICETYPE</AverageCost> <!-- optional -->
                                        <QuantityOnOrder >QUANTYPE</QuantityOnOrder> <!-- optional -->
                                        <QuantityOnSalesOrder >QUANTYPE</QuantityOnSalesOrder> <!-- optional -->
                                        <ExternalGUID >GUIDTYPE</ExternalGUID> <!-- optional -->
                                        <ItemInventoryAssemblyLine> <!-- optional, may repeat -->
                                                <ItemInventoryRef> <!-- required -->
                                                        <ListID >IDTYPE</ListID> <!-- optional -->
                                                        <FullName >STRTYPE</FullName> <!-- optional -->
                                                </ItemInventoryRef>
                                                <Quantity >QUANTYPE</Quantity> <!-- optional -->
                                        </ItemInventoryAssemblyLine>
                                        <DataExtRet> <!-- optional, may repeat -->
                                                <OwnerID >GUIDTYPE</OwnerID> <!-- optional -->
                                                <DataExtName >STRTYPE</DataExtName> <!-- required -->
                                                <!-- DataExtType may have one of the following values: AMTTYPE, DATETIMETYPE, INTTYPE, PERCENTTYPE, PRICETYPE, QUANTYPE, STR1024TYPE, STR255TYPE -->
                                                <DataExtType >ENUMTYPE</DataExtType> <!-- required -->
                                                <DataExtValue >STRTYPE</DataExtValue> <!-- required -->
                                        </DataExtRet>
                                </ItemInventoryAssemblyRet>
                        <!-- OR -->
                                <ItemFixedAssetRet> <!-- optional -->
                                        <ListID >IDTYPE</ListID> <!-- required -->
                                        <TimeCreated >DATETIMETYPE</TimeCreated> <!-- required -->
                                        <TimeModified >DATETIMETYPE</TimeModified> <!-- required -->
                                        <EditSequence >STRTYPE</EditSequence> <!-- required -->
                                        <Name >STRTYPE</Name> <!-- required -->
                                        <BarCodeValue >STRTYPE</BarCodeValue> <!-- optional -->
                                        <IsActive >BOOLTYPE</IsActive> <!-- optional -->
                                        <ClassRef> <!-- optional -->
                                                <ListID >IDTYPE</ListID> <!-- optional -->
                                                <FullName >STRTYPE</FullName> <!-- optional -->
                                        </ClassRef>
                                        <!-- AcquiredAs may have one of the following values: New, Old -->
                                        <AcquiredAs >ENUMTYPE</AcquiredAs> <!-- required -->
                                        <PurchaseDesc >STRTYPE</PurchaseDesc> <!-- required -->
                                        <PurchaseDate >DATETYPE</PurchaseDate> <!-- required -->
                                        <PurchaseCost >PRICETYPE</PurchaseCost> <!-- optional -->
                                        <VendorOrPayeeName >STRTYPE</VendorOrPayeeName> <!-- optional -->
                                        <AssetAccountRef> <!-- optional -->
                                                <ListID >IDTYPE</ListID> <!-- optional -->
                                                <FullName >STRTYPE</FullName> <!-- optional -->
                                        </AssetAccountRef>
                                        <FixedAssetSalesInfo> <!-- optional -->
                                                <SalesDesc >STRTYPE</SalesDesc> <!-- required -->
                                                <SalesDate >DATETYPE</SalesDate> <!-- required -->
                                                <SalesPrice >PRICETYPE</SalesPrice> <!-- optional -->
                                                <SalesExpense >PRICETYPE</SalesExpense> <!-- optional -->
                                        </FixedAssetSalesInfo>
                                        <AssetDesc >STRTYPE</AssetDesc> <!-- optional -->
                                        <Location >STRTYPE</Location> <!-- optional -->
                                        <PONumber >STRTYPE</PONumber> <!-- optional -->
                                        <SerialNumber >STRTYPE</SerialNumber> <!-- optional -->
                                        <WarrantyExpDate >DATETYPE</WarrantyExpDate> <!-- optional -->
                                        <Notes >STRTYPE</Notes> <!-- optional -->
                                        <AssetNumber >STRTYPE</AssetNumber> <!-- optional -->
                                        <CostBasis >AMTTYPE</CostBasis> <!-- optional -->
                                        <YearEndAccumulatedDepreciation >AMTTYPE</YearEndAccumulatedDepreciation> <!-- optional -->
                                        <YearEndBookValue >AMTTYPE</YearEndBookValue> <!-- optional -->
                                        <ExternalGUID >GUIDTYPE</ExternalGUID> <!-- optional -->
                                        <DataExtRet> <!-- optional, may repeat -->
                                                <OwnerID >GUIDTYPE</OwnerID> <!-- optional -->
                                                <DataExtName >STRTYPE</DataExtName> <!-- required -->
                                                <!-- DataExtType may have one of the following values: AMTTYPE, DATETIMETYPE, INTTYPE, PERCENTTYPE, PRICETYPE, QUANTYPE, STR1024TYPE, STR255TYPE -->
                                                <DataExtType >ENUMTYPE</DataExtType> <!-- required -->
                                                <DataExtValue >STRTYPE</DataExtValue> <!-- required -->
                                        </DataExtRet>
                                </ItemFixedAssetRet>
                        <!-- OR -->
                                <ItemSubtotalRet> <!-- optional -->
                                        <ListID >IDTYPE</ListID> <!-- required -->
                                        <TimeCreated >DATETIMETYPE</TimeCreated> <!-- required -->
                                        <TimeModified >DATETIMETYPE</TimeModified> <!-- required -->
                                        <EditSequence >STRTYPE</EditSequence> <!-- required -->
                                        <Name >STRTYPE</Name> <!-- required -->
                                        <BarCodeValue >STRTYPE</BarCodeValue> <!-- optional -->
                                        <IsActive >BOOLTYPE</IsActive> <!-- optional -->
                                        <ItemDesc >STRTYPE</ItemDesc> <!-- optional -->
                                        <!-- SpecialItemType may have one of the following values: FinanceCharge, ReimbursableExpenseGroup, ReimbursableExpenseSubtotal -->
                                        <SpecialItemType >ENUMTYPE</SpecialItemType> <!-- optional -->
                                        <ExternalGUID >GUIDTYPE</ExternalGUID> <!-- optional -->
                                        <DataExtRet> <!-- optional, may repeat -->
                                                <OwnerID >GUIDTYPE</OwnerID> <!-- optional -->
                                                <DataExtName >STRTYPE</DataExtName> <!-- required -->
                                                <!-- DataExtType may have one of the following values: AMTTYPE, DATETIMETYPE, INTTYPE, PERCENTTYPE, PRICETYPE, QUANTYPE, STR1024TYPE, STR255TYPE -->
                                                <DataExtType >ENUMTYPE</DataExtType> <!-- required -->
                                                <DataExtValue >STRTYPE</DataExtValue> <!-- required -->
                                        </DataExtRet>
                                </ItemSubtotalRet>
                        <!-- OR -->
                                <ItemDiscountRet> <!-- optional -->
                                        <ListID >IDTYPE</ListID> <!-- required -->
                                        <TimeCreated >DATETIMETYPE</TimeCreated> <!-- required -->
                                        <TimeModified >DATETIMETYPE</TimeModified> <!-- required -->
                                        <EditSequence >STRTYPE</EditSequence> <!-- required -->
                                        <Name >STRTYPE</Name> <!-- required -->
                                        <FullName >STRTYPE</FullName> <!-- required -->
                                        <BarCodeValue >STRTYPE</BarCodeValue> <!-- optional -->
                                        <IsActive >BOOLTYPE</IsActive> <!-- optional -->
                                        <ClassRef> <!-- optional -->
                                                <ListID >IDTYPE</ListID> <!-- optional -->
                                                <FullName >STRTYPE</FullName> <!-- optional -->
                                        </ClassRef>
                                        <ParentRef> <!-- optional -->
                                                <ListID >IDTYPE</ListID> <!-- optional -->
                                                <FullName >STRTYPE</FullName> <!-- optional -->
                                        </ParentRef>
                                        <Sublevel >INTTYPE</Sublevel> <!-- required -->
                                        <ItemDesc >STRTYPE</ItemDesc> <!-- optional -->
                                        <SalesTaxCodeRef> <!-- optional -->
                                                <ListID >IDTYPE</ListID> <!-- optional -->
                                                <FullName >STRTYPE</FullName> <!-- optional -->
                                        </SalesTaxCodeRef>
                                        <!-- BEGIN OR -->
                                                <DiscountRate >PRICETYPE</DiscountRate> <!-- optional -->
                                        <!-- OR -->
                                                <DiscountRatePercent >PERCENTTYPE</DiscountRatePercent> <!-- optional -->
                                        <!-- END OR -->
                                        <AccountRef> <!-- optional -->
                                                <ListID >IDTYPE</ListID> <!-- optional -->
                                                <FullName >STRTYPE</FullName> <!-- optional -->
                                        </AccountRef>
                                        <ExternalGUID >GUIDTYPE</ExternalGUID> <!-- optional -->
                                        <DataExtRet> <!-- optional, may repeat -->
                                                <OwnerID >GUIDTYPE</OwnerID> <!-- optional -->
                                                <DataExtName >STRTYPE</DataExtName> <!-- required -->
                                                <!-- DataExtType may have one of the following values: AMTTYPE, DATETIMETYPE, INTTYPE, PERCENTTYPE, PRICETYPE, QUANTYPE, STR1024TYPE, STR255TYPE -->
                                                <DataExtType >ENUMTYPE</DataExtType> <!-- required -->
                                                <DataExtValue >STRTYPE</DataExtValue> <!-- required -->
                                        </DataExtRet>
                                </ItemDiscountRet>
                        <!-- OR -->
                                <ItemPaymentRet> <!-- optional -->
                                        <ListID >IDTYPE</ListID> <!-- required -->
                                        <TimeCreated >DATETIMETYPE</TimeCreated> <!-- required -->
                                        <TimeModified >DATETIMETYPE</TimeModified> <!-- required -->
                                        <EditSequence >STRTYPE</EditSequence> <!-- required -->
                                        <Name >STRTYPE</Name> <!-- required -->
                                        <BarCodeValue >STRTYPE</BarCodeValue> <!-- optional -->
                                        <IsActive >BOOLTYPE</IsActive> <!-- optional -->
                                        <ClassRef> <!-- optional -->
                                                <ListID >IDTYPE</ListID> <!-- optional -->
                                                <FullName >STRTYPE</FullName> <!-- optional -->
                                        </ClassRef>
                                        <ItemDesc >STRTYPE</ItemDesc> <!-- optional -->
                                        <DepositToAccountRef> <!-- optional -->
                                                <ListID >IDTYPE</ListID> <!-- optional -->
                                                <FullName >STRTYPE</FullName> <!-- optional -->
                                        </DepositToAccountRef>
                                        <PaymentMethodRef> <!-- optional -->
                                                <ListID >IDTYPE</ListID> <!-- optional -->
                                                <FullName >STRTYPE</FullName> <!-- optional -->
                                        </PaymentMethodRef>
                                        <ExternalGUID >GUIDTYPE</ExternalGUID> <!-- optional -->
                                        <DataExtRet> <!-- optional, may repeat -->
                                                <OwnerID >GUIDTYPE</OwnerID> <!-- optional -->
                                                <DataExtName >STRTYPE</DataExtName> <!-- required -->
                                                <!-- DataExtType may have one of the following values: AMTTYPE, DATETIMETYPE, INTTYPE, PERCENTTYPE, PRICETYPE, QUANTYPE, STR1024TYPE, STR255TYPE -->
                                                <DataExtType >ENUMTYPE</DataExtType> <!-- required -->
                                                <DataExtValue >STRTYPE</DataExtValue> <!-- required -->
                                        </DataExtRet>
                                </ItemPaymentRet>
                        <!-- OR -->
                                <ItemSalesTaxRet> <!-- optional -->
                                        <ListID >IDTYPE</ListID> <!-- required -->
                                        <TimeCreated >DATETIMETYPE</TimeCreated> <!-- required -->
                                        <TimeModified >DATETIMETYPE</TimeModified> <!-- required -->
                                        <EditSequence >STRTYPE</EditSequence> <!-- required -->
                                        <Name >STRTYPE</Name> <!-- required -->
                                        <BarCodeValue >STRTYPE</BarCodeValue> <!-- optional -->
                                        <IsActive >BOOLTYPE</IsActive> <!-- optional -->
                                        <ClassRef> <!-- optional -->
                                                <ListID >IDTYPE</ListID> <!-- optional -->
                                                <FullName >STRTYPE</FullName> <!-- optional -->
                                        </ClassRef>
                                        <ItemDesc >STRTYPE</ItemDesc> <!-- optional -->
                                        <TaxRate >PERCENTTYPE</TaxRate> <!-- optional -->
                                        <TaxVendorRef> <!-- optional -->
                                                <ListID >IDTYPE</ListID> <!-- optional -->
                                                <FullName >STRTYPE</FullName> <!-- optional -->
                                        </TaxVendorRef>
                                        <SalesTaxReturnLineRef> <!-- optional -->
                                                <ListID >IDTYPE</ListID> <!-- optional -->
                                                <FullName >STRTYPE</FullName> <!-- optional -->
                                        </SalesTaxReturnLineRef>
                                        <ExternalGUID >GUIDTYPE</ExternalGUID> <!-- optional -->
                                        <DataExtRet> <!-- optional, may repeat -->
                                                <OwnerID >GUIDTYPE</OwnerID> <!-- optional -->
                                                <DataExtName >STRTYPE</DataExtName> <!-- required -->
                                                <!-- DataExtType may have one of the following values: AMTTYPE, DATETIMETYPE, INTTYPE, PERCENTTYPE, PRICETYPE, QUANTYPE, STR1024TYPE, STR255TYPE -->
                                                <DataExtType >ENUMTYPE</DataExtType> <!-- required -->
                                                <DataExtValue >STRTYPE</DataExtValue> <!-- required -->
                                        </DataExtRet>
                                </ItemSalesTaxRet>
                        <!-- OR -->
                                <ItemSalesTaxGroupRet> <!-- optional -->
                                        <ListID >IDTYPE</ListID> <!-- required -->
                                        <TimeCreated >DATETIMETYPE</TimeCreated> <!-- required -->
                                        <TimeModified >DATETIMETYPE</TimeModified> <!-- required -->
                                        <EditSequence >STRTYPE</EditSequence> <!-- required -->
                                        <Name >STRTYPE</Name> <!-- required -->
                                        <BarCodeValue >STRTYPE</BarCodeValue> <!-- optional -->
                                        <IsActive >BOOLTYPE</IsActive> <!-- optional -->
                                        <ItemDesc >STRTYPE</ItemDesc> <!-- optional -->
                                        <ExternalGUID >GUIDTYPE</ExternalGUID> <!-- optional -->
                                        <ItemSalesTaxRef> <!-- optional, may repeat -->
                                                <ListID >IDTYPE</ListID> <!-- optional -->
                                                <FullName >STRTYPE</FullName> <!-- optional -->
                                        </ItemSalesTaxRef>
                                        <DataExtRet> <!-- optional, may repeat -->
                                                <OwnerID >GUIDTYPE</OwnerID> <!-- optional -->
                                                <DataExtName >STRTYPE</DataExtName> <!-- required -->
                                                <!-- DataExtType may have one of the following values: AMTTYPE, DATETIMETYPE, INTTYPE, PERCENTTYPE, PRICETYPE, QUANTYPE, STR1024TYPE, STR255TYPE -->
                                                <DataExtType >ENUMTYPE</DataExtType> <!-- required -->
                                                <DataExtValue >STRTYPE</DataExtValue> <!-- required -->
                                        </DataExtRet>
                                </ItemSalesTaxGroupRet>
                        <!-- OR -->
                                <ItemGroupRet> <!-- optional -->
                                        <ListID >IDTYPE</ListID> <!-- required -->
                                        <TimeCreated >DATETIMETYPE</TimeCreated> <!-- required -->
                                        <TimeModified >DATETIMETYPE</TimeModified> <!-- required -->
                                        <EditSequence >STRTYPE</EditSequence> <!-- required -->
                                        <Name >STRTYPE</Name> <!-- required -->
                                        <BarCodeValue >STRTYPE</BarCodeValue> <!-- optional -->
                                        <IsActive >BOOLTYPE</IsActive> <!-- optional -->
                                        <ItemDesc >STRTYPE</ItemDesc> <!-- optional -->
                                        <UnitOfMeasureSetRef> <!-- optional -->
                                                <ListID >IDTYPE</ListID> <!-- optional -->
                                                <FullName >STRTYPE</FullName> <!-- optional -->
                                        </UnitOfMeasureSetRef>
                                        <IsPrintItemsInGroup >BOOLTYPE</IsPrintItemsInGroup> <!-- optional -->
                                        <!-- SpecialItemType may have one of the following values: FinanceCharge, ReimbursableExpenseGroup, ReimbursableExpenseSubtotal -->
                                        <SpecialItemType >ENUMTYPE</SpecialItemType> <!-- optional -->
                                        <ExternalGUID >GUIDTYPE</ExternalGUID> <!-- optional -->
                                        <ItemGroupLine> <!-- optional, may repeat -->
                                                <ItemRef> <!-- optional -->
                                                        <ListID >IDTYPE</ListID> <!-- optional -->
                                                        <FullName >STRTYPE</FullName> <!-- optional -->
                                                </ItemRef>
                                                <Quantity >QUANTYPE</Quantity> <!-- optional -->
                                                <UnitOfMeasure >STRTYPE</UnitOfMeasure> <!-- optional -->
                                        </ItemGroupLine>
                                        <DataExtRet> <!-- optional, may repeat -->
                                                <OwnerID >GUIDTYPE</OwnerID> <!-- optional -->
                                                <DataExtName >STRTYPE</DataExtName> <!-- required -->
                                                <!-- DataExtType may have one of the following values: AMTTYPE, DATETIMETYPE, INTTYPE, PERCENTTYPE, PRICETYPE, QUANTYPE, STR1024TYPE, STR255TYPE -->
                                                <DataExtType >ENUMTYPE</DataExtType> <!-- required -->
                                                <DataExtValue >STRTYPE</DataExtValue> <!-- required -->
                                        </DataExtRet>
                                </ItemGroupRet>
                        <!-- END OR -->
                </ItemQueryRs>
        </QBXMLMsgsRq>
</QBXML>

```

## ItemReceiptQuery
### XMLOps
```
<?xml version="1.0" encoding="utf-8"?>
<?qbxml version="16.0"?>
<QBXML>
        <QBXMLMsgsRq onError="stopOnError">
                <ItemReceiptQueryRq metaData="ENUMTYPE" iterator="ENUMTYPE" iteratorID="UUIDTYPE">
                        <!-- BEGIN OR -->
                                <TxnID >IDTYPE</TxnID> <!-- optional, may repeat -->
                        <!-- OR -->
                                <RefNumber >STRTYPE</RefNumber> <!-- optional, may repeat -->
                        <!-- OR -->
                                <RefNumberCaseSensitive >STRTYPE</RefNumberCaseSensitive> <!-- optional, may repeat -->
                        <!-- OR -->
                                <MaxReturned >INTTYPE</MaxReturned> <!-- optional -->
                                <!-- BEGIN OR -->
                                        <ModifiedDateRangeFilter> <!-- optional -->
                                                <FromModifiedDate >DATETIMETYPE</FromModifiedDate> <!-- optional -->
                                                <ToModifiedDate >DATETIMETYPE</ToModifiedDate> <!-- optional -->
                                        </ModifiedDateRangeFilter>
                                <!-- OR -->
                                        <TxnDateRangeFilter> <!-- optional -->
                                                <!-- BEGIN OR -->
                                                        <FromTxnDate >DATETYPE</FromTxnDate> <!-- optional -->
                                                        <ToTxnDate >DATETYPE</ToTxnDate> <!-- optional -->
                                                <!-- OR -->
                                                        <!-- DateMacro may have one of the following values: All, Today, ThisWeek, ThisWeekToDate, ThisMonth, ThisMonthToDate, ThisCalendarQuarter, ThisCalendarQuarterToDate, ThisFiscalQuarter, ThisFiscalQuarterToDate, ThisCalendarYear, ThisCalendarYearToDate, ThisFiscalYear, ThisFiscalYearToDate, Yesterday, LastWeek, LastWeekToDate, LastMonth, LastMonthToDate, LastCalendarQuarter, LastCalendarQuarterToDate, LastFiscalQuarter, LastFiscalQuarterToDate, LastCalendarYear, LastCalendarYearToDate, LastFiscalYear, LastFiscalYearToDate, NextWeek, NextFourWeeks, NextMonth, NextCalendarQuarter, NextCalendarYear, NextFiscalQuarter, NextFiscalYear -->
                                                        <DateMacro >ENUMTYPE</DateMacro> <!-- optional -->
                                                <!-- END OR -->
                                        </TxnDateRangeFilter>
                                <!-- END OR -->
                                <EntityFilter> <!-- optional -->
                                        <!-- BEGIN OR -->
                                                <ListID >IDTYPE</ListID> <!-- optional, may repeat -->
                                        <!-- OR -->
                                                <FullName >STRTYPE</FullName> <!-- optional, may repeat -->
                                        <!-- OR -->
                                                <ListIDWithChildren >IDTYPE</ListIDWithChildren> <!-- optional -->
                                        <!-- OR -->
                                                <FullNameWithChildren >STRTYPE</FullNameWithChildren> <!-- optional -->
                                        <!-- END OR -->
                                </EntityFilter>
                                <AccountFilter> <!-- optional -->
                                        <!-- BEGIN OR -->
                                                <ListID >IDTYPE</ListID> <!-- optional, may repeat -->
                                        <!-- OR -->
                                                <FullName >STRTYPE</FullName> <!-- optional, may repeat -->
                                        <!-- OR -->
                                                <ListIDWithChildren >IDTYPE</ListIDWithChildren> <!-- optional -->
                                        <!-- OR -->
                                                <FullNameWithChildren >STRTYPE</FullNameWithChildren> <!-- optional -->
                                        <!-- END OR -->
                                </AccountFilter>
                                <!-- BEGIN OR -->
                                        <RefNumberFilter> <!-- optional -->
                                                <!-- MatchCriterion may have one of the following values: StartsWith, Contains, EndsWith -->
                                                <MatchCriterion >ENUMTYPE</MatchCriterion> <!-- required -->
                                                <RefNumber >STRTYPE</RefNumber> <!-- required -->
                                        </RefNumberFilter>
                                <!-- OR -->
                                        <RefNumberRangeFilter> <!-- optional -->
                                                <FromRefNumber >STRTYPE</FromRefNumber> <!-- optional -->
                                                <ToRefNumber >STRTYPE</ToRefNumber> <!-- optional -->
                                        </RefNumberRangeFilter>
                                <!-- END OR -->
                                <CurrencyFilter> <!-- optional -->
                                        <!-- BEGIN OR -->
                                                <ListID >IDTYPE</ListID> <!-- optional, may repeat -->
                                        <!-- OR -->
                                                <FullName >STRTYPE</FullName> <!-- optional, may repeat -->
                                        <!-- END OR -->
                                </CurrencyFilter>
                        <!-- END OR -->
                        <IncludeLineItems >BOOLTYPE</IncludeLineItems> <!-- optional -->
                        <IncludeLinkedTxns >BOOLTYPE</IncludeLinkedTxns> <!-- optional -->
                        <IncludeRetElement >STRTYPE</IncludeRetElement> <!-- optional, may repeat -->
                        <OwnerID >GUIDTYPE</OwnerID> <!-- optional, may repeat -->
                </ItemReceiptQueryRq>

                <ItemReceiptQueryRs statusCode="INTTYPE" statusSeverity="STRTYPE" statusMessage="STRTYPE" retCount="INTTYPE" iteratorRemainingCount="INTTYPE" iteratorID="UUIDTYPE">
                        <ItemReceiptRet> <!-- optional, may repeat -->
                                <TxnID >IDTYPE</TxnID> <!-- required -->
                                <TimeCreated >DATETIMETYPE</TimeCreated> <!-- required -->
                                <TimeModified >DATETIMETYPE</TimeModified> <!-- required -->
                                <EditSequence >STRTYPE</EditSequence> <!-- required -->
                                <TxnNumber >INTTYPE</TxnNumber> <!-- optional -->
                                <VendorRef> <!-- required -->
                                        <ListID >IDTYPE</ListID> <!-- optional -->
                                        <FullName >STRTYPE</FullName> <!-- optional -->
                                </VendorRef>
                                <!-- BEGIN OR -->
                                        <APAccountRef> <!-- optional -->
                                                <ListID >IDTYPE</ListID> <!-- optional -->
                                                <FullName >STRTYPE</FullName> <!-- optional -->
                                        </APAccountRef>
                                <!-- OR -->
                                        <LiabilityAccountRef> <!-- optional -->
                                                <ListID >IDTYPE</ListID> <!-- optional -->
                                                <FullName >STRTYPE</FullName> <!-- optional -->
                                        </LiabilityAccountRef>
                                <!-- END OR -->
                                <TxnDate >DATETYPE</TxnDate> <!-- required -->
                                <TotalAmount >AMTTYPE</TotalAmount> <!-- required -->
                                <CurrencyRef> <!-- optional -->
                                        <ListID >IDTYPE</ListID> <!-- optional -->
                                        <FullName >STRTYPE</FullName> <!-- optional -->
                                </CurrencyRef>
                                <ExchangeRate >FLOATTYPE</ExchangeRate> <!-- optional -->
                                <TotalAmountInHomeCurrency >AMTTYPE</TotalAmountInHomeCurrency> <!-- optional -->
                                <RefNumber >STRTYPE</RefNumber> <!-- optional -->
                                <Memo >STRTYPE</Memo> <!-- optional -->
                                <IsTaxIncluded >BOOLTYPE</IsTaxIncluded> <!-- optional -->
                                <SalesTaxCodeRef> <!-- optional -->
                                        <ListID >IDTYPE</ListID> <!-- optional -->
                                        <FullName >STRTYPE</FullName> <!-- optional -->
                                </SalesTaxCodeRef>
                                <ExternalGUID >GUIDTYPE</ExternalGUID> <!-- optional -->
                                <LinkedTxn> <!-- optional, may repeat -->
                                        <TxnID >IDTYPE</TxnID> <!-- required -->
                                        <!-- TxnType may have one of the following values: ARRefundCreditCard, Bill, BillPaymentCheck, BillPaymentCreditCard, BuildAssembly, Charge, Check, CreditCardCharge, CreditCardCredit, CreditMemo, Deposit, Estimate, InventoryAdjustment, Invoice, ItemReceipt, JournalEntry, LiabilityAdjustment, Paycheck, PayrollLiabilityCheck, PurchaseOrder, ReceivePayment, SalesOrder, SalesReceipt, SalesTaxPaymentCheck, Transfer, VendorCredit, YTDAdjustment -->
                                        <TxnType >ENUMTYPE</TxnType> <!-- required -->
                                        <TxnDate >DATETYPE</TxnDate> <!-- required -->
                                        <RefNumber >STRTYPE</RefNumber> <!-- optional -->
                                        <!-- LinkType may have one of the following values: AMTTYPE, QUANTYPE -->
                                        <LinkType >ENUMTYPE</LinkType> <!-- optional -->
                                        <Amount >AMTTYPE</Amount> <!-- required -->
                                </LinkedTxn>
                                <ExpenseLineRet> <!-- optional, may repeat -->
                                        <TxnLineID >IDTYPE</TxnLineID> <!-- required -->
                                        <AccountRef> <!-- optional -->
                                                <ListID >IDTYPE</ListID> <!-- optional -->
                                                <FullName >STRTYPE</FullName> <!-- optional -->
                                        </AccountRef>
                                        <Amount >AMTTYPE</Amount> <!-- optional -->
                                        <Memo >STRTYPE</Memo> <!-- optional -->
                                        <CustomerRef> <!-- optional -->
                                                <ListID >IDTYPE</ListID> <!-- optional -->
                                                <FullName >STRTYPE</FullName> <!-- optional -->
                                        </CustomerRef>
                                        <ClassRef> <!-- optional -->
                                                <ListID >IDTYPE</ListID> <!-- optional -->
                                                <FullName >STRTYPE</FullName> <!-- optional -->
                                        </ClassRef>
                                        <SalesTaxCodeRef> <!-- optional -->
                                                <ListID >IDTYPE</ListID> <!-- optional -->
                                                <FullName >STRTYPE</FullName> <!-- optional -->
                                        </SalesTaxCodeRef>
                                        <!-- BillableStatus may have one of the following values: Billable, NotBillable, HasBeenBilled -->
                                        <BillableStatus >ENUMTYPE</BillableStatus> <!-- optional -->
                                        <SalesRepRef> <!-- optional -->
                                                <ListID >IDTYPE</ListID> <!-- optional -->
                                                <FullName >STRTYPE</FullName> <!-- optional -->
                                        </SalesRepRef>
                                        <DataExtRet> <!-- optional, may repeat -->
                                                <OwnerID >GUIDTYPE</OwnerID> <!-- optional -->
                                                <DataExtName >STRTYPE</DataExtName> <!-- required -->
                                                <!-- DataExtType may have one of the following values: AMTTYPE, DATETIMETYPE, INTTYPE, PERCENTTYPE, PRICETYPE, QUANTYPE, STR1024TYPE, STR255TYPE -->
                                                <DataExtType >ENUMTYPE</DataExtType> <!-- required -->
                                                <DataExtValue >STRTYPE</DataExtValue> <!-- required -->
                                        </DataExtRet>
                                </ExpenseLineRet>
                                <!-- BEGIN OR -->
                                        <ItemLineRet> <!-- optional -->
                                                <TxnLineID >IDTYPE</TxnLineID> <!-- required -->
                                                <ItemRef> <!-- optional -->
                                                        <ListID >IDTYPE</ListID> <!-- optional -->
                                                        <FullName >STRTYPE</FullName> <!-- optional -->
                                                </ItemRef>
                                                <InventorySiteRef> <!-- optional -->
                                                        <ListID >IDTYPE</ListID> <!-- optional -->
                                                        <FullName >STRTYPE</FullName> <!-- optional -->
                                                </InventorySiteRef>
                                                <InventorySiteLocationRef> <!-- optional -->
                                                        <ListID >IDTYPE</ListID> <!-- optional -->
                                                        <FullName >STRTYPE</FullName> <!-- optional -->
                                                </InventorySiteLocationRef>
                                                <!-- BEGIN OR -->
                                                        <SerialNumber >STRTYPE</SerialNumber> <!-- optional -->
                                                <!-- OR -->
                                                        <LotNumber >STRTYPE</LotNumber> <!-- optional -->
                                                <!-- END OR -->
                                                <ExpirationDateForSerialLotNumber>STRTYPE</ExpirationDateForSerialLotNumber> <!-- optional -->
                                                <Desc >STRTYPE</Desc> <!-- optional -->
                                                <Quantity >QUANTYPE</Quantity> <!-- optional -->
                                                <UnitOfMeasure >STRTYPE</UnitOfMeasure> <!-- optional -->
                                                <OverrideUOMSetRef> <!-- optional -->
                                                        <ListID >IDTYPE</ListID> <!-- optional -->
                                                        <FullName >STRTYPE</FullName> <!-- optional -->
                                                </OverrideUOMSetRef>
                                                <Cost >PRICETYPE</Cost> <!-- optional -->
                                                <Amount >AMTTYPE</Amount> <!-- optional -->
                                                <CustomerRef> <!-- optional -->
                                                        <ListID >IDTYPE</ListID> <!-- optional -->
                                                        <FullName >STRTYPE</FullName> <!-- optional -->
                                                </CustomerRef>
                                                <ClassRef> <!-- optional -->
                                                        <ListID >IDTYPE</ListID> <!-- optional -->
                                                        <FullName >STRTYPE</FullName> <!-- optional -->
                                                </ClassRef>
                                                <SalesTaxCodeRef> <!-- optional -->
                                                        <ListID >IDTYPE</ListID> <!-- optional -->
                                                        <FullName >STRTYPE</FullName> <!-- optional -->
                                                </SalesTaxCodeRef>
                                                <!-- BillableStatus may have one of the following values: Billable, NotBillable, HasBeenBilled -->
                                                <BillableStatus >ENUMTYPE</BillableStatus> <!-- optional -->
                                                <SalesRepRef> <!-- optional -->
                                                        <ListID >IDTYPE</ListID> <!-- optional -->
                                                        <FullName >STRTYPE</FullName> <!-- optional -->
                                                </SalesRepRef>
                                                <DataExtRet> <!-- optional, may repeat -->
                                                        <OwnerID >GUIDTYPE</OwnerID> <!-- optional -->
                                                        <DataExtName >STRTYPE</DataExtName> <!-- required -->
                                                        <!-- DataExtType may have one of the following values: AMTTYPE, DATETIMETYPE, INTTYPE, PERCENTTYPE, PRICETYPE, QUANTYPE, STR1024TYPE, STR255TYPE -->
                                                        <DataExtType >ENUMTYPE</DataExtType> <!-- required -->
                                                        <DataExtValue >STRTYPE</DataExtValue> <!-- required -->
                                                </DataExtRet>
                                        </ItemLineRet>
                                <!-- OR -->
                                        <ItemGroupLineRet> <!-- optional -->
                                                <TxnLineID >IDTYPE</TxnLineID> <!-- required -->
                                                <ItemGroupRef> <!-- required -->
                                                        <ListID >IDTYPE</ListID> <!-- optional -->
                                                        <FullName >STRTYPE</FullName> <!-- optional -->
                                                </ItemGroupRef>
                                                <Desc >STRTYPE</Desc> <!-- optional -->
                                                <Quantity >QUANTYPE</Quantity> <!-- optional -->
                                                <UnitOfMeasure >STRTYPE</UnitOfMeasure> <!-- optional -->
                                                <OverrideUOMSetRef> <!-- optional -->
                                                        <ListID >IDTYPE</ListID> <!-- optional -->
                                                        <FullName >STRTYPE</FullName> <!-- optional -->
                                                </OverrideUOMSetRef>
                                                <TotalAmount >AMTTYPE</TotalAmount> <!-- required -->
                                                <ItemLineRet> <!-- optional, may repeat -->
                                                        <TxnLineID >IDTYPE</TxnLineID> <!-- required -->
                                                        <ItemRef> <!-- optional -->
                                                                <ListID >IDTYPE</ListID> <!-- optional -->
                                                                <FullName >STRTYPE</FullName> <!-- optional -->
                                                        </ItemRef>
                                                        <InventorySiteRef> <!-- optional -->
                                                                <ListID >IDTYPE</ListID> <!-- optional -->
                                                                <FullName >STRTYPE</FullName> <!-- optional -->
                                                        </InventorySiteRef>
                                                        <InventorySiteLocationRef> <!-- optional -->
                                                                <ListID >IDTYPE</ListID> <!-- optional -->
                                                                <FullName >STRTYPE</FullName> <!-- optional -->
                                                        </InventorySiteLocationRef>
                                                        <!-- BEGIN OR -->
                                                                <SerialNumber >STRTYPE</SerialNumber> <!-- optional -->
                                                        <!-- OR -->
                                                                <LotNumber >STRTYPE</LotNumber> <!-- optional -->
                                                        <!-- END OR -->
                                                        <ExpirationDateForSerialLotNumber>STRTYPE</ExpirationDateForSerialLotNumber> <!-- optional -->
                                                        <Desc >STRTYPE</Desc> <!-- optional -->
                                                        <Quantity >QUANTYPE</Quantity> <!-- optional -->
                                                        <UnitOfMeasure >STRTYPE</UnitOfMeasure> <!-- optional -->
                                                        <OverrideUOMSetRef> <!-- optional -->
                                                                <ListID >IDTYPE</ListID> <!-- optional -->
                                                                <FullName >STRTYPE</FullName> <!-- optional -->
                                                        </OverrideUOMSetRef>
                                                        <Cost >PRICETYPE</Cost> <!-- optional -->
                                                        <Amount >AMTTYPE</Amount> <!-- optional -->
                                                        <CustomerRef> <!-- optional -->
                                                                <ListID >IDTYPE</ListID> <!-- optional -->
                                                                <FullName >STRTYPE</FullName> <!-- optional -->
                                                        </CustomerRef>
                                                        <ClassRef> <!-- optional -->
                                                                <ListID >IDTYPE</ListID> <!-- optional -->
                                                                <FullName >STRTYPE</FullName> <!-- optional -->
                                                        </ClassRef>
                                                        <SalesTaxCodeRef> <!-- optional -->
                                                                <ListID >IDTYPE</ListID> <!-- optional -->
                                                                <FullName >STRTYPE</FullName> <!-- optional -->
                                                        </SalesTaxCodeRef>
                                                        <!-- BillableStatus may have one of the following values: Billable, NotBillable, HasBeenBilled -->
                                                        <BillableStatus >ENUMTYPE</BillableStatus> <!-- optional -->
                                                        <SalesRepRef> <!-- optional -->
                                                                <ListID >IDTYPE</ListID> <!-- optional -->
                                                                <FullName >STRTYPE</FullName> <!-- optional -->
                                                        </SalesRepRef>
                                                        <DataExtRet> <!-- optional, may repeat -->
                                                                <OwnerID >GUIDTYPE</OwnerID> <!-- optional -->
                                                                <DataExtName >STRTYPE</DataExtName> <!-- required -->
                                                                <!-- DataExtType may have one of the following values: AMTTYPE, DATETIMETYPE, INTTYPE, PERCENTTYPE, PRICETYPE, QUANTYPE, STR1024TYPE, STR255TYPE -->
                                                                <DataExtType >ENUMTYPE</DataExtType> <!-- required -->
                                                                <DataExtValue >STRTYPE</DataExtValue> <!-- required -->
                                                        </DataExtRet>
                                                </ItemLineRet>
                                                <DataExt> <!-- optional, may repeat -->
                                                        <OwnerID >GUIDTYPE</OwnerID> <!-- required -->
                                                        <DataExtName >STRTYPE</DataExtName> <!-- required -->
                                                        <DataExtValue >STRTYPE</DataExtValue> <!-- required -->
                                                </DataExt>
                                        </ItemGroupLineRet>
                                <!-- END OR -->
                                <DataExtRet> <!-- optional, may repeat -->
                                        <OwnerID >GUIDTYPE</OwnerID> <!-- optional -->
                                        <DataExtName >STRTYPE</DataExtName> <!-- required -->
                                        <!-- DataExtType may have one of the following values: AMTTYPE, DATETIMETYPE, INTTYPE, PERCENTTYPE, PRICETYPE, QUANTYPE, STR1024TYPE, STR255TYPE -->
                                        <DataExtType >ENUMTYPE</DataExtType> <!-- required -->
                                        <DataExtValue >STRTYPE</DataExtValue> <!-- required -->
                                </DataExtRet>
                        </ItemReceiptRet>
                </ItemReceiptQueryRs>
        </QBXMLMsgsRq>
</QBXML>
```

## ItemSalesTaxGroupQuery
### XMLOps
```
<?xml version="1.0" encoding="utf-8"?>
<?qbxml version="16.0"?>
<QBXML>
        <QBXMLMsgsRq onError="stopOnError">
                <ItemSalesTaxGroupQueryRq metaData="ENUMTYPE" iterator="ENUMTYPE" iteratorID="UUIDTYPE">
                        <!-- BEGIN OR -->
                                <ListID >IDTYPE</ListID> <!-- optional, may repeat -->
                        <!-- OR -->
                                <FullName >STRTYPE</FullName> <!-- optional, may repeat -->
                        <!-- OR -->
                                <MaxReturned >INTTYPE</MaxReturned> <!-- optional -->
                                <!-- ActiveStatus may have one of the following values: ActiveOnly [DEFAULT], InactiveOnly, All -->
                                <ActiveStatus >ENUMTYPE</ActiveStatus> <!-- optional -->
                                <FromModifiedDate >DATETIMETYPE</FromModifiedDate> <!-- optional -->
                                <ToModifiedDate >DATETIMETYPE</ToModifiedDate> <!-- optional -->
                                <!-- BEGIN OR -->
                                        <NameFilter> <!-- optional -->
                                                <!-- MatchCriterion may have one of the following values: StartsWith, Contains, EndsWith -->
                                                <MatchCriterion >ENUMTYPE</MatchCriterion> <!-- required -->
                                                <Name >STRTYPE</Name> <!-- required -->
                                        </NameFilter>
                                <!-- OR -->
                                        <NameRangeFilter> <!-- optional -->
                                                <FromName >STRTYPE</FromName> <!-- optional -->
                                                <ToName >STRTYPE</ToName> <!-- optional -->
                                        </NameRangeFilter>
                                <!-- END OR -->
                        <!-- END OR -->
                        <IncludeRetElement >STRTYPE</IncludeRetElement> <!-- optional, may repeat -->
                        <OwnerID >GUIDTYPE</OwnerID> <!-- optional, may repeat -->
                </ItemSalesTaxGroupQueryRq>

                <ItemSalesTaxGroupQueryRs statusCode="INTTYPE" statusSeverity="STRTYPE" statusMessage="STRTYPE" retCount="INTTYPE" iteratorRemainingCount="INTTYPE" iteratorID="UUIDTYPE">
                        <ItemSalesTaxGroupRet> <!-- optional, may repeat -->
                                <ListID >IDTYPE</ListID> <!-- required -->
                                <TimeCreated >DATETIMETYPE</TimeCreated> <!-- required -->
                                <TimeModified >DATETIMETYPE</TimeModified> <!-- required -->
                                <EditSequence >STRTYPE</EditSequence> <!-- required -->
                                <Name >STRTYPE</Name> <!-- required -->
                                <BarCodeValue >STRTYPE</BarCodeValue> <!-- optional -->
                                <IsActive >BOOLTYPE</IsActive> <!-- optional -->
                                <ItemDesc >STRTYPE</ItemDesc> <!-- optional -->
                                <ExternalGUID >GUIDTYPE</ExternalGUID> <!-- optional -->
                                <ItemSalesTaxRef> <!-- optional, may repeat -->
                                        <ListID >IDTYPE</ListID> <!-- optional -->
                                        <FullName >STRTYPE</FullName> <!-- optional -->
                                </ItemSalesTaxRef>
                                <DataExtRet> <!-- optional, may repeat -->
                                        <OwnerID >GUIDTYPE</OwnerID> <!-- optional -->
                                        <DataExtName >STRTYPE</DataExtName> <!-- required -->
                                        <!-- DataExtType may have one of the following values: AMTTYPE, DATETIMETYPE, INTTYPE, PERCENTTYPE, PRICETYPE, QUANTYPE, STR1024TYPE, STR255TYPE -->
                                        <DataExtType >ENUMTYPE</DataExtType> <!-- required -->
                                        <DataExtValue >STRTYPE</DataExtValue> <!-- required -->
                                </DataExtRet>
                        </ItemSalesTaxGroupRet>
                </ItemSalesTaxGroupQueryRs>
        </QBXMLMsgsRq>
</QBXML>
```

## ItemSalesTaxQuery
### XMLOps
```
<?xml version="1.0" encoding="utf-8"?>
<?qbxml version="16.0"?>
<QBXML>
        <QBXMLMsgsRq onError="stopOnError">
                <ItemSalesTaxQueryRq metaData="ENUMTYPE" iterator="ENUMTYPE" iteratorID="UUIDTYPE">
                        <!-- BEGIN OR -->
                                <ListID >IDTYPE</ListID> <!-- optional, may repeat -->
                        <!-- OR -->
                                <FullName >STRTYPE</FullName> <!-- optional, may repeat -->
                        <!-- OR -->
                                <MaxReturned >INTTYPE</MaxReturned> <!-- optional -->
                                <!-- ActiveStatus may have one of the following values: ActiveOnly [DEFAULT], InactiveOnly, All -->
                                <ActiveStatus >ENUMTYPE</ActiveStatus> <!-- optional -->
                                <FromModifiedDate >DATETIMETYPE</FromModifiedDate> <!-- optional -->
                                <ToModifiedDate >DATETIMETYPE</ToModifiedDate> <!-- optional -->
                                <!-- BEGIN OR -->
                                        <NameFilter> <!-- optional -->
                                                <!-- MatchCriterion may have one of the following values: StartsWith, Contains, EndsWith -->
                                                <MatchCriterion >ENUMTYPE</MatchCriterion> <!-- required -->
                                                <Name >STRTYPE</Name> <!-- required -->
                                        </NameFilter>
                                <!-- OR -->
                                        <NameRangeFilter> <!-- optional -->
                                                <FromName >STRTYPE</FromName> <!-- optional -->
                                                <ToName >STRTYPE</ToName> <!-- optional -->
                                        </NameRangeFilter>
                                <!-- END OR -->
                                <ClassFilter> <!-- optional -->
                                        <!-- BEGIN OR -->
                                                <ListID >IDTYPE</ListID> <!-- optional, may repeat -->
                                        <!-- OR -->
                                                <FullName >STRTYPE</FullName> <!-- optional, may repeat -->
                                        <!-- OR -->
                                                <ListIDWithChildren >IDTYPE</ListIDWithChildren> <!-- optional -->
                                        <!-- OR -->
                                                <FullNameWithChildren >STRTYPE</FullNameWithChildren> <!-- optional -->
                                        <!-- END OR -->
                                </ClassFilter>
                        <!-- END OR -->
                        <IncludeRetElement >STRTYPE</IncludeRetElement> <!-- optional, may repeat -->
                        <OwnerID >GUIDTYPE</OwnerID> <!-- optional, may repeat -->
                </ItemSalesTaxQueryRq>

                <ItemSalesTaxQueryRs statusCode="INTTYPE" statusSeverity="STRTYPE" statusMessage="STRTYPE" retCount="INTTYPE" iteratorRemainingCount="INTTYPE" iteratorID="UUIDTYPE">
                        <ItemSalesTaxRet> <!-- optional, may repeat -->
                                <ListID >IDTYPE</ListID> <!-- required -->
                                <TimeCreated >DATETIMETYPE</TimeCreated> <!-- required -->
                                <TimeModified >DATETIMETYPE</TimeModified> <!-- required -->
                                <EditSequence >STRTYPE</EditSequence> <!-- required -->
                                <Name >STRTYPE</Name> <!-- required -->
                                <BarCodeValue >STRTYPE</BarCodeValue> <!-- optional -->
                                <IsActive >BOOLTYPE</IsActive> <!-- optional -->
                                <ClassRef> <!-- optional -->
                                        <ListID >IDTYPE</ListID> <!-- optional -->
                                        <FullName >STRTYPE</FullName> <!-- optional -->
                                </ClassRef>
                                <ItemDesc >STRTYPE</ItemDesc> <!-- optional -->
                                <TaxRate >PERCENTTYPE</TaxRate> <!-- optional -->
                                <TaxVendorRef> <!-- optional -->
                                        <ListID >IDTYPE</ListID> <!-- optional -->
                                        <FullName >STRTYPE</FullName> <!-- optional -->
                                </TaxVendorRef>
                                <SalesTaxReturnLineRef> <!-- optional -->
                                        <ListID >IDTYPE</ListID> <!-- optional -->
                                        <FullName >STRTYPE</FullName> <!-- optional -->
                                </SalesTaxReturnLineRef>
                                <ExternalGUID >GUIDTYPE</ExternalGUID> <!-- optional -->
                                <DataExtRet> <!-- optional, may repeat -->
                                        <OwnerID >GUIDTYPE</OwnerID> <!-- optional -->
                                        <DataExtName >STRTYPE</DataExtName> <!-- required -->
                                        <!-- DataExtType may have one of the following values: AMTTYPE, DATETIMETYPE, INTTYPE, PERCENTTYPE, PRICETYPE, QUANTYPE, STR1024TYPE, STR255TYPE -->
                                        <DataExtType >ENUMTYPE</DataExtType> <!-- required -->
                                        <DataExtValue >STRTYPE</DataExtValue> <!-- required -->
                                </DataExtRet>
                        </ItemSalesTaxRet>
                </ItemSalesTaxQueryRs>
        </QBXMLMsgsRq>
</QBXML>
```
## ItemServiceQuery
### XMLOps
```
<?xml version="1.0" encoding="utf-8"?>
<?qbxml version="16.0"?>
<QBXML>
        <QBXMLMsgsRq onError="stopOnError">
                <ItemServiceQueryRq metaData="ENUMTYPE" iterator="ENUMTYPE" iteratorID="UUIDTYPE">
                        <!-- BEGIN OR -->
                                <ListID >IDTYPE</ListID> <!-- optional, may repeat -->
                        <!-- OR -->
                                <FullName >STRTYPE</FullName> <!-- optional, may repeat -->
                        <!-- OR -->
                                <MaxReturned >INTTYPE</MaxReturned> <!-- optional -->
                                <!-- ActiveStatus may have one of the following values: ActiveOnly [DEFAULT], InactiveOnly, All -->
                                <ActiveStatus >ENUMTYPE</ActiveStatus> <!-- optional -->
                                <FromModifiedDate >DATETIMETYPE</FromModifiedDate> <!-- optional -->
                                <ToModifiedDate >DATETIMETYPE</ToModifiedDate> <!-- optional -->
                                <!-- BEGIN OR -->
                                        <NameFilter> <!-- optional -->
                                                <!-- MatchCriterion may have one of the following values: StartsWith, Contains, EndsWith -->
                                                <MatchCriterion >ENUMTYPE</MatchCriterion> <!-- required -->
                                                <Name >STRTYPE</Name> <!-- required -->
                                        </NameFilter>
                                <!-- OR -->
                                        <NameRangeFilter> <!-- optional -->
                                                <FromName >STRTYPE</FromName> <!-- optional -->
                                                <ToName >STRTYPE</ToName> <!-- optional -->
                                        </NameRangeFilter>
                                <!-- END OR -->
                                <ClassFilter> <!-- optional -->
                                        <!-- BEGIN OR -->
                                                <ListID >IDTYPE</ListID> <!-- optional, may repeat -->
                                        <!-- OR -->
                                                <FullName >STRTYPE</FullName> <!-- optional, may repeat -->
                                        <!-- OR -->
                                                <ListIDWithChildren >IDTYPE</ListIDWithChildren> <!-- optional -->
                                        <!-- OR -->
                                                <FullNameWithChildren >STRTYPE</FullNameWithChildren> <!-- optional -->
                                        <!-- END OR -->
                                </ClassFilter>
                        <!-- END OR -->
                        <IncludeRetElement >STRTYPE</IncludeRetElement> <!-- optional, may repeat -->
                        <OwnerID >GUIDTYPE</OwnerID> <!-- optional, may repeat -->
                </ItemServiceQueryRq>

                <ItemServiceQueryRs statusCode="INTTYPE" statusSeverity="STRTYPE" statusMessage="STRTYPE" retCount="INTTYPE" iteratorRemainingCount="INTTYPE" iteratorID="UUIDTYPE">
                        <ItemServiceRet> <!-- optional, may repeat -->
                                <ListID >IDTYPE</ListID> <!-- required -->
                                <TimeCreated >DATETIMETYPE</TimeCreated> <!-- required -->
                                <TimeModified >DATETIMETYPE</TimeModified> <!-- required -->
                                <EditSequence >STRTYPE</EditSequence> <!-- required -->
                                <Name >STRTYPE</Name> <!-- required -->
                                <FullName >STRTYPE</FullName> <!-- required -->
                                <BarCodeValue >STRTYPE</BarCodeValue> <!-- optional -->
                                <IsActive >BOOLTYPE</IsActive> <!-- optional -->
                                <ClassRef> <!-- optional -->
                                        <ListID >IDTYPE</ListID> <!-- optional -->
                                        <FullName >STRTYPE</FullName> <!-- optional -->
                                </ClassRef>
                                <ParentRef> <!-- optional -->
                                        <ListID >IDTYPE</ListID> <!-- optional -->
                                        <FullName >STRTYPE</FullName> <!-- optional -->
                                </ParentRef>
                                <Sublevel >INTTYPE</Sublevel> <!-- required -->
                                <UnitOfMeasureSetRef> <!-- optional -->
                                        <ListID >IDTYPE</ListID> <!-- optional -->
                                        <FullName >STRTYPE</FullName> <!-- optional -->
                                </UnitOfMeasureSetRef>
                                <IsTaxIncluded >BOOLTYPE</IsTaxIncluded> <!-- optional -->
                                <SalesTaxCodeRef> <!-- optional -->
                                        <ListID >IDTYPE</ListID> <!-- optional -->
                                        <FullName >STRTYPE</FullName> <!-- optional -->
                                </SalesTaxCodeRef>
                                <!-- BEGIN OR -->
                                        <SalesOrPurchase> <!-- optional -->
                                                <Desc >STRTYPE</Desc> <!-- optional -->
                                                <!-- BEGIN OR -->
                                                        <Price >PRICETYPE</Price> <!-- optional -->
                                                <!-- OR -->
                                                        <PricePercent >PERCENTTYPE</PricePercent> <!-- optional -->
                                                <!-- END OR -->
                                                <AccountRef> <!-- optional -->
                                                        <ListID >IDTYPE</ListID> <!-- optional -->
                                                        <FullName >STRTYPE</FullName> <!-- optional -->
                                                </AccountRef>
                                        </SalesOrPurchase>
                                <!-- OR -->
                                        <SalesAndPurchase> <!-- optional -->
                                                <SalesDesc >STRTYPE</SalesDesc> <!-- optional -->
                                                <SalesPrice >PRICETYPE</SalesPrice> <!-- optional -->
                                                <IncomeAccountRef> <!-- optional -->
                                                        <ListID >IDTYPE</ListID> <!-- optional -->
                                                        <FullName >STRTYPE</FullName> <!-- optional -->
                                                </IncomeAccountRef>
                                                <PurchaseDesc >STRTYPE</PurchaseDesc> <!-- optional -->
                                                <PurchaseCost >PRICETYPE</PurchaseCost> <!-- optional -->
                                                <PurchaseTaxCodeRef> <!-- optional -->
                                                        <ListID >IDTYPE</ListID> <!-- optional -->
                                                        <FullName >STRTYPE</FullName> <!-- optional -->
                                                </PurchaseTaxCodeRef>
                                                <ExpenseAccountRef> <!-- optional -->
                                                        <ListID >IDTYPE</ListID> <!-- optional -->
                                                        <FullName >STRTYPE</FullName> <!-- optional -->
                                                </ExpenseAccountRef>
                                                <PrefVendorRef> <!-- optional -->
                                                        <ListID >IDTYPE</ListID> <!-- optional -->
                                                        <FullName >STRTYPE</FullName> <!-- optional -->
                                                </PrefVendorRef>
                                        </SalesAndPurchase>
                                <!-- END OR -->
                                <ExternalGUID >GUIDTYPE</ExternalGUID> <!-- optional -->
                                <DataExtRet> <!-- optional, may repeat -->
                                        <OwnerID >GUIDTYPE</OwnerID> <!-- optional -->
                                        <DataExtName >STRTYPE</DataExtName> <!-- required -->
                                        <!-- DataExtType may have one of the following values: AMTTYPE, DATETIMETYPE, INTTYPE, PERCENTTYPE, PRICETYPE, QUANTYPE, STR1024TYPE, STR255TYPE -->
                                        <DataExtType >ENUMTYPE</DataExtType> <!-- required -->
                                        <DataExtValue >STRTYPE</DataExtValue> <!-- required -->
                                </DataExtRet>
                        </ItemServiceRet>
                </ItemServiceQueryRs>
        </QBXMLMsgsRq>
</QBXML>
```
## ItemSitesQuery
### XMLOps
```
<?xml version="1.0" encoding="utf-8"?>
<?qbxml version="16.0"?>
<QBXML>
        <QBXMLMsgsRq onError="stopOnError">
                <ItemSitesQueryRq metaData="ENUMTYPE" iterator="ENUMTYPE" iteratorID="UUIDTYPE">
                        <!-- BEGIN OR -->
                                <ListID >IDTYPE</ListID> <!-- optional, may repeat -->
                        <!-- OR -->
                                <!-- BEGIN OR -->
                                        <!-- ItemTypeFilter may have one of the following values: AllExceptFixedAsset, Assembly, Discount, FixedAsset, Inventory, InventoryAndAssembly, NonInventory, OtherCharge, Payment, Sales, SalesTax, Service -->
                                        <ItemTypeFilter >ENUMTYPE</ItemTypeFilter> <!-- optional -->
                                <!-- OR -->
                                        <ItemSiteFilter> <!-- optional -->
                                                <ItemFilter> <!-- optional -->
                                                        <!-- BEGIN OR -->
                                                                <ListID >IDTYPE</ListID> <!-- optional, may repeat -->
                                                        <!-- OR -->
                                                                <FullName >STRTYPE</FullName> <!-- optional, may repeat -->
                                                        <!-- OR -->
                                                                <ListIDWithChildren >IDTYPE</ListIDWithChildren> <!-- optional -->
                                                        <!-- OR -->
                                                                <FullNameWithChildren >STRTYPE</FullNameWithChildren> <!-- optional -->
                                                        <!-- END OR -->
                                                </ItemFilter>
                                                <SiteFilter> <!-- optional -->
                                                        <!-- BEGIN OR -->
                                                                <ListID >IDTYPE</ListID> <!-- optional, may repeat -->
                                                        <!-- OR -->
                                                                <FullName >STRTYPE</FullName> <!-- optional, may repeat -->
                                                        <!-- END OR -->
                                                </SiteFilter>
                                        </ItemSiteFilter>
                                <!-- END OR -->
                        <!-- END OR -->
                        <MaxReturned >INTTYPE</MaxReturned> <!-- optional -->
                        <!-- ActiveStatus may have one of the following values: ActiveOnly [DEFAULT], InactiveOnly, All -->
                        <ActiveStatus >ENUMTYPE</ActiveStatus> <!-- optional -->
                        <IncludeRetElement >STRTYPE</IncludeRetElement> <!-- optional, may repeat -->
                </ItemSitesQueryRq>

                <ItemSitesQueryRs statusCode="INTTYPE" statusSeverity="STRTYPE" statusMessage="STRTYPE" retCount="INTTYPE" iteratorRemainingCount="INTTYPE" iteratorID="UUIDTYPE">
                        <ItemSitesRet> <!-- optional, may repeat -->
                                <ListID >IDTYPE</ListID> <!-- optional -->
                                <TimeCreated >DATETIMETYPE</TimeCreated> <!-- optional -->
                                <TimeModified >DATETIMETYPE</TimeModified> <!-- optional -->
                                <EditSequence >STRTYPE</EditSequence> <!-- optional -->
                                <!-- BEGIN OR -->
                                        <ItemInventoryAssemblyRef> <!-- optional -->
                                                <ListID >IDTYPE</ListID> <!-- optional -->
                                                <FullName >STRTYPE</FullName> <!-- optional -->
                                        </ItemInventoryAssemblyRef>
                                <!-- OR -->
                                        <ItemInventoryRef> <!-- optional -->
                                                <ListID >IDTYPE</ListID> <!-- optional -->
                                                <FullName >STRTYPE</FullName> <!-- optional -->
                                        </ItemInventoryRef>
                                <!-- END OR -->
                                <InventorySiteRef> <!-- optional -->
                                        <ListID >IDTYPE</ListID> <!-- optional -->
                                        <FullName >STRTYPE</FullName> <!-- optional -->
                                </InventorySiteRef>
                                <InventorySiteLocationRef> <!-- optional -->
                                        <ListID >IDTYPE</ListID> <!-- optional -->
                                        <FullName >STRTYPE</FullName> <!-- optional -->
                                </InventorySiteLocationRef>
                                <ReorderLevel >QUANTYPE</ReorderLevel> <!-- optional -->
                                <QuantityOnHand >QUANTYPE</QuantityOnHand> <!-- optional -->
                                <QuantityOnPurchaseOrders >QUANTYPE</QuantityOnPurchaseOrders> <!-- optional -->
                                <QuantityOnSalesOrders >QUANTYPE</QuantityOnSalesOrders> <!-- optional -->
                                <QuantityToBeBuiltByPendingBuildTxns >QUANTYPE</QuantityToBeBuiltByPendingBuildTxns> <!-- optional -->
                                <QuantityRequiredByPendingBuildTxns >QUANTYPE</QuantityRequiredByPendingBuildTxns> <!-- optional -->
                                <QuantityOnPendingTransfers >QUANTYPE</QuantityOnPendingTransfers> <!-- optional -->
                                <AssemblyBuildPoint >QUANTYPE</AssemblyBuildPoint> <!-- optional -->
                        </ItemSitesRet>
                </ItemSitesQueryRs>
        </QBXMLMsgsRq>
</QBXML>
```
## ItemSubtotalQuery
### XMLOps
```
<?xml version="1.0" encoding="utf-8"?>
<?qbxml version="16.0"?>
<QBXML>
        <QBXMLMsgsRq onError="stopOnError">
                <ItemSubtotalQueryRq metaData="ENUMTYPE" iterator="ENUMTYPE" iteratorID="UUIDTYPE">
                        <!-- BEGIN OR -->
                                <ListID >IDTYPE</ListID> <!-- optional, may repeat -->
                        <!-- OR -->
                                <FullName >STRTYPE</FullName> <!-- optional, may repeat -->
                        <!-- OR -->
                                <MaxReturned >INTTYPE</MaxReturned> <!-- optional -->
                                <!-- ActiveStatus may have one of the following values: ActiveOnly [DEFAULT], InactiveOnly, All -->
                                <ActiveStatus >ENUMTYPE</ActiveStatus> <!-- optional -->
                                <FromModifiedDate >DATETIMETYPE</FromModifiedDate> <!-- optional -->
                                <ToModifiedDate >DATETIMETYPE</ToModifiedDate> <!-- optional -->
                                <!-- BEGIN OR -->
                                        <NameFilter> <!-- optional -->
                                                <!-- MatchCriterion may have one of the following values: StartsWith, Contains, EndsWith -->
                                                <MatchCriterion >ENUMTYPE</MatchCriterion> <!-- required -->
                                                <Name >STRTYPE</Name> <!-- required -->
                                        </NameFilter>
                                <!-- OR -->
                                        <NameRangeFilter> <!-- optional -->
                                                <FromName >STRTYPE</FromName> <!-- optional -->
                                                <ToName >STRTYPE</ToName> <!-- optional -->
                                        </NameRangeFilter>
                                <!-- END OR -->
                        <!-- END OR -->
                        <IncludeRetElement >STRTYPE</IncludeRetElement> <!-- optional, may repeat -->
                        <OwnerID >GUIDTYPE</OwnerID> <!-- optional, may repeat -->
                </ItemSubtotalQueryRq>

                <ItemSubtotalQueryRs statusCode="INTTYPE" statusSeverity="STRTYPE" statusMessage="STRTYPE" retCount="INTTYPE" iteratorRemainingCount="INTTYPE" iteratorID="UUIDTYPE">
                        <ItemSubtotalRet> <!-- optional, may repeat -->
                                <ListID >IDTYPE</ListID> <!-- required -->
                                <TimeCreated >DATETIMETYPE</TimeCreated> <!-- required -->
                                <TimeModified >DATETIMETYPE</TimeModified> <!-- required -->
                                <EditSequence >STRTYPE</EditSequence> <!-- required -->
                                <Name >STRTYPE</Name> <!-- required -->
                                <BarCodeValue >STRTYPE</BarCodeValue> <!-- optional -->
                                <IsActive >BOOLTYPE</IsActive> <!-- optional -->
                                <ItemDesc >STRTYPE</ItemDesc> <!-- optional -->
                                <!-- SpecialItemType may have one of the following values: FinanceCharge, ReimbursableExpenseGroup, ReimbursableExpenseSubtotal -->
                                <SpecialItemType >ENUMTYPE</SpecialItemType> <!-- optional -->
                                <ExternalGUID >GUIDTYPE</ExternalGUID> <!-- optional -->
                                <DataExtRet> <!-- optional, may repeat -->
                                        <OwnerID >GUIDTYPE</OwnerID> <!-- optional -->
                                        <DataExtName >STRTYPE</DataExtName> <!-- required -->
                                        <!-- DataExtType may have one of the following values: AMTTYPE, DATETIMETYPE, INTTYPE, PERCENTTYPE, PRICETYPE, QUANTYPE, STR1024TYPE, STR255TYPE -->
                                        <DataExtType >ENUMTYPE</DataExtType> <!-- required -->
                                        <DataExtValue >STRTYPE</DataExtValue> <!-- required -->
                                </DataExtRet>
                        </ItemSubtotalRet>
                </ItemSubtotalQueryRs>
        </QBXMLMsgsRq>
</QBXML>
```

## JobReportQuery
### XMLOps
```
<?xml version="1.0" encoding="utf-8"?>
<?qbxml version="16.0"?>
<QBXML>
        <QBXMLMsgsRq onError="stopOnError">
                <JobReportQueryRq>
                        <!-- JobReportType may have one of the following values: ItemEstimatesVsActuals, ItemProfitability, JobEstimatesVsActualsDetail, JobEstimatesVsActualsSummary, JobProfitabilityDetail, JobProfitabilitySummary,  -->
                        <JobReportType >ENUMTYPE</JobReportType> <!-- required -->
                        <DisplayReport >BOOLTYPE</DisplayReport> <!-- optional -->
                        <!-- BEGIN OR -->
                                <ReportPeriod> <!-- optional -->
                                        <FromReportDate >DATETYPE</FromReportDate> <!-- optional -->
                                        <ToReportDate >DATETYPE</ToReportDate> <!-- optional -->
                                </ReportPeriod>
                        <!-- OR -->
                                <!-- ReportDateMacro may have one of the following values: All, Today, ThisWeek, ThisWeekToDate, ThisMonth, ThisMonthToDate, ThisQuarter, ThisQuarterToDate, ThisYear, ThisYearToDate, Yesterday, LastWeek, LastWeekToDate, LastMonth, LastMonthToDate, LastQuarter, LastQuarterToDate, LastYear, LastYearToDate, NextWeek, NextFourWeeks, NextMonth, NextQuarter, NextYear -->
                                <ReportDateMacro >ENUMTYPE</ReportDateMacro> <!-- optional -->
                        <!-- END OR -->
                        <ReportAccountFilter> <!-- optional -->
                                <!-- BEGIN OR -->
                                        <!-- AccountTypeFilter may have one of the following values: AccountsPayable, AccountsReceivable, AllowedFor1099, APAndSalesTax, APOrCreditCard, ARAndAP, Asset, BalanceSheet, Bank, BankAndARAndAPAndUF, BankAndUF, CostOfSales, CreditCard, CurrentAsset, CurrentAssetAndExpense, CurrentLiability, Equity, EquityAndIncomeAndExpense, ExpenseAndOtherExpense, FixedAsset, IncomeAndExpense, IncomeAndOtherIncome, Liability, LiabilityAndEquity, LongTermLiability, NonPosting, OrdinaryExpense, OrdinaryIncome, OrdinaryIncomeAndCOGS, OrdinaryIncomeAndExpense, OtherAsset, OtherCurrentAsset, OtherCurrentLiability, OtherExpense, OtherIncome, OtherIncomeOrExpense -->
                                        <AccountTypeFilter >ENUMTYPE</AccountTypeFilter> <!-- optional -->
                                <!-- OR -->
                                        <ListID >IDTYPE</ListID> <!-- optional, may repeat -->
                                <!-- OR -->
                                        <FullName >STRTYPE</FullName> <!-- optional, may repeat -->
                                <!-- OR -->
                                        <ListIDWithChildren >IDTYPE</ListIDWithChildren> <!-- optional -->
                                <!-- OR -->
                                        <FullNameWithChildren >STRTYPE</FullNameWithChildren> <!-- optional -->
                                <!-- END OR -->
                        </ReportAccountFilter>
                        <ReportEntityFilter> <!-- optional -->
                                <!-- BEGIN OR -->
                                        <!-- EntityTypeFilter may have one of the following values: Customer, Employee, OtherName, Vendor -->
                                        <EntityTypeFilter >ENUMTYPE</EntityTypeFilter> <!-- optional -->
                                <!-- OR -->
                                        <ListID >IDTYPE</ListID> <!-- optional, may repeat -->
                                <!-- OR -->
                                        <FullName >STRTYPE</FullName> <!-- optional, may repeat -->
                                <!-- OR -->
                                        <ListIDWithChildren >IDTYPE</ListIDWithChildren> <!-- optional -->
                                <!-- OR -->
                                        <FullNameWithChildren >STRTYPE</FullNameWithChildren> <!-- optional -->
                                <!-- END OR -->
                        </ReportEntityFilter>
                        <ReportItemFilter> <!-- optional -->
                                <!-- BEGIN OR -->
                                        <!-- ItemTypeFilter may have one of the following values: AllExceptFixedAsset, Assembly, Discount, FixedAsset, Inventory, InventoryAndAssembly, NonInventory, OtherCharge, Payment, Sales, SalesTax, Service -->
                                        <ItemTypeFilter >ENUMTYPE</ItemTypeFilter> <!-- optional -->
                                <!-- OR -->
                                        <ListID >IDTYPE</ListID> <!-- optional, may repeat -->
                                <!-- OR -->
                                        <FullName >STRTYPE</FullName> <!-- optional, may repeat -->
                                <!-- OR -->
                                        <ListIDWithChildren >IDTYPE</ListIDWithChildren> <!-- optional -->
                                <!-- OR -->
                                        <FullNameWithChildren >STRTYPE</FullNameWithChildren> <!-- optional -->
                                <!-- END OR -->
                        </ReportItemFilter>
                        <ReportClassFilter> <!-- optional -->
                                <!-- BEGIN OR -->
                                        <ListID >IDTYPE</ListID> <!-- optional, may repeat -->
                                <!-- OR -->
                                        <FullName >STRTYPE</FullName> <!-- optional, may repeat -->
                                <!-- OR -->
                                        <ListIDWithChildren >IDTYPE</ListIDWithChildren> <!-- optional -->
                                <!-- OR -->
                                        <FullNameWithChildren >STRTYPE</FullNameWithChildren> <!-- optional -->
                                <!-- END OR -->
                        </ReportClassFilter>
                        <ReportTxnTypeFilter> <!-- optional -->
                                <!-- TxnTypeFilter may have one of the following values: All, ARRefundCreditCard, Bill, BillPaymentCheck, BillPaymentCreditCard, BuildAssembly, Charge, Check, CreditCardCharge, CreditCardCredit, CreditMemo, Deposit, Estimate, InventoryAdjustment, Invoice, ItemReceipt, JournalEntry, LiabilityAdjustment, Paycheck, PayrollLiabilityCheck, PurchaseOrder, ReceivePayment, SalesOrder, SalesReceipt, SalesTaxPaymentCheck, Transfer, VendorCredit, YTDAdjustment -->
                                <TxnTypeFilter >ENUMTYPE</TxnTypeFilter> <!-- required, may repeat -->
                        </ReportTxnTypeFilter>
                        <!-- BEGIN OR -->
                                <ReportModifiedDateRangeFilter> <!-- optional -->
                                        <FromReportModifiedDate >DATETYPE</FromReportModifiedDate> <!-- optional -->
                                        <ToReportModifiedDate >DATETYPE</ToReportModifiedDate> <!-- optional -->
                                </ReportModifiedDateRangeFilter>
                        <!-- OR -->
                                <!-- ReportModifiedDateRangeMacro may have one of the following values: All, Today, ThisWeek, ThisWeekToDate, ThisMonth, ThisMonthToDate, ThisQuarter, ThisQuarterToDate, ThisYear, ThisYearToDate, Yesterday, LastWeek, LastWeekToDate, LastMonth, LastMonthToDate, LastQuarter, LastQuarterToDate, LastYear, LastYearToDate, NextWeek, NextFourWeeks, NextMonth, NextQuarter, NextYear -->
                                <ReportModifiedDateRangeMacro >ENUMTYPE</ReportModifiedDateRangeMacro> <!-- optional -->
                        <!-- END OR -->
                        <!-- ReportDetailLevelFilter may have one of the following values: All [DEFAULT], AllExceptSummary, SummaryOnly -->
                        <ReportDetailLevelFilter >ENUMTYPE</ReportDetailLevelFilter> <!-- optional -->
                        <!-- ReportPostingStatusFilter may have one of the following values: Either, NonPosting, Posting -->
                        <ReportPostingStatusFilter >ENUMTYPE</ReportPostingStatusFilter> <!-- optional -->
                        <!-- SummarizeColumnsBy may have one of the following values: Account, BalanceSheet, Class, Customer, CustomerType, Day, Employee, FourWeek, HalfMonth, IncomeStatement, ItemDetail, ItemType, Month, Payee, PaymentMethod, PayrollItemDetail, PayrollYtdDetail, Quarter, SalesRep, SalesTaxCode, ShipMethod, Terms, TotalOnly, TwoWeek, Vendor, VendorType, Week, Year -->
                        <SummarizeColumnsBy >ENUMTYPE</SummarizeColumnsBy> <!-- optional -->
                        <IncludeSubcolumns >BOOLTYPE</IncludeSubcolumns> <!-- optional -->
                </JobReportQueryRq>

                <JobReportQueryRs statusCode="INTTYPE" statusSeverity="STRTYPE" statusMessage="STRTYPE">
                        <ReportRet> <!-- optional -->
                                <ReportTitle >STRTYPE</ReportTitle> <!-- required -->
                                <ReportSubtitle >STRTYPE</ReportSubtitle> <!-- required -->
                                <!-- ReportBasis may have one of the following values: Accrual, Cash, None [DEFAULT] -->
                                <ReportBasis >ENUMTYPE</ReportBasis> <!-- optional -->
                                <NumRows >INTTYPE</NumRows> <!-- required -->
                                <NumColumns >INTTYPE</NumColumns> <!-- required -->
                                <NumColTitleRows >INTTYPE</NumColTitleRows> <!-- required -->
                                <ColDesc colID="INTTYPE" dataType="ENUMTYPE"> <!-- required, may repeat -->
                                        <ColTitle titleRow="INTTYPE" value="STRTYPE"> <!-- required, may repeat -->
                                        </ColTitle>
                                        <!-- ColType may have one of the following values: Account, Addr1, Addr2, Addr3, Addr4, Addr5, Aging, Amount, AmountDifference, AverageCost, BilledDate, BillingStatus, Blank, CalculatedAmount, Class, ClearedStatus, CostPrice, CreateDate, Credit, CustomField, Date, Debit, DeliveryDate, DueDate, Duration, EarliestReceiptDate, EstimateActive, FOB, IncomeSubjectToTax, Invoiced, IsAdjustment, Item, ItemDesc, ItemVendor, Label, LastModifiedBy, LatestOrPriorState, Memo, ModifiedTime, Name, NameAccountNumber, NameAddress, NameCity, NameContact, NameEmail, NameFax, NamePhone, NameState, NameZip, OpenBalance, OriginalAmount, PaidAmount, PaidStatus, PaidThroughDate, PaymentMethod, PayrollItem, Percent, PercentChange, PercentOfTotalRetail, PercentOfTotalValue, PhysicalCount, PONumber, PrintStatus, ProgressAmount, ProgressPercent, Quantity, QuantityAvailable, QuantityOnHand, QuantityOnOrder, QuantityOnPendingBuild, QuantityOnSalesOrder, ReceivedQuantity, RefNumber, ReorderPoint, RetailValueOnHand, RunningBalance, SalesPerWeek, SalesRep, SalesTaxCode, ShipDate, ShipMethod, ShipToAddr1, ShipToAddr2, ShipToAddr3, ShipToAddr4, ShipToAddr5, SONumber, SourceName, SplitAccount, SSNOrTaxID, SuggestedReorder, TaxLine, TaxTableVersion, Terms, Total, TxnID, TxnNumber, TxnType, UnitPrice, UserEdit, ValueOnHand, WageBase, WageBaseTips -->
                                        <ColType >ENUMTYPE</ColType> <!-- required -->
                                </ColDesc>
                                <ReportData> <!-- optional -->
                                        <!-- BEGIN OR -->
                                                <DataRow> <!-- optional -->
                                                        <RowData rowType="ENUMTYPE" value="STRTYPE"> <!-- optional -->
                                                        </RowData>
                                                        <ColData colID="INTTYPE" value="STRTYPE" dataType="ENUMTYPE"> <!-- optional, may repeat -->
                                                        </ColData>
                                                </DataRow>
                                        <!-- OR -->
                                                <TextRow rowNumber="INTTYPE" value="STRTYPE"> <!-- optional -->
                                                </TextRow>
                                        <!-- OR -->
                                                <SubtotalRow> <!-- optional -->
                                                        <RowData rowType="ENUMTYPE" value="STRTYPE"> <!-- optional -->
                                                        </RowData>
                                                        <ColData colID="INTTYPE" value="STRTYPE" dataType="ENUMTYPE"> <!-- optional, may repeat -->
                                                        </ColData>
                                                </SubtotalRow>
                                        <!-- OR -->
                                                <TotalRow> <!-- optional -->
                                                        <RowData rowType="ENUMTYPE" value="STRTYPE"> <!-- optional -->
                                                        </RowData>
                                                        <ColData colID="INTTYPE" value="STRTYPE" dataType="ENUMTYPE"> <!-- optional, may repeat -->
                                                        </ColData>
                                                </TotalRow>
                                        <!-- END OR -->
                                </ReportData>
                        </ReportRet>
                </JobReportQueryRs>
        </QBXMLMsgsRq>
</QBXML>
```

## JobTypeQuery
## XMLOps
```
<?xml version="1.0" encoding="utf-8"?>
<?qbxml version="16.0"?>
<QBXML>
        <QBXMLMsgsRq onError="stopOnError">
                <JobTypeQueryRq metaData="ENUMTYPE">
                        <!-- BEGIN OR -->
                                <ListID >IDTYPE</ListID> <!-- optional, may repeat -->
                        <!-- OR -->
                                <FullName >STRTYPE</FullName> <!-- optional, may repeat -->
                        <!-- OR -->
                                <MaxReturned >INTTYPE</MaxReturned> <!-- optional -->
                                <!-- ActiveStatus may have one of the following values: ActiveOnly [DEFAULT], InactiveOnly, All -->
                                <ActiveStatus >ENUMTYPE</ActiveStatus> <!-- optional -->
                                <FromModifiedDate >DATETIMETYPE</FromModifiedDate> <!-- optional -->
                                <ToModifiedDate >DATETIMETYPE</ToModifiedDate> <!-- optional -->
                                <!-- BEGIN OR -->
                                        <NameFilter> <!-- optional -->
                                                <!-- MatchCriterion may have one of the following values: StartsWith, Contains, EndsWith -->
                                                <MatchCriterion >ENUMTYPE</MatchCriterion> <!-- required -->
                                                <Name >STRTYPE</Name> <!-- required -->
                                        </NameFilter>
                                <!-- OR -->
                                        <NameRangeFilter> <!-- optional -->
                                                <FromName >STRTYPE</FromName> <!-- optional -->
                                                <ToName >STRTYPE</ToName> <!-- optional -->
                                        </NameRangeFilter>
                                <!-- END OR -->
                        <!-- END OR -->
                        <IncludeRetElement >STRTYPE</IncludeRetElement> <!-- optional, may repeat -->
                </JobTypeQueryRq>

                <JobTypeQueryRs statusCode="INTTYPE" statusSeverity="STRTYPE" statusMessage="STRTYPE" retCount="INTTYPE">
                        <JobTypeRet> <!-- optional, may repeat -->
                                <ListID >IDTYPE</ListID> <!-- required -->
                                <TimeCreated >DATETIMETYPE</TimeCreated> <!-- required -->
                                <TimeModified >DATETIMETYPE</TimeModified> <!-- required -->
                                <EditSequence >STRTYPE</EditSequence> <!-- required -->
                                <Name >STRTYPE</Name> <!-- required -->
                                <FullName >STRTYPE</FullName> <!-- required -->
                                <IsActive >BOOLTYPE</IsActive> <!-- optional -->
                                <ParentRef> <!-- optional -->
                                        <ListID >IDTYPE</ListID> <!-- optional -->
                                        <FullName >STRTYPE</FullName> <!-- optional -->
                                </ParentRef>
                                <Sublevel >INTTYPE</Sublevel> <!-- required -->
                        </JobTypeRet>
                </JobTypeQueryRs>
        </QBXMLMsgsRq>
</QBXML>
```
## JournalEntryQuery
In traditional accounting, transactions are entered into the general journal and categorized exclusively by account. In QuickBooks, most transactions can be categorized either by account or by type (invoice, check, and so on). For a few activities in QuickBooks, you must use the general journal directly, for example for recording depreciation. Notice that you must supply the credit line and a corresponding debit line in the same request. It will not work to supply them in two distinct requests. You can supply as many credit lines and debit lines in one single request as you want so long as the total monetary amount from the credits equals the total monetary amount from the debits in that request. Finally, DO NOT supply negative sign for the monetary amounts. QuickBooks does that for you. If you do supply the negative sign amounts will add instead of cancel and you’ll get a runtime error. Querying for Condensed Transactions If you need the query to return condensed transactions, you can do this by using either an Entity or Account filter in the journal query request. Alternatively, you could use the The generic TransactionQuery, which can return condensed transactions.
### XMLOps
```
<?xml version="1.0" encoding="utf-8"?>
<?qbxml version="16.0"?>
<QBXML>
        <QBXMLMsgsRq onError="stopOnError">
                <JournalEntryQueryRq metaData="ENUMTYPE" iterator="ENUMTYPE" iteratorID="UUIDTYPE">
                        <!-- BEGIN OR -->
                                <TxnID >IDTYPE</TxnID> <!-- optional, may repeat -->
                        <!-- OR -->
                                <RefNumber >STRTYPE</RefNumber> <!-- optional, may repeat -->
                        <!-- OR -->
                                <RefNumberCaseSensitive >STRTYPE</RefNumberCaseSensitive> <!-- optional, may repeat -->
                        <!-- OR -->
                                <MaxReturned >INTTYPE</MaxReturned> <!-- optional -->
                                <!-- BEGIN OR -->
                                        <ModifiedDateRangeFilter> <!-- optional -->
                                                <FromModifiedDate >DATETIMETYPE</FromModifiedDate> <!-- optional -->
                                                <ToModifiedDate >DATETIMETYPE</ToModifiedDate> <!-- optional -->
                                        </ModifiedDateRangeFilter>
                                <!-- OR -->
                                        <TxnDateRangeFilter> <!-- optional -->
                                                <!-- BEGIN OR -->
                                                        <FromTxnDate >DATETYPE</FromTxnDate> <!-- optional -->
                                                        <ToTxnDate >DATETYPE</ToTxnDate> <!-- optional -->
                                                <!-- OR -->
                                                        <!-- DateMacro may have one of the following values: All, Today, ThisWeek, ThisWeekToDate, ThisMonth, ThisMonthToDate, ThisCalendarQuarter, ThisCalendarQuarterToDate, ThisFiscalQuarter, ThisFiscalQuarterToDate, ThisCalendarYear, ThisCalendarYearToDate, ThisFiscalYear, ThisFiscalYearToDate, Yesterday, LastWeek, LastWeekToDate, LastMonth, LastMonthToDate, LastCalendarQuarter, LastCalendarQuarterToDate, LastFiscalQuarter, LastFiscalQuarterToDate, LastCalendarYear, LastCalendarYearToDate, LastFiscalYear, LastFiscalYearToDate, NextWeek, NextFourWeeks, NextMonth, NextCalendarQuarter, NextCalendarYear, NextFiscalQuarter, NextFiscalYear -->
                                                        <DateMacro >ENUMTYPE</DateMacro> <!-- optional -->
                                                <!-- END OR -->
                                        </TxnDateRangeFilter>
                                <!-- END OR -->
                                <EntityFilter> <!-- optional -->
                                        <!-- BEGIN OR -->
                                                <ListID >IDTYPE</ListID> <!-- optional, may repeat -->
                                        <!-- OR -->
                                                <FullName >STRTYPE</FullName> <!-- optional, may repeat -->
                                        <!-- OR -->
                                                <ListIDWithChildren >IDTYPE</ListIDWithChildren> <!-- optional -->
                                        <!-- OR -->
                                                <FullNameWithChildren >STRTYPE</FullNameWithChildren> <!-- optional -->
                                        <!-- END OR -->
                                </EntityFilter>
                                <AccountFilter> <!-- optional -->
                                        <!-- BEGIN OR -->
                                                <ListID >IDTYPE</ListID> <!-- optional, may repeat -->
                                        <!-- OR -->
                                                <FullName >STRTYPE</FullName> <!-- optional, may repeat -->
                                        <!-- OR -->
                                                <ListIDWithChildren >IDTYPE</ListIDWithChildren> <!-- optional -->
                                        <!-- OR -->
                                                <FullNameWithChildren >STRTYPE</FullNameWithChildren> <!-- optional -->
                                        <!-- END OR -->
                                </AccountFilter>
                                <!-- BEGIN OR -->
                                        <RefNumberFilter> <!-- optional -->
                                                <!-- MatchCriterion may have one of the following values: StartsWith, Contains, EndsWith -->
                                                <MatchCriterion >ENUMTYPE</MatchCriterion> <!-- required -->
                                                <RefNumber >STRTYPE</RefNumber> <!-- required -->
                                        </RefNumberFilter>
                                <!-- OR -->
                                        <RefNumberRangeFilter> <!-- optional -->
                                                <FromRefNumber >STRTYPE</FromRefNumber> <!-- optional -->
                                                <ToRefNumber >STRTYPE</ToRefNumber> <!-- optional -->
                                        </RefNumberRangeFilter>
                                <!-- END OR -->
                                <CurrencyFilter> <!-- optional -->
                                        <!-- BEGIN OR -->
                                                <ListID >IDTYPE</ListID> <!-- optional, may repeat -->
                                        <!-- OR -->
                                                <FullName >STRTYPE</FullName> <!-- optional, may repeat -->
                                        <!-- END OR -->
                                </CurrencyFilter>
                        <!-- END OR -->
                        <IncludeLineItems >BOOLTYPE</IncludeLineItems> <!-- optional -->
                        <IncludeRetElement >STRTYPE</IncludeRetElement> <!-- optional, may repeat -->
                        <OwnerID >GUIDTYPE</OwnerID> <!-- optional, may repeat -->
                </JournalEntryQueryRq>

                <JournalEntryQueryRs statusCode="INTTYPE" statusSeverity="STRTYPE" statusMessage="STRTYPE" retCount="INTTYPE" iteratorRemainingCount="INTTYPE" iteratorID="UUIDTYPE">
                        <JournalEntryRet> <!-- optional, may repeat -->
                                <TxnID >IDTYPE</TxnID> <!-- required -->
                                <TimeCreated >DATETIMETYPE</TimeCreated> <!-- required -->
                                <TimeModified >DATETIMETYPE</TimeModified> <!-- required -->
                                <EditSequence >STRTYPE</EditSequence> <!-- required -->
                                <TxnNumber >INTTYPE</TxnNumber> <!-- optional -->
                                <TxnDate >DATETYPE</TxnDate> <!-- required -->
                                <RefNumber >STRTYPE</RefNumber> <!-- optional -->
                                <IsAdjustment >BOOLTYPE</IsAdjustment> <!-- optional -->
                                <IsHomeCurrencyAdjustment >BOOLTYPE</IsHomeCurrencyAdjustment> <!-- optional -->
                                <IsAmountsEnteredInHomeCurrency >BOOLTYPE</IsAmountsEnteredInHomeCurrency> <!-- optional -->
                                <CurrencyRef> <!-- optional -->
                                        <ListID >IDTYPE</ListID> <!-- optional -->
                                        <FullName >STRTYPE</FullName> <!-- optional -->
                                </CurrencyRef>
                                <ExchangeRate >FLOATTYPE</ExchangeRate> <!-- optional -->
                                <ExternalGUID >GUIDTYPE</ExternalGUID> <!-- optional -->
                                <!-- BEGIN OR -->
                                        <JournalDebitLine defMacro="MACROTYPE"> <!-- optional -->
                                                <TxnLineID >IDTYPE</TxnLineID> <!-- optional -->
                                                <AccountRef> <!-- optional -->
                                                        <ListID >IDTYPE</ListID> <!-- optional -->
                                                        <FullName >STRTYPE</FullName> <!-- optional -->
                                                </AccountRef>
                                                <Amount >AMTTYPE</Amount> <!-- optional -->
                                                <Memo >STRTYPE</Memo> <!-- optional -->
                                                <EntityRef> <!-- optional -->
                                                        <ListID >IDTYPE</ListID> <!-- optional -->
                                                        <FullName >STRTYPE</FullName> <!-- optional -->
                                                </EntityRef>
                                                <ClassRef> <!-- optional -->
                                                        <ListID >IDTYPE</ListID> <!-- optional -->
                                                        <FullName >STRTYPE</FullName> <!-- optional -->
                                                </ClassRef>
                                                <ItemSalesTaxRef> <!-- optional -->
                                                        <ListID >IDTYPE</ListID> <!-- optional -->
                                                        <FullName >STRTYPE</FullName> <!-- optional -->
                                                </ItemSalesTaxRef>
                                                <!-- BillableStatus may have one of the following values: Billable, NotBillable, HasBeenBilled -->
                                                <BillableStatus >ENUMTYPE</BillableStatus> <!-- optional -->
                                        </JournalDebitLine>
                                <!-- OR -->
                                        <JournalCreditLine defMacro="MACROTYPE"> <!-- optional -->
                                                <TxnLineID >IDTYPE</TxnLineID> <!-- optional -->
                                                <AccountRef> <!-- optional -->
                                                        <ListID >IDTYPE</ListID> <!-- optional -->
                                                        <FullName >STRTYPE</FullName> <!-- optional -->
                                                </AccountRef>
                                                <Amount >AMTTYPE</Amount> <!-- optional -->
                                                <Memo >STRTYPE</Memo> <!-- optional -->
                                                <EntityRef> <!-- optional -->
                                                        <ListID >IDTYPE</ListID> <!-- optional -->
                                                        <FullName >STRTYPE</FullName> <!-- optional -->
                                                </EntityRef>
                                                <ClassRef> <!-- optional -->
                                                        <ListID >IDTYPE</ListID> <!-- optional -->
                                                        <FullName >STRTYPE</FullName> <!-- optional -->
                                                </ClassRef>
                                                <ItemSalesTaxRef> <!-- optional -->
                                                        <ListID >IDTYPE</ListID> <!-- optional -->
                                                        <FullName >STRTYPE</FullName> <!-- optional -->
                                                </ItemSalesTaxRef>
                                                <!-- BillableStatus may have one of the following values: Billable, NotBillable, HasBeenBilled -->
                                                <BillableStatus >ENUMTYPE</BillableStatus> <!-- optional -->
                                        </JournalCreditLine>
                                <!-- END OR -->
                                <DataExtRet> <!-- optional, may repeat -->
                                        <OwnerID >GUIDTYPE</OwnerID> <!-- optional -->
                                        <DataExtName >STRTYPE</DataExtName> <!-- required -->
                                        <!-- DataExtType may have one of the following values: AMTTYPE, DATETIMETYPE, INTTYPE, PERCENTTYPE, PRICETYPE, QUANTYPE, STR1024TYPE, STR255TYPE -->
                                        <DataExtType >ENUMTYPE</DataExtType> <!-- required -->
                                        <DataExtValue >STRTYPE</DataExtValue> <!-- required -->
                                </DataExtRet>
                        </JournalEntryRet>
                </JournalEntryQueryRs>
        </QBXMLMsgsRq>
</QBXML>

```

## LeadQuery
### XMLOps
```
<?xml version="1.0" encoding="utf-8"?>
<?qbxml version="16.0"?>
<QBXML>
        <QBXMLMsgsRq onError="stopOnError">
                <LeadQueryRq metaData="ENUMTYPE" iterator="ENUMTYPE" iteratorID="UUIDTYPE">
                        <!-- BEGIN OR -->
                                <ListID >IDTYPE</ListID> <!-- optional, may repeat -->
                        <!-- OR -->
                                <Name >STRTYPE</Name> <!-- optional, may repeat -->
                        <!-- OR -->
                                <MaxReturned >INTTYPE</MaxReturned> <!-- optional -->
                                <FromModifiedDate >DATETIMETYPE</FromModifiedDate> <!-- optional -->
                                <ToModifiedDate >DATETIMETYPE</ToModifiedDate> <!-- optional -->
                                <!-- BEGIN OR -->
                                        <NameFilter> <!-- optional -->
                                                <!-- MatchCriterion may have one of the following values: StartsWith, Contains, EndsWith -->
                                                <MatchCriterion >ENUMTYPE</MatchCriterion> <!-- required -->
                                                <Name >STRTYPE</Name> <!-- required -->
                                        </NameFilter>
                                <!-- OR -->
                                        <NameRangeFilter> <!-- optional -->
                                                <FromName >STRTYPE</FromName> <!-- optional -->
                                                <ToName >STRTYPE</ToName> <!-- optional -->
                                        </NameRangeFilter>
                                <!-- END OR -->
                        <!-- END OR -->
                        <IncludeRetElement >STRTYPE</IncludeRetElement> <!-- optional, may repeat -->
                </LeadQueryRq>

                <LeadQueryRs statusCode="INTTYPE" statusSeverity="STRTYPE" statusMessage="STRTYPE" retCount="INTTYPE" iteratorRemainingCount="INTTYPE" iteratorID="UUIDTYPE">
                        <LeadRet> <!-- optional, may repeat -->
                                <ListID >IDTYPE</ListID> <!-- required -->
                                <TimeCreated >DATETIMETYPE</TimeCreated> <!-- required -->
                                <TimeModified >DATETIMETYPE</TimeModified> <!-- required -->
                                <EditSequence >STRTYPE</EditSequence> <!-- required -->
                                <FullName >STRTYPE</FullName> <!-- required -->
                                <!-- Status may have one of the following values: Hot [Default], Warm, Cold -->
                                <Status >ENUMTYPE</Status> <!-- optional -->
                                <CompanyName >STRTYPE</CompanyName> <!-- optional -->
                                <MainPhone >STRTYPE</MainPhone> <!-- optional -->
                                <AdditionalContactRef> <!-- must occur 0 - 3 times -->
                                        <ContactName >STRTYPE</ContactName> <!-- required -->
                                        <ContactValue >STRTYPE</ContactValue> <!-- required -->
                                </AdditionalContactRef>
                                <LocationsRet> <!-- optional, may repeat -->
                                        <LocationID >INTTYPE</LocationID> <!-- required -->
                                        <MainAddress >STRTYPE</MainAddress> <!-- required -->
                                        <Location >STRTYPE</Location> <!-- required -->
                                        <LeadAddress> <!-- optional -->
                                                <Addr1 >STRTYPE</Addr1> <!-- optional -->
                                                <Addr2 >STRTYPE</Addr2> <!-- optional -->
                                                <Addr3 >STRTYPE</Addr3> <!-- optional -->
                                                <Addr4 >STRTYPE</Addr4> <!-- optional -->
                                                <Addr5 >STRTYPE</Addr5> <!-- optional -->
                                        </LeadAddress>
                                </LocationsRet>
                                <LeadContactsRet> <!-- optional, may repeat -->
                                        <LeadContactID >INTTYPE</LeadContactID> <!-- required -->
                                        <Salutation >STRTYPE</Salutation> <!-- optional -->
                                        <FirstName >STRTYPE</FirstName> <!-- required -->
                                        <MiddleName >STRTYPE</MiddleName> <!-- optional -->
                                        <LastName >STRTYPE</LastName> <!-- optional -->
                                        <JobTitle >STRTYPE</JobTitle> <!-- optional -->
                                        <AdditionalContactRef> <!-- must occur 0 - 5 times -->
                                                <ContactName >STRTYPE</ContactName> <!-- required -->
                                                <ContactValue >STRTYPE</ContactValue> <!-- required -->
                                        </AdditionalContactRef>
                                        <IsPrimaryContact >BOOLTYPE</IsPrimaryContact> <!-- optional -->
                                </LeadContactsRet>
                        </LeadRet>
                </LeadQueryRs>
        </QBXMLMsgsRq>
</QBXML>
```
## ListDeletedQuery

A ListDeletedQuery will return all list elements deleted within the last 90 days, grouped according to object type.
If you are synchronizing deletes, you might want to specify ListDelType elements in order of dependency in a ListDeletedQuery request; for example, first specify a ListDelType of Item, then specify a ListDelType of Vendor. This way the SDK will return Item deletes before Vendor deletes (both in order of real delete times). Item depends on (refers to) to Vendor, so by having the Item deletes returned first you avoid a dependency problem.
By default, the records of each type are returned in ascending order, according to the “real” delete time. For example:

    If list object A is deleted at 10 a.m. and list object B is deleted at 11 a.m., the query request will return A first, then B.
    However, if the QuickBooks user moves the clock back before deleting B (for example, B is deleted at 9 a.m.), the query will still return first A then B, because B was deleted after A in “real” time.

### XMLOps
```
<?xml version="1.0" encoding="utf-8"?>
<?qbxml version="16.0"?>
<QBXML>
        <QBXMLMsgsRq onError="stopOnError">
                <ListDeletedQueryRq metaData="ENUMTYPE">
                        <!-- ListDelType may have one of the following values: Account, BillingRate, Class, Currency, Customer, CustomerMsg, CustomerType, DateDrivenTerms, Employee, InventorySite, ItemDiscount, ItemFixedAsset, ItemGroup, ItemInventory, ItemInventoryAssembly, ItemNonInventory, ItemOtherCharge, ItemPayment, ItemSalesTax, ItemSalesTaxGroup, ItemService, ItemSubtotal, JobType, OtherName, PaymentMethod, PayrollItemNonWage, PayrollItemWage, PriceLevel, SalesRep, SalesTaxCode, ShipMethod, StandardTerms, ToDo, UnitOfMeasureSet, Vehicle, Vendor, VendorType, WorkersCompCode -->
                        <ListDelType >ENUMTYPE</ListDelType> <!-- required, may repeat -->
                        <DeletedDateRangeFilter> <!-- optional -->
                                <FromDeletedDate >DATETIMETYPE</FromDeletedDate> <!-- optional -->
                                <ToDeletedDate >DATETIMETYPE</ToDeletedDate> <!-- optional -->
                        </DeletedDateRangeFilter>
                        <IncludeRetElement >STRTYPE</IncludeRetElement> <!-- optional, may repeat -->
                </ListDeletedQueryRq>

                <ListDeletedQueryRs statusCode="INTTYPE" statusSeverity="STRTYPE" statusMessage="STRTYPE" retCount="INTTYPE">
                        <ListDeletedRet> <!-- optional, may repeat -->
                                <!-- ListDelType may have one of the following values: Account, BillingRate, Class, Currency, Customer, CustomerMsg, CustomerType, DateDrivenTerms, Employee, InventorySite, ItemDiscount, ItemFixedAsset, ItemGroup, ItemInventory, ItemInventoryAssembly, ItemNonInventory, ItemOtherCharge, ItemPayment, ItemSalesTax, ItemSalesTaxGroup, ItemService, ItemSubtotal, JobType, OtherName, PaymentMethod, PayrollItemNonWage, PayrollItemWage, PriceLevel, SalesRep, SalesTaxCode, ShipMethod, StandardTerms, ToDo, UnitOfMeasureSet, Vehicle, Vendor, VendorType, WorkersCompCode -->
                                <ListDelType >ENUMTYPE</ListDelType> <!-- required -->
                                <ListID >IDTYPE</ListID> <!-- required -->
                                <TimeCreated >DATETIMETYPE</TimeCreated> <!-- required -->
                                <TimeDeleted >DATETIMETYPE</TimeDeleted> <!-- required -->
                                <FullName >STRTYPE</FullName> <!-- optional -->
                        </ListDeletedRet>
                </ListDeletedQueryRs>
        </QBXMLMsgsRq>
</QBXML>
```
## OtherNameQuery
### XMLOps
```
<?xml version="1.0" encoding="utf-8"?>
<?qbxml version="16.0"?>
<QBXML>
        <QBXMLMsgsRq onError="stopOnError">
                <OtherNameQueryRq metaData="ENUMTYPE">
                        <!-- BEGIN OR -->
                                <ListID >IDTYPE</ListID> <!-- optional, may repeat -->
                        <!-- OR -->
                                <FullName >STRTYPE</FullName> <!-- optional, may repeat -->
                        <!-- OR -->
                                <MaxReturned >INTTYPE</MaxReturned> <!-- optional -->
                                <!-- ActiveStatus may have one of the following values: ActiveOnly [DEFAULT], InactiveOnly, All -->
                                <ActiveStatus >ENUMTYPE</ActiveStatus> <!-- optional -->
                                <FromModifiedDate >DATETIMETYPE</FromModifiedDate> <!-- optional -->
                                <ToModifiedDate >DATETIMETYPE</ToModifiedDate> <!-- optional -->
                                <!-- BEGIN OR -->
                                        <NameFilter> <!-- optional -->
                                                <!-- MatchCriterion may have one of the following values: StartsWith, Contains, EndsWith -->
                                                <MatchCriterion >ENUMTYPE</MatchCriterion> <!-- required -->
                                                <Name >STRTYPE</Name> <!-- required -->
                                        </NameFilter>
                                <!-- OR -->
                                        <NameRangeFilter> <!-- optional -->
                                                <FromName >STRTYPE</FromName> <!-- optional -->
                                                <ToName >STRTYPE</ToName> <!-- optional -->
                                        </NameRangeFilter>
                                <!-- END OR -->
                        <!-- END OR -->
                        <IncludeRetElement >STRTYPE</IncludeRetElement> <!-- optional, may repeat -->
                        <OwnerID >GUIDTYPE</OwnerID> <!-- optional, may repeat -->
                </OtherNameQueryRq>

                <OtherNameQueryRs statusCode="INTTYPE" statusSeverity="STRTYPE" statusMessage="STRTYPE" retCount="INTTYPE">
                        <OtherNameRet> <!-- optional, may repeat -->
                                <ListID >IDTYPE</ListID> <!-- required -->
                                <TimeCreated >DATETIMETYPE</TimeCreated> <!-- required -->
                                <TimeModified >DATETIMETYPE</TimeModified> <!-- required -->
                                <EditSequence >STRTYPE</EditSequence> <!-- required -->
                                <Name >STRTYPE</Name> <!-- required -->
                                <IsActive >BOOLTYPE</IsActive> <!-- optional -->
                                <CompanyName >STRTYPE</CompanyName> <!-- optional -->
                                <Salutation >STRTYPE</Salutation> <!-- optional -->
                                <FirstName >STRTYPE</FirstName> <!-- optional -->
                                <MiddleName >STRTYPE</MiddleName> <!-- optional -->
                                <LastName >STRTYPE</LastName> <!-- optional -->
                                <OtherNameAddress> <!-- optional -->
                                        <Addr1 >STRTYPE</Addr1> <!-- optional -->
                                        <Addr2 >STRTYPE</Addr2> <!-- optional -->
                                        <Addr3 >STRTYPE</Addr3> <!-- optional -->
                                        <Addr4 >STRTYPE</Addr4> <!-- optional -->
                                        <Addr5 >STRTYPE</Addr5> <!-- optional -->
                                        <City >STRTYPE</City> <!-- optional -->
                                        <State >STRTYPE</State> <!-- optional -->
                                        <PostalCode >STRTYPE</PostalCode> <!-- optional -->
                                        <Country >STRTYPE</Country> <!-- optional -->
                                        <Note >STRTYPE</Note> <!-- optional -->
                                </OtherNameAddress>
                                <OtherNameAddressBlock> <!-- optional -->
                                        <Addr1 >STRTYPE</Addr1> <!-- optional -->
                                        <Addr2 >STRTYPE</Addr2> <!-- optional -->
                                        <Addr3 >STRTYPE</Addr3> <!-- optional -->
                                        <Addr4 >STRTYPE</Addr4> <!-- optional -->
                                        <Addr5 >STRTYPE</Addr5> <!-- optional -->
                                </OtherNameAddressBlock>
                                <Phone >STRTYPE</Phone> <!-- optional -->
                                <AltPhone >STRTYPE</AltPhone> <!-- optional -->
                                <Fax >STRTYPE</Fax> <!-- optional -->
                                <Email >STRTYPE</Email> <!-- optional -->
                                <Contact >STRTYPE</Contact> <!-- optional -->
                                <AltContact >STRTYPE</AltContact> <!-- optional -->
                                <AccountNumber >STRTYPE</AccountNumber> <!-- optional -->
                                <Notes >STRTYPE</Notes> <!-- optional -->
                                <ExternalGUID >GUIDTYPE</ExternalGUID> <!-- optional -->
                                <DataExtRet> <!-- optional, may repeat -->
                                        <OwnerID >GUIDTYPE</OwnerID> <!-- optional -->
                                        <DataExtName >STRTYPE</DataExtName> <!-- required -->
                                        <!-- DataExtType may have one of the following values: AMTTYPE, DATETIMETYPE, INTTYPE, PERCENTTYPE, PRICETYPE, QUANTYPE, STR1024TYPE, STR255TYPE -->
                                        <DataExtType >ENUMTYPE</DataExtType> <!-- required -->
                                        <DataExtValue >STRTYPE</DataExtValue> <!-- required -->
                                </DataExtRet>
                        </OtherNameRet>
                </OtherNameQueryRs>
        </QBXMLMsgsRq>
</QBXML>
```
## PaymentMethodQuery
### XMLOps
```
<?xml version="1.0" encoding="utf-8"?>
<?qbxml version="16.0"?>
<QBXML>
        <QBXMLMsgsRq onError="stopOnError">
                <PaymentMethodQueryRq metaData="ENUMTYPE">
                        <!-- BEGIN OR -->
                                <ListID >IDTYPE</ListID> <!-- optional, may repeat -->
                        <!-- OR -->
                                <FullName >STRTYPE</FullName> <!-- optional, may repeat -->
                        <!-- OR -->
                                <MaxReturned >INTTYPE</MaxReturned> <!-- optional -->
                                <!-- ActiveStatus may have one of the following values: ActiveOnly [DEFAULT], InactiveOnly, All -->
                                <ActiveStatus >ENUMTYPE</ActiveStatus> <!-- optional -->
                                <FromModifiedDate >DATETIMETYPE</FromModifiedDate> <!-- optional -->
                                <ToModifiedDate >DATETIMETYPE</ToModifiedDate> <!-- optional -->
                                <!-- BEGIN OR -->
                                        <NameFilter> <!-- optional -->
                                                <!-- MatchCriterion may have one of the following values: StartsWith, Contains, EndsWith -->
                                                <MatchCriterion >ENUMTYPE</MatchCriterion> <!-- required -->
                                                <Name >STRTYPE</Name> <!-- required -->
                                        </NameFilter>
                                <!-- OR -->
                                        <NameRangeFilter> <!-- optional -->
                                                <FromName >STRTYPE</FromName> <!-- optional -->
                                                <ToName >STRTYPE</ToName> <!-- optional -->
                                        </NameRangeFilter>
                                <!-- END OR -->
                                <!-- PaymentMethodType may have one of the following values: AmericanExpress, Cash, Check, DebitCard, Discover, ECheck, GiftCard, MasterCard, Other, OtherCreditCard, Visa -->
                                <PaymentMethodType >ENUMTYPE</PaymentMethodType> <!-- optional, may repeat -->
                        <!-- END OR -->
                        <IncludeRetElement >STRTYPE</IncludeRetElement> <!-- optional, may repeat -->
                </PaymentMethodQueryRq>

                <PaymentMethodQueryRs statusCode="INTTYPE" statusSeverity="STRTYPE" statusMessage="STRTYPE" retCount="INTTYPE">
                        <PaymentMethodRet> <!-- optional, may repeat -->
                                <ListID >IDTYPE</ListID> <!-- required -->
                                <TimeCreated >DATETIMETYPE</TimeCreated> <!-- required -->
                                <TimeModified >DATETIMETYPE</TimeModified> <!-- required -->
                                <EditSequence >STRTYPE</EditSequence> <!-- required -->
                                <Name >STRTYPE</Name> <!-- required -->
                                <IsActive >BOOLTYPE</IsActive> <!-- optional -->
                                <!-- PaymentMethodType may have one of the following values: AmericanExpress, Cash, Check, DebitCard, Discover, ECheck, GiftCard, MasterCard, Other, OtherCreditCard, Visa -->
                                <PaymentMethodType >ENUMTYPE</PaymentMethodType> <!-- optional -->
                        </PaymentMethodRet>
                </PaymentMethodQueryRs>
        </QBXMLMsgsRq>
</QBXML>
```
## PayrollDetailReportQuery
Returns information from any of five QuickBooks payroll reports:

    - Employee state taxes detail report
    - Payroll item detail report (lists the payroll transactions on which each payroll item appears)
    - Payroll detail review report (provides detailed information about how QuickBooks calculates tax amounts on employee paychecks and in year-to-date transactions)
    - Payroll transaction detail report (shows the line-item detail that appears on each payroll transaction)
    - Payroll transactions by payee report (lists payroll transactions, grouping them by payee)

Payroll Summary Reports can be generated if your application is accessing a company file that is currently signed up for a subscription to a payroll service. (If your application is not signed up, it will receive an error when it attempts to generate a report in this category.)

The restrictions noted above about payroll reports requiring the use of the Intuit Payroll service do not apply to the QuickBooks sample companies. You can still test out these reports on the sample companies without subscribing to the payroll service. For all other companies, however, the company must be subscribed.
### XMLOps
```
<?xml version="1.0" encoding="utf-8"?>
<?qbxml version="16.0"?>
<QBXML>
        <QBXMLMsgsRq onError="stopOnError">
                <PayrollDetailReportQueryRq>
                        <!-- PayrollDetailReportType may have one of the following values: EmployeeStateTaxesDetail, PayrollItemDetail, PayrollReviewDetail, PayrollTransactionDetail, PayrollTransactionsByPayee -->
                        <PayrollDetailReportType >ENUMTYPE</PayrollDetailReportType> <!-- required -->
                        <DisplayReport >BOOLTYPE</DisplayReport> <!-- optional -->
                        <!-- BEGIN OR -->
                                <ReportPeriod> <!-- optional -->
                                        <FromReportDate >DATETYPE</FromReportDate> <!-- optional -->
                                        <ToReportDate >DATETYPE</ToReportDate> <!-- optional -->
                                </ReportPeriod>
                        <!-- OR -->
                                <!-- ReportDateMacro may have one of the following values: All, Today, ThisWeek, ThisWeekToDate, ThisMonth, ThisMonthToDate, ThisQuarter, ThisQuarterToDate, ThisYear, ThisYearToDate, Yesterday, LastWeek, LastWeekToDate, LastMonth, LastMonthToDate, LastQuarter, LastQuarterToDate, LastYear, LastYearToDate, NextWeek, NextFourWeeks, NextMonth, NextQuarter, NextYear -->
                                <ReportDateMacro >ENUMTYPE</ReportDateMacro> <!-- optional -->
                        <!-- END OR -->
                        <ReportAccountFilter> <!-- optional -->
                                <!-- BEGIN OR -->
                                        <!-- AccountTypeFilter may have one of the following values: AccountsPayable, AccountsReceivable, AllowedFor1099, APAndSalesTax, APOrCreditCard, ARAndAP, Asset, BalanceSheet, Bank, BankAndARAndAPAndUF, BankAndUF, CostOfSales, CreditCard, CurrentAsset, CurrentAssetAndExpense, CurrentLiability, Equity, EquityAndIncomeAndExpense, ExpenseAndOtherExpense, FixedAsset, IncomeAndExpense, IncomeAndOtherIncome, Liability, LiabilityAndEquity, LongTermLiability, NonPosting, OrdinaryExpense, OrdinaryIncome, OrdinaryIncomeAndCOGS, OrdinaryIncomeAndExpense, OtherAsset, OtherCurrentAsset, OtherCurrentLiability, OtherExpense, OtherIncome, OtherIncomeOrExpense -->
                                        <AccountTypeFilter >ENUMTYPE</AccountTypeFilter> <!-- optional -->
                                <!-- OR -->
                                        <ListID >IDTYPE</ListID> <!-- optional, may repeat -->
                                <!-- OR -->
                                        <FullName >STRTYPE</FullName> <!-- optional, may repeat -->
                                <!-- OR -->
                                        <ListIDWithChildren >IDTYPE</ListIDWithChildren> <!-- optional -->
                                <!-- OR -->
                                        <FullNameWithChildren >STRTYPE</FullNameWithChildren> <!-- optional -->
                                <!-- END OR -->
                        </ReportAccountFilter>
                        <ReportEntityFilter> <!-- optional -->
                                <!-- BEGIN OR -->
                                        <!-- EntityTypeFilter may have one of the following values: Customer, Employee, OtherName, Vendor -->
                                        <EntityTypeFilter >ENUMTYPE</EntityTypeFilter> <!-- optional -->
                                <!-- OR -->
                                        <ListID >IDTYPE</ListID> <!-- optional, may repeat -->
                                <!-- OR -->
                                        <FullName >STRTYPE</FullName> <!-- optional, may repeat -->
                                <!-- OR -->
                                        <ListIDWithChildren >IDTYPE</ListIDWithChildren> <!-- optional -->
                                <!-- OR -->
                                        <FullNameWithChildren >STRTYPE</FullNameWithChildren> <!-- optional -->
                                <!-- END OR -->
                        </ReportEntityFilter>
                        <ReportItemFilter> <!-- optional -->
                                <!-- BEGIN OR -->
                                        <!-- ItemTypeFilter may have one of the following values: AllExceptFixedAsset, Assembly, Discount, FixedAsset, Inventory, InventoryAndAssembly, NonInventory, OtherCharge, Payment, Sales, SalesTax, Service -->
                                        <ItemTypeFilter >ENUMTYPE</ItemTypeFilter> <!-- optional -->
                                <!-- OR -->
                                        <ListID >IDTYPE</ListID> <!-- optional, may repeat -->
                                <!-- OR -->
                                        <FullName >STRTYPE</FullName> <!-- optional, may repeat -->
                                <!-- OR -->
                                        <ListIDWithChildren >IDTYPE</ListIDWithChildren> <!-- optional -->
                                <!-- OR -->
                                        <FullNameWithChildren >STRTYPE</FullNameWithChildren> <!-- optional -->
                                <!-- END OR -->
                        </ReportItemFilter>
                        <ReportClassFilter> <!-- optional -->
                                <!-- BEGIN OR -->
                                        <ListID >IDTYPE</ListID> <!-- optional, may repeat -->
                                <!-- OR -->
                                        <FullName >STRTYPE</FullName> <!-- optional, may repeat -->
                                <!-- OR -->
                                        <ListIDWithChildren >IDTYPE</ListIDWithChildren> <!-- optional -->
                                <!-- OR -->
                                        <FullNameWithChildren >STRTYPE</FullNameWithChildren> <!-- optional -->
                                <!-- END OR -->
                        </ReportClassFilter>
                        <!-- BEGIN OR -->
                                <ReportModifiedDateRangeFilter> <!-- optional -->
                                        <FromReportModifiedDate >DATETYPE</FromReportModifiedDate> <!-- optional -->
                                        <ToReportModifiedDate >DATETYPE</ToReportModifiedDate> <!-- optional -->
                                </ReportModifiedDateRangeFilter>
                        <!-- OR -->
                                <!-- ReportModifiedDateRangeMacro may have one of the following values: All, Today, ThisWeek, ThisWeekToDate, ThisMonth, ThisMonthToDate, ThisQuarter, ThisQuarterToDate, ThisYear, ThisYearToDate, Yesterday, LastWeek, LastWeekToDate, LastMonth, LastMonthToDate, LastQuarter, LastQuarterToDate, LastYear, LastYearToDate, NextWeek, NextFourWeeks, NextMonth, NextQuarter, NextYear -->
                                <ReportModifiedDateRangeMacro >ENUMTYPE</ReportModifiedDateRangeMacro> <!-- optional -->
                        <!-- END OR -->
                        <!-- ReportDetailLevelFilter may have one of the following values: All [DEFAULT], AllExceptSummary, SummaryOnly -->
                        <ReportDetailLevelFilter >ENUMTYPE</ReportDetailLevelFilter> <!-- optional -->
                        <!-- ReportPostingStatusFilter may have one of the following values: Either, NonPosting, Posting -->
                        <ReportPostingStatusFilter >ENUMTYPE</ReportPostingStatusFilter> <!-- optional -->
                        <!-- SummarizeRowsBy may have one of the following values: Account, BalanceSheet, Class, Customer, CustomerType, Day, Employee, FourWeek, HalfMonth, IncomeStatement, ItemDetail, ItemType, Month, Payee, PaymentMethod, PayrollItemDetail, PayrollYtdDetail, Quarter, SalesRep, SalesTaxCode, ShipMethod, TaxLine, Terms, TotalOnly, TwoWeek, Vendor, VendorType, Week, Year -->
                        <SummarizeRowsBy >ENUMTYPE</SummarizeRowsBy> <!-- optional -->
                        <!-- IncludeColumn may have one of the following values: Account, Aging, Amount, AmountDifference, AverageCost, BilledDate, BillingStatus, CalculatedAmount, Class, ClearedStatus, CostPrice, Credit, Currency, Date, Debit, DeliveryDate, DueDate, EstimateActive, ExchangeRate, FOB, IncomeSubjectToTax, Invoiced, Item, ItemDesc, LastModifiedBy, LatestOrPriorState, Memo, ModifiedTime, Name, NameAccountNumber, NameAddress, NameCity, NameContact, NameEmail, NameFax, NamePhone, NameState, NameZip, OpenBalance, OriginalAmount, PaidAmount, PaidStatus, PaidThroughDate, PaymentMethod, PayrollItem, PONumber, PrintStatus, ProgressAmount, ProgressPercent, Quantity, QuantityAvailable, QuantityOnHand, QuantityOnSalesOrder, ReceivedQuantity, RefNumber, RunningBalance, SalesRep, SalesTaxCode, SerialOrLotNumber, ShipDate, ShipMethod, SourceName, SplitAccount, SSNOrTaxID, TaxLine, TaxTableVersion, Terms, TxnID, TxnNumber, TxnType, UnitPrice, UserEdit, ValueOnHand, WageBase, WageBaseTips -->
                        <IncludeColumn >ENUMTYPE</IncludeColumn> <!-- optional, may repeat -->
                        <!-- IncludeAccounts may have one of the following values: All, InUse -->
                        <IncludeAccounts >ENUMTYPE</IncludeAccounts> <!-- optional -->
                        <!-- ReportOpenBalanceAsOf may have one of the following values: ReportEndDate, Today [DEFAULT] -->
                        <ReportOpenBalanceAsOf >ENUMTYPE</ReportOpenBalanceAsOf> <!-- optional -->
                </PayrollDetailReportQueryRq>

                <PayrollDetailReportQueryRs statusCode="INTTYPE" statusSeverity="STRTYPE" statusMessage="STRTYPE">
                        <ReportRet> <!-- optional -->
                                <ReportTitle >STRTYPE</ReportTitle> <!-- required -->
                                <ReportSubtitle >STRTYPE</ReportSubtitle> <!-- required -->
                                <!-- ReportBasis may have one of the following values: Accrual, Cash, None [DEFAULT] -->
                                <ReportBasis >ENUMTYPE</ReportBasis> <!-- optional -->
                                <NumRows >INTTYPE</NumRows> <!-- required -->
                                <NumColumns >INTTYPE</NumColumns> <!-- required -->
                                <NumColTitleRows >INTTYPE</NumColTitleRows> <!-- required -->
                                <ColDesc colID="INTTYPE" dataType="ENUMTYPE"> <!-- required, may repeat -->
                                        <ColTitle titleRow="INTTYPE" value="STRTYPE"> <!-- required, may repeat -->
                                        </ColTitle>
                                        <!-- ColType may have one of the following values: Account, Addr1, Addr2, Addr3, Addr4, Addr5, Aging, Amount, AmountDifference, AverageCost, BilledDate, BillingStatus, Blank, CalculatedAmount, Class, ClearedStatus, CostPrice, CreateDate, Credit, CustomField, Date, Debit, DeliveryDate, DueDate, Duration, EarliestReceiptDate, EstimateActive, FOB, IncomeSubjectToTax, Invoiced, IsAdjustment, Item, ItemDesc, ItemVendor, Label, LastModifiedBy, LatestOrPriorState, Memo, ModifiedTime, Name, NameAccountNumber, NameAddress, NameCity, NameContact, NameEmail, NameFax, NamePhone, NameState, NameZip, OpenBalance, OriginalAmount, PaidAmount, PaidStatus, PaidThroughDate, PaymentMethod, PayrollItem, Percent, PercentChange, PercentOfTotalRetail, PercentOfTotalValue, PhysicalCount, PONumber, PrintStatus, ProgressAmount, ProgressPercent, Quantity, QuantityAvailable, QuantityOnHand, QuantityOnOrder, QuantityOnPendingBuild, QuantityOnSalesOrder, ReceivedQuantity, RefNumber, ReorderPoint, RetailValueOnHand, RunningBalance, SalesPerWeek, SalesRep, SalesTaxCode, ShipDate, ShipMethod, ShipToAddr1, ShipToAddr2, ShipToAddr3, ShipToAddr4, ShipToAddr5, SONumber, SourceName, SplitAccount, SSNOrTaxID, SuggestedReorder, TaxLine, TaxTableVersion, Terms, Total, TxnID, TxnNumber, TxnType, UnitPrice, UserEdit, ValueOnHand, WageBase, WageBaseTips -->
                                        <ColType >ENUMTYPE</ColType> <!-- required -->
                                </ColDesc>
                                <ReportData> <!-- optional -->
                                        <!-- BEGIN OR -->
                                                <DataRow> <!-- optional -->
                                                        <RowData rowType="ENUMTYPE" value="STRTYPE"> <!-- optional -->
                                                        </RowData>
                                                        <ColData colID="INTTYPE" value="STRTYPE" dataType="ENUMTYPE"> <!-- optional, may repeat -->
                                                        </ColData>
                                                </DataRow>
                                        <!-- OR -->
                                                <TextRow rowNumber="INTTYPE" value="STRTYPE"> <!-- optional -->
                                                </TextRow>
                                        <!-- OR -->
                                                <SubtotalRow> <!-- optional -->
                                                        <RowData rowType="ENUMTYPE" value="STRTYPE"> <!-- optional -->
                                                        </RowData>
                                                        <ColData colID="INTTYPE" value="STRTYPE" dataType="ENUMTYPE"> <!-- optional, may repeat -->
                                                        </ColData>
                                                </SubtotalRow>
                                        <!-- OR -->
                                                <TotalRow> <!-- optional -->
                                                        <RowData rowType="ENUMTYPE" value="STRTYPE"> <!-- optional -->
                                                        </RowData>
                                                        <ColData colID="INTTYPE" value="STRTYPE" dataType="ENUMTYPE"> <!-- optional, may repeat -->
                                                        </ColData>
                                                </TotalRow>
                                        <!-- END OR -->
                                </ReportData>
                        </ReportRet>
                </PayrollDetailReportQueryRs>
        </QBXMLMsgsRq>
</QBXML>

```
## PayrollItemNonWageQuery
### XMLOps
```
<?xml version="1.0" encoding="utf-8"?>
<?qbxml version="16.0"?>
<QBXML>
        <QBXMLMsgsRq onError="stopOnError">
                <PayrollItemNonWageQueryRq metaData="ENUMTYPE">
                        <!-- BEGIN OR -->
                                <ListID >IDTYPE</ListID> <!-- optional, may repeat -->
                        <!-- OR -->
                                <FullName >STRTYPE</FullName> <!-- optional, may repeat -->
                        <!-- OR -->
                                <MaxReturned >INTTYPE</MaxReturned> <!-- optional -->
                                <!-- ActiveStatus may have one of the following values: ActiveOnly [DEFAULT], InactiveOnly, All -->
                                <ActiveStatus >ENUMTYPE</ActiveStatus> <!-- optional -->
                                <FromModifiedDate >DATETIMETYPE</FromModifiedDate> <!-- optional -->
                                <ToModifiedDate >DATETIMETYPE</ToModifiedDate> <!-- optional -->
                                <!-- BEGIN OR -->
                                        <NameFilter> <!-- optional -->
                                                <!-- MatchCriterion may have one of the following values: StartsWith, Contains, EndsWith -->
                                                <MatchCriterion >ENUMTYPE</MatchCriterion> <!-- required -->
                                                <Name >STRTYPE</Name> <!-- required -->
                                        </NameFilter>
                                <!-- OR -->
                                        <NameRangeFilter> <!-- optional -->
                                                <FromName >STRTYPE</FromName> <!-- optional -->
                                                <ToName >STRTYPE</ToName> <!-- optional -->
                                        </NameRangeFilter>
                                <!-- END OR -->
                        <!-- END OR -->
                        <IncludeRetElement >STRTYPE</IncludeRetElement> <!-- optional, may repeat -->
                </PayrollItemNonWageQueryRq>

                <PayrollItemNonWageQueryRs statusCode="INTTYPE" statusSeverity="STRTYPE" statusMessage="STRTYPE" retCount="INTTYPE">
                        <PayrollItemNonWageRet> <!-- optional, may repeat -->
                                <ListID >IDTYPE</ListID> <!-- required -->
                                <TimeCreated >DATETIMETYPE</TimeCreated> <!-- required -->
                                <TimeModified >DATETIMETYPE</TimeModified> <!-- required -->
                                <EditSequence >STRTYPE</EditSequence> <!-- required -->
                                <Name >STRTYPE</Name> <!-- required -->
                                <IsActive >BOOLTYPE</IsActive> <!-- optional -->
                                <!-- NonWageType may have one of the following values: Addition, CompanyContribution, Deduction, DirectDeposit, Tax -->
                                <NonWageType >ENUMTYPE</NonWageType> <!-- required -->
                                <ExpenseAccountRef> <!-- optional -->
                                        <ListID >IDTYPE</ListID> <!-- optional -->
                                        <FullName >STRTYPE</FullName> <!-- optional -->
                                </ExpenseAccountRef>
                                <LiabilityAccountRef> <!-- optional -->
                                        <ListID >IDTYPE</ListID> <!-- optional -->
                                        <FullName >STRTYPE</FullName> <!-- optional -->
                                </LiabilityAccountRef>
                        </PayrollItemNonWageRet>
                </PayrollItemNonWageQueryRs>
        </QBXMLMsgsRq>
</QBXML>
```
## PayrollItemWageQuery
### XMLOps
```
<?xml version="1.0" encoding="utf-8"?>
<?qbxml version="16.0"?>
<QBXML>
        <QBXMLMsgsRq onError="stopOnError">
                <PayrollItemWageQueryRq metaData="ENUMTYPE">
                        <!-- BEGIN OR -->
                                <ListID >IDTYPE</ListID> <!-- optional, may repeat -->
                        <!-- OR -->
                                <FullName >STRTYPE</FullName> <!-- optional, may repeat -->
                        <!-- OR -->
                                <MaxReturned >INTTYPE</MaxReturned> <!-- optional -->
                                <!-- ActiveStatus may have one of the following values: ActiveOnly [DEFAULT], InactiveOnly, All -->
                                <ActiveStatus >ENUMTYPE</ActiveStatus> <!-- optional -->
                                <FromModifiedDate >DATETIMETYPE</FromModifiedDate> <!-- optional -->
                                <ToModifiedDate >DATETIMETYPE</ToModifiedDate> <!-- optional -->
                                <!-- BEGIN OR -->
                                        <NameFilter> <!-- optional -->
                                                <!-- MatchCriterion may have one of the following values: StartsWith, Contains, EndsWith -->
                                                <MatchCriterion >ENUMTYPE</MatchCriterion> <!-- required -->
                                                <Name >STRTYPE</Name> <!-- required -->
                                        </NameFilter>
                                <!-- OR -->
                                        <NameRangeFilter> <!-- optional -->
                                                <FromName >STRTYPE</FromName> <!-- optional -->
                                                <ToName >STRTYPE</ToName> <!-- optional -->
                                        </NameRangeFilter>
                                <!-- END OR -->
                        <!-- END OR -->
                        <IncludeRetElement >STRTYPE</IncludeRetElement> <!-- optional, may repeat -->
                </PayrollItemWageQueryRq>

                <PayrollItemWageQueryRs statusCode="INTTYPE" statusSeverity="STRTYPE" statusMessage="STRTYPE" retCount="INTTYPE">
                        <PayrollItemWageRet> <!-- optional, may repeat -->
                                <ListID >IDTYPE</ListID> <!-- required -->
                                <TimeCreated >DATETIMETYPE</TimeCreated> <!-- required -->
                                <TimeModified >DATETIMETYPE</TimeModified> <!-- required -->
                                <EditSequence >STRTYPE</EditSequence> <!-- required -->
                                <Name >STRTYPE</Name> <!-- required -->
                                <IsActive >BOOLTYPE</IsActive> <!-- optional -->
                                <!-- WageType may have one of the following values: Bonus, Commission, HourlyOvertime, HourlyRegular, HourlySick, HourlyVacation, SalaryRegular, SalarySick, SalaryVacation -->
                                <WageType >ENUMTYPE</WageType> <!-- required -->
                                <ExpenseAccountRef> <!-- required -->
                                        <ListID >IDTYPE</ListID> <!-- optional -->
                                        <FullName >STRTYPE</FullName> <!-- optional -->
                                </ExpenseAccountRef>
                        </PayrollItemWageRet>
                </PayrollItemWageQueryRs>
        </QBXMLMsgsRq>
</QBXML>
```

## PayrollSummaryReportQuery
This report returns information from any of three QuickBooks payroll reports:

    - Payroll summary report This report shows the total wages, taxes withheld, deductions from net pay, additions to net pay, and employer-paid taxes and contributions for each employee on the payroll.
    - Employee earnings summary report This report shows information similar to the payroll summary report, but in a different layout. The report has a row for each employee and a column for each payroll item.
    - Payroll liability balances report This report lists the payroll liabilities the QuickBooks company owes to various agencies, such as the federal government, your state government, insurance plan administrators, labor unions, etc. The report covers unpaid liabilities incurred during the period of time shown in the From and To fields. If the company paid a liability incurred within the date range of the report, the report omits that liability, even if the payment occurred after the ending date of the report.

Payroll Summary Reports can be generated if your application is accessing a company file that is currently signed up for a subscription to a payroll service. (If your application is not signed up, it will receive an error when it attempts to generate a report in this category.)

The restrictions noted above about payroll reports requiring the use of the Intuit Payroll service do not apply to the QuickBooks sample companies. You can still test out these reports on the sample companies without subscribing to the payroll service. For all other companies, however, the company must be subscribed.
### XMLOps
```
<?xml version="1.0" encoding="utf-8"?>
<?qbxml version="16.0"?>
<QBXML>
        <QBXMLMsgsRq onError="stopOnError">
                <PayrollSummaryReportQueryRq>
                        <!-- PayrollSummaryReportType may have one of the following values: EmployeeEarningsSummary, PayrollLiabilityBalances, PayrollSummary -->
                        <PayrollSummaryReportType >ENUMTYPE</PayrollSummaryReportType> <!-- required -->
                        <DisplayReport >BOOLTYPE</DisplayReport> <!-- optional -->
                        <!-- BEGIN OR -->
                                <ReportPeriod> <!-- optional -->
                                        <FromReportDate >DATETYPE</FromReportDate> <!-- optional -->
                                        <ToReportDate >DATETYPE</ToReportDate> <!-- optional -->
                                </ReportPeriod>
                        <!-- OR -->
                                <!-- ReportDateMacro may have one of the following values: All, Today, ThisWeek, ThisWeekToDate, ThisMonth, ThisMonthToDate, ThisQuarter, ThisQuarterToDate, ThisYear, ThisYearToDate, Yesterday, LastWeek, LastWeekToDate, LastMonth, LastMonthToDate, LastQuarter, LastQuarterToDate, LastYear, LastYearToDate, NextWeek, NextFourWeeks, NextMonth, NextQuarter, NextYear -->
                                <ReportDateMacro >ENUMTYPE</ReportDateMacro> <!-- optional -->
                        <!-- END OR -->
                        <ReportAccountFilter> <!-- optional -->
                                <!-- BEGIN OR -->
                                        <!-- AccountTypeFilter may have one of the following values: AccountsPayable, AccountsReceivable, AllowedFor1099, APAndSalesTax, APOrCreditCard, ARAndAP, Asset, BalanceSheet, Bank, BankAndARAndAPAndUF, BankAndUF, CostOfSales, CreditCard, CurrentAsset, CurrentAssetAndExpense, CurrentLiability, Equity, EquityAndIncomeAndExpense, ExpenseAndOtherExpense, FixedAsset, IncomeAndExpense, IncomeAndOtherIncome, Liability, LiabilityAndEquity, LongTermLiability, NonPosting, OrdinaryExpense, OrdinaryIncome, OrdinaryIncomeAndCOGS, OrdinaryIncomeAndExpense, OtherAsset, OtherCurrentAsset, OtherCurrentLiability, OtherExpense, OtherIncome, OtherIncomeOrExpense -->
                                        <AccountTypeFilter >ENUMTYPE</AccountTypeFilter> <!-- optional -->
                                <!-- OR -->
                                        <ListID >IDTYPE</ListID> <!-- optional, may repeat -->
                                <!-- OR -->
                                        <FullName >STRTYPE</FullName> <!-- optional, may repeat -->
                                <!-- OR -->
                                        <ListIDWithChildren >IDTYPE</ListIDWithChildren> <!-- optional -->
                                <!-- OR -->
                                        <FullNameWithChildren >STRTYPE</FullNameWithChildren> <!-- optional -->
                                <!-- END OR -->
                        </ReportAccountFilter>
                        <ReportEntityFilter> <!-- optional -->
                                <!-- BEGIN OR -->
                                        <!-- EntityTypeFilter may have one of the following values: Customer, Employee, OtherName, Vendor -->
                                        <EntityTypeFilter >ENUMTYPE</EntityTypeFilter> <!-- optional -->
                                <!-- OR -->
                                        <ListID >IDTYPE</ListID> <!-- optional, may repeat -->
                                <!-- OR -->
                                        <FullName >STRTYPE</FullName> <!-- optional, may repeat -->
                                <!-- OR -->
                                        <ListIDWithChildren >IDTYPE</ListIDWithChildren> <!-- optional -->
                                <!-- OR -->
                                        <FullNameWithChildren >STRTYPE</FullNameWithChildren> <!-- optional -->
                                <!-- END OR -->
                        </ReportEntityFilter>
                        <ReportItemFilter> <!-- optional -->
                                <!-- BEGIN OR -->
                                        <!-- ItemTypeFilter may have one of the following values: AllExceptFixedAsset, Assembly, Discount, FixedAsset, Inventory, InventoryAndAssembly, NonInventory, OtherCharge, Payment, Sales, SalesTax, Service -->
                                        <ItemTypeFilter >ENUMTYPE</ItemTypeFilter> <!-- optional -->
                                <!-- OR -->
                                        <ListID >IDTYPE</ListID> <!-- optional, may repeat -->
                                <!-- OR -->
                                        <FullName >STRTYPE</FullName> <!-- optional, may repeat -->
                                <!-- OR -->
                                        <ListIDWithChildren >IDTYPE</ListIDWithChildren> <!-- optional -->
                                <!-- OR -->
                                        <FullNameWithChildren >STRTYPE</FullNameWithChildren> <!-- optional -->
                                <!-- END OR -->
                        </ReportItemFilter>
                        <ReportClassFilter> <!-- optional -->
                                <!-- BEGIN OR -->
                                        <ListID >IDTYPE</ListID> <!-- optional, may repeat -->
                                <!-- OR -->
                                        <FullName >STRTYPE</FullName> <!-- optional, may repeat -->
                                <!-- OR -->
                                        <ListIDWithChildren >IDTYPE</ListIDWithChildren> <!-- optional -->
                                <!-- OR -->
                                        <FullNameWithChildren >STRTYPE</FullNameWithChildren> <!-- optional -->
                                <!-- END OR -->
                        </ReportClassFilter>
                        <!-- BEGIN OR -->
                                <ReportModifiedDateRangeFilter> <!-- optional -->
                                        <FromReportModifiedDate >DATETYPE</FromReportModifiedDate> <!-- optional -->
                                        <ToReportModifiedDate >DATETYPE</ToReportModifiedDate> <!-- optional -->
                                </ReportModifiedDateRangeFilter>
                        <!-- OR -->
                                <!-- ReportModifiedDateRangeMacro may have one of the following values: All, Today, ThisWeek, ThisWeekToDate, ThisMonth, ThisMonthToDate, ThisQuarter, ThisQuarterToDate, ThisYear, ThisYearToDate, Yesterday, LastWeek, LastWeekToDate, LastMonth, LastMonthToDate, LastQuarter, LastQuarterToDate, LastYear, LastYearToDate, NextWeek, NextFourWeeks, NextMonth, NextQuarter, NextYear -->
                                <ReportModifiedDateRangeMacro >ENUMTYPE</ReportModifiedDateRangeMacro> <!-- optional -->
                        <!-- END OR -->
                        <!-- ReportDetailLevelFilter may have one of the following values: All [DEFAULT], AllExceptSummary, SummaryOnly -->
                        <ReportDetailLevelFilter >ENUMTYPE</ReportDetailLevelFilter> <!-- optional -->
                        <!-- ReportPostingStatusFilter may have one of the following values: Either, NonPosting, Posting -->
                        <ReportPostingStatusFilter >ENUMTYPE</ReportPostingStatusFilter> <!-- optional -->
                        <!-- SummarizeColumnsBy may have one of the following values: Account, BalanceSheet, Class, Customer, CustomerType, Day, Employee, FourWeek, HalfMonth, IncomeStatement, ItemDetail, ItemType, Month, Payee, PaymentMethod, PayrollItemDetail, PayrollYtdDetail, Quarter, SalesRep, SalesTaxCode, ShipMethod, Terms, TotalOnly, TwoWeek, Vendor, VendorType, Week, Year -->
                        <SummarizeColumnsBy >ENUMTYPE</SummarizeColumnsBy> <!-- optional -->
                        <IncludeSubcolumns >BOOLTYPE</IncludeSubcolumns> <!-- optional -->
                        <!-- ReportCalendar may have one of the following values: CalendarYear, FiscalYear, TaxYear -->
                        <ReportCalendar >ENUMTYPE</ReportCalendar> <!-- optional -->
                        <!-- ReturnRows may have one of the following values: ActiveOnly, NonZero, All -->
                        <ReturnRows >ENUMTYPE</ReturnRows> <!-- optional -->
                        <!-- ReturnColumns may have one of the following values: ActiveOnly, NonZero, All -->
                        <ReturnColumns >ENUMTYPE</ReturnColumns> <!-- optional -->
                </PayrollSummaryReportQueryRq>

                <PayrollSummaryReportQueryRs statusCode="INTTYPE" statusSeverity="STRTYPE" statusMessage="STRTYPE">
                        <ReportRet> <!-- optional -->
                                <ReportTitle >STRTYPE</ReportTitle> <!-- required -->
                                <ReportSubtitle >STRTYPE</ReportSubtitle> <!-- required -->
                                <!-- ReportBasis may have one of the following values: Accrual, Cash, None [DEFAULT] -->
                                <ReportBasis >ENUMTYPE</ReportBasis> <!-- optional -->
                                <NumRows >INTTYPE</NumRows> <!-- required -->
                                <NumColumns >INTTYPE</NumColumns> <!-- required -->
                                <NumColTitleRows >INTTYPE</NumColTitleRows> <!-- required -->
                                <ColDesc colID="INTTYPE" dataType="ENUMTYPE"> <!-- required, may repeat -->
                                        <ColTitle titleRow="INTTYPE" value="STRTYPE"> <!-- required, may repeat -->
                                        </ColTitle>
                                        <!-- ColType may have one of the following values: Account, Addr1, Addr2, Addr3, Addr4, Addr5, Aging, Amount, AmountDifference, AverageCost, BilledDate, BillingStatus, Blank, CalculatedAmount, Class, ClearedStatus, CostPrice, CreateDate, Credit, CustomField, Date, Debit, DeliveryDate, DueDate, Duration, EarliestReceiptDate, EstimateActive, FOB, IncomeSubjectToTax, Invoiced, IsAdjustment, Item, ItemDesc, ItemVendor, Label, LastModifiedBy, LatestOrPriorState, Memo, ModifiedTime, Name, NameAccountNumber, NameAddress, NameCity, NameContact, NameEmail, NameFax, NamePhone, NameState, NameZip, OpenBalance, OriginalAmount, PaidAmount, PaidStatus, PaidThroughDate, PaymentMethod, PayrollItem, Percent, PercentChange, PercentOfTotalRetail, PercentOfTotalValue, PhysicalCount, PONumber, PrintStatus, ProgressAmount, ProgressPercent, Quantity, QuantityAvailable, QuantityOnHand, QuantityOnOrder, QuantityOnPendingBuild, QuantityOnSalesOrder, ReceivedQuantity, RefNumber, ReorderPoint, RetailValueOnHand, RunningBalance, SalesPerWeek, SalesRep, SalesTaxCode, ShipDate, ShipMethod, ShipToAddr1, ShipToAddr2, ShipToAddr3, ShipToAddr4, ShipToAddr5, SONumber, SourceName, SplitAccount, SSNOrTaxID, SuggestedReorder, TaxLine, TaxTableVersion, Terms, Total, TxnID, TxnNumber, TxnType, UnitPrice, UserEdit, ValueOnHand, WageBase, WageBaseTips -->
                                        <ColType >ENUMTYPE</ColType> <!-- required -->
                                </ColDesc>
                                <ReportData> <!-- optional -->
                                        <!-- BEGIN OR -->
                                                <DataRow> <!-- optional -->
                                                        <RowData rowType="ENUMTYPE" value="STRTYPE"> <!-- optional -->
                                                        </RowData>
                                                        <ColData colID="INTTYPE" value="STRTYPE" dataType="ENUMTYPE"> <!-- optional, may repeat -->
                                                        </ColData>
                                                </DataRow>
                                        <!-- OR -->
                                                <TextRow rowNumber="INTTYPE" value="STRTYPE"> <!-- optional -->
                                                </TextRow>
                                        <!-- OR -->
                                                <SubtotalRow> <!-- optional -->
                                                        <RowData rowType="ENUMTYPE" value="STRTYPE"> <!-- optional -->
                                                        </RowData>
                                                        <ColData colID="INTTYPE" value="STRTYPE" dataType="ENUMTYPE"> <!-- optional, may repeat -->
                                                        </ColData>
                                                </SubtotalRow>
                                        <!-- OR -->
                                                <TotalRow> <!-- optional -->
                                                        <RowData rowType="ENUMTYPE" value="STRTYPE"> <!-- optional -->
                                                        </RowData>
                                                        <ColData colID="INTTYPE" value="STRTYPE" dataType="ENUMTYPE"> <!-- optional, may repeat -->
                                                        </ColData>
                                                </TotalRow>
                                        <!-- END OR -->
                                </ReportData>
                        </ReportRet>
                </PayrollSummaryReportQueryRs>
        </QBXMLMsgsRq>
</QBXML>

```

## PreferencesQuery
A PreferencesQueryRq request message returns information about many of the preferences that the QuickBooks user has set in the company file. Preferences cannot be modified through the SDK, only through the QuickBooks user interface. Note: If you include an explicit end tag in a PreferencesQueryRq request, you will receive an error if there is any space between the opening tag and the end tag. The following table shows valid and invalid ways of constructing this request:
Valid
(no space between opening and closing tags)
Valid

(combined opening and closing tag)
Invalid
(space between opening and closing tags)

### XMLOps
```
<?xml version="1.0" encoding="utf-8"?>
<?qbxml version="16.0"?>
<QBXML>
        <QBXMLMsgsRq onError="stopOnError">
                <PreferencesQueryRq>
                        <IncludeRetElement >STRTYPE</IncludeRetElement> <!-- optional, may repeat -->
                </PreferencesQueryRq>

                <PreferencesQueryRs statusCode="INTTYPE" statusSeverity="STRTYPE" statusMessage="STRTYPE">
                        <PreferencesRet> <!-- optional -->
                                <AccountingPreferences> <!-- required -->
                                        <IsUsingAccountNumbers >BOOLTYPE</IsUsingAccountNumbers> <!-- required -->
                                        <IsRequiringAccounts >BOOLTYPE</IsRequiringAccounts> <!-- required -->
                                        <IsUsingClassTracking >BOOLTYPE</IsUsingClassTracking> <!-- required -->
                                        <!-- AssignClassesTo may have one of the following values: None [DEFAULT], Accounts, Items, Names -->
                                        <AssignClassesTo >ENUMTYPE</AssignClassesTo> <!-- optional -->
                                        <IsUsingAuditTrail >BOOLTYPE</IsUsingAuditTrail> <!-- required -->
                                        <IsAssigningJournalEntryNumbers >BOOLTYPE</IsAssigningJournalEntryNumbers> <!-- required -->
                                        <ClosingDate >DATETYPE</ClosingDate> <!-- optional -->
                                </AccountingPreferences>
                                <FinanceChargePreferences> <!-- required -->
                                        <AnnualInterestRate >PERCENTTYPE</AnnualInterestRate> <!-- optional -->
                                        <MinFinanceCharge >AMTTYPE</MinFinanceCharge> <!-- optional -->
                                        <GracePeriod >INTTYPE</GracePeriod> <!-- required -->
                                        <FinanceChargeAccountRef> <!-- optional -->
                                                <ListID >IDTYPE</ListID> <!-- optional -->
                                                <FullName >STRTYPE</FullName> <!-- optional -->
                                        </FinanceChargeAccountRef>
                                        <IsAssessingForOverdueCharges >BOOLTYPE</IsAssessingForOverdueCharges> <!-- required -->
                                        <!-- CalculateChargesFrom may have one of the following values: DueDate, InvoiceOrBilledDate -->
                                        <CalculateChargesFrom >ENUMTYPE</CalculateChargesFrom> <!-- required -->
                                        <IsMarkedToBePrinted >BOOLTYPE</IsMarkedToBePrinted> <!-- required -->
                                </FinanceChargePreferences>
                                <JobsAndEstimatesPreferences> <!-- required -->
                                        <IsUsingEstimates >BOOLTYPE</IsUsingEstimates> <!-- required -->
                                        <IsUsingProgressInvoicing >BOOLTYPE</IsUsingProgressInvoicing> <!-- required -->
                                        <IsPrintingItemsWithZeroAmounts >BOOLTYPE</IsPrintingItemsWithZeroAmounts> <!-- required -->
                                </JobsAndEstimatesPreferences>
                                <MultiCurrencyPreferences> <!-- optional -->
                                        <IsMultiCurrencyOn >BOOLTYPE</IsMultiCurrencyOn> <!-- optional -->
                                        <HomeCurrencyRef> <!-- optional -->
                                                <ListID >IDTYPE</ListID> <!-- optional -->
                                                <FullName >STRTYPE</FullName> <!-- optional -->
                                        </HomeCurrencyRef>
                                </MultiCurrencyPreferences>
                                <MultiLocationInventoryPreferences> <!-- optional -->
                                        <IsMultiLocationInventoryAvailable >BOOLTYPE</IsMultiLocationInventoryAvailable> <!-- optional -->
                                        <IsMultiLocationInventoryEnabled >BOOLTYPE</IsMultiLocationInventoryEnabled> <!-- optional -->
                                </MultiLocationInventoryPreferences>
                                <PurchasesAndVendorsPreferences> <!-- required -->
                                        <IsUsingInventory >BOOLTYPE</IsUsingInventory> <!-- required -->
                                        <DaysBillsAreDue >INTTYPE</DaysBillsAreDue> <!-- required -->
                                        <IsAutomaticallyUsingDiscounts >BOOLTYPE</IsAutomaticallyUsingDiscounts> <!-- required -->
                                        <DefaultDiscountAccountRef> <!-- optional -->
                                                <ListID >IDTYPE</ListID> <!-- optional -->
                                                <FullName >STRTYPE</FullName> <!-- optional -->
                                        </DefaultDiscountAccountRef>
                                </PurchasesAndVendorsPreferences>
                                <ReportsPreferences> <!-- required -->
                                        <!-- AgingReportBasis may have one of the following values: AgeFromDueDate, AgeFromTransactionDate -->
                                        <AgingReportBasis >ENUMTYPE</AgingReportBasis> <!-- required -->
                                        <!-- SummaryReportBasis may have one of the following values: Accrual, Cash -->
                                        <SummaryReportBasis >ENUMTYPE</SummaryReportBasis> <!-- required -->
                                </ReportsPreferences>
                                <SalesAndCustomersPreferences> <!-- required -->
                                        <DefaultShipMethodRef> <!-- optional -->
                                                <ListID >IDTYPE</ListID> <!-- optional -->
                                                <FullName >STRTYPE</FullName> <!-- optional -->
                                        </DefaultShipMethodRef>
                                        <DefaultFOB >STRTYPE</DefaultFOB> <!-- optional -->
                                        <DefaultMarkup >PERCENTTYPE</DefaultMarkup> <!-- optional -->
                                        <IsTrackingReimbursedExpensesAsIncome >BOOLTYPE</IsTrackingReimbursedExpensesAsIncome> <!-- required -->
                                        <IsAutoApplyingPayments >BOOLTYPE</IsAutoApplyingPayments> <!-- required -->
                                        <PriceLevels> <!-- optional -->
                                                <IsUsingPriceLevels >BOOLTYPE</IsUsingPriceLevels> <!-- required -->
                                                <IsRoundingSalesPriceUp >BOOLTYPE</IsRoundingSalesPriceUp> <!-- optional -->
                                        </PriceLevels>
                                </SalesAndCustomersPreferences>
                                <SalesTaxPreferences> <!-- optional -->
                                        <DefaultItemSalesTaxRef> <!-- required -->
                                                <ListID >IDTYPE</ListID> <!-- optional -->
                                                <FullName >STRTYPE</FullName> <!-- optional -->
                                        </DefaultItemSalesTaxRef>
                                        <!-- PaySalesTax may have one of the following values: Monthly, Quarterly, Annually -->
                                        <PaySalesTax >ENUMTYPE</PaySalesTax> <!-- required -->
                                        <DefaultTaxableSalesTaxCodeRef> <!-- required -->
                                                <ListID >IDTYPE</ListID> <!-- optional -->
                                                <FullName >STRTYPE</FullName> <!-- optional -->
                                        </DefaultTaxableSalesTaxCodeRef>
                                        <DefaultNonTaxableSalesTaxCodeRef> <!-- required -->
                                                <ListID >IDTYPE</ListID> <!-- optional -->
                                                <FullName >STRTYPE</FullName> <!-- optional -->
                                        </DefaultNonTaxableSalesTaxCodeRef>
                                        <IsUsingVendorTaxCode >BOOLTYPE</IsUsingVendorTaxCode> <!-- optional -->
                                        <IsUsingCustomerTaxCode >BOOLTYPE</IsUsingCustomerTaxCode> <!-- optional -->
                                        <IsUsingAmountsIncludeTax >BOOLTYPE</IsUsingAmountsIncludeTax> <!-- optional -->
                                </SalesTaxPreferences>
                                <TimeTrackingPreferences> <!-- optional -->
                                        <!-- FirstDayOfWeek may have one of the following values: Monday, Tuesday, Wednesday, Thursday, Friday, Saturday, Sunday -->
                                        <FirstDayOfWeek >ENUMTYPE</FirstDayOfWeek> <!-- required -->
                                </TimeTrackingPreferences>
                                <CurrentAppAccessRights> <!-- required -->
                                        <IsAutomaticLoginAllowed >BOOLTYPE</IsAutomaticLoginAllowed> <!-- required -->
                                        <AutomaticLoginUserName >STRTYPE</AutomaticLoginUserName> <!-- optional -->
                                        <IsPersonalDataAccessAllowed >BOOLTYPE</IsPersonalDataAccessAllowed> <!-- required -->
                                </CurrentAppAccessRights>
                                <ItemsAndInventoryPreferences> <!-- optional -->
                                        <EnhancedInventoryReceivingEnabled >BOOLTYPE</EnhancedInventoryReceivingEnabled> <!-- optional -->
                                        <!-- IsTrackingSerialOrLotNumber may have one of the following values: None [DEFAULT], SerialNumber, LotNumber -->
                                        <IsTrackingSerialOrLotNumber >ENUMTYPE</IsTrackingSerialOrLotNumber> <!-- optional -->
                                        <IsInventoryExpirationDateEnabled >BOOLTYPE</IsInventoryExpirationDateEnabled> <!-- optional -->
                                        <isTrackingOnSalesTransactionsEnabled >BOOLTYPE</isTrackingOnSalesTransactionsEnabled> <!-- optional -->
                                        <isTrackingOnPurchaseTransactionsEnabled >BOOLTYPE</isTrackingOnPurchaseTransactionsEnabled> <!-- optional -->
                                        <isTrackingOnInventoryAdjustmentEnabled >BOOLTYPE</isTrackingOnInventoryAdjustmentEnabled> <!-- optional -->
                                        <isTrackingOnBuildAssemblyEnabled >BOOLTYPE</isTrackingOnBuildAssemblyEnabled> <!-- optional -->
                                        <FIFOEnabled >BOOLTYPE</FIFOEnabled> <!-- optional -->
                                        <FIFOEffectiveDate >DATETYPE</FIFOEffectiveDate> <!-- optional -->
                                        <IsRSBEnabled >BOOLTYPE</IsRSBEnabled> <!-- optional -->
                                        <IsBarcodeEnabled >BOOLTYPE</IsBarcodeEnabled> <!-- optional -->
                                </ItemsAndInventoryPreferences>
                        </PreferencesRet>
                </PreferencesQueryRs>
        </QBXMLMsgsRq>
</QBXML>
```

## PriceLevelQuery
### XMLOps
```
<?xml version="1.0" encoding="utf-8"?>
<?qbxml version="16.0"?>
<QBXML>
        <QBXMLMsgsRq onError="stopOnError">
                <PriceLevelQueryRq metaData="ENUMTYPE">
                        <!-- BEGIN OR -->
                                <ListID >IDTYPE</ListID> <!-- optional, may repeat -->
                        <!-- OR -->
                                <FullName >STRTYPE</FullName> <!-- optional, may repeat -->
                        <!-- OR -->
                                <MaxReturned >INTTYPE</MaxReturned> <!-- optional -->
                                <!-- ActiveStatus may have one of the following values: ActiveOnly [DEFAULT], InactiveOnly, All -->
                                <ActiveStatus >ENUMTYPE</ActiveStatus> <!-- optional -->
                                <FromModifiedDate >DATETIMETYPE</FromModifiedDate> <!-- optional -->
                                <ToModifiedDate >DATETIMETYPE</ToModifiedDate> <!-- optional -->
                                <!-- BEGIN OR -->
                                        <NameFilter> <!-- optional -->
                                                <!-- MatchCriterion may have one of the following values: StartsWith, Contains, EndsWith -->
                                                <MatchCriterion >ENUMTYPE</MatchCriterion> <!-- required -->
                                                <Name >STRTYPE</Name> <!-- required -->
                                        </NameFilter>
                                <!-- OR -->
                                        <NameRangeFilter> <!-- optional -->
                                                <FromName >STRTYPE</FromName> <!-- optional -->
                                                <ToName >STRTYPE</ToName> <!-- optional -->
                                        </NameRangeFilter>
                                <!-- END OR -->
                                <ItemRef> <!-- optional -->
                                        <ListID >IDTYPE</ListID> <!-- optional -->
                                        <FullName >STRTYPE</FullName> <!-- optional -->
                                </ItemRef>
                                <CurrencyFilter> <!-- optional -->
                                        <!-- BEGIN OR -->
                                                <ListID >IDTYPE</ListID> <!-- optional, may repeat -->
                                        <!-- OR -->
                                                <FullName >STRTYPE</FullName> <!-- optional, may repeat -->
                                        <!-- END OR -->
                                </CurrencyFilter>
                        <!-- END OR -->
                        <IncludeRetElement >STRTYPE</IncludeRetElement> <!-- optional, may repeat -->
                </PriceLevelQueryRq>

                <PriceLevelQueryRs statusCode="INTTYPE" statusSeverity="STRTYPE" statusMessage="STRTYPE" retCount="INTTYPE">
                        <PriceLevelRet> <!-- optional, may repeat -->
                                <ListID >IDTYPE</ListID> <!-- optional -->
                                <TimeCreated >DATETIMETYPE</TimeCreated> <!-- optional -->
                                <TimeModified >DATETIMETYPE</TimeModified> <!-- optional -->
                                <EditSequence >STRTYPE</EditSequence> <!-- optional -->
                                <Name >STRTYPE</Name> <!-- optional -->
                                <IsActive >BOOLTYPE</IsActive> <!-- optional -->
                                <!-- PriceLevelType may have one of the following values: FixedPercentage, PerItem -->
                                <PriceLevelType >ENUMTYPE</PriceLevelType> <!-- optional -->
                                <!-- BEGIN OR -->
                                        <PriceLevelFixedPercentage >PERCENTTYPE</PriceLevelFixedPercentage> <!-- optional -->
                                <!-- OR -->
                                        <PriceLevelPerItemRet> <!-- required, may repeat -->
                                                <ItemRef> <!-- required -->
                                                        <ListID >IDTYPE</ListID> <!-- optional -->
                                                        <FullName >STRTYPE</FullName> <!-- optional -->
                                                </ItemRef>
                                                <!-- BEGIN OR -->
                                                        <CustomPrice >PRICETYPE</CustomPrice> <!-- optional -->
                                                <!-- OR -->
                                                        <CustomPricePercent >PERCENTTYPE</CustomPricePercent> <!-- optional -->
                                                <!-- END OR -->
                                        </PriceLevelPerItemRet>
                                        <CurrencyRef> <!-- optional -->
                                                <ListID >IDTYPE</ListID> <!-- optional -->
                                                <FullName >STRTYPE</FullName> <!-- optional -->
                                        </CurrencyRef>
                                <!-- END OR -->
                        </PriceLevelRet>
                </PriceLevelQueryRs>
        </QBXMLMsgsRq>
</QBXML>
```
## PurchaseOrderQuery
### XMLOps
```
<?xml version="1.0" encoding="utf-8"?>
<?qbxml version="16.0"?>
<QBXML>
        <QBXMLMsgsRq onError="stopOnError">
                <PurchaseOrderQueryRq metaData="ENUMTYPE" iterator="ENUMTYPE" iteratorID="UUIDTYPE">
                        <!-- BEGIN OR -->
                                <TxnID >IDTYPE</TxnID> <!-- optional, may repeat -->
                        <!-- OR -->
                                <RefNumber >STRTYPE</RefNumber> <!-- optional, may repeat -->
                        <!-- OR -->
                                <RefNumberCaseSensitive >STRTYPE</RefNumberCaseSensitive> <!-- optional, may repeat -->
                        <!-- OR -->
                                <MaxReturned >INTTYPE</MaxReturned> <!-- optional -->
                                <!-- BEGIN OR -->
                                        <ModifiedDateRangeFilter> <!-- optional -->
                                                <FromModifiedDate >DATETIMETYPE</FromModifiedDate> <!-- optional -->
                                                <ToModifiedDate >DATETIMETYPE</ToModifiedDate> <!-- optional -->
                                        </ModifiedDateRangeFilter>
                                <!-- OR -->
                                        <TxnDateRangeFilter> <!-- optional -->
                                                <!-- BEGIN OR -->
                                                        <FromTxnDate >DATETYPE</FromTxnDate> <!-- optional -->
                                                        <ToTxnDate >DATETYPE</ToTxnDate> <!-- optional -->
                                                <!-- OR -->
                                                        <!-- DateMacro may have one of the following values: All, Today, ThisWeek, ThisWeekToDate, ThisMonth, ThisMonthToDate, ThisCalendarQuarter, ThisCalendarQuarterToDate, ThisFiscalQuarter, ThisFiscalQuarterToDate, ThisCalendarYear, ThisCalendarYearToDate, ThisFiscalYear, ThisFiscalYearToDate, Yesterday, LastWeek, LastWeekToDate, LastMonth, LastMonthToDate, LastCalendarQuarter, LastCalendarQuarterToDate, LastFiscalQuarter, LastFiscalQuarterToDate, LastCalendarYear, LastCalendarYearToDate, LastFiscalYear, LastFiscalYearToDate, NextWeek, NextFourWeeks, NextMonth, NextCalendarQuarter, NextCalendarYear, NextFiscalQuarter, NextFiscalYear -->
                                                        <DateMacro >ENUMTYPE</DateMacro> <!-- optional -->
                                                <!-- END OR -->
                                        </TxnDateRangeFilter>
                                <!-- END OR -->
                                <EntityFilter> <!-- optional -->
                                        <!-- BEGIN OR -->
                                                <ListID >IDTYPE</ListID> <!-- optional, may repeat -->
                                        <!-- OR -->
                                                <FullName >STRTYPE</FullName> <!-- optional, may repeat -->
                                        <!-- OR -->
                                                <ListIDWithChildren >IDTYPE</ListIDWithChildren> <!-- optional -->
                                        <!-- OR -->
                                                <FullNameWithChildren >STRTYPE</FullNameWithChildren> <!-- optional -->
                                        <!-- END OR -->
                                </EntityFilter>
                                <AccountFilter> <!-- optional -->
                                        <!-- BEGIN OR -->
                                                <ListID >IDTYPE</ListID> <!-- optional, may repeat -->
                                        <!-- OR -->
                                                <FullName >STRTYPE</FullName> <!-- optional, may repeat -->
                                        <!-- OR -->
                                                <ListIDWithChildren >IDTYPE</ListIDWithChildren> <!-- optional -->
                                        <!-- OR -->
                                                <FullNameWithChildren >STRTYPE</FullNameWithChildren> <!-- optional -->
                                        <!-- END OR -->
                                </AccountFilter>
                                <!-- BEGIN OR -->
                                        <RefNumberFilter> <!-- optional -->
                                                <!-- MatchCriterion may have one of the following values: StartsWith, Contains, EndsWith -->
                                                <MatchCriterion >ENUMTYPE</MatchCriterion> <!-- required -->
                                                <RefNumber >STRTYPE</RefNumber> <!-- required -->
                                        </RefNumberFilter>
                                <!-- OR -->
                                        <RefNumberRangeFilter> <!-- optional -->
                                                <FromRefNumber >STRTYPE</FromRefNumber> <!-- optional -->
                                                <ToRefNumber >STRTYPE</ToRefNumber> <!-- optional -->
                                        </RefNumberRangeFilter>
                                <!-- END OR -->
                                <CurrencyFilter> <!-- optional -->
                                        <!-- BEGIN OR -->
                                                <ListID >IDTYPE</ListID> <!-- optional, may repeat -->
                                        <!-- OR -->
                                                <FullName >STRTYPE</FullName> <!-- optional, may repeat -->
                                        <!-- END OR -->
                                </CurrencyFilter>
                        <!-- END OR -->
                        <IncludeLineItems >BOOLTYPE</IncludeLineItems> <!-- optional -->
                        <IncludeLinkedTxns >BOOLTYPE</IncludeLinkedTxns> <!-- optional -->
                        <IncludeRetElement >STRTYPE</IncludeRetElement> <!-- optional, may repeat -->
                        <OwnerID >GUIDTYPE</OwnerID> <!-- optional, may repeat -->
                </PurchaseOrderQueryRq>

                <PurchaseOrderQueryRs statusCode="INTTYPE" statusSeverity="STRTYPE" statusMessage="STRTYPE" retCount="INTTYPE" iteratorRemainingCount="INTTYPE" iteratorID="UUIDTYPE">
                        <PurchaseOrderRet> <!-- optional, may repeat -->
                                <TxnID >IDTYPE</TxnID> <!-- required -->
                                <TimeCreated >DATETIMETYPE</TimeCreated> <!-- required -->
                                <TimeModified >DATETIMETYPE</TimeModified> <!-- required -->
                                <EditSequence >STRTYPE</EditSequence> <!-- required -->
                                <TxnNumber >INTTYPE</TxnNumber> <!-- optional -->
                                <VendorRef> <!-- optional -->
                                        <ListID >IDTYPE</ListID> <!-- optional -->
                                        <FullName >STRTYPE</FullName> <!-- optional -->
                                </VendorRef>
                                <ClassRef> <!-- optional -->
                                        <ListID >IDTYPE</ListID> <!-- optional -->
                                        <FullName >STRTYPE</FullName> <!-- optional -->
                                </ClassRef>
                                <InventorySiteRef> <!-- optional -->
                                        <ListID >IDTYPE</ListID> <!-- optional -->
                                        <FullName >STRTYPE</FullName> <!-- optional -->
                                </InventorySiteRef>
                                <ShipToEntityRef> <!-- optional -->
                                        <ListID >IDTYPE</ListID> <!-- optional -->
                                        <FullName >STRTYPE</FullName> <!-- optional -->
                                </ShipToEntityRef>
                                <TemplateRef> <!-- optional -->
                                        <ListID >IDTYPE</ListID> <!-- optional -->
                                        <FullName >STRTYPE</FullName> <!-- optional -->
                                </TemplateRef>
                                <TxnDate >DATETYPE</TxnDate> <!-- required -->
                                <RefNumber >STRTYPE</RefNumber> <!-- optional -->
                                <VendorAddress> <!-- optional -->
                                        <Addr1 >STRTYPE</Addr1> <!-- optional -->
                                        <Addr2 >STRTYPE</Addr2> <!-- optional -->
                                        <Addr3 >STRTYPE</Addr3> <!-- optional -->
                                        <Addr4 >STRTYPE</Addr4> <!-- optional -->
                                        <Addr5 >STRTYPE</Addr5> <!-- optional -->
                                        <City >STRTYPE</City> <!-- optional -->
                                        <State >STRTYPE</State> <!-- optional -->
                                        <PostalCode >STRTYPE</PostalCode> <!-- optional -->
                                        <Country >STRTYPE</Country> <!-- optional -->
                                        <Note >STRTYPE</Note> <!-- optional -->
                                </VendorAddress>
                                <VendorAddressBlock> <!-- optional -->
                                        <Addr1 >STRTYPE</Addr1> <!-- optional -->
                                        <Addr2 >STRTYPE</Addr2> <!-- optional -->
                                        <Addr3 >STRTYPE</Addr3> <!-- optional -->
                                        <Addr4 >STRTYPE</Addr4> <!-- optional -->
                                        <Addr5 >STRTYPE</Addr5> <!-- optional -->
                                </VendorAddressBlock>
                                <ShipAddress> <!-- optional -->
                                        <Addr1 >STRTYPE</Addr1> <!-- optional -->
                                        <Addr2 >STRTYPE</Addr2> <!-- optional -->
                                        <Addr3 >STRTYPE</Addr3> <!-- optional -->
                                        <Addr4 >STRTYPE</Addr4> <!-- optional -->
                                        <Addr5 >STRTYPE</Addr5> <!-- optional -->
                                        <City >STRTYPE</City> <!-- optional -->
                                        <State >STRTYPE</State> <!-- optional -->
                                        <PostalCode >STRTYPE</PostalCode> <!-- optional -->
                                        <Country >STRTYPE</Country> <!-- optional -->
                                        <Note >STRTYPE</Note> <!-- optional -->
                                </ShipAddress>
                                <ShipAddressBlock> <!-- optional -->
                                        <Addr1 >STRTYPE</Addr1> <!-- optional -->
                                        <Addr2 >STRTYPE</Addr2> <!-- optional -->
                                        <Addr3 >STRTYPE</Addr3> <!-- optional -->
                                        <Addr4 >STRTYPE</Addr4> <!-- optional -->
                                        <Addr5 >STRTYPE</Addr5> <!-- optional -->
                                </ShipAddressBlock>
                                <TermsRef> <!-- optional -->
                                        <ListID >IDTYPE</ListID> <!-- optional -->
                                        <FullName >STRTYPE</FullName> <!-- optional -->
                                </TermsRef>
                                <DueDate >DATETYPE</DueDate> <!-- optional -->
                                <ExpectedDate >DATETYPE</ExpectedDate> <!-- optional -->
                                <ShipMethodRef> <!-- optional -->
                                        <ListID >IDTYPE</ListID> <!-- optional -->
                                        <FullName >STRTYPE</FullName> <!-- optional -->
                                </ShipMethodRef>
                                <FOB >STRTYPE</FOB> <!-- optional -->
                                <TotalAmount >AMTTYPE</TotalAmount> <!-- optional -->
                                <CurrencyRef> <!-- optional -->
                                        <ListID >IDTYPE</ListID> <!-- optional -->
                                        <FullName >STRTYPE</FullName> <!-- optional -->
                                </CurrencyRef>
                                <ExchangeRate >FLOATTYPE</ExchangeRate> <!-- optional -->
                                <TotalAmountInHomeCurrency >AMTTYPE</TotalAmountInHomeCurrency> <!-- optional -->
                                <IsManuallyClosed >BOOLTYPE</IsManuallyClosed> <!-- optional -->
                                <IsFullyReceived >BOOLTYPE</IsFullyReceived> <!-- optional -->
                                <Memo >STRTYPE</Memo> <!-- optional -->
                                <VendorMsg >STRTYPE</VendorMsg> <!-- optional -->
                                <IsToBePrinted >BOOLTYPE</IsToBePrinted> <!-- optional -->
                                <IsToBeEmailed >BOOLTYPE</IsToBeEmailed> <!-- optional -->
                                <IsTaxIncluded >BOOLTYPE</IsTaxIncluded> <!-- optional -->
                                <SalesTaxCodeRef> <!-- optional -->
                                        <ListID >IDTYPE</ListID> <!-- optional -->
                                        <FullName >STRTYPE</FullName> <!-- optional -->
                                </SalesTaxCodeRef>
                                <Other1 >STRTYPE</Other1> <!-- optional -->
                                <Other2 >STRTYPE</Other2> <!-- optional -->
                                <ExternalGUID >GUIDTYPE</ExternalGUID> <!-- optional -->
                                <LinkedTxn> <!-- optional, may repeat -->
                                        <TxnID >IDTYPE</TxnID> <!-- required -->
                                        <!-- TxnType may have one of the following values: ARRefundCreditCard, Bill, BillPaymentCheck, BillPaymentCreditCard, BuildAssembly, Charge, Check, CreditCardCharge, CreditCardCredit, CreditMemo, Deposit, Estimate, InventoryAdjustment, Invoice, ItemReceipt, JournalEntry, LiabilityAdjustment, Paycheck, PayrollLiabilityCheck, PurchaseOrder, ReceivePayment, SalesOrder, SalesReceipt, SalesTaxPaymentCheck, Transfer, VendorCredit, YTDAdjustment -->
                                        <TxnType >ENUMTYPE</TxnType> <!-- required -->
                                        <TxnDate >DATETYPE</TxnDate> <!-- required -->
                                        <RefNumber >STRTYPE</RefNumber> <!-- optional -->
                                        <!-- LinkType may have one of the following values: AMTTYPE, QUANTYPE -->
                                        <LinkType >ENUMTYPE</LinkType> <!-- optional -->
                                        <Amount >AMTTYPE</Amount> <!-- required -->
                                </LinkedTxn>
                                <!-- BEGIN OR -->
                                        <PurchaseOrderLineRet> <!-- optional -->
                                                <TxnLineID >IDTYPE</TxnLineID> <!-- required -->
                                                <ItemRef> <!-- optional -->
                                                        <ListID >IDTYPE</ListID> <!-- optional -->
                                                        <FullName >STRTYPE</FullName> <!-- optional -->
                                                </ItemRef>
                                                <ManufacturerPartNumber >STRTYPE</ManufacturerPartNumber> <!-- optional -->
                                                <Desc >STRTYPE</Desc> <!-- optional -->
                                                <Quantity >QUANTYPE</Quantity> <!-- optional -->
                                                <UnitOfMeasure >STRTYPE</UnitOfMeasure> <!-- optional -->
                                                <OverrideUOMSetRef> <!-- optional -->
                                                        <ListID >IDTYPE</ListID> <!-- optional -->
                                                        <FullName >STRTYPE</FullName> <!-- optional -->
                                                </OverrideUOMSetRef>
                                                <Rate >PRICETYPE</Rate> <!-- optional -->
                                                <ClassRef> <!-- optional -->
                                                        <ListID >IDTYPE</ListID> <!-- optional -->
                                                        <FullName >STRTYPE</FullName> <!-- optional -->
                                                </ClassRef>
                                                <Amount >AMTTYPE</Amount> <!-- optional -->
                                                <InventorySiteLocationRef> <!-- optional -->
                                                        <ListID >IDTYPE</ListID> <!-- optional -->
                                                        <FullName >STRTYPE</FullName> <!-- optional -->
                                                </InventorySiteLocationRef>
                                                <CustomerRef> <!-- optional -->
                                                        <ListID >IDTYPE</ListID> <!-- optional -->
                                                        <FullName >STRTYPE</FullName> <!-- optional -->
                                                </CustomerRef>
                                                <ServiceDate >DATETYPE</ServiceDate> <!-- optional -->
                                                <SalesTaxCodeRef> <!-- optional -->
                                                        <ListID >IDTYPE</ListID> <!-- optional -->
                                                        <FullName >STRTYPE</FullName> <!-- optional -->
                                                </SalesTaxCodeRef>
                                                <ReceivedQuantity >QUANTYPE</ReceivedQuantity> <!-- optional -->
                                                <UnbilledQuantity >QUANTYPE</UnbilledQuantity> <!-- optional -->
                                                <IsBilled >BOOLTYPE</IsBilled> <!-- optional -->
                                                <IsManuallyClosed >BOOLTYPE</IsManuallyClosed> <!-- optional -->
                                                <Other1 >STRTYPE</Other1> <!-- optional -->
                                                <Other2 >STRTYPE</Other2> <!-- optional -->
                                                <DataExtRet> <!-- optional, may repeat -->
                                                        <OwnerID >GUIDTYPE</OwnerID> <!-- optional -->
                                                        <DataExtName >STRTYPE</DataExtName> <!-- required -->
                                                        <!-- DataExtType may have one of the following values: AMTTYPE, DATETIMETYPE, INTTYPE, PERCENTTYPE, PRICETYPE, QUANTYPE, STR1024TYPE, STR255TYPE -->
                                                        <DataExtType >ENUMTYPE</DataExtType> <!-- required -->
                                                        <DataExtValue >STRTYPE</DataExtValue> <!-- required -->
                                                </DataExtRet>
                                        </PurchaseOrderLineRet>
                                <!-- OR -->
                                        <PurchaseOrderLineGroupRet> <!-- optional -->
                                                <TxnLineID >IDTYPE</TxnLineID> <!-- required -->
                                                <ItemGroupRef> <!-- required -->
                                                        <ListID >IDTYPE</ListID> <!-- optional -->
                                                        <FullName >STRTYPE</FullName> <!-- optional -->
                                                </ItemGroupRef>
                                                <Desc >STRTYPE</Desc> <!-- optional -->
                                                <Quantity >QUANTYPE</Quantity> <!-- optional -->
                                                <UnitOfMeasure >STRTYPE</UnitOfMeasure> <!-- optional -->
                                                <OverrideUOMSetRef> <!-- optional -->
                                                        <ListID >IDTYPE</ListID> <!-- optional -->
                                                        <FullName >STRTYPE</FullName> <!-- optional -->
                                                </OverrideUOMSetRef>
                                                <IsPrintItemsInGroup >BOOLTYPE</IsPrintItemsInGroup> <!-- required -->
                                                <TotalAmount >AMTTYPE</TotalAmount> <!-- required -->
                                                <PurchaseOrderLineRet> <!-- optional, may repeat -->
                                                        <TxnLineID >IDTYPE</TxnLineID> <!-- required -->
                                                        <ItemRef> <!-- optional -->
                                                                <ListID >IDTYPE</ListID> <!-- optional -->
                                                                <FullName >STRTYPE</FullName> <!-- optional -->
                                                        </ItemRef>
                                                        <ManufacturerPartNumber >STRTYPE</ManufacturerPartNumber> <!-- optional -->
                                                        <Desc >STRTYPE</Desc> <!-- optional -->
                                                        <Quantity >QUANTYPE</Quantity> <!-- optional -->
                                                        <UnitOfMeasure >STRTYPE</UnitOfMeasure> <!-- optional -->
                                                        <OverrideUOMSetRef> <!-- optional -->
                                                                <ListID >IDTYPE</ListID> <!-- optional -->
                                                                <FullName >STRTYPE</FullName> <!-- optional -->
                                                        </OverrideUOMSetRef>
                                                        <Rate >PRICETYPE</Rate> <!-- optional -->
                                                        <ClassRef> <!-- optional -->
                                                                <ListID >IDTYPE</ListID> <!-- optional -->
                                                                <FullName >STRTYPE</FullName> <!-- optional -->
                                                        </ClassRef>
                                                        <Amount >AMTTYPE</Amount> <!-- optional -->
                                                        <InventorySiteLocationRef> <!-- optional -->
                                                                <ListID >IDTYPE</ListID> <!-- optional -->
                                                                <FullName >STRTYPE</FullName> <!-- optional -->
                                                        </InventorySiteLocationRef>
                                                        <CustomerRef> <!-- optional -->
                                                                <ListID >IDTYPE</ListID> <!-- optional -->
                                                                <FullName >STRTYPE</FullName> <!-- optional -->
                                                        </CustomerRef>
                                                        <ServiceDate >DATETYPE</ServiceDate> <!-- optional -->
                                                        <SalesTaxCodeRef> <!-- optional -->
                                                                <ListID >IDTYPE</ListID> <!-- optional -->
                                                                <FullName >STRTYPE</FullName> <!-- optional -->
                                                        </SalesTaxCodeRef>
                                                        <ReceivedQuantity >QUANTYPE</ReceivedQuantity> <!-- optional -->
                                                        <UnbilledQuantity >QUANTYPE</UnbilledQuantity> <!-- optional -->
                                                        <IsBilled >BOOLTYPE</IsBilled> <!-- optional -->
                                                        <IsManuallyClosed >BOOLTYPE</IsManuallyClosed> <!-- optional -->
                                                        <Other1 >STRTYPE</Other1> <!-- optional -->
                                                        <Other2 >STRTYPE</Other2> <!-- optional -->
                                                        <DataExtRet> <!-- optional, may repeat -->
                                                                <OwnerID >GUIDTYPE</OwnerID> <!-- optional -->
                                                                <DataExtName >STRTYPE</DataExtName> <!-- required -->
                                                                <!-- DataExtType may have one of the following values: AMTTYPE, DATETIMETYPE, INTTYPE, PERCENTTYPE, PRICETYPE, QUANTYPE, STR1024TYPE, STR255TYPE -->
                                                                <DataExtType >ENUMTYPE</DataExtType> <!-- required -->
                                                                <DataExtValue >STRTYPE</DataExtValue> <!-- required -->
                                                        </DataExtRet>
                                                </PurchaseOrderLineRet>
                                                <DataExtRet> <!-- optional, may repeat -->
                                                        <OwnerID >GUIDTYPE</OwnerID> <!-- optional -->
                                                        <DataExtName >STRTYPE</DataExtName> <!-- required -->
                                                        <!-- DataExtType may have one of the following values: AMTTYPE, DATETIMETYPE, INTTYPE, PERCENTTYPE, PRICETYPE, QUANTYPE, STR1024TYPE, STR255TYPE -->
                                                        <DataExtType >ENUMTYPE</DataExtType> <!-- required -->
                                                        <DataExtValue >STRTYPE</DataExtValue> <!-- required -->
                                                </DataExtRet>
                                        </PurchaseOrderLineGroupRet>
                                <!-- END OR -->
                                <DataExtRet> <!-- optional, may repeat -->
                                        <OwnerID >GUIDTYPE</OwnerID> <!-- optional -->
                                        <DataExtName >STRTYPE</DataExtName> <!-- required -->
                                        <!-- DataExtType may have one of the following values: AMTTYPE, DATETIMETYPE, INTTYPE, PERCENTTYPE, PRICETYPE, QUANTYPE, STR1024TYPE, STR255TYPE -->
                                        <DataExtType >ENUMTYPE</DataExtType> <!-- required -->
                                        <DataExtValue >STRTYPE</DataExtValue> <!-- required -->
                                </DataExtRet>
                        </PurchaseOrderRet>
                </PurchaseOrderQueryRs>
        </QBXMLMsgsRq>
</QBXML>
```
## ReceivePaymentQuery
### XMLOps
```
<?xml version="1.0" encoding="utf-8"?>
<?qbxml version="16.0"?>
<QBXML>
        <QBXMLMsgsRq onError="stopOnError">
                <ReceivePaymentQueryRq metaData="ENUMTYPE" iterator="ENUMTYPE" iteratorID="UUIDTYPE">
                        <!-- BEGIN OR -->
                                <TxnID >IDTYPE</TxnID> <!-- optional, may repeat -->
                        <!-- OR -->
                                <RefNumber >STRTYPE</RefNumber> <!-- optional, may repeat -->
                        <!-- OR -->
                                <RefNumberCaseSensitive >STRTYPE</RefNumberCaseSensitive> <!-- optional, may repeat -->
                        <!-- OR -->
                                <MaxReturned >INTTYPE</MaxReturned> <!-- optional -->
                                <!-- BEGIN OR -->
                                        <ModifiedDateRangeFilter> <!-- optional -->
                                                <FromModifiedDate >DATETIMETYPE</FromModifiedDate> <!-- optional -->
                                                <ToModifiedDate >DATETIMETYPE</ToModifiedDate> <!-- optional -->
                                        </ModifiedDateRangeFilter>
                                <!-- OR -->
                                        <TxnDateRangeFilter> <!-- optional -->
                                                <!-- BEGIN OR -->
                                                        <FromTxnDate >DATETYPE</FromTxnDate> <!-- optional -->
                                                        <ToTxnDate >DATETYPE</ToTxnDate> <!-- optional -->
                                                <!-- OR -->
                                                        <!-- DateMacro may have one of the following values: All, Today, ThisWeek, ThisWeekToDate, ThisMonth, ThisMonthToDate, ThisCalendarQuarter, ThisCalendarQuarterToDate, ThisFiscalQuarter, ThisFiscalQuarterToDate, ThisCalendarYear, ThisCalendarYearToDate, ThisFiscalYear, ThisFiscalYearToDate, Yesterday, LastWeek, LastWeekToDate, LastMonth, LastMonthToDate, LastCalendarQuarter, LastCalendarQuarterToDate, LastFiscalQuarter, LastFiscalQuarterToDate, LastCalendarYear, LastCalendarYearToDate, LastFiscalYear, LastFiscalYearToDate, NextWeek, NextFourWeeks, NextMonth, NextCalendarQuarter, NextCalendarYear, NextFiscalQuarter, NextFiscalYear -->
                                                        <DateMacro >ENUMTYPE</DateMacro> <!-- optional -->
                                                <!-- END OR -->
                                        </TxnDateRangeFilter>
                                <!-- END OR -->
                                <EntityFilter> <!-- optional -->
                                        <!-- BEGIN OR -->
                                                <ListID >IDTYPE</ListID> <!-- optional, may repeat -->
                                        <!-- OR -->
                                                <FullName >STRTYPE</FullName> <!-- optional, may repeat -->
                                        <!-- OR -->
                                                <ListIDWithChildren >IDTYPE</ListIDWithChildren> <!-- optional -->
                                        <!-- OR -->
                                                <FullNameWithChildren >STRTYPE</FullNameWithChildren> <!-- optional -->
                                        <!-- END OR -->
                                </EntityFilter>
                                <AccountFilter> <!-- optional -->
                                        <!-- BEGIN OR -->
                                                <ListID >IDTYPE</ListID> <!-- optional, may repeat -->
                                        <!-- OR -->
                                                <FullName >STRTYPE</FullName> <!-- optional, may repeat -->
                                        <!-- OR -->
                                                <ListIDWithChildren >IDTYPE</ListIDWithChildren> <!-- optional -->
                                        <!-- OR -->
                                                <FullNameWithChildren >STRTYPE</FullNameWithChildren> <!-- optional -->
                                        <!-- END OR -->
                                </AccountFilter>
                                <!-- BEGIN OR -->
                                        <RefNumberFilter> <!-- optional -->
                                                <!-- MatchCriterion may have one of the following values: StartsWith, Contains, EndsWith -->
                                                <MatchCriterion >ENUMTYPE</MatchCriterion> <!-- required -->
                                                <RefNumber >STRTYPE</RefNumber> <!-- required -->
                                        </RefNumberFilter>
                                <!-- OR -->
                                        <RefNumberRangeFilter> <!-- optional -->
                                                <FromRefNumber >STRTYPE</FromRefNumber> <!-- optional -->
                                                <ToRefNumber >STRTYPE</ToRefNumber> <!-- optional -->
                                        </RefNumberRangeFilter>
                                <!-- END OR -->
                                <CurrencyFilter> <!-- optional -->
                                        <!-- BEGIN OR -->
                                                <ListID >IDTYPE</ListID> <!-- optional, may repeat -->
                                        <!-- OR -->
                                                <FullName >STRTYPE</FullName> <!-- optional, may repeat -->
                                        <!-- END OR -->
                                </CurrencyFilter>
                        <!-- END OR -->
                        <IncludeLineItems >BOOLTYPE</IncludeLineItems> <!-- optional -->
                        <IncludeRetElement >STRTYPE</IncludeRetElement> <!-- optional, may repeat -->
                        <OwnerID >GUIDTYPE</OwnerID> <!-- optional, may repeat -->
                </ReceivePaymentQueryRq>

                <ReceivePaymentQueryRs statusCode="INTTYPE" statusSeverity="STRTYPE" statusMessage="STRTYPE" retCount="INTTYPE" iteratorRemainingCount="INTTYPE" iteratorID="UUIDTYPE">
                        <ReceivePaymentRet> <!-- optional, may repeat -->
                                <TxnID >IDTYPE</TxnID> <!-- optional -->
                                <TimeCreated >DATETIMETYPE</TimeCreated> <!-- optional -->
                                <TimeModified >DATETIMETYPE</TimeModified> <!-- optional -->
                                <EditSequence >STRTYPE</EditSequence> <!-- optional -->
                                <TxnNumber >INTTYPE</TxnNumber> <!-- optional -->
                                <CustomerRef> <!-- optional -->
                                        <ListID >IDTYPE</ListID> <!-- optional -->
                                        <FullName >STRTYPE</FullName> <!-- optional -->
                                </CustomerRef>
                                <ARAccountRef> <!-- optional -->
                                        <ListID >IDTYPE</ListID> <!-- optional -->
                                        <FullName >STRTYPE</FullName> <!-- optional -->
                                </ARAccountRef>
                                <TxnDate >DATETYPE</TxnDate> <!-- optional -->
                                <RefNumber >STRTYPE</RefNumber> <!-- optional -->
                                <TotalAmount >AMTTYPE</TotalAmount> <!-- optional -->
                                <CurrencyRef> <!-- optional -->
                                        <ListID >IDTYPE</ListID> <!-- optional -->
                                        <FullName >STRTYPE</FullName> <!-- optional -->
                                </CurrencyRef>
                                <ExchangeRate >FLOATTYPE</ExchangeRate> <!-- optional -->
                                <TotalAmountInHomeCurrency >AMTTYPE</TotalAmountInHomeCurrency> <!-- optional -->
                                <PaymentMethodRef> <!-- optional -->
                                        <ListID >IDTYPE</ListID> <!-- optional -->
                                        <FullName >STRTYPE</FullName> <!-- optional -->
                                </PaymentMethodRef>
                                <Memo >STRTYPE</Memo> <!-- optional -->
                                <DepositToAccountRef> <!-- optional -->
                                        <ListID >IDTYPE</ListID> <!-- optional -->
                                        <FullName >STRTYPE</FullName> <!-- optional -->
                                </DepositToAccountRef>
                                <CreditCardTxnInfo> <!-- optional -->
                                        <CreditCardTxnInputInfo> <!-- required -->
                                                <CreditCardNumber >STRTYPE</CreditCardNumber> <!-- required -->
                                                <ExpirationMonth >INTTYPE</ExpirationMonth> <!-- required -->
                                                <ExpirationYear >INTTYPE</ExpirationYear> <!-- required -->
                                                <NameOnCard >STRTYPE</NameOnCard> <!-- required -->
                                                <CreditCardAddress >STRTYPE</CreditCardAddress> <!-- optional -->
                                                <CreditCardPostalCode >STRTYPE</CreditCardPostalCode> <!-- optional -->
                                                <CommercialCardCode >STRTYPE</CommercialCardCode> <!-- optional -->
                                                <!-- TransactionMode may have one of the following values: CardNotPresent [DEFAULT], CardPresent -->
                                                <TransactionMode >ENUMTYPE</TransactionMode> <!-- optional -->
                                                <!-- CreditCardTxnType may have one of the following values: Authorization, Capture, Charge, Refund, VoiceAuthorization -->
                                                <CreditCardTxnType >ENUMTYPE</CreditCardTxnType> <!-- optional -->
                                        </CreditCardTxnInputInfo>
                                        <CreditCardTxnResultInfo> <!-- required -->
                                                <ResultCode >INTTYPE</ResultCode> <!-- required -->
                                                <ResultMessage >STRTYPE</ResultMessage> <!-- required -->
                                                <CreditCardTransID >STRTYPE</CreditCardTransID> <!-- required -->
                                                <MerchantAccountNumber >STRTYPE</MerchantAccountNumber> <!-- required -->
                                                <AuthorizationCode >STRTYPE</AuthorizationCode> <!-- optional -->
                                                <!-- AVSStreet may have one of the following values: Pass, Fail, NotAvailable -->
                                                <AVSStreet >ENUMTYPE</AVSStreet> <!-- optional -->
                                                <!-- AVSZip may have one of the following values: Pass, Fail, NotAvailable -->
                                                <AVSZip >ENUMTYPE</AVSZip> <!-- optional -->
                                                <!-- CardSecurityCodeMatch may have one of the following values: Pass, Fail, NotAvailable -->
                                                <CardSecurityCodeMatch >ENUMTYPE</CardSecurityCodeMatch> <!-- optional -->
                                                <ReconBatchID >STRTYPE</ReconBatchID> <!-- optional -->
                                                <PaymentGroupingCode >INTTYPE</PaymentGroupingCode> <!-- optional -->
                                                <!-- PaymentStatus may have one of the following values: Unknown, Completed -->
                                                <PaymentStatus >ENUMTYPE</PaymentStatus> <!-- required -->
                                                <TxnAuthorizationTime >DATETIMETYPE</TxnAuthorizationTime> <!-- required -->
                                                <TxnAuthorizationStamp >INTTYPE</TxnAuthorizationStamp> <!-- optional -->
                                                <ClientTransID >STRTYPE</ClientTransID> <!-- optional -->
                                        </CreditCardTxnResultInfo>
                                </CreditCardTxnInfo>
                                <UnusedPayment >AMTTYPE</UnusedPayment> <!-- optional -->
                                <UnusedCredits >AMTTYPE</UnusedCredits> <!-- optional -->
                                <ExternalGUID >GUIDTYPE</ExternalGUID> <!-- optional -->
                                <AppliedToTxnRet> <!-- optional, may repeat -->
                                        <TxnID >IDTYPE</TxnID> <!-- required -->
                                        <!-- TxnType may have one of the following values: ARRefundCreditCard, Bill, BillPaymentCheck, BillPaymentCreditCard, BuildAssembly, Charge, Check, CreditCardCharge, CreditCardCredit, CreditMemo, Deposit, Estimate, InventoryAdjustment, Invoice, ItemReceipt, JournalEntry, LiabilityAdjustment, Paycheck, PayrollLiabilityCheck, PurchaseOrder, ReceivePayment, SalesOrder, SalesReceipt, SalesTaxPaymentCheck, Transfer, VendorCredit, YTDAdjustment -->
                                        <TxnType >ENUMTYPE</TxnType> <!-- required -->
                                        <TxnDate >DATETYPE</TxnDate> <!-- optional -->
                                        <RefNumber >STRTYPE</RefNumber> <!-- optional -->
                                        <BalanceRemaining >AMTTYPE</BalanceRemaining> <!-- optional -->
                                        <Amount >AMTTYPE</Amount> <!-- optional -->
                                        <DiscountAmount >AMTTYPE</DiscountAmount> <!-- optional -->
                                        <DiscountAccountRef> <!-- optional -->
                                                <ListID >IDTYPE</ListID> <!-- optional -->
                                                <FullName >STRTYPE</FullName> <!-- optional -->
                                        </DiscountAccountRef>
                                        <DiscountClassRef> <!-- optional -->
                                                <ListID >IDTYPE</ListID> <!-- optional -->
                                                <FullName >STRTYPE</FullName> <!-- optional -->
                                        </DiscountClassRef>
                                        <LinkedTxn> <!-- optional, may repeat -->
                                                <TxnID >IDTYPE</TxnID> <!-- required -->
                                                <!-- TxnType may have one of the following values: ARRefundCreditCard, Bill, BillPaymentCheck, BillPaymentCreditCard, BuildAssembly, Charge, Check, CreditCardCharge, CreditCardCredit, CreditMemo, Deposit, Estimate, InventoryAdjustment, Invoice, ItemReceipt, JournalEntry, LiabilityAdjustment, Paycheck, PayrollLiabilityCheck, PurchaseOrder, ReceivePayment, SalesOrder, SalesReceipt, SalesTaxPaymentCheck, Transfer, VendorCredit, YTDAdjustment -->
                                                <TxnType >ENUMTYPE</TxnType> <!-- required -->
                                                <TxnDate >DATETYPE</TxnDate> <!-- required -->
                                                <RefNumber >STRTYPE</RefNumber> <!-- optional -->
                                                <!-- LinkType may have one of the following values: AMTTYPE, QUANTYPE -->
                                                <LinkType >ENUMTYPE</LinkType> <!-- optional -->
                                                <Amount >AMTTYPE</Amount> <!-- required -->
                                        </LinkedTxn>
                                </AppliedToTxnRet>
                                <DataExtRet> <!-- optional, may repeat -->
                                        <OwnerID >GUIDTYPE</OwnerID> <!-- optional -->
                                        <DataExtName >STRTYPE</DataExtName> <!-- required -->
                                        <!-- DataExtType may have one of the following values: AMTTYPE, DATETIMETYPE, INTTYPE, PERCENTTYPE, PRICETYPE, QUANTYPE, STR1024TYPE, STR255TYPE -->
                                        <DataExtType >ENUMTYPE</DataExtType> <!-- required -->
                                        <DataExtValue >STRTYPE</DataExtValue> <!-- required -->
                                </DataExtRet>
                        </ReceivePaymentRet>
                </ReceivePaymentQueryRs>
        </QBXMLMsgsRq>
</QBXML>
```
## ReceivePaymentToDepositQuery
This query returns information about payments that have been received and are ready to deposit. You can use any returned TxnID and TxnLineID elements as PaymentTxnID and PaymentTxnLineID elements in subsequent DespositAdd requests. Note: If you include an explicit end tag in a ReceivePaymentToDepositQuery request, you will receive an error if there is any space between the opening tag and the end tag. The following table shows valid and invalid ways of constructing this request:
Valid
(no space between opening and closing tags)
Valid

(combined opening and closing tag)
Invalid
(space between opening and closing tags)

### XMLOps
```
<?xml version="1.0" encoding="utf-8"?>
<?qbxml version="16.0"?>
<QBXML>
        <QBXMLMsgsRq onError="stopOnError">
                <ReceivePaymentToDepositQueryRq metaData="ENUMTYPE">
                        <IncludeRetElement >STRTYPE</IncludeRetElement> <!-- optional, may repeat -->
                </ReceivePaymentToDepositQueryRq>

                <ReceivePaymentToDepositQueryRs statusCode="INTTYPE" statusSeverity="STRTYPE" statusMessage="STRTYPE" retCount="INTTYPE">
                        <ReceivePaymentToDepositRet> <!-- optional, may repeat -->
                                <TxnID >IDTYPE</TxnID> <!-- required -->
                                <TxnLineID >IDTYPE</TxnLineID> <!-- optional -->
                                <!-- TxnType may have one of the following values: ARRefundCreditCard, Bill, BillPaymentCheck, BillPaymentCreditCard, BuildAssembly, Charge, Check, CreditCardCharge, CreditCardCredit, CreditMemo, Deposit, Estimate, InventoryAdjustment, Invoice, ItemReceipt, JournalEntry, LiabilityAdjustment, Paycheck, PayrollLiabilityCheck, PurchaseOrder, ReceivePayment, SalesOrder, SalesReceipt, SalesTaxPaymentCheck, Transfer, VendorCredit, YTDAdjustment -->
                                <TxnType >ENUMTYPE</TxnType> <!-- required -->
                                <CustomerRef> <!-- optional -->
                                        <ListID >IDTYPE</ListID> <!-- optional -->
                                        <FullName >STRTYPE</FullName> <!-- optional -->
                                </CustomerRef>
                                <TxnDate >DATETYPE</TxnDate> <!-- required -->
                                <RefNumber >STRTYPE</RefNumber> <!-- optional -->
                                <Amount >AMTTYPE</Amount> <!-- required -->
                                <CurrencyRef> <!-- optional -->
                                        <ListID >IDTYPE</ListID> <!-- optional -->
                                        <FullName >STRTYPE</FullName> <!-- optional -->
                                </CurrencyRef>
                                <ExchangeRate >FLOATTYPE</ExchangeRate> <!-- optional -->
                                <AmountInHomeCurrency >AMTTYPE</AmountInHomeCurrency> <!-- optional -->
                        </ReceivePaymentToDepositRet>
                </ReceivePaymentToDepositQueryRs>
        </QBXMLMsgsRq>
</QBXML>
```
## SalesOrderQuery
### XMLOps
```
<?xml version="1.0" encoding="utf-8"?>
<?qbxml version="16.0"?>
<QBXML>
        <QBXMLMsgsRq onError="stopOnError">
                <SalesOrderQueryRq metaData="ENUMTYPE" iterator="ENUMTYPE" iteratorID="UUIDTYPE">
                        <!-- BEGIN OR -->
                                <TxnID >IDTYPE</TxnID> <!-- optional, may repeat -->
                        <!-- OR -->
                                <RefNumber >STRTYPE</RefNumber> <!-- optional, may repeat -->
                        <!-- OR -->
                                <RefNumberCaseSensitive >STRTYPE</RefNumberCaseSensitive> <!-- optional, may repeat -->
                        <!-- OR -->
                                <MaxReturned >INTTYPE</MaxReturned> <!-- optional -->
                                <!-- BEGIN OR -->
                                        <ModifiedDateRangeFilter> <!-- optional -->
                                                <FromModifiedDate >DATETIMETYPE</FromModifiedDate> <!-- optional -->
                                                <ToModifiedDate >DATETIMETYPE</ToModifiedDate> <!-- optional -->
                                        </ModifiedDateRangeFilter>
                                <!-- OR -->
                                        <TxnDateRangeFilter> <!-- optional -->
                                                <!-- BEGIN OR -->
                                                        <FromTxnDate >DATETYPE</FromTxnDate> <!-- optional -->
                                                        <ToTxnDate >DATETYPE</ToTxnDate> <!-- optional -->
                                                <!-- OR -->
                                                        <!-- DateMacro may have one of the following values: All, Today, ThisWeek, ThisWeekToDate, ThisMonth, ThisMonthToDate, ThisCalendarQuarter, ThisCalendarQuarterToDate, ThisFiscalQuarter, ThisFiscalQuarterToDate, ThisCalendarYear, ThisCalendarYearToDate, ThisFiscalYear, ThisFiscalYearToDate, Yesterday, LastWeek, LastWeekToDate, LastMonth, LastMonthToDate, LastCalendarQuarter, LastCalendarQuarterToDate, LastFiscalQuarter, LastFiscalQuarterToDate, LastCalendarYear, LastCalendarYearToDate, LastFiscalYear, LastFiscalYearToDate, NextWeek, NextFourWeeks, NextMonth, NextCalendarQuarter, NextCalendarYear, NextFiscalQuarter, NextFiscalYear -->
                                                        <DateMacro >ENUMTYPE</DateMacro> <!-- optional -->
                                                <!-- END OR -->
                                        </TxnDateRangeFilter>
                                <!-- END OR -->
                                <EntityFilter> <!-- optional -->
                                        <!-- BEGIN OR -->
                                                <ListID >IDTYPE</ListID> <!-- optional, may repeat -->
                                        <!-- OR -->
                                                <FullName >STRTYPE</FullName> <!-- optional, may repeat -->
                                        <!-- OR -->
                                                <ListIDWithChildren >IDTYPE</ListIDWithChildren> <!-- optional -->
                                        <!-- OR -->
                                                <FullNameWithChildren >STRTYPE</FullNameWithChildren> <!-- optional -->
                                        <!-- END OR -->
                                </EntityFilter>
                                <!-- BEGIN OR -->
                                        <RefNumberFilter> <!-- optional -->
                                                <!-- MatchCriterion may have one of the following values: StartsWith, Contains, EndsWith -->
                                                <MatchCriterion >ENUMTYPE</MatchCriterion> <!-- required -->
                                                <RefNumber >STRTYPE</RefNumber> <!-- required -->
                                        </RefNumberFilter>
                                <!-- OR -->
                                        <RefNumberRangeFilter> <!-- optional -->
                                                <FromRefNumber >STRTYPE</FromRefNumber> <!-- optional -->
                                                <ToRefNumber >STRTYPE</ToRefNumber> <!-- optional -->
                                        </RefNumberRangeFilter>
                                <!-- END OR -->
                                <CurrencyFilter> <!-- optional -->
                                        <!-- BEGIN OR -->
                                                <ListID >IDTYPE</ListID> <!-- optional, may repeat -->
                                        <!-- OR -->
                                                <FullName >STRTYPE</FullName> <!-- optional, may repeat -->
                                        <!-- END OR -->
                                </CurrencyFilter>
                        <!-- END OR -->
                        <IncludeLineItems >BOOLTYPE</IncludeLineItems> <!-- optional -->
                        <IncludeLinkedTxns >BOOLTYPE</IncludeLinkedTxns> <!-- optional -->
                        <IncludeRetElement >STRTYPE</IncludeRetElement> <!-- optional, may repeat -->
                        <OwnerID >GUIDTYPE</OwnerID> <!-- optional, may repeat -->
                </SalesOrderQueryRq>

                <SalesOrderQueryRs statusCode="INTTYPE" statusSeverity="STRTYPE" statusMessage="STRTYPE" retCount="INTTYPE" iteratorRemainingCount="INTTYPE" iteratorID="UUIDTYPE">
                        <SalesOrderRet> <!-- optional, may repeat -->
                                <TxnID >IDTYPE</TxnID> <!-- required -->
                                <TimeCreated >DATETIMETYPE</TimeCreated> <!-- required -->
                                <TimeModified >DATETIMETYPE</TimeModified> <!-- required -->
                                <EditSequence >STRTYPE</EditSequence> <!-- required -->
                                <TxnNumber >INTTYPE</TxnNumber> <!-- optional -->
                                <CustomerRef> <!-- required -->
                                        <ListID >IDTYPE</ListID> <!-- optional -->
                                        <FullName >STRTYPE</FullName> <!-- optional -->
                                </CustomerRef>
                                <ClassRef> <!-- optional -->
                                        <ListID >IDTYPE</ListID> <!-- optional -->
                                        <FullName >STRTYPE</FullName> <!-- optional -->
                                </ClassRef>
                                <TemplateRef> <!-- optional -->
                                        <ListID >IDTYPE</ListID> <!-- optional -->
                                        <FullName >STRTYPE</FullName> <!-- optional -->
                                </TemplateRef>
                                <TxnDate >DATETYPE</TxnDate> <!-- required -->
                                <RefNumber >STRTYPE</RefNumber> <!-- optional -->
                                <BillAddress> <!-- optional -->
                                        <Addr1 >STRTYPE</Addr1> <!-- optional -->
                                        <Addr2 >STRTYPE</Addr2> <!-- optional -->
                                        <Addr3 >STRTYPE</Addr3> <!-- optional -->
                                        <Addr4 >STRTYPE</Addr4> <!-- optional -->
                                        <Addr5 >STRTYPE</Addr5> <!-- optional -->
                                        <City >STRTYPE</City> <!-- optional -->
                                        <State >STRTYPE</State> <!-- optional -->
                                        <PostalCode >STRTYPE</PostalCode> <!-- optional -->
                                        <Country >STRTYPE</Country> <!-- optional -->
                                        <Note >STRTYPE</Note> <!-- optional -->
                                </BillAddress>
                                <BillAddressBlock> <!-- optional -->
                                        <Addr1 >STRTYPE</Addr1> <!-- optional -->
                                        <Addr2 >STRTYPE</Addr2> <!-- optional -->
                                        <Addr3 >STRTYPE</Addr3> <!-- optional -->
                                        <Addr4 >STRTYPE</Addr4> <!-- optional -->
                                        <Addr5 >STRTYPE</Addr5> <!-- optional -->
                                </BillAddressBlock>
                                <ShipAddress> <!-- optional -->
                                        <Addr1 >STRTYPE</Addr1> <!-- optional -->
                                        <Addr2 >STRTYPE</Addr2> <!-- optional -->
                                        <Addr3 >STRTYPE</Addr3> <!-- optional -->
                                        <Addr4 >STRTYPE</Addr4> <!-- optional -->
                                        <Addr5 >STRTYPE</Addr5> <!-- optional -->
                                        <City >STRTYPE</City> <!-- optional -->
                                        <State >STRTYPE</State> <!-- optional -->
                                        <PostalCode >STRTYPE</PostalCode> <!-- optional -->
                                        <Country >STRTYPE</Country> <!-- optional -->
                                        <Note >STRTYPE</Note> <!-- optional -->
                                </ShipAddress>
                                <ShipAddressBlock> <!-- optional -->
                                        <Addr1 >STRTYPE</Addr1> <!-- optional -->
                                        <Addr2 >STRTYPE</Addr2> <!-- optional -->
                                        <Addr3 >STRTYPE</Addr3> <!-- optional -->
                                        <Addr4 >STRTYPE</Addr4> <!-- optional -->
                                        <Addr5 >STRTYPE</Addr5> <!-- optional -->
                                </ShipAddressBlock>
                                <PONumber >STRTYPE</PONumber> <!-- optional -->
                                <TermsRef> <!-- optional -->
                                        <ListID >IDTYPE</ListID> <!-- optional -->
                                        <FullName >STRTYPE</FullName> <!-- optional -->
                                </TermsRef>
                                <DueDate >DATETYPE</DueDate> <!-- optional -->
                                <SalesRepRef> <!-- optional -->
                                        <ListID >IDTYPE</ListID> <!-- optional -->
                                        <FullName >STRTYPE</FullName> <!-- optional -->
                                </SalesRepRef>
                                <FOB >STRTYPE</FOB> <!-- optional -->
                                <ShipDate >DATETYPE</ShipDate> <!-- optional -->
                                <ShipMethodRef> <!-- optional -->
                                        <ListID >IDTYPE</ListID> <!-- optional -->
                                        <FullName >STRTYPE</FullName> <!-- optional -->
                                </ShipMethodRef>
                                <Subtotal >AMTTYPE</Subtotal> <!-- optional -->
                                <ItemSalesTaxRef> <!-- optional -->
                                        <ListID >IDTYPE</ListID> <!-- optional -->
                                        <FullName >STRTYPE</FullName> <!-- optional -->
                                </ItemSalesTaxRef>
                                <SalesTaxPercentage >PERCENTTYPE</SalesTaxPercentage> <!-- optional -->
                                <SalesTaxTotal >AMTTYPE</SalesTaxTotal> <!-- optional -->
                                <TotalAmount >AMTTYPE</TotalAmount> <!-- optional -->
                                <CurrencyRef> <!-- optional -->
                                        <ListID >IDTYPE</ListID> <!-- optional -->
                                        <FullName >STRTYPE</FullName> <!-- optional -->
                                </CurrencyRef>
                                <ExchangeRate >FLOATTYPE</ExchangeRate> <!-- optional -->
                                <TotalAmountInHomeCurrency >AMTTYPE</TotalAmountInHomeCurrency> <!-- optional -->
                                <IsManuallyClosed >BOOLTYPE</IsManuallyClosed> <!-- optional -->
                                <IsFullyInvoiced >BOOLTYPE</IsFullyInvoiced> <!-- optional -->
                                <Memo >STRTYPE</Memo> <!-- optional -->
                                <CustomerMsgRef> <!-- optional -->
                                        <ListID >IDTYPE</ListID> <!-- optional -->
                                        <FullName >STRTYPE</FullName> <!-- optional -->
                                </CustomerMsgRef>
                                <IsToBePrinted >BOOLTYPE</IsToBePrinted> <!-- optional -->
                                <IsToBeEmailed >BOOLTYPE</IsToBeEmailed> <!-- optional -->
                                <IsTaxIncluded >BOOLTYPE</IsTaxIncluded> <!-- optional -->
                                <CustomerSalesTaxCodeRef> <!-- optional -->
                                        <ListID >IDTYPE</ListID> <!-- optional -->
                                        <FullName >STRTYPE</FullName> <!-- optional -->
                                </CustomerSalesTaxCodeRef>
                                <Other >STRTYPE</Other> <!-- optional -->
                                <ExternalGUID >GUIDTYPE</ExternalGUID> <!-- optional -->
                                <LinkedTxn> <!-- optional, may repeat -->
                                        <TxnID >IDTYPE</TxnID> <!-- required -->
                                        <!-- TxnType may have one of the following values: ARRefundCreditCard, Bill, BillPaymentCheck, BillPaymentCreditCard, BuildAssembly, Charge, Check, CreditCardCharge, CreditCardCredit, CreditMemo, Deposit, Estimate, InventoryAdjustment, Invoice, ItemReceipt, JournalEntry, LiabilityAdjustment, Paycheck, PayrollLiabilityCheck, PurchaseOrder, ReceivePayment, SalesOrder, SalesReceipt, SalesTaxPaymentCheck, Transfer, VendorCredit, YTDAdjustment -->
                                        <TxnType >ENUMTYPE</TxnType> <!-- required -->
                                        <TxnDate >DATETYPE</TxnDate> <!-- required -->
                                        <RefNumber >STRTYPE</RefNumber> <!-- optional -->
                                        <!-- LinkType may have one of the following values: AMTTYPE, QUANTYPE -->
                                        <LinkType >ENUMTYPE</LinkType> <!-- optional -->
                                        <Amount >AMTTYPE</Amount> <!-- required -->
                                </LinkedTxn>
                                <!-- BEGIN OR -->
                                        <SalesOrderLineRet> <!-- optional -->
                                                <TxnLineID >IDTYPE</TxnLineID> <!-- required -->
                                                <ItemRef> <!-- optional -->
                                                        <ListID >IDTYPE</ListID> <!-- optional -->
                                                        <FullName >STRTYPE</FullName> <!-- optional -->
                                                </ItemRef>
                                                <Desc >STRTYPE</Desc> <!-- optional -->
                                                <Quantity >QUANTYPE</Quantity> <!-- optional -->
                                                <UnitOfMeasure >STRTYPE</UnitOfMeasure> <!-- optional -->
                                                <OverrideUOMSetRef> <!-- optional -->
                                                        <ListID >IDTYPE</ListID> <!-- optional -->
                                                        <FullName >STRTYPE</FullName> <!-- optional -->
                                                </OverrideUOMSetRef>
                                                <!-- BEGIN OR -->
                                                        <Rate >PRICETYPE</Rate> <!-- optional -->
                                                <!-- OR -->
                                                        <RatePercent >PERCENTTYPE</RatePercent> <!-- optional -->
                                                <!-- END OR -->
                                                <ClassRef> <!-- optional -->
                                                        <ListID >IDTYPE</ListID> <!-- optional -->
                                                        <FullName >STRTYPE</FullName> <!-- optional -->
                                                </ClassRef>
                                                <Amount >AMTTYPE</Amount> <!-- optional -->
                                                <InventorySiteRef> <!-- optional -->
                                                        <ListID >IDTYPE</ListID> <!-- optional -->
                                                        <FullName >STRTYPE</FullName> <!-- optional -->
                                                </InventorySiteRef>
                                                <InventorySiteLocationRef> <!-- optional -->
                                                        <ListID >IDTYPE</ListID> <!-- optional -->
                                                        <FullName >STRTYPE</FullName> <!-- optional -->
                                                </InventorySiteLocationRef>
                                                <!-- BEGIN OR -->
                                                        <SerialNumber >STRTYPE</SerialNumber> <!-- optional -->
                                                <!-- OR -->
                                                        <LotNumber >STRTYPE</LotNumber> <!-- optional -->
                                                <!-- END OR -->
                                                <ExpirationDateForSerialLotNumber>STRTYPE</ExpirationDateForSerialLotNumber> <!-- optional -->
                                                <SalesTaxCodeRef> <!-- optional -->
                                                        <ListID >IDTYPE</ListID> <!-- optional -->
                                                        <FullName >STRTYPE</FullName> <!-- optional -->
                                                </SalesTaxCodeRef>
                                                <Invoiced >QUANTYPE</Invoiced> <!-- optional -->
                                                <IsManuallyClosed >BOOLTYPE</IsManuallyClosed> <!-- optional -->
                                                <Other1 >STRTYPE</Other1> <!-- optional -->
                                                <Other2 >STRTYPE</Other2> <!-- optional -->
                                                <DataExtRet> <!-- optional, may repeat -->
                                                        <OwnerID >GUIDTYPE</OwnerID> <!-- optional -->
                                                        <DataExtName >STRTYPE</DataExtName> <!-- required -->
                                                        <!-- DataExtType may have one of the following values: AMTTYPE, DATETIMETYPE, INTTYPE, PERCENTTYPE, PRICETYPE, QUANTYPE, STR1024TYPE, STR255TYPE -->
                                                        <DataExtType >ENUMTYPE</DataExtType> <!-- required -->
                                                        <DataExtValue >STRTYPE</DataExtValue> <!-- required -->
                                                </DataExtRet>
                                        </SalesOrderLineRet>
                                <!-- OR -->
                                        <SalesOrderLineGroupRet> <!-- optional -->
                                                <TxnLineID >IDTYPE</TxnLineID> <!-- required -->
                                                <ItemGroupRef> <!-- required -->
                                                        <ListID >IDTYPE</ListID> <!-- optional -->
                                                        <FullName >STRTYPE</FullName> <!-- optional -->
                                                </ItemGroupRef>
                                                <Desc >STRTYPE</Desc> <!-- optional -->
                                                <Quantity >QUANTYPE</Quantity> <!-- optional -->
                                                <UnitOfMeasure >STRTYPE</UnitOfMeasure> <!-- optional -->
                                                <OverrideUOMSetRef> <!-- optional -->
                                                        <ListID >IDTYPE</ListID> <!-- optional -->
                                                        <FullName >STRTYPE</FullName> <!-- optional -->
                                                </OverrideUOMSetRef>
                                                <IsPrintItemsInGroup >BOOLTYPE</IsPrintItemsInGroup> <!-- required -->
                                                <TotalAmount >AMTTYPE</TotalAmount> <!-- required -->
                                                <SalesOrderLineRet> <!-- optional, may repeat -->
                                                        <TxnLineID >IDTYPE</TxnLineID> <!-- required -->
                                                        <ItemRef> <!-- optional -->
                                                                <ListID >IDTYPE</ListID> <!-- optional -->
                                                                <FullName >STRTYPE</FullName> <!-- optional -->
                                                        </ItemRef>
                                                        <Desc >STRTYPE</Desc> <!-- optional -->
                                                        <Quantity >QUANTYPE</Quantity> <!-- optional -->
                                                        <UnitOfMeasure >STRTYPE</UnitOfMeasure> <!-- optional -->
                                                        <OverrideUOMSetRef> <!-- optional -->
                                                                <ListID >IDTYPE</ListID> <!-- optional -->
                                                                <FullName >STRTYPE</FullName> <!-- optional -->
                                                        </OverrideUOMSetRef>
                                                        <!-- BEGIN OR -->
                                                                <Rate >PRICETYPE</Rate> <!-- optional -->
                                                        <!-- OR -->
                                                                <RatePercent >PERCENTTYPE</RatePercent> <!-- optional -->
                                                        <!-- END OR -->
                                                        <ClassRef> <!-- optional -->
                                                                <ListID >IDTYPE</ListID> <!-- optional -->
                                                                <FullName >STRTYPE</FullName> <!-- optional -->
                                                        </ClassRef>
                                                        <Amount >AMTTYPE</Amount> <!-- optional -->
                                                        <InventorySiteRef> <!-- optional -->
                                                                <ListID >IDTYPE</ListID> <!-- optional -->
                                                                <FullName >STRTYPE</FullName> <!-- optional -->
                                                        </InventorySiteRef>
                                                        <InventorySiteLocationRef> <!-- optional -->
                                                                <ListID >IDTYPE</ListID> <!-- optional -->
                                                                <FullName >STRTYPE</FullName> <!-- optional -->
                                                        </InventorySiteLocationRef>
                                                        <!-- BEGIN OR -->
                                                                <SerialNumber >STRTYPE</SerialNumber> <!-- optional -->
                                                        <!-- OR -->
                                                                <LotNumber >STRTYPE</LotNumber> <!-- optional -->
                                                        <!-- END OR -->
                                                        <ExpirationDateForSerialLotNumber>STRTYPE</ExpirationDateForSerialLotNumber> <!-- optional -->
                                                        <SalesTaxCodeRef> <!-- optional -->
                                                                <ListID >IDTYPE</ListID> <!-- optional -->
                                                                <FullName >STRTYPE</FullName> <!-- optional -->
                                                        </SalesTaxCodeRef>
                                                        <Invoiced >QUANTYPE</Invoiced> <!-- optional -->
                                                        <IsManuallyClosed >BOOLTYPE</IsManuallyClosed> <!-- optional -->
                                                        <Other1 >STRTYPE</Other1> <!-- optional -->
                                                        <Other2 >STRTYPE</Other2> <!-- optional -->
                                                        <DataExtRet> <!-- optional, may repeat -->
                                                                <OwnerID >GUIDTYPE</OwnerID> <!-- optional -->
                                                                <DataExtName >STRTYPE</DataExtName> <!-- required -->
                                                                <!-- DataExtType may have one of the following values: AMTTYPE, DATETIMETYPE, INTTYPE, PERCENTTYPE, PRICETYPE, QUANTYPE, STR1024TYPE, STR255TYPE -->
                                                                <DataExtType >ENUMTYPE</DataExtType> <!-- required -->
                                                                <DataExtValue >STRTYPE</DataExtValue> <!-- required -->
                                                        </DataExtRet>
                                                </SalesOrderLineRet>
                                                <DataExtRet> <!-- optional, may repeat -->
                                                        <OwnerID >GUIDTYPE</OwnerID> <!-- optional -->
                                                        <DataExtName >STRTYPE</DataExtName> <!-- required -->
                                                        <!-- DataExtType may have one of the following values: AMTTYPE, DATETIMETYPE, INTTYPE, PERCENTTYPE, PRICETYPE, QUANTYPE, STR1024TYPE, STR255TYPE -->
                                                        <DataExtType >ENUMTYPE</DataExtType> <!-- required -->
                                                        <DataExtValue >STRTYPE</DataExtValue> <!-- required -->
                                                </DataExtRet>
                                        </SalesOrderLineGroupRet>
                                <!-- END OR -->
                                <DataExtRet> <!-- optional, may repeat -->
                                        <OwnerID >GUIDTYPE</OwnerID> <!-- optional -->
                                        <DataExtName >STRTYPE</DataExtName> <!-- required -->
                                        <!-- DataExtType may have one of the following values: AMTTYPE, DATETIMETYPE, INTTYPE, PERCENTTYPE, PRICETYPE, QUANTYPE, STR1024TYPE, STR255TYPE -->
                                        <DataExtType >ENUMTYPE</DataExtType> <!-- required -->
                                        <DataExtValue >STRTYPE</DataExtValue> <!-- required -->
                                </DataExtRet>
                                <FulfillmentStatus>ENUMTYPE</FulfillmentStatus> <!-- optional -->
                                <ShippingDetails> <!-- optional -->
                                <ShippingDetailsLineRet> <!-- optional -->
                                <TrackingID>IDTYPE</TrackingID>  <!-- optional -->
                                <CarrierName>STRTYPE</CarrierName>  <!-- optional -->
                                <ShippingMethod>STRTYPE</ShippingMethod>  <!-- optional -->
                                <ShippingCharges>AMTTYPE</ShippingCharges>  <!-- optional -->
                                </ShippingDetailsLineRet>
                                </ShippingDetails>
                                <SOChannel>ENUMTYPE</SOChannel> <!-- optional -->
                                <StoreName>STRTYPE</StoreName> <!-- optional -->
                                <StoreType>STRTYPE</StoreType> <!-- optional -->
                        </SalesOrderRet>
                </SalesOrderQueryRs>
        </QBXMLMsgsRq>
</QBXML>
```
## SalesReceiptQuery
### XMLOps
```
<?xml version="1.0" encoding="utf-8"?>
<?qbxml version="16.0"?>
<QBXML>
        <QBXMLMsgsRq onError="stopOnError">
                <SalesReceiptQueryRq metaData="ENUMTYPE" iterator="ENUMTYPE" iteratorID="UUIDTYPE">
                        <!-- BEGIN OR -->
                                <TxnID >IDTYPE</TxnID> <!-- optional, may repeat -->
                        <!-- OR -->
                                <RefNumber >STRTYPE</RefNumber> <!-- optional, may repeat -->
                        <!-- OR -->
                                <RefNumberCaseSensitive >STRTYPE</RefNumberCaseSensitive> <!-- optional, may repeat -->
                        <!-- OR -->
                                <MaxReturned >INTTYPE</MaxReturned> <!-- optional -->
                                <!-- BEGIN OR -->
                                        <ModifiedDateRangeFilter> <!-- optional -->
                                                <FromModifiedDate >DATETIMETYPE</FromModifiedDate> <!-- optional -->
                                                <ToModifiedDate >DATETIMETYPE</ToModifiedDate> <!-- optional -->
                                        </ModifiedDateRangeFilter>
                                <!-- OR -->
                                        <TxnDateRangeFilter> <!-- optional -->
                                                <!-- BEGIN OR -->
                                                        <FromTxnDate >DATETYPE</FromTxnDate> <!-- optional -->
                                                        <ToTxnDate >DATETYPE</ToTxnDate> <!-- optional -->
                                                <!-- OR -->
                                                        <!-- DateMacro may have one of the following values: All, Today, ThisWeek, ThisWeekToDate, ThisMonth, ThisMonthToDate, ThisCalendarQuarter, ThisCalendarQuarterToDate, ThisFiscalQuarter, ThisFiscalQuarterToDate, ThisCalendarYear, ThisCalendarYearToDate, ThisFiscalYear, ThisFiscalYearToDate, Yesterday, LastWeek, LastWeekToDate, LastMonth, LastMonthToDate, LastCalendarQuarter, LastCalendarQuarterToDate, LastFiscalQuarter, LastFiscalQuarterToDate, LastCalendarYear, LastCalendarYearToDate, LastFiscalYear, LastFiscalYearToDate, NextWeek, NextFourWeeks, NextMonth, NextCalendarQuarter, NextCalendarYear, NextFiscalQuarter, NextFiscalYear -->
                                                        <DateMacro >ENUMTYPE</DateMacro> <!-- optional -->
                                                <!-- END OR -->
                                        </TxnDateRangeFilter>
                                <!-- END OR -->
                                <EntityFilter> <!-- optional -->
                                        <!-- BEGIN OR -->
                                                <ListID >IDTYPE</ListID> <!-- optional, may repeat -->
                                        <!-- OR -->
                                                <FullName >STRTYPE</FullName> <!-- optional, may repeat -->
                                        <!-- OR -->
                                                <ListIDWithChildren >IDTYPE</ListIDWithChildren> <!-- optional -->
                                        <!-- OR -->
                                                <FullNameWithChildren >STRTYPE</FullNameWithChildren> <!-- optional -->
                                        <!-- END OR -->
                                </EntityFilter>
                                <AccountFilter> <!-- optional -->
                                        <!-- BEGIN OR -->
                                                <ListID >IDTYPE</ListID> <!-- optional, may repeat -->
                                        <!-- OR -->
                                                <FullName >STRTYPE</FullName> <!-- optional, may repeat -->
                                        <!-- OR -->
                                                <ListIDWithChildren >IDTYPE</ListIDWithChildren> <!-- optional -->
                                        <!-- OR -->
                                                <FullNameWithChildren >STRTYPE</FullNameWithChildren> <!-- optional -->
                                        <!-- END OR -->
                                </AccountFilter>
                                <!-- BEGIN OR -->
                                        <RefNumberFilter> <!-- optional -->
                                                <!-- MatchCriterion may have one of the following values: StartsWith, Contains, EndsWith -->
                                                <MatchCriterion >ENUMTYPE</MatchCriterion> <!-- required -->
                                                <RefNumber >STRTYPE</RefNumber> <!-- required -->
                                        </RefNumberFilter>
                                <!-- OR -->
                                        <RefNumberRangeFilter> <!-- optional -->
                                                <FromRefNumber >STRTYPE</FromRefNumber> <!-- optional -->
                                                <ToRefNumber >STRTYPE</ToRefNumber> <!-- optional -->
                                        </RefNumberRangeFilter>
                                <!-- END OR -->
                                <CurrencyFilter> <!-- optional -->
                                        <!-- BEGIN OR -->
                                                <ListID >IDTYPE</ListID> <!-- optional, may repeat -->
                                        <!-- OR -->
                                                <FullName >STRTYPE</FullName> <!-- optional, may repeat -->
                                        <!-- END OR -->
                                </CurrencyFilter>
                        <!-- END OR -->
                        <IncludeLineItems >BOOLTYPE</IncludeLineItems> <!-- optional -->
                        <IncludeRetElement >STRTYPE</IncludeRetElement> <!-- optional, may repeat -->
                        <OwnerID >GUIDTYPE</OwnerID> <!-- optional, may repeat -->
                </SalesReceiptQueryRq>

                <SalesReceiptQueryRs statusCode="INTTYPE" statusSeverity="STRTYPE" statusMessage="STRTYPE" retCount="INTTYPE" iteratorRemainingCount="INTTYPE" iteratorID="UUIDTYPE">
                        <SalesReceiptRet> <!-- optional, may repeat -->
                                <TxnID >IDTYPE</TxnID> <!-- required -->
                                <TimeCreated >DATETIMETYPE</TimeCreated> <!-- required -->
                                <TimeModified >DATETIMETYPE</TimeModified> <!-- required -->
                                <EditSequence >STRTYPE</EditSequence> <!-- required -->
                                <TxnNumber >INTTYPE</TxnNumber> <!-- optional -->
                                <CustomerRef> <!-- optional -->
                                        <ListID >IDTYPE</ListID> <!-- optional -->
                                        <FullName >STRTYPE</FullName> <!-- optional -->
                                </CustomerRef>
                                <ClassRef> <!-- optional -->
                                        <ListID >IDTYPE</ListID> <!-- optional -->
                                        <FullName >STRTYPE</FullName> <!-- optional -->
                                </ClassRef>
                                <TemplateRef> <!-- optional -->
                                        <ListID >IDTYPE</ListID> <!-- optional -->
                                        <FullName >STRTYPE</FullName> <!-- optional -->
                                </TemplateRef>
                                <TxnDate >DATETYPE</TxnDate> <!-- required -->
                                <RefNumber >STRTYPE</RefNumber> <!-- optional -->
                                <BillAddress> <!-- optional -->
                                        <Addr1 >STRTYPE</Addr1> <!-- optional -->
                                        <Addr2 >STRTYPE</Addr2> <!-- optional -->
                                        <Addr3 >STRTYPE</Addr3> <!-- optional -->
                                        <Addr4 >STRTYPE</Addr4> <!-- optional -->
                                        <Addr5 >STRTYPE</Addr5> <!-- optional -->
                                        <City >STRTYPE</City> <!-- optional -->
                                        <State >STRTYPE</State> <!-- optional -->
                                        <PostalCode >STRTYPE</PostalCode> <!-- optional -->
                                        <Country >STRTYPE</Country> <!-- optional -->
                                        <Note >STRTYPE</Note> <!-- optional -->
                                </BillAddress>
                                <BillAddressBlock> <!-- optional -->
                                        <Addr1 >STRTYPE</Addr1> <!-- optional -->
                                        <Addr2 >STRTYPE</Addr2> <!-- optional -->
                                        <Addr3 >STRTYPE</Addr3> <!-- optional -->
                                        <Addr4 >STRTYPE</Addr4> <!-- optional -->
                                        <Addr5 >STRTYPE</Addr5> <!-- optional -->
                                </BillAddressBlock>
                                <ShipAddress> <!-- optional -->
                                        <Addr1 >STRTYPE</Addr1> <!-- optional -->
                                        <Addr2 >STRTYPE</Addr2> <!-- optional -->
                                        <Addr3 >STRTYPE</Addr3> <!-- optional -->
                                        <Addr4 >STRTYPE</Addr4> <!-- optional -->
                                        <Addr5 >STRTYPE</Addr5> <!-- optional -->
                                        <City >STRTYPE</City> <!-- optional -->
                                        <State >STRTYPE</State> <!-- optional -->
                                        <PostalCode >STRTYPE</PostalCode> <!-- optional -->
                                        <Country >STRTYPE</Country> <!-- optional -->
                                        <Note >STRTYPE</Note> <!-- optional -->
                                </ShipAddress>
                                <ShipAddressBlock> <!-- optional -->
                                        <Addr1 >STRTYPE</Addr1> <!-- optional -->
                                        <Addr2 >STRTYPE</Addr2> <!-- optional -->
                                        <Addr3 >STRTYPE</Addr3> <!-- optional -->
                                        <Addr4 >STRTYPE</Addr4> <!-- optional -->
                                        <Addr5 >STRTYPE</Addr5> <!-- optional -->
                                </ShipAddressBlock>
                                <IsPending >BOOLTYPE</IsPending> <!-- optional -->
                                <CheckNumber >STRTYPE</CheckNumber> <!-- optional -->
                                <PaymentMethodRef> <!-- optional -->
                                        <ListID >IDTYPE</ListID> <!-- optional -->
                                        <FullName >STRTYPE</FullName> <!-- optional -->
                                </PaymentMethodRef>
                                <DueDate >DATETYPE</DueDate> <!-- optional -->
                                <SalesRepRef> <!-- optional -->
                                        <ListID >IDTYPE</ListID> <!-- optional -->
                                        <FullName >STRTYPE</FullName> <!-- optional -->
                                </SalesRepRef>
                                <ShipDate >DATETYPE</ShipDate> <!-- optional -->
                                <ShipMethodRef> <!-- optional -->
                                        <ListID >IDTYPE</ListID> <!-- optional -->
                                        <FullName >STRTYPE</FullName> <!-- optional -->
                                </ShipMethodRef>
                                <FOB >STRTYPE</FOB> <!-- optional -->
                                <Subtotal >AMTTYPE</Subtotal> <!-- optional -->
                                <ItemSalesTaxRef> <!-- optional -->
                                        <ListID >IDTYPE</ListID> <!-- optional -->
                                        <FullName >STRTYPE</FullName> <!-- optional -->
                                </ItemSalesTaxRef>
                                <SalesTaxPercentage >PERCENTTYPE</SalesTaxPercentage> <!-- optional -->
                                <SalesTaxTotal >AMTTYPE</SalesTaxTotal> <!-- optional -->
                                <TotalAmount >AMTTYPE</TotalAmount> <!-- optional -->
                                <CurrencyRef> <!-- optional -->
                                        <ListID >IDTYPE</ListID> <!-- optional -->
                                        <FullName >STRTYPE</FullName> <!-- optional -->
                                </CurrencyRef>
                                <ExchangeRate >FLOATTYPE</ExchangeRate> <!-- optional -->
                                <TotalAmountInHomeCurrency >AMTTYPE</TotalAmountInHomeCurrency> <!-- optional -->
                                <Memo >STRTYPE</Memo> <!-- optional -->
                                <CustomerMsgRef> <!-- optional -->
                                        <ListID >IDTYPE</ListID> <!-- optional -->
                                        <FullName >STRTYPE</FullName> <!-- optional -->
                                </CustomerMsgRef>
                                <IsToBePrinted >BOOLTYPE</IsToBePrinted> <!-- optional -->
                                <IsToBeEmailed >BOOLTYPE</IsToBeEmailed> <!-- optional -->
                                <IsTaxIncluded >BOOLTYPE</IsTaxIncluded> <!-- optional -->
                                <CustomerSalesTaxCodeRef> <!-- optional -->
                                        <ListID >IDTYPE</ListID> <!-- optional -->
                                        <FullName >STRTYPE</FullName> <!-- optional -->
                                </CustomerSalesTaxCodeRef>
                                <DepositToAccountRef> <!-- optional -->
                                        <ListID >IDTYPE</ListID> <!-- optional -->
                                        <FullName >STRTYPE</FullName> <!-- optional -->
                                </DepositToAccountRef>
                                <CreditCardTxnInfo> <!-- optional -->
                                        <CreditCardTxnInputInfo> <!-- required -->
                                                <CreditCardNumber >STRTYPE</CreditCardNumber> <!-- required -->
                                                <ExpirationMonth >INTTYPE</ExpirationMonth> <!-- required -->
                                                <ExpirationYear >INTTYPE</ExpirationYear> <!-- required -->
                                                <NameOnCard >STRTYPE</NameOnCard> <!-- required -->
                                                <CreditCardAddress >STRTYPE</CreditCardAddress> <!-- optional -->
                                                <CreditCardPostalCode >STRTYPE</CreditCardPostalCode> <!-- optional -->
                                                <CommercialCardCode >STRTYPE</CommercialCardCode> <!-- optional -->
                                                <!-- TransactionMode may have one of the following values: CardNotPresent [DEFAULT], CardPresent -->
                                                <TransactionMode >ENUMTYPE</TransactionMode> <!-- optional -->
                                                <!-- CreditCardTxnType may have one of the following values: Authorization, Capture, Charge, Refund, VoiceAuthorization -->
                                                <CreditCardTxnType >ENUMTYPE</CreditCardTxnType> <!-- optional -->
                                        </CreditCardTxnInputInfo>
                                        <CreditCardTxnResultInfo> <!-- required -->
                                                <ResultCode >INTTYPE</ResultCode> <!-- required -->
                                                <ResultMessage >STRTYPE</ResultMessage> <!-- required -->
                                                <CreditCardTransID >STRTYPE</CreditCardTransID> <!-- required -->
                                                <MerchantAccountNumber >STRTYPE</MerchantAccountNumber> <!-- required -->
                                                <AuthorizationCode >STRTYPE</AuthorizationCode> <!-- optional -->
                                                <!-- AVSStreet may have one of the following values: Pass, Fail, NotAvailable -->
                                                <AVSStreet >ENUMTYPE</AVSStreet> <!-- optional -->
                                                <!-- AVSZip may have one of the following values: Pass, Fail, NotAvailable -->
                                                <AVSZip >ENUMTYPE</AVSZip> <!-- optional -->
                                                <!-- CardSecurityCodeMatch may have one of the following values: Pass, Fail, NotAvailable -->
                                                <CardSecurityCodeMatch >ENUMTYPE</CardSecurityCodeMatch> <!-- optional -->
                                                <ReconBatchID >STRTYPE</ReconBatchID> <!-- optional -->
                                                <PaymentGroupingCode >INTTYPE</PaymentGroupingCode> <!-- optional -->
                                                <!-- PaymentStatus may have one of the following values: Unknown, Completed -->
                                                <PaymentStatus >ENUMTYPE</PaymentStatus> <!-- required -->
                                                <TxnAuthorizationTime >DATETIMETYPE</TxnAuthorizationTime> <!-- required -->
                                                <TxnAuthorizationStamp >INTTYPE</TxnAuthorizationStamp> <!-- optional -->
                                                <ClientTransID >STRTYPE</ClientTransID> <!-- optional -->
                                        </CreditCardTxnResultInfo>
                                </CreditCardTxnInfo>
                                <Other >STRTYPE</Other> <!-- optional -->
                                <ExternalGUID >GUIDTYPE</ExternalGUID> <!-- optional -->
                                <!-- BEGIN OR -->
                                        <SalesReceiptLineRet> <!-- optional -->
                                                <TxnLineID >IDTYPE</TxnLineID> <!-- required -->
                                                <ItemRef> <!-- optional -->
                                                        <ListID >IDTYPE</ListID> <!-- optional -->
                                                        <FullName >STRTYPE</FullName> <!-- optional -->
                                                </ItemRef>
                                                <Desc >STRTYPE</Desc> <!-- optional -->
                                                <Quantity >QUANTYPE</Quantity> <!-- optional -->
                                                <UnitOfMeasure >STRTYPE</UnitOfMeasure> <!-- optional -->
                                                <OverrideUOMSetRef> <!-- optional -->
                                                        <ListID >IDTYPE</ListID> <!-- optional -->
                                                        <FullName >STRTYPE</FullName> <!-- optional -->
                                                </OverrideUOMSetRef>
                                                <!-- BEGIN OR -->
                                                        <Rate >PRICETYPE</Rate> <!-- optional -->
                                                <!-- OR -->
                                                        <RatePercent >PERCENTTYPE</RatePercent> <!-- optional -->
                                                <!-- END OR -->
                                                <ClassRef> <!-- optional -->
                                                        <ListID >IDTYPE</ListID> <!-- optional -->
                                                        <FullName >STRTYPE</FullName> <!-- optional -->
                                                </ClassRef>
                                                <Amount >AMTTYPE</Amount> <!-- optional -->
                                                <InventorySiteRef> <!-- optional -->
                                                        <ListID >IDTYPE</ListID> <!-- optional -->
                                                        <FullName >STRTYPE</FullName> <!-- optional -->
                                                </InventorySiteRef>
                                                <InventorySiteLocationRef> <!-- optional -->
                                                        <ListID >IDTYPE</ListID> <!-- optional -->
                                                        <FullName >STRTYPE</FullName> <!-- optional -->
                                                </InventorySiteLocationRef>
                                                <!-- BEGIN OR -->
                                                        <SerialNumber >STRTYPE</SerialNumber> <!-- optional -->
                                                <!-- OR -->
                                                        <LotNumber >STRTYPE</LotNumber> <!-- optional -->
                                                <!-- END OR -->
                                                <ExpirationDateForSerialLotNumber>STRTYPE</ExpirationDateForSerialLotNumber> <!-- optional -->
                                                <ServiceDate >DATETYPE</ServiceDate> <!-- optional -->
                                                <SalesTaxCodeRef> <!-- optional -->
                                                        <ListID >IDTYPE</ListID> <!-- optional -->
                                                        <FullName >STRTYPE</FullName> <!-- optional -->
                                                </SalesTaxCodeRef>
                                                <Other1 >STRTYPE</Other1> <!-- optional -->
                                                <Other2 >STRTYPE</Other2> <!-- optional -->
                                                <CreditCardTxnInfo> <!-- optional -->
                                                        <CreditCardTxnInputInfo> <!-- required -->
                                                                <CreditCardNumber >STRTYPE</CreditCardNumber> <!-- required -->
                                                                <ExpirationMonth >INTTYPE</ExpirationMonth> <!-- required -->
                                                                <ExpirationYear >INTTYPE</ExpirationYear> <!-- required -->
                                                                <NameOnCard >STRTYPE</NameOnCard> <!-- required -->
                                                                <CreditCardAddress >STRTYPE</CreditCardAddress> <!-- optional -->
                                                                <CreditCardPostalCode >STRTYPE</CreditCardPostalCode> <!-- optional -->
                                                                <CommercialCardCode >STRTYPE</CommercialCardCode> <!-- optional -->
                                                                <!-- TransactionMode may have one of the following values: CardNotPresent [DEFAULT], CardPresent -->
                                                                <TransactionMode >ENUMTYPE</TransactionMode> <!-- optional -->
                                                                <!-- CreditCardTxnType may have one of the following values: Authorization, Capture, Charge, Refund, VoiceAuthorization -->
                                                                <CreditCardTxnType >ENUMTYPE</CreditCardTxnType> <!-- optional -->
                                                        </CreditCardTxnInputInfo>
                                                        <CreditCardTxnResultInfo> <!-- required -->
                                                                <ResultCode >INTTYPE</ResultCode> <!-- required -->
                                                                <ResultMessage >STRTYPE</ResultMessage> <!-- required -->
                                                                <CreditCardTransID >STRTYPE</CreditCardTransID> <!-- required -->
                                                                <MerchantAccountNumber >STRTYPE</MerchantAccountNumber> <!-- required -->
                                                                <AuthorizationCode >STRTYPE</AuthorizationCode> <!-- optional -->
                                                                <!-- AVSStreet may have one of the following values: Pass, Fail, NotAvailable -->
                                                                <AVSStreet >ENUMTYPE</AVSStreet> <!-- optional -->
                                                                <!-- AVSZip may have one of the following values: Pass, Fail, NotAvailable -->
                                                                <AVSZip >ENUMTYPE</AVSZip> <!-- optional -->
                                                                <!-- CardSecurityCodeMatch may have one of the following values: Pass, Fail, NotAvailable -->
                                                                <CardSecurityCodeMatch >ENUMTYPE</CardSecurityCodeMatch> <!-- optional -->
                                                                <ReconBatchID >STRTYPE</ReconBatchID> <!-- optional -->
                                                                <PaymentGroupingCode >INTTYPE</PaymentGroupingCode> <!-- optional -->
                                                                <!-- PaymentStatus may have one of the following values: Unknown, Completed -->
                                                                <PaymentStatus >ENUMTYPE</PaymentStatus> <!-- required -->
                                                                <TxnAuthorizationTime >DATETIMETYPE</TxnAuthorizationTime> <!-- required -->
                                                                <TxnAuthorizationStamp >INTTYPE</TxnAuthorizationStamp> <!-- optional -->
                                                                <ClientTransID >STRTYPE</ClientTransID> <!-- optional -->
                                                        </CreditCardTxnResultInfo>
                                                </CreditCardTxnInfo>
                                                <DataExtRet> <!-- optional, may repeat -->
                                                        <OwnerID >GUIDTYPE</OwnerID> <!-- optional -->
                                                        <DataExtName >STRTYPE</DataExtName> <!-- required -->
                                                        <!-- DataExtType may have one of the following values: AMTTYPE, DATETIMETYPE, INTTYPE, PERCENTTYPE, PRICETYPE, QUANTYPE, STR1024TYPE, STR255TYPE -->
                                                        <DataExtType >ENUMTYPE</DataExtType> <!-- required -->
                                                        <DataExtValue >STRTYPE</DataExtValue> <!-- required -->
                                                </DataExtRet>
                                        </SalesReceiptLineRet>
                                <!-- OR -->
                                        <SalesReceiptLineGroupRet> <!-- optional -->
                                                <TxnLineID >IDTYPE</TxnLineID> <!-- required -->
                                                <ItemGroupRef> <!-- required -->
                                                        <ListID >IDTYPE</ListID> <!-- optional -->
                                                        <FullName >STRTYPE</FullName> <!-- optional -->
                                                </ItemGroupRef>
                                                <Desc >STRTYPE</Desc> <!-- optional -->
                                                <Quantity >QUANTYPE</Quantity> <!-- optional -->
                                                <UnitOfMeasure >STRTYPE</UnitOfMeasure> <!-- optional -->
                                                <OverrideUOMSetRef> <!-- optional -->
                                                        <ListID >IDTYPE</ListID> <!-- optional -->
                                                        <FullName >STRTYPE</FullName> <!-- optional -->
                                                </OverrideUOMSetRef>
                                                <IsPrintItemsInGroup >BOOLTYPE</IsPrintItemsInGroup> <!-- required -->
                                                <TotalAmount >AMTTYPE</TotalAmount> <!-- required -->
                                                <SalesReceiptLineRet> <!-- optional, may repeat -->
                                                        <TxnLineID >IDTYPE</TxnLineID> <!-- required -->
                                                        <ItemRef> <!-- optional -->
                                                                <ListID >IDTYPE</ListID> <!-- optional -->
                                                                <FullName >STRTYPE</FullName> <!-- optional -->
                                                        </ItemRef>
                                                        <Desc >STRTYPE</Desc> <!-- optional -->
                                                        <Quantity >QUANTYPE</Quantity> <!-- optional -->
                                                        <UnitOfMeasure >STRTYPE</UnitOfMeasure> <!-- optional -->
                                                        <OverrideUOMSetRef> <!-- optional -->
                                                                <ListID >IDTYPE</ListID> <!-- optional -->
                                                                <FullName >STRTYPE</FullName> <!-- optional -->
                                                        </OverrideUOMSetRef>
                                                        <!-- BEGIN OR -->
                                                                <Rate >PRICETYPE</Rate> <!-- optional -->
                                                        <!-- OR -->
                                                                <RatePercent >PERCENTTYPE</RatePercent> <!-- optional -->
                                                        <!-- END OR -->
                                                        <ClassRef> <!-- optional -->
                                                                <ListID >IDTYPE</ListID> <!-- optional -->
                                                                <FullName >STRTYPE</FullName> <!-- optional -->
                                                        </ClassRef>
                                                        <Amount >AMTTYPE</Amount> <!-- optional -->
                                                        <InventorySiteRef> <!-- optional -->
                                                                <ListID >IDTYPE</ListID> <!-- optional -->
                                                                <FullName >STRTYPE</FullName> <!-- optional -->
                                                        </InventorySiteRef>
                                                        <InventorySiteLocationRef> <!-- optional -->
                                                                <ListID >IDTYPE</ListID> <!-- optional -->
                                                                <FullName >STRTYPE</FullName> <!-- optional -->
                                                        </InventorySiteLocationRef>
                                                        <!-- BEGIN OR -->
                                                                <SerialNumber >STRTYPE</SerialNumber> <!-- optional -->
                                                        <!-- OR -->
                                                                <LotNumber >STRTYPE</LotNumber> <!-- optional -->
                                                        <!-- END OR -->
                                                        <ExpirationDateForSerialLotNumber>STRTYPE</ExpirationDateForSerialLotNumber> <!-- optional -->
                                                        <ServiceDate >DATETYPE</ServiceDate> <!-- optional -->
                                                        <SalesTaxCodeRef> <!-- optional -->
                                                                <ListID >IDTYPE</ListID> <!-- optional -->
                                                                <FullName >STRTYPE</FullName> <!-- optional -->
                                                        </SalesTaxCodeRef>
                                                        <Other1 >STRTYPE</Other1> <!-- optional -->
                                                        <Other2 >STRTYPE</Other2> <!-- optional -->
                                                        <CreditCardTxnInfo> <!-- optional -->
                                                                <CreditCardTxnInputInfo> <!-- required -->
                                                                        <CreditCardNumber >STRTYPE</CreditCardNumber> <!-- required -->
                                                                        <ExpirationMonth >INTTYPE</ExpirationMonth> <!-- required -->
                                                                        <ExpirationYear >INTTYPE</ExpirationYear> <!-- required -->
                                                                        <NameOnCard >STRTYPE</NameOnCard> <!-- required -->
                                                                        <CreditCardAddress >STRTYPE</CreditCardAddress> <!-- optional -->
                                                                        <CreditCardPostalCode >STRTYPE</CreditCardPostalCode> <!-- optional -->
                                                                        <CommercialCardCode >STRTYPE</CommercialCardCode> <!-- optional -->
                                                                        <!-- TransactionMode may have one of the following values: CardNotPresent [DEFAULT], CardPresent -->
                                                                        <TransactionMode >ENUMTYPE</TransactionMode> <!-- optional -->
                                                                        <!-- CreditCardTxnType may have one of the following values: Authorization, Capture, Charge, Refund, VoiceAuthorization -->
                                                                        <CreditCardTxnType >ENUMTYPE</CreditCardTxnType> <!-- optional -->
                                                                </CreditCardTxnInputInfo>
                                                                <CreditCardTxnResultInfo> <!-- required -->
                                                                        <ResultCode >INTTYPE</ResultCode> <!-- required -->
                                                                        <ResultMessage >STRTYPE</ResultMessage> <!-- required -->
                                                                        <CreditCardTransID >STRTYPE</CreditCardTransID> <!-- required -->
                                                                        <MerchantAccountNumber >STRTYPE</MerchantAccountNumber> <!-- required -->
                                                                        <AuthorizationCode >STRTYPE</AuthorizationCode> <!-- optional -->
                                                                        <!-- AVSStreet may have one of the following values: Pass, Fail, NotAvailable -->
                                                                        <AVSStreet >ENUMTYPE</AVSStreet> <!-- optional -->
                                                                        <!-- AVSZip may have one of the following values: Pass, Fail, NotAvailable -->
                                                                        <AVSZip >ENUMTYPE</AVSZip> <!-- optional -->
                                                                        <!-- CardSecurityCodeMatch may have one of the following values: Pass, Fail, NotAvailable -->
                                                                        <CardSecurityCodeMatch >ENUMTYPE</CardSecurityCodeMatch> <!-- optional -->
                                                                        <ReconBatchID >STRTYPE</ReconBatchID> <!-- optional -->
                                                                        <PaymentGroupingCode >INTTYPE</PaymentGroupingCode> <!-- optional -->
                                                                        <!-- PaymentStatus may have one of the following values: Unknown, Completed -->
                                                                        <PaymentStatus >ENUMTYPE</PaymentStatus> <!-- required -->
                                                                        <TxnAuthorizationTime >DATETIMETYPE</TxnAuthorizationTime> <!-- required -->
                                                                        <TxnAuthorizationStamp >INTTYPE</TxnAuthorizationStamp> <!-- optional -->
                                                                        <ClientTransID >STRTYPE</ClientTransID> <!-- optional -->
                                                                </CreditCardTxnResultInfo>
                                                        </CreditCardTxnInfo>
                                                        <DataExtRet> <!-- optional, may repeat -->
                                                                <OwnerID >GUIDTYPE</OwnerID> <!-- optional -->
                                                                <DataExtName >STRTYPE</DataExtName> <!-- required -->
                                                                <!-- DataExtType may have one of the following values: AMTTYPE, DATETIMETYPE, INTTYPE, PERCENTTYPE, PRICETYPE, QUANTYPE, STR1024TYPE, STR255TYPE -->
                                                                <DataExtType >ENUMTYPE</DataExtType> <!-- required -->
                                                                <DataExtValue >STRTYPE</DataExtValue> <!-- required -->
                                                        </DataExtRet>
                                                </SalesReceiptLineRet>
                                                <DataExtRet> <!-- optional, may repeat -->
                                                        <OwnerID >GUIDTYPE</OwnerID> <!-- optional -->
                                                        <DataExtName >STRTYPE</DataExtName> <!-- required -->
                                                        <!-- DataExtType may have one of the following values: AMTTYPE, DATETIMETYPE, INTTYPE, PERCENTTYPE, PRICETYPE, QUANTYPE, STR1024TYPE, STR255TYPE -->
                                                        <DataExtType >ENUMTYPE</DataExtType> <!-- required -->
                                                        <DataExtValue >STRTYPE</DataExtValue> <!-- required -->
                                                </DataExtRet>
                                        </SalesReceiptLineGroupRet>
                                <!-- END OR -->
                                <DataExtRet> <!-- optional, may repeat -->
                                        <OwnerID >GUIDTYPE</OwnerID> <!-- optional -->
                                        <DataExtName >STRTYPE</DataExtName> <!-- required -->
                                        <!-- DataExtType may have one of the following values: AMTTYPE, DATETIMETYPE, INTTYPE, PERCENTTYPE, PRICETYPE, QUANTYPE, STR1024TYPE, STR255TYPE -->
                                        <DataExtType >ENUMTYPE</DataExtType> <!-- required -->
                                        <DataExtValue >STRTYPE</DataExtValue> <!-- required -->
                                </DataExtRet>
                        </SalesReceiptRet>
                </SalesReceiptQueryRs>
        </QBXMLMsgsRq>
</QBXML>
```
## SalesRepQuery
### XMLOps
```
<?xml version="1.0" encoding="utf-8"?>
<?qbxml version="16.0"?>
<QBXML>
        <QBXMLMsgsRq onError="stopOnError">
                <SalesReceiptQueryRq metaData="ENUMTYPE" iterator="ENUMTYPE" iteratorID="UUIDTYPE">
                        <!-- BEGIN OR -->
                                <TxnID >IDTYPE</TxnID> <!-- optional, may repeat -->
                        <!-- OR -->
                                <RefNumber >STRTYPE</RefNumber> <!-- optional, may repeat -->
                        <!-- OR -->
                                <RefNumberCaseSensitive >STRTYPE</RefNumberCaseSensitive> <!-- optional, may repeat -->
                        <!-- OR -->
                                <MaxReturned >INTTYPE</MaxReturned> <!-- optional -->
                                <!-- BEGIN OR -->
                                        <ModifiedDateRangeFilter> <!-- optional -->
                                                <FromModifiedDate >DATETIMETYPE</FromModifiedDate> <!-- optional -->
                                                <ToModifiedDate >DATETIMETYPE</ToModifiedDate> <!-- optional -->
                                        </ModifiedDateRangeFilter>
                                <!-- OR -->
                                        <TxnDateRangeFilter> <!-- optional -->
                                                <!-- BEGIN OR -->
                                                        <FromTxnDate >DATETYPE</FromTxnDate> <!-- optional -->
                                                        <ToTxnDate >DATETYPE</ToTxnDate> <!-- optional -->
                                                <!-- OR -->
                                                        <!-- DateMacro may have one of the following values: All, Today, ThisWeek, ThisWeekToDate, ThisMonth, ThisMonthToDate, ThisCalendarQuarter, ThisCalendarQuarterToDate, ThisFiscalQuarter, ThisFiscalQuarterToDate, ThisCalendarYear, ThisCalendarYearToDate, ThisFiscalYear, ThisFiscalYearToDate, Yesterday, LastWeek, LastWeekToDate, LastMonth, LastMonthToDate, LastCalendarQuarter, LastCalendarQuarterToDate, LastFiscalQuarter, LastFiscalQuarterToDate, LastCalendarYear, LastCalendarYearToDate, LastFiscalYear, LastFiscalYearToDate, NextWeek, NextFourWeeks, NextMonth, NextCalendarQuarter, NextCalendarYear, NextFiscalQuarter, NextFiscalYear -->
                                                        <DateMacro >ENUMTYPE</DateMacro> <!-- optional -->
                                                <!-- END OR -->
                                        </TxnDateRangeFilter>
                                <!-- END OR -->
                                <EntityFilter> <!-- optional -->
                                        <!-- BEGIN OR -->
                                                <ListID >IDTYPE</ListID> <!-- optional, may repeat -->
                                        <!-- OR -->
                                                <FullName >STRTYPE</FullName> <!-- optional, may repeat -->
                                        <!-- OR -->
                                                <ListIDWithChildren >IDTYPE</ListIDWithChildren> <!-- optional -->
                                        <!-- OR -->
                                                <FullNameWithChildren >STRTYPE</FullNameWithChildren> <!-- optional -->
                                        <!-- END OR -->
                                </EntityFilter>
                                <AccountFilter> <!-- optional -->
                                        <!-- BEGIN OR -->
                                                <ListID >IDTYPE</ListID> <!-- optional, may repeat -->
                                        <!-- OR -->
                                                <FullName >STRTYPE</FullName> <!-- optional, may repeat -->
                                        <!-- OR -->
                                                <ListIDWithChildren >IDTYPE</ListIDWithChildren> <!-- optional -->
                                        <!-- OR -->
                                                <FullNameWithChildren >STRTYPE</FullNameWithChildren> <!-- optional -->
                                        <!-- END OR -->
                                </AccountFilter>
                                <!-- BEGIN OR -->
                                        <RefNumberFilter> <!-- optional -->
                                                <!-- MatchCriterion may have one of the following values: StartsWith, Contains, EndsWith -->
                                                <MatchCriterion >ENUMTYPE</MatchCriterion> <!-- required -->
                                                <RefNumber >STRTYPE</RefNumber> <!-- required -->
                                        </RefNumberFilter>
                                <!-- OR -->
                                        <RefNumberRangeFilter> <!-- optional -->
                                                <FromRefNumber >STRTYPE</FromRefNumber> <!-- optional -->
                                                <ToRefNumber >STRTYPE</ToRefNumber> <!-- optional -->
                                        </RefNumberRangeFilter>
                                <!-- END OR -->
                                <CurrencyFilter> <!-- optional -->
                                        <!-- BEGIN OR -->
                                                <ListID >IDTYPE</ListID> <!-- optional, may repeat -->
                                        <!-- OR -->
                                                <FullName >STRTYPE</FullName> <!-- optional, may repeat -->
                                        <!-- END OR -->
                                </CurrencyFilter>
                        <!-- END OR -->
                        <IncludeLineItems >BOOLTYPE</IncludeLineItems> <!-- optional -->
                        <IncludeRetElement >STRTYPE</IncludeRetElement> <!-- optional, may repeat -->
                        <OwnerID >GUIDTYPE</OwnerID> <!-- optional, may repeat -->
                </SalesReceiptQueryRq>

                <SalesReceiptQueryRs statusCode="INTTYPE" statusSeverity="STRTYPE" statusMessage="STRTYPE" retCount="INTTYPE" iteratorRemainingCount="INTTYPE" iteratorID="UUIDTYPE">
                        <SalesReceiptRet> <!-- optional, may repeat -->
                                <TxnID >IDTYPE</TxnID> <!-- required -->
                                <TimeCreated >DATETIMETYPE</TimeCreated> <!-- required -->
                                <TimeModified >DATETIMETYPE</TimeModified> <!-- required -->
                                <EditSequence >STRTYPE</EditSequence> <!-- required -->
                                <TxnNumber >INTTYPE</TxnNumber> <!-- optional -->
                                <CustomerRef> <!-- optional -->
                                        <ListID >IDTYPE</ListID> <!-- optional -->
                                        <FullName >STRTYPE</FullName> <!-- optional -->
                                </CustomerRef>
                                <ClassRef> <!-- optional -->
                                        <ListID >IDTYPE</ListID> <!-- optional -->
                                        <FullName >STRTYPE</FullName> <!-- optional -->
                                </ClassRef>
                                <TemplateRef> <!-- optional -->
                                        <ListID >IDTYPE</ListID> <!-- optional -->
                                        <FullName >STRTYPE</FullName> <!-- optional -->
                                </TemplateRef>
                                <TxnDate >DATETYPE</TxnDate> <!-- required -->
                                <RefNumber >STRTYPE</RefNumber> <!-- optional -->
                                <BillAddress> <!-- optional -->
                                        <Addr1 >STRTYPE</Addr1> <!-- optional -->
                                        <Addr2 >STRTYPE</Addr2> <!-- optional -->
                                        <Addr3 >STRTYPE</Addr3> <!-- optional -->
                                        <Addr4 >STRTYPE</Addr4> <!-- optional -->
                                        <Addr5 >STRTYPE</Addr5> <!-- optional -->
                                        <City >STRTYPE</City> <!-- optional -->
                                        <State >STRTYPE</State> <!-- optional -->
                                        <PostalCode >STRTYPE</PostalCode> <!-- optional -->
                                        <Country >STRTYPE</Country> <!-- optional -->
                                        <Note >STRTYPE</Note> <!-- optional -->
                                </BillAddress>
                                <BillAddressBlock> <!-- optional -->
                                        <Addr1 >STRTYPE</Addr1> <!-- optional -->
                                        <Addr2 >STRTYPE</Addr2> <!-- optional -->
                                        <Addr3 >STRTYPE</Addr3> <!-- optional -->
                                        <Addr4 >STRTYPE</Addr4> <!-- optional -->
                                        <Addr5 >STRTYPE</Addr5> <!-- optional -->
                                </BillAddressBlock>
                                <ShipAddress> <!-- optional -->
                                        <Addr1 >STRTYPE</Addr1> <!-- optional -->
                                        <Addr2 >STRTYPE</Addr2> <!-- optional -->
                                        <Addr3 >STRTYPE</Addr3> <!-- optional -->
                                        <Addr4 >STRTYPE</Addr4> <!-- optional -->
                                        <Addr5 >STRTYPE</Addr5> <!-- optional -->
                                        <City >STRTYPE</City> <!-- optional -->
                                        <State >STRTYPE</State> <!-- optional -->
                                        <PostalCode >STRTYPE</PostalCode> <!-- optional -->
                                        <Country >STRTYPE</Country> <!-- optional -->
                                        <Note >STRTYPE</Note> <!-- optional -->
                                </ShipAddress>
                                <ShipAddressBlock> <!-- optional -->
                                        <Addr1 >STRTYPE</Addr1> <!-- optional -->
                                        <Addr2 >STRTYPE</Addr2> <!-- optional -->
                                        <Addr3 >STRTYPE</Addr3> <!-- optional -->
                                        <Addr4 >STRTYPE</Addr4> <!-- optional -->
                                        <Addr5 >STRTYPE</Addr5> <!-- optional -->
                                </ShipAddressBlock>
                                <IsPending >BOOLTYPE</IsPending> <!-- optional -->
                                <CheckNumber >STRTYPE</CheckNumber> <!-- optional -->
                                <PaymentMethodRef> <!-- optional -->
                                        <ListID >IDTYPE</ListID> <!-- optional -->
                                        <FullName >STRTYPE</FullName> <!-- optional -->
                                </PaymentMethodRef>
                                <DueDate >DATETYPE</DueDate> <!-- optional -->
                                <SalesRepRef> <!-- optional -->
                                        <ListID >IDTYPE</ListID> <!-- optional -->
                                        <FullName >STRTYPE</FullName> <!-- optional -->
                                </SalesRepRef>
                                <ShipDate >DATETYPE</ShipDate> <!-- optional -->
                                <ShipMethodRef> <!-- optional -->
                                        <ListID >IDTYPE</ListID> <!-- optional -->
                                        <FullName >STRTYPE</FullName> <!-- optional -->
                                </ShipMethodRef>
                                <FOB >STRTYPE</FOB> <!-- optional -->
                                <Subtotal >AMTTYPE</Subtotal> <!-- optional -->
                                <ItemSalesTaxRef> <!-- optional -->
                                        <ListID >IDTYPE</ListID> <!-- optional -->
                                        <FullName >STRTYPE</FullName> <!-- optional -->
                                </ItemSalesTaxRef>
                                <SalesTaxPercentage >PERCENTTYPE</SalesTaxPercentage> <!-- optional -->
                                <SalesTaxTotal >AMTTYPE</SalesTaxTotal> <!-- optional -->
                                <TotalAmount >AMTTYPE</TotalAmount> <!-- optional -->
                                <CurrencyRef> <!-- optional -->
                                        <ListID >IDTYPE</ListID> <!-- optional -->
                                        <FullName >STRTYPE</FullName> <!-- optional -->
                                </CurrencyRef>
                                <ExchangeRate >FLOATTYPE</ExchangeRate> <!-- optional -->
                                <TotalAmountInHomeCurrency >AMTTYPE</TotalAmountInHomeCurrency> <!-- optional -->
                                <Memo >STRTYPE</Memo> <!-- optional -->
                                <CustomerMsgRef> <!-- optional -->
                                        <ListID >IDTYPE</ListID> <!-- optional -->
                                        <FullName >STRTYPE</FullName> <!-- optional -->
                                </CustomerMsgRef>
                                <IsToBePrinted >BOOLTYPE</IsToBePrinted> <!-- optional -->
                                <IsToBeEmailed >BOOLTYPE</IsToBeEmailed> <!-- optional -->
                                <IsTaxIncluded >BOOLTYPE</IsTaxIncluded> <!-- optional -->
                                <CustomerSalesTaxCodeRef> <!-- optional -->
                                        <ListID >IDTYPE</ListID> <!-- optional -->
                                        <FullName >STRTYPE</FullName> <!-- optional -->
                                </CustomerSalesTaxCodeRef>
                                <DepositToAccountRef> <!-- optional -->
                                        <ListID >IDTYPE</ListID> <!-- optional -->
                                        <FullName >STRTYPE</FullName> <!-- optional -->
                                </DepositToAccountRef>
                                <CreditCardTxnInfo> <!-- optional -->
                                        <CreditCardTxnInputInfo> <!-- required -->
                                                <CreditCardNumber >STRTYPE</CreditCardNumber> <!-- required -->
                                                <ExpirationMonth >INTTYPE</ExpirationMonth> <!-- required -->
                                                <ExpirationYear >INTTYPE</ExpirationYear> <!-- required -->
                                                <NameOnCard >STRTYPE</NameOnCard> <!-- required -->
                                                <CreditCardAddress >STRTYPE</CreditCardAddress> <!-- optional -->
                                                <CreditCardPostalCode >STRTYPE</CreditCardPostalCode> <!-- optional -->
                                                <CommercialCardCode >STRTYPE</CommercialCardCode> <!-- optional -->
                                                <!-- TransactionMode may have one of the following values: CardNotPresent [DEFAULT], CardPresent -->
                                                <TransactionMode >ENUMTYPE</TransactionMode> <!-- optional -->
                                                <!-- CreditCardTxnType may have one of the following values: Authorization, Capture, Charge, Refund, VoiceAuthorization -->
                                                <CreditCardTxnType >ENUMTYPE</CreditCardTxnType> <!-- optional -->
                                        </CreditCardTxnInputInfo>
                                        <CreditCardTxnResultInfo> <!-- required -->
                                                <ResultCode >INTTYPE</ResultCode> <!-- required -->
                                                <ResultMessage >STRTYPE</ResultMessage> <!-- required -->
                                                <CreditCardTransID >STRTYPE</CreditCardTransID> <!-- required -->
                                                <MerchantAccountNumber >STRTYPE</MerchantAccountNumber> <!-- required -->
                                                <AuthorizationCode >STRTYPE</AuthorizationCode> <!-- optional -->
                                                <!-- AVSStreet may have one of the following values: Pass, Fail, NotAvailable -->
                                                <AVSStreet >ENUMTYPE</AVSStreet> <!-- optional -->
                                                <!-- AVSZip may have one of the following values: Pass, Fail, NotAvailable -->
                                                <AVSZip >ENUMTYPE</AVSZip> <!-- optional -->
                                                <!-- CardSecurityCodeMatch may have one of the following values: Pass, Fail, NotAvailable -->
                                                <CardSecurityCodeMatch >ENUMTYPE</CardSecurityCodeMatch> <!-- optional -->
                                                <ReconBatchID >STRTYPE</ReconBatchID> <!-- optional -->
                                                <PaymentGroupingCode >INTTYPE</PaymentGroupingCode> <!-- optional -->
                                                <!-- PaymentStatus may have one of the following values: Unknown, Completed -->
                                                <PaymentStatus >ENUMTYPE</PaymentStatus> <!-- required -->
                                                <TxnAuthorizationTime >DATETIMETYPE</TxnAuthorizationTime> <!-- required -->
                                                <TxnAuthorizationStamp >INTTYPE</TxnAuthorizationStamp> <!-- optional -->
                                                <ClientTransID >STRTYPE</ClientTransID> <!-- optional -->
                                        </CreditCardTxnResultInfo>
                                </CreditCardTxnInfo>
                                <Other >STRTYPE</Other> <!-- optional -->
                                <ExternalGUID >GUIDTYPE</ExternalGUID> <!-- optional -->
                                <!-- BEGIN OR -->
                                        <SalesReceiptLineRet> <!-- optional -->
                                                <TxnLineID >IDTYPE</TxnLineID> <!-- required -->
                                                <ItemRef> <!-- optional -->
                                                        <ListID >IDTYPE</ListID> <!-- optional -->
                                                        <FullName >STRTYPE</FullName> <!-- optional -->
                                                </ItemRef>
                                                <Desc >STRTYPE</Desc> <!-- optional -->
                                                <Quantity >QUANTYPE</Quantity> <!-- optional -->
                                                <UnitOfMeasure >STRTYPE</UnitOfMeasure> <!-- optional -->
                                                <OverrideUOMSetRef> <!-- optional -->
                                                        <ListID >IDTYPE</ListID> <!-- optional -->
                                                        <FullName >STRTYPE</FullName> <!-- optional -->
                                                </OverrideUOMSetRef>
                                                <!-- BEGIN OR -->
                                                        <Rate >PRICETYPE</Rate> <!-- optional -->
                                                <!-- OR -->
                                                        <RatePercent >PERCENTTYPE</RatePercent> <!-- optional -->
                                                <!-- END OR -->
                                                <ClassRef> <!-- optional -->
                                                        <ListID >IDTYPE</ListID> <!-- optional -->
                                                        <FullName >STRTYPE</FullName> <!-- optional -->
                                                </ClassRef>
                                                <Amount >AMTTYPE</Amount> <!-- optional -->
                                                <InventorySiteRef> <!-- optional -->
                                                        <ListID >IDTYPE</ListID> <!-- optional -->
                                                        <FullName >STRTYPE</FullName> <!-- optional -->
                                                </InventorySiteRef>
                                                <InventorySiteLocationRef> <!-- optional -->
                                                        <ListID >IDTYPE</ListID> <!-- optional -->
                                                        <FullName >STRTYPE</FullName> <!-- optional -->
                                                </InventorySiteLocationRef>
                                                <!-- BEGIN OR -->
                                                        <SerialNumber >STRTYPE</SerialNumber> <!-- optional -->
                                                <!-- OR -->
                                                        <LotNumber >STRTYPE</LotNumber> <!-- optional -->
                                                <!-- END OR -->
                                                <ExpirationDateForSerialLotNumber>STRTYPE</ExpirationDateForSerialLotNumber> <!-- optional -->
                                                <ServiceDate >DATETYPE</ServiceDate> <!-- optional -->
                                                <SalesTaxCodeRef> <!-- optional -->
                                                        <ListID >IDTYPE</ListID> <!-- optional -->
                                                        <FullName >STRTYPE</FullName> <!-- optional -->
                                                </SalesTaxCodeRef>
                                                <Other1 >STRTYPE</Other1> <!-- optional -->
                                                <Other2 >STRTYPE</Other2> <!-- optional -->
                                                <CreditCardTxnInfo> <!-- optional -->
                                                        <CreditCardTxnInputInfo> <!-- required -->
                                                                <CreditCardNumber >STRTYPE</CreditCardNumber> <!-- required -->
                                                                <ExpirationMonth >INTTYPE</ExpirationMonth> <!-- required -->
                                                                <ExpirationYear >INTTYPE</ExpirationYear> <!-- required -->
                                                                <NameOnCard >STRTYPE</NameOnCard> <!-- required -->
                                                                <CreditCardAddress >STRTYPE</CreditCardAddress> <!-- optional -->
                                                                <CreditCardPostalCode >STRTYPE</CreditCardPostalCode> <!-- optional -->
                                                                <CommercialCardCode >STRTYPE</CommercialCardCode> <!-- optional -->
                                                                <!-- TransactionMode may have one of the following values: CardNotPresent [DEFAULT], CardPresent -->
                                                                <TransactionMode >ENUMTYPE</TransactionMode> <!-- optional -->
                                                                <!-- CreditCardTxnType may have one of the following values: Authorization, Capture, Charge, Refund, VoiceAuthorization -->
                                                                <CreditCardTxnType >ENUMTYPE</CreditCardTxnType> <!-- optional -->
                                                        </CreditCardTxnInputInfo>
                                                        <CreditCardTxnResultInfo> <!-- required -->
                                                                <ResultCode >INTTYPE</ResultCode> <!-- required -->
                                                                <ResultMessage >STRTYPE</ResultMessage> <!-- required -->
                                                                <CreditCardTransID >STRTYPE</CreditCardTransID> <!-- required -->
                                                                <MerchantAccountNumber >STRTYPE</MerchantAccountNumber> <!-- required -->
                                                                <AuthorizationCode >STRTYPE</AuthorizationCode> <!-- optional -->
                                                                <!-- AVSStreet may have one of the following values: Pass, Fail, NotAvailable -->
                                                                <AVSStreet >ENUMTYPE</AVSStreet> <!-- optional -->
                                                                <!-- AVSZip may have one of the following values: Pass, Fail, NotAvailable -->
                                                                <AVSZip >ENUMTYPE</AVSZip> <!-- optional -->
                                                                <!-- CardSecurityCodeMatch may have one of the following values: Pass, Fail, NotAvailable -->
                                                                <CardSecurityCodeMatch >ENUMTYPE</CardSecurityCodeMatch> <!-- optional -->
                                                                <ReconBatchID >STRTYPE</ReconBatchID> <!-- optional -->
                                                                <PaymentGroupingCode >INTTYPE</PaymentGroupingCode> <!-- optional -->
                                                                <!-- PaymentStatus may have one of the following values: Unknown, Completed -->
                                                                <PaymentStatus >ENUMTYPE</PaymentStatus> <!-- required -->
                                                                <TxnAuthorizationTime >DATETIMETYPE</TxnAuthorizationTime> <!-- required -->
                                                                <TxnAuthorizationStamp >INTTYPE</TxnAuthorizationStamp> <!-- optional -->
                                                                <ClientTransID >STRTYPE</ClientTransID> <!-- optional -->
                                                        </CreditCardTxnResultInfo>
                                                </CreditCardTxnInfo>
                                                <DataExtRet> <!-- optional, may repeat -->
                                                        <OwnerID >GUIDTYPE</OwnerID> <!-- optional -->
                                                        <DataExtName >STRTYPE</DataExtName> <!-- required -->
                                                        <!-- DataExtType may have one of the following values: AMTTYPE, DATETIMETYPE, INTTYPE, PERCENTTYPE, PRICETYPE, QUANTYPE, STR1024TYPE, STR255TYPE -->
                                                        <DataExtType >ENUMTYPE</DataExtType> <!-- required -->
                                                        <DataExtValue >STRTYPE</DataExtValue> <!-- required -->
                                                </DataExtRet>
                                        </SalesReceiptLineRet>
                                <!-- OR -->
                                        <SalesReceiptLineGroupRet> <!-- optional -->
                                                <TxnLineID >IDTYPE</TxnLineID> <!-- required -->
                                                <ItemGroupRef> <!-- required -->
                                                        <ListID >IDTYPE</ListID> <!-- optional -->
                                                        <FullName >STRTYPE</FullName> <!-- optional -->
                                                </ItemGroupRef>
                                                <Desc >STRTYPE</Desc> <!-- optional -->
                                                <Quantity >QUANTYPE</Quantity> <!-- optional -->
                                                <UnitOfMeasure >STRTYPE</UnitOfMeasure> <!-- optional -->
                                                <OverrideUOMSetRef> <!-- optional -->
                                                        <ListID >IDTYPE</ListID> <!-- optional -->
                                                        <FullName >STRTYPE</FullName> <!-- optional -->
                                                </OverrideUOMSetRef>
                                                <IsPrintItemsInGroup >BOOLTYPE</IsPrintItemsInGroup> <!-- required -->
                                                <TotalAmount >AMTTYPE</TotalAmount> <!-- required -->
                                                <SalesReceiptLineRet> <!-- optional, may repeat -->
                                                        <TxnLineID >IDTYPE</TxnLineID> <!-- required -->
                                                        <ItemRef> <!-- optional -->
                                                                <ListID >IDTYPE</ListID> <!-- optional -->
                                                                <FullName >STRTYPE</FullName> <!-- optional -->
                                                        </ItemRef>
                                                        <Desc >STRTYPE</Desc> <!-- optional -->
                                                        <Quantity >QUANTYPE</Quantity> <!-- optional -->
                                                        <UnitOfMeasure >STRTYPE</UnitOfMeasure> <!-- optional -->
                                                        <OverrideUOMSetRef> <!-- optional -->
                                                                <ListID >IDTYPE</ListID> <!-- optional -->
                                                                <FullName >STRTYPE</FullName> <!-- optional -->
                                                        </OverrideUOMSetRef>
                                                        <!-- BEGIN OR -->
                                                                <Rate >PRICETYPE</Rate> <!-- optional -->
                                                        <!-- OR -->
                                                                <RatePercent >PERCENTTYPE</RatePercent> <!-- optional -->
                                                        <!-- END OR -->
                                                        <ClassRef> <!-- optional -->
                                                                <ListID >IDTYPE</ListID> <!-- optional -->
                                                                <FullName >STRTYPE</FullName> <!-- optional -->
                                                        </ClassRef>
                                                        <Amount >AMTTYPE</Amount> <!-- optional -->
                                                        <InventorySiteRef> <!-- optional -->
                                                                <ListID >IDTYPE</ListID> <!-- optional -->
                                                                <FullName >STRTYPE</FullName> <!-- optional -->
                                                        </InventorySiteRef>
                                                        <InventorySiteLocationRef> <!-- optional -->
                                                                <ListID >IDTYPE</ListID> <!-- optional -->
                                                                <FullName >STRTYPE</FullName> <!-- optional -->
                                                        </InventorySiteLocationRef>
                                                        <!-- BEGIN OR -->
                                                                <SerialNumber >STRTYPE</SerialNumber> <!-- optional -->
                                                        <!-- OR -->
                                                                <LotNumber >STRTYPE</LotNumber> <!-- optional -->
                                                        <!-- END OR -->
                                                        <ExpirationDateForSerialLotNumber>STRTYPE</ExpirationDateForSerialLotNumber> <!-- optional -->
                                                        <ServiceDate >DATETYPE</ServiceDate> <!-- optional -->
                                                        <SalesTaxCodeRef> <!-- optional -->
                                                                <ListID >IDTYPE</ListID> <!-- optional -->
                                                                <FullName >STRTYPE</FullName> <!-- optional -->
                                                        </SalesTaxCodeRef>
                                                        <Other1 >STRTYPE</Other1> <!-- optional -->
                                                        <Other2 >STRTYPE</Other2> <!-- optional -->
                                                        <CreditCardTxnInfo> <!-- optional -->
                                                                <CreditCardTxnInputInfo> <!-- required -->
                                                                        <CreditCardNumber >STRTYPE</CreditCardNumber> <!-- required -->
                                                                        <ExpirationMonth >INTTYPE</ExpirationMonth> <!-- required -->
                                                                        <ExpirationYear >INTTYPE</ExpirationYear> <!-- required -->
                                                                        <NameOnCard >STRTYPE</NameOnCard> <!-- required -->
                                                                        <CreditCardAddress >STRTYPE</CreditCardAddress> <!-- optional -->
                                                                        <CreditCardPostalCode >STRTYPE</CreditCardPostalCode> <!-- optional -->
                                                                        <CommercialCardCode >STRTYPE</CommercialCardCode> <!-- optional -->
                                                                        <!-- TransactionMode may have one of the following values: CardNotPresent [DEFAULT], CardPresent -->
                                                                        <TransactionMode >ENUMTYPE</TransactionMode> <!-- optional -->
                                                                        <!-- CreditCardTxnType may have one of the following values: Authorization, Capture, Charge, Refund, VoiceAuthorization -->
                                                                        <CreditCardTxnType >ENUMTYPE</CreditCardTxnType> <!-- optional -->
                                                                </CreditCardTxnInputInfo>
                                                                <CreditCardTxnResultInfo> <!-- required -->
                                                                        <ResultCode >INTTYPE</ResultCode> <!-- required -->
                                                                        <ResultMessage >STRTYPE</ResultMessage> <!-- required -->
                                                                        <CreditCardTransID >STRTYPE</CreditCardTransID> <!-- required -->
                                                                        <MerchantAccountNumber >STRTYPE</MerchantAccountNumber> <!-- required -->
                                                                        <AuthorizationCode >STRTYPE</AuthorizationCode> <!-- optional -->
                                                                        <!-- AVSStreet may have one of the following values: Pass, Fail, NotAvailable -->
                                                                        <AVSStreet >ENUMTYPE</AVSStreet> <!-- optional -->
                                                                        <!-- AVSZip may have one of the following values: Pass, Fail, NotAvailable -->
                                                                        <AVSZip >ENUMTYPE</AVSZip> <!-- optional -->
                                                                        <!-- CardSecurityCodeMatch may have one of the following values: Pass, Fail, NotAvailable -->
                                                                        <CardSecurityCodeMatch >ENUMTYPE</CardSecurityCodeMatch> <!-- optional -->
                                                                        <ReconBatchID >STRTYPE</ReconBatchID> <!-- optional -->
                                                                        <PaymentGroupingCode >INTTYPE</PaymentGroupingCode> <!-- optional -->
                                                                        <!-- PaymentStatus may have one of the following values: Unknown, Completed -->
                                                                        <PaymentStatus >ENUMTYPE</PaymentStatus> <!-- required -->
                                                                        <TxnAuthorizationTime >DATETIMETYPE</TxnAuthorizationTime> <!-- required -->
                                                                        <TxnAuthorizationStamp >INTTYPE</TxnAuthorizationStamp> <!-- optional -->
                                                                        <ClientTransID >STRTYPE</ClientTransID> <!-- optional -->
                                                                </CreditCardTxnResultInfo>
                                                        </CreditCardTxnInfo>
                                                        <DataExtRet> <!-- optional, may repeat -->
                                                                <OwnerID >GUIDTYPE</OwnerID> <!-- optional -->
                                                                <DataExtName >STRTYPE</DataExtName> <!-- required -->
                                                                <!-- DataExtType may have one of the following values: AMTTYPE, DATETIMETYPE, INTTYPE, PERCENTTYPE, PRICETYPE, QUANTYPE, STR1024TYPE, STR255TYPE -->
                                                                <DataExtType >ENUMTYPE</DataExtType> <!-- required -->
                                                                <DataExtValue >STRTYPE</DataExtValue> <!-- required -->
                                                        </DataExtRet>
                                                </SalesReceiptLineRet>
                                                <DataExtRet> <!-- optional, may repeat -->
                                                        <OwnerID >GUIDTYPE</OwnerID> <!-- optional -->
                                                        <DataExtName >STRTYPE</DataExtName> <!-- required -->
                                                        <!-- DataExtType may have one of the following values: AMTTYPE, DATETIMETYPE, INTTYPE, PERCENTTYPE, PRICETYPE, QUANTYPE, STR1024TYPE, STR255TYPE -->
                                                        <DataExtType >ENUMTYPE</DataExtType> <!-- required -->
                                                        <DataExtValue >STRTYPE</DataExtValue> <!-- required -->
                                                </DataExtRet>
                                        </SalesReceiptLineGroupRet>
                                <!-- END OR -->
                                <DataExtRet> <!-- optional, may repeat -->
                                        <OwnerID >GUIDTYPE</OwnerID> <!-- optional -->
                                        <DataExtName >STRTYPE</DataExtName> <!-- required -->
                                        <!-- DataExtType may have one of the following values: AMTTYPE, DATETIMETYPE, INTTYPE, PERCENTTYPE, PRICETYPE, QUANTYPE, STR1024TYPE, STR255TYPE -->
                                        <DataExtType >ENUMTYPE</DataExtType> <!-- required -->
                                        <DataExtValue >STRTYPE</DataExtValue> <!-- required -->
                                </DataExtRet>
                        </SalesReceiptRet>
                </SalesReceiptQueryRs>
        </QBXMLMsgsRq>
</QBXML>
```
## SalesRepQuery
### XMLOps
```
<?xml version="1.0" encoding="utf-8"?>
<?qbxml version="16.0"?>
<QBXML>
        <QBXMLMsgsRq onError="stopOnError">
                <SalesRepQueryRq metaData="ENUMTYPE">
                        <!-- BEGIN OR -->
                                <ListID >IDTYPE</ListID> <!-- optional, may repeat -->
                        <!-- OR -->
                                <FullName >STRTYPE</FullName> <!-- optional, may repeat -->
                        <!-- OR -->
                                <MaxReturned >INTTYPE</MaxReturned> <!-- optional -->
                                <!-- ActiveStatus may have one of the following values: ActiveOnly [DEFAULT], InactiveOnly, All -->
                                <ActiveStatus >ENUMTYPE</ActiveStatus> <!-- optional -->
                                <FromModifiedDate >DATETIMETYPE</FromModifiedDate> <!-- optional -->
                                <ToModifiedDate >DATETIMETYPE</ToModifiedDate> <!-- optional -->
                                <!-- BEGIN OR -->
                                        <NameFilter> <!-- optional -->
                                                <!-- MatchCriterion may have one of the following values: StartsWith, Contains, EndsWith -->
                                                <MatchCriterion >ENUMTYPE</MatchCriterion> <!-- required -->
                                                <Name >STRTYPE</Name> <!-- required -->
                                        </NameFilter>
                                <!-- OR -->
                                        <NameRangeFilter> <!-- optional -->
                                                <FromName >STRTYPE</FromName> <!-- optional -->
                                                <ToName >STRTYPE</ToName> <!-- optional -->
                                        </NameRangeFilter>
                                <!-- END OR -->
                        <!-- END OR -->
                        <IncludeRetElement >STRTYPE</IncludeRetElement> <!-- optional, may repeat -->
                </SalesRepQueryRq>

                <SalesRepQueryRs statusCode="INTTYPE" statusSeverity="STRTYPE" statusMessage="STRTYPE" retCount="INTTYPE">
                        <SalesRepRet> <!-- optional, may repeat -->
                                <ListID >IDTYPE</ListID> <!-- required -->
                                <TimeCreated >DATETIMETYPE</TimeCreated> <!-- required -->
                                <TimeModified >DATETIMETYPE</TimeModified> <!-- required -->
                                <EditSequence >STRTYPE</EditSequence> <!-- required -->
                                <Initial >STRTYPE</Initial> <!-- required -->
                                <IsActive >BOOLTYPE</IsActive> <!-- optional -->
                                <SalesRepEntityRef> <!-- required -->
                                        <ListID >IDTYPE</ListID> <!-- optional -->
                                        <FullName >STRTYPE</FullName> <!-- optional -->
                                </SalesRepEntityRef>
                        </SalesRepRet>
                </SalesRepQueryRs>
        </QBXMLMsgsRq>
</QBXML>

```
## SalesTaxCodeQuery
### XMLOps
```
<?xml version="1.0" encoding="utf-8"?>
<?qbxml version="16.0"?>
<QBXML>
        <QBXMLMsgsRq onError="stopOnError">
                <SalesTaxCodeQueryRq metaData="ENUMTYPE">
                        <!-- BEGIN OR -->
                                <ListID >IDTYPE</ListID> <!-- optional, may repeat -->
                        <!-- OR -->
                                <FullName >STRTYPE</FullName> <!-- optional, may repeat -->
                        <!-- OR -->
                                <MaxReturned >INTTYPE</MaxReturned> <!-- optional -->
                                <!-- ActiveStatus may have one of the following values: ActiveOnly [DEFAULT], InactiveOnly, All -->
                                <ActiveStatus >ENUMTYPE</ActiveStatus> <!-- optional -->
                                <FromModifiedDate >DATETIMETYPE</FromModifiedDate> <!-- optional -->
                                <ToModifiedDate >DATETIMETYPE</ToModifiedDate> <!-- optional -->
                                <!-- BEGIN OR -->
                                        <NameFilter> <!-- optional -->
                                                <!-- MatchCriterion may have one of the following values: StartsWith, Contains, EndsWith -->
                                                <MatchCriterion >ENUMTYPE</MatchCriterion> <!-- required -->
                                                <Name >STRTYPE</Name> <!-- required -->
                                        </NameFilter>
                                <!-- OR -->
                                        <NameRangeFilter> <!-- optional -->
                                                <FromName >STRTYPE</FromName> <!-- optional -->
                                                <ToName >STRTYPE</ToName> <!-- optional -->
                                        </NameRangeFilter>
                                <!-- END OR -->
                        <!-- END OR -->
                        <IncludeRetElement >STRTYPE</IncludeRetElement> <!-- optional, may repeat -->
                </SalesTaxCodeQueryRq>

                <SalesTaxCodeQueryRs statusCode="INTTYPE" statusSeverity="STRTYPE" statusMessage="STRTYPE" retCount="INTTYPE">
                        <SalesTaxCodeRet> <!-- optional, may repeat -->
                                <ListID >IDTYPE</ListID> <!-- required -->
                                <TimeCreated >DATETIMETYPE</TimeCreated> <!-- required -->
                                <TimeModified >DATETIMETYPE</TimeModified> <!-- required -->
                                <EditSequence >STRTYPE</EditSequence> <!-- required -->
                                <Name >STRTYPE</Name> <!-- required -->
                                <IsActive >BOOLTYPE</IsActive> <!-- optional -->
                                <IsTaxable >BOOLTYPE</IsTaxable> <!-- required -->
                                <Desc >STRTYPE</Desc> <!-- optional -->
                                <ItemPurchaseTaxRef> <!-- optional -->
                                        <ListID >IDTYPE</ListID> <!-- optional -->
                                        <FullName >STRTYPE</FullName> <!-- optional -->
                                </ItemPurchaseTaxRef>
                                <ItemSalesTaxRef> <!-- optional -->
                                        <ListID >IDTYPE</ListID> <!-- optional -->
                                        <FullName >STRTYPE</FullName> <!-- optional -->
                                </ItemSalesTaxRef>
                        </SalesTaxCodeRet>
                </SalesTaxCodeQueryRs>
        </QBXMLMsgsRq>
</QBXML>
```
## SalesTaxPayableQuery
### XMLOps
```
<?xml version="1.0" encoding="utf-8"?>
<?qbxml version="16.0"?>
<QBXML>
        <QBXMLMsgsRq onError="stopOnError">
                <SalesTaxPayableQueryRq metaData="ENUMTYPE">
                        <AsOfDate >DATETYPE</AsOfDate> <!-- optional -->
                        <IncludeRetElement >STRTYPE</IncludeRetElement> <!-- optional, may repeat -->
                </SalesTaxPayableQueryRq>

                <SalesTaxPayableQueryRs statusCode="INTTYPE" statusSeverity="STRTYPE" statusMessage="STRTYPE" retCount="INTTYPE">
                        <SalesTaxPayableRet> <!-- optional, may repeat -->
                                <PayeeEntityRef> <!-- optional -->
                                        <ListID >IDTYPE</ListID> <!-- optional -->
                                        <FullName >STRTYPE</FullName> <!-- optional -->
                                </PayeeEntityRef>
                                <Amount >AMTTYPE</Amount> <!-- optional -->
                                <SalesTaxPayableLineRet> <!-- optional, may repeat -->
                                        <ItemSalesTaxRef> <!-- optional -->
                                                <ListID >IDTYPE</ListID> <!-- optional -->
                                                <FullName >STRTYPE</FullName> <!-- optional -->
                                        </ItemSalesTaxRef>
                                        <Amount >AMTTYPE</Amount> <!-- required -->
                                </SalesTaxPayableLineRet>
                        </SalesTaxPayableRet>
                </SalesTaxPayableQueryRs>
        </QBXMLMsgsRq>
</QBXML>
```
## SalesTaxPaymentCheckQuery
Queries for payments that have been made for sales tax owed (for example, to a state sales tax authority).
### XMLOps
```
<?xml version="1.0" encoding="utf-8"?>
<?qbxml version="16.0"?>
<QBXML>
        <QBXMLMsgsRq onError="stopOnError">
                <SalesTaxPaymentCheckQueryRq metaData="ENUMTYPE" iterator="ENUMTYPE" iteratorID="UUIDTYPE">
                        <!-- BEGIN OR -->
                                <TxnID >IDTYPE</TxnID> <!-- optional, may repeat -->
                        <!-- OR -->
                                <RefNumber >STRTYPE</RefNumber> <!-- optional, may repeat -->
                        <!-- OR -->
                                <RefNumberCaseSensitive >STRTYPE</RefNumberCaseSensitive> <!-- optional, may repeat -->
                        <!-- OR -->
                                <MaxReturned >INTTYPE</MaxReturned> <!-- optional -->
                                <!-- BEGIN OR -->
                                        <ModifiedDateRangeFilter> <!-- optional -->
                                                <FromModifiedDate >DATETIMETYPE</FromModifiedDate> <!-- optional -->
                                                <ToModifiedDate >DATETIMETYPE</ToModifiedDate> <!-- optional -->
                                        </ModifiedDateRangeFilter>
                                <!-- OR -->
                                        <TxnDateRangeFilter> <!-- optional -->
                                                <!-- BEGIN OR -->
                                                        <FromTxnDate >DATETYPE</FromTxnDate> <!-- optional -->
                                                        <ToTxnDate >DATETYPE</ToTxnDate> <!-- optional -->
                                                <!-- OR -->
                                                        <!-- DateMacro may have one of the following values: All, Today, ThisWeek, ThisWeekToDate, ThisMonth, ThisMonthToDate, ThisCalendarQuarter, ThisCalendarQuarterToDate, ThisFiscalQuarter, ThisFiscalQuarterToDate, ThisCalendarYear, ThisCalendarYearToDate, ThisFiscalYear, ThisFiscalYearToDate, Yesterday, LastWeek, LastWeekToDate, LastMonth, LastMonthToDate, LastCalendarQuarter, LastCalendarQuarterToDate, LastFiscalQuarter, LastFiscalQuarterToDate, LastCalendarYear, LastCalendarYearToDate, LastFiscalYear, LastFiscalYearToDate, NextWeek, NextFourWeeks, NextMonth, NextCalendarQuarter, NextCalendarYear, NextFiscalQuarter, NextFiscalYear -->
                                                        <DateMacro >ENUMTYPE</DateMacro> <!-- optional -->
                                                <!-- END OR -->
                                        </TxnDateRangeFilter>
                                <!-- END OR -->
                                <EntityFilter> <!-- optional -->
                                        <!-- BEGIN OR -->
                                                <ListID >IDTYPE</ListID> <!-- optional, may repeat -->
                                        <!-- OR -->
                                                <FullName >STRTYPE</FullName> <!-- optional, may repeat -->
                                        <!-- OR -->
                                                <ListIDWithChildren >IDTYPE</ListIDWithChildren> <!-- optional -->
                                        <!-- OR -->
                                                <FullNameWithChildren >STRTYPE</FullNameWithChildren> <!-- optional -->
                                        <!-- END OR -->
                                </EntityFilter>
                                <AccountFilter> <!-- optional -->
                                        <!-- BEGIN OR -->
                                                <ListID >IDTYPE</ListID> <!-- optional, may repeat -->
                                        <!-- OR -->
                                                <FullName >STRTYPE</FullName> <!-- optional, may repeat -->
                                        <!-- OR -->
                                                <ListIDWithChildren >IDTYPE</ListIDWithChildren> <!-- optional -->
                                        <!-- OR -->
                                                <FullNameWithChildren >STRTYPE</FullNameWithChildren> <!-- optional -->
                                        <!-- END OR -->
                                </AccountFilter>
                                <ItemFilter> <!-- optional -->
                                        <!-- BEGIN OR -->
                                                <ListID >IDTYPE</ListID> <!-- optional, may repeat -->
                                        <!-- OR -->
                                                <FullName >STRTYPE</FullName> <!-- optional, may repeat -->
                                        <!-- OR -->
                                                <ListIDWithChildren >IDTYPE</ListIDWithChildren> <!-- optional -->
                                        <!-- OR -->
                                                <FullNameWithChildren >STRTYPE</FullNameWithChildren> <!-- optional -->
                                        <!-- END OR -->
                                </ItemFilter>
                                <!-- BEGIN OR -->
                                        <RefNumberFilter> <!-- optional -->
                                                <!-- MatchCriterion may have one of the following values: StartsWith, Contains, EndsWith -->
                                                <MatchCriterion >ENUMTYPE</MatchCriterion> <!-- required -->
                                                <RefNumber >STRTYPE</RefNumber> <!-- required -->
                                        </RefNumberFilter>
                                <!-- OR -->
                                        <RefNumberRangeFilter> <!-- optional -->
                                                <FromRefNumber >STRTYPE</FromRefNumber> <!-- optional -->
                                                <ToRefNumber >STRTYPE</ToRefNumber> <!-- optional -->
                                        </RefNumberRangeFilter>
                                <!-- END OR -->
                        <!-- END OR -->
                        <IncludeLineItems >BOOLTYPE</IncludeLineItems> <!-- optional -->
                        <IncludeRetElement >STRTYPE</IncludeRetElement> <!-- optional, may repeat -->
                        <OwnerID >GUIDTYPE</OwnerID> <!-- optional, may repeat -->
                </SalesTaxPaymentCheckQueryRq>

                <SalesTaxPaymentCheckQueryRs statusCode="INTTYPE" statusSeverity="STRTYPE" statusMessage="STRTYPE" retCount="INTTYPE" iteratorRemainingCount="INTTYPE" iteratorID="UUIDTYPE">
                        <SalesTaxPaymentCheckRet> <!-- optional, may repeat -->
                                <TxnID >IDTYPE</TxnID> <!-- required -->
                                <TimeCreated >DATETIMETYPE</TimeCreated> <!-- required -->
                                <TimeModified >DATETIMETYPE</TimeModified> <!-- required -->
                                <EditSequence >STRTYPE</EditSequence> <!-- required -->
                                <TxnNumber >INTTYPE</TxnNumber> <!-- optional -->
                                <PayeeEntityRef> <!-- optional -->
                                        <ListID >IDTYPE</ListID> <!-- optional -->
                                        <FullName >STRTYPE</FullName> <!-- optional -->
                                </PayeeEntityRef>
                                <TxnDate >DATETYPE</TxnDate> <!-- required -->
                                <BankAccountRef> <!-- required -->
                                        <ListID >IDTYPE</ListID> <!-- optional -->
                                        <FullName >STRTYPE</FullName> <!-- optional -->
                                </BankAccountRef>
                                <Amount >AMTTYPE</Amount> <!-- required -->
                                <RefNumber >STRTYPE</RefNumber> <!-- optional -->
                                <Memo >STRTYPE</Memo> <!-- optional -->
                                <Address> <!-- optional -->
                                        <Addr1 >STRTYPE</Addr1> <!-- optional -->
                                        <Addr2 >STRTYPE</Addr2> <!-- optional -->
                                        <Addr3 >STRTYPE</Addr3> <!-- optional -->
                                        <Addr4 >STRTYPE</Addr4> <!-- optional -->
                                        <Addr5 >STRTYPE</Addr5> <!-- optional -->
                                        <City >STRTYPE</City> <!-- optional -->
                                        <State >STRTYPE</State> <!-- optional -->
                                        <PostalCode >STRTYPE</PostalCode> <!-- optional -->
                                        <Country >STRTYPE</Country> <!-- optional -->
                                        <Note >STRTYPE</Note> <!-- optional -->
                                </Address>
                                <AddressBlock> <!-- optional -->
                                        <Addr1 >STRTYPE</Addr1> <!-- optional -->
                                        <Addr2 >STRTYPE</Addr2> <!-- optional -->
                                        <Addr3 >STRTYPE</Addr3> <!-- optional -->
                                        <Addr4 >STRTYPE</Addr4> <!-- optional -->
                                        <Addr5 >STRTYPE</Addr5> <!-- optional -->
                                </AddressBlock>
                                <IsToBePrinted >BOOLTYPE</IsToBePrinted> <!-- optional -->
                                <ExternalGUID >GUIDTYPE</ExternalGUID> <!-- optional -->
                                <SalesTaxPaymentCheckLineRet> <!-- optional, may repeat -->
                                        <TxnLineID >IDTYPE</TxnLineID> <!-- required -->
                                        <ItemSalesTaxRef> <!-- optional -->
                                                <ListID >IDTYPE</ListID> <!-- optional -->
                                                <FullName >STRTYPE</FullName> <!-- optional -->
                                        </ItemSalesTaxRef>
                                        <Amount >AMTTYPE</Amount> <!-- optional -->
                                </SalesTaxPaymentCheckLineRet>
                                <DataExtRet> <!-- optional, may repeat -->
                                        <OwnerID >GUIDTYPE</OwnerID> <!-- optional -->
                                        <DataExtName >STRTYPE</DataExtName> <!-- required -->
                                        <!-- DataExtType may have one of the following values: AMTTYPE, DATETIMETYPE, INTTYPE, PERCENTTYPE, PRICETYPE, QUANTYPE, STR1024TYPE, STR255TYPE -->
                                        <DataExtType >ENUMTYPE</DataExtType> <!-- required -->
                                        <DataExtValue >STRTYPE</DataExtValue> <!-- required -->
                                </DataExtRet>
                        </SalesTaxPaymentCheckRet>
                </SalesTaxPaymentCheckQueryRs>
        </QBXMLMsgsRq>
</QBXML>
```
## SalesTaxReturnQuery
### XMLOps
```
<?xml version="1.0" encoding="utf-8"?>
<?qbxml version="16.0"?>
<QBXML>
        <QBXMLMsgsRq onError="stopOnError">
                <SalesTaxReturnQueryRq metaData="ENUMTYPE">
                </SalesTaxReturnQueryRq>

                <SalesTaxReturnQueryRs statusCode="INTTYPE" statusSeverity="STRTYPE" statusMessage="STRTYPE" retCount="INTTYPE">
                        <SalesTaxReturnRet> <!-- optional, may repeat -->
                                <ListID >IDTYPE</ListID> <!-- required -->
                                <FullName >STRTYPE</FullName> <!-- optional -->
                                <Desc >STRTYPE</Desc> <!-- optional -->
                        </SalesTaxReturnRet>
                </SalesTaxReturnQueryRs>
        </QBXMLMsgsRq>
</QBXML>
```
## ShipMethodQuery
### XMLOps
```
<?xml version="1.0" encoding="utf-8"?>
<?qbxml version="16.0"?>
<QBXML>
        <QBXMLMsgsRq onError="stopOnError">
                <ShipMethodQueryRq metaData="ENUMTYPE">
                        <!-- BEGIN OR -->
                                <ListID >IDTYPE</ListID> <!-- optional, may repeat -->
                        <!-- OR -->
                                <FullName >STRTYPE</FullName> <!-- optional, may repeat -->
                        <!-- OR -->
                                <MaxReturned >INTTYPE</MaxReturned> <!-- optional -->
                                <!-- ActiveStatus may have one of the following values: ActiveOnly [DEFAULT], InactiveOnly, All -->
                                <ActiveStatus >ENUMTYPE</ActiveStatus> <!-- optional -->
                                <FromModifiedDate >DATETIMETYPE</FromModifiedDate> <!-- optional -->
                                <ToModifiedDate >DATETIMETYPE</ToModifiedDate> <!-- optional -->
                                <!-- BEGIN OR -->
                                        <NameFilter> <!-- optional -->
                                                <!-- MatchCriterion may have one of the following values: StartsWith, Contains, EndsWith -->
                                                <MatchCriterion >ENUMTYPE</MatchCriterion> <!-- required -->
                                                <Name >STRTYPE</Name> <!-- required -->
                                        </NameFilter>
                                <!-- OR -->
                                        <NameRangeFilter> <!-- optional -->
                                                <FromName >STRTYPE</FromName> <!-- optional -->
                                                <ToName >STRTYPE</ToName> <!-- optional -->
                                        </NameRangeFilter>
                                <!-- END OR -->
                        <!-- END OR -->
                        <IncludeRetElement >STRTYPE</IncludeRetElement> <!-- optional, may repeat -->
                </ShipMethodQueryRq>

                <ShipMethodQueryRs statusCode="INTTYPE" statusSeverity="STRTYPE" statusMessage="STRTYPE" retCount="INTTYPE">
                        <ShipMethodRet> <!-- optional, may repeat -->
                                <ListID >IDTYPE</ListID> <!-- required -->
                                <TimeCreated >DATETIMETYPE</TimeCreated> <!-- required -->
                                <TimeModified >DATETIMETYPE</TimeModified> <!-- required -->
                                <EditSequence >STRTYPE</EditSequence> <!-- required -->
                                <Name >STRTYPE</Name> <!-- required -->
                                <IsActive >BOOLTYPE</IsActive> <!-- optional -->
                        </ShipMethodRet>
                </ShipMethodQueryRs>
        </QBXMLMsgsRq>
</QBXML>
```
## StandardTermsQuery
### XMLOps
```
<?xml version="1.0" encoding="utf-8"?>
<?qbxml version="16.0"?>
<QBXML>
        <QBXMLMsgsRq onError="stopOnError">
                <StandardTermsQueryRq metaData="ENUMTYPE">
                        <!-- BEGIN OR -->
                                <ListID >IDTYPE</ListID> <!-- optional, may repeat -->
                        <!-- OR -->
                                <FullName >STRTYPE</FullName> <!-- optional, may repeat -->
                        <!-- OR -->
                                <MaxReturned >INTTYPE</MaxReturned> <!-- optional -->
                                <!-- ActiveStatus may have one of the following values: ActiveOnly [DEFAULT], InactiveOnly, All -->
                                <ActiveStatus >ENUMTYPE</ActiveStatus> <!-- optional -->
                                <FromModifiedDate >DATETIMETYPE</FromModifiedDate> <!-- optional -->
                                <ToModifiedDate >DATETIMETYPE</ToModifiedDate> <!-- optional -->
                                <!-- BEGIN OR -->
                                        <NameFilter> <!-- optional -->
                                                <!-- MatchCriterion may have one of the following values: StartsWith, Contains, EndsWith -->
                                                <MatchCriterion >ENUMTYPE</MatchCriterion> <!-- required -->
                                                <Name >STRTYPE</Name> <!-- required -->
                                        </NameFilter>
                                <!-- OR -->
                                        <NameRangeFilter> <!-- optional -->
                                                <FromName >STRTYPE</FromName> <!-- optional -->
                                                <ToName >STRTYPE</ToName> <!-- optional -->
                                        </NameRangeFilter>
                                <!-- END OR -->
                        <!-- END OR -->
                        <IncludeRetElement >STRTYPE</IncludeRetElement> <!-- optional, may repeat -->
                </StandardTermsQueryRq>

                <StandardTermsQueryRs statusCode="INTTYPE" statusSeverity="STRTYPE" statusMessage="STRTYPE" retCount="INTTYPE">
                        <StandardTermsRet> <!-- optional, may repeat -->
                                <ListID >IDTYPE</ListID> <!-- required -->
                                <TimeCreated >DATETIMETYPE</TimeCreated> <!-- required -->
                                <TimeModified >DATETIMETYPE</TimeModified> <!-- required -->
                                <EditSequence >STRTYPE</EditSequence> <!-- required -->
                                <Name >STRTYPE</Name> <!-- required -->
                                <IsActive >BOOLTYPE</IsActive> <!-- optional -->
                                <StdDueDays >INTTYPE</StdDueDays> <!-- optional -->
                                <StdDiscountDays >INTTYPE</StdDiscountDays> <!-- optional -->
                                <DiscountPct >PERCENTTYPE</DiscountPct> <!-- optional -->
                        </StandardTermsRet>
                </StandardTermsQueryRs>
        </QBXMLMsgsRq>
</QBXML>
```
## TemplateQuery
### XMLOps
```
<?xml version="1.0" encoding="utf-8"?>
<?qbxml version="16.0"?>
<QBXML>
        <QBXMLMsgsRq onError="stopOnError">
                <TemplateQueryRq metaData="ENUMTYPE">
                        <IncludeRetElement >STRTYPE</IncludeRetElement> <!-- optional, may repeat -->
                </TemplateQueryRq>

                <TemplateQueryRs statusCode="INTTYPE" statusSeverity="STRTYPE" statusMessage="STRTYPE" retCount="INTTYPE">
                        <TemplateRet> <!-- optional, may repeat -->
                                <ListID >IDTYPE</ListID> <!-- required -->
                                <TimeCreated >DATETIMETYPE</TimeCreated> <!-- required -->
                                <TimeModified >DATETIMETYPE</TimeModified> <!-- required -->
                                <EditSequence >STRTYPE</EditSequence> <!-- required -->
                                <Name >STRTYPE</Name> <!-- required -->
                                <IsActive >BOOLTYPE</IsActive> <!-- optional -->
                                <!-- TemplateType may have one of the following values: BuildAssembly, CreditMemo, Estimate, Invoice, PurchaseOrder, SalesOrder, SalesReceipt, receipt payment, bill payment -->
                                <TemplateType >ENUMTYPE</TemplateType> <!-- required -->
                        </TemplateRet>
                </TemplateQueryRs>
        </QBXMLMsgsRq>
</QBXML>
```
## TermsQuery
### XMLOps
```
<?xml version="1.0" encoding="utf-8"?>
<?qbxml version="16.0"?>
<QBXML>
        <QBXMLMsgsRq onError="stopOnError">
                <TermsQueryRq metaData="ENUMTYPE">
                        <!-- BEGIN OR -->
                                <ListID >IDTYPE</ListID> <!-- optional, may repeat -->
                        <!-- OR -->
                                <FullName >STRTYPE</FullName> <!-- optional, may repeat -->
                        <!-- OR -->
                                <MaxReturned >INTTYPE</MaxReturned> <!-- optional -->
                                <!-- ActiveStatus may have one of the following values: ActiveOnly [DEFAULT], InactiveOnly, All -->
                                <ActiveStatus >ENUMTYPE</ActiveStatus> <!-- optional -->
                                <FromModifiedDate >DATETIMETYPE</FromModifiedDate> <!-- optional -->
                                <ToModifiedDate >DATETIMETYPE</ToModifiedDate> <!-- optional -->
                                <!-- BEGIN OR -->
                                        <NameFilter> <!-- optional -->
                                                <!-- MatchCriterion may have one of the following values: StartsWith, Contains, EndsWith -->
                                                <MatchCriterion >ENUMTYPE</MatchCriterion> <!-- required -->
                                                <Name >STRTYPE</Name> <!-- required -->
                                        </NameFilter>
                                <!-- OR -->
                                        <NameRangeFilter> <!-- optional -->
                                                <FromName >STRTYPE</FromName> <!-- optional -->
                                                <ToName >STRTYPE</ToName> <!-- optional -->
                                        </NameRangeFilter>
                                <!-- END OR -->
                        <!-- END OR -->
                        <IncludeRetElement >STRTYPE</IncludeRetElement> <!-- optional, may repeat -->
                </TermsQueryRq>

                <TermsQueryRs statusCode="INTTYPE" statusSeverity="STRTYPE" statusMessage="STRTYPE" retCount="INTTYPE">
                        <!-- BEGIN OR -->
                                <StandardTermsRet> <!-- optional -->
                                        <ListID >IDTYPE</ListID> <!-- required -->
                                        <TimeCreated >DATETIMETYPE</TimeCreated> <!-- required -->
                                        <TimeModified >DATETIMETYPE</TimeModified> <!-- required -->
                                        <EditSequence >STRTYPE</EditSequence> <!-- required -->
                                        <Name >STRTYPE</Name> <!-- required -->
                                        <IsActive >BOOLTYPE</IsActive> <!-- optional -->
                                        <StdDueDays >INTTYPE</StdDueDays> <!-- optional -->
                                        <StdDiscountDays >INTTYPE</StdDiscountDays> <!-- optional -->
                                        <DiscountPct >PERCENTTYPE</DiscountPct> <!-- optional -->
                                </StandardTermsRet>
                        <!-- OR -->
                                <DateDrivenTermsRet> <!-- optional -->
                                        <ListID >IDTYPE</ListID> <!-- required -->
                                        <TimeCreated >DATETIMETYPE</TimeCreated> <!-- required -->
                                        <TimeModified >DATETIMETYPE</TimeModified> <!-- required -->
                                        <EditSequence >STRTYPE</EditSequence> <!-- required -->
                                        <Name >STRTYPE</Name> <!-- required -->
                                        <IsActive >BOOLTYPE</IsActive> <!-- optional -->
                                        <DayOfMonthDue >INTTYPE</DayOfMonthDue> <!-- required -->
                                        <DueNextMonthDays >INTTYPE</DueNextMonthDays> <!-- optional -->
                                        <DiscountDayOfMonth >INTTYPE</DiscountDayOfMonth> <!-- optional -->
                                        <DiscountPct >PERCENTTYPE</DiscountPct> <!-- optional -->
                                </DateDrivenTermsRet>
                        <!-- END OR -->
                </TermsQueryRs>
        </QBXMLMsgsRq>
</QBXML>
```
## TimeReportQuery
The Time Reports category includes summary and detail reports related by time. Summarized columns can be customized in these reports.
### XMLOps
```
<?xml version="1.0" encoding="utf-8"?>
<?qbxml version="16.0"?>
<QBXML>
        <QBXMLMsgsRq onError="stopOnError">
                <TimeReportQueryRq>
                        <!-- TimeReportType may have one of the following values: TimeByItem, TimeByJobDetail, TimeByJobSummary, TimeByName -->
                        <TimeReportType >ENUMTYPE</TimeReportType> <!-- required -->
                        <DisplayReport >BOOLTYPE</DisplayReport> <!-- optional -->
                        <!-- BEGIN OR -->
                                <ReportPeriod> <!-- optional -->
                                        <FromReportDate >DATETYPE</FromReportDate> <!-- optional -->
                                        <ToReportDate >DATETYPE</ToReportDate> <!-- optional -->
                                </ReportPeriod>
                        <!-- OR -->
                                <!-- ReportDateMacro may have one of the following values: All, Today, ThisWeek, ThisWeekToDate, ThisMonth, ThisMonthToDate, ThisQuarter, ThisQuarterToDate, ThisYear, ThisYearToDate, Yesterday, LastWeek, LastWeekToDate, LastMonth, LastMonthToDate, LastQuarter, LastQuarterToDate, LastYear, LastYearToDate, NextWeek, NextFourWeeks, NextMonth, NextQuarter, NextYear -->
                                <ReportDateMacro >ENUMTYPE</ReportDateMacro> <!-- optional -->
                        <!-- END OR -->
                        <ReportEntityFilter> <!-- optional -->
                                <!-- BEGIN OR -->
                                        <!-- EntityTypeFilter may have one of the following values: Customer, Employee, OtherName, Vendor -->
                                        <EntityTypeFilter >ENUMTYPE</EntityTypeFilter> <!-- optional -->
                                <!-- OR -->
                                        <ListID >IDTYPE</ListID> <!-- optional, may repeat -->
                                <!-- OR -->
                                        <FullName >STRTYPE</FullName> <!-- optional, may repeat -->
                                <!-- OR -->
                                        <ListIDWithChildren >IDTYPE</ListIDWithChildren> <!-- optional -->
                                <!-- OR -->
                                        <FullNameWithChildren >STRTYPE</FullNameWithChildren> <!-- optional -->
                                <!-- END OR -->
                        </ReportEntityFilter>
                        <ReportItemFilter> <!-- optional -->
                                <!-- BEGIN OR -->
                                        <!-- ItemTypeFilter may have one of the following values: AllExceptFixedAsset, Assembly, Discount, FixedAsset, Inventory, InventoryAndAssembly, NonInventory, OtherCharge, Payment, Sales, SalesTax, Service -->
                                        <ItemTypeFilter >ENUMTYPE</ItemTypeFilter> <!-- optional -->
                                <!-- OR -->
                                        <ListID >IDTYPE</ListID> <!-- optional, may repeat -->
                                <!-- OR -->
                                        <FullName >STRTYPE</FullName> <!-- optional, may repeat -->
                                <!-- OR -->
                                        <ListIDWithChildren >IDTYPE</ListIDWithChildren> <!-- optional -->
                                <!-- OR -->
                                        <FullNameWithChildren >STRTYPE</FullNameWithChildren> <!-- optional -->
                                <!-- END OR -->
                        </ReportItemFilter>
                        <ReportClassFilter> <!-- optional -->
                                <!-- BEGIN OR -->
                                        <ListID >IDTYPE</ListID> <!-- optional, may repeat -->
                                <!-- OR -->
                                        <FullName >STRTYPE</FullName> <!-- optional, may repeat -->
                                <!-- OR -->
                                        <ListIDWithChildren >IDTYPE</ListIDWithChildren> <!-- optional -->
                                <!-- OR -->
                                        <FullNameWithChildren >STRTYPE</FullNameWithChildren> <!-- optional -->
                                <!-- END OR -->
                        </ReportClassFilter>
                        <!-- SummarizeColumnsBy may have one of the following values: Account, BalanceSheet, Class, Customer, CustomerType, Day, Employee, FourWeek, HalfMonth, IncomeStatement, ItemDetail, ItemType, Month, Payee, PaymentMethod, PayrollItemDetail, PayrollYtdDetail, Quarter, SalesRep, SalesTaxCode, ShipMethod, Terms, TotalOnly, TwoWeek, Vendor, VendorType, Week, Year -->
                        <SummarizeColumnsBy >ENUMTYPE</SummarizeColumnsBy> <!-- optional -->
                        <!-- IncludeColumn may have one of the following values: Account, Aging, Amount, AmountDifference, AverageCost, BilledDate, BillingStatus, CalculatedAmount, Class, ClearedStatus, CostPrice, Credit, Currency, Date, Debit, DeliveryDate, DueDate, EstimateActive, ExchangeRate, FOB, IncomeSubjectToTax, Invoiced, Item, ItemDesc, LastModifiedBy, LatestOrPriorState, Memo, ModifiedTime, Name, NameAccountNumber, NameAddress, NameCity, NameContact, NameEmail, NameFax, NamePhone, NameState, NameZip, OpenBalance, OriginalAmount, PaidAmount, PaidStatus, PaidThroughDate, PaymentMethod, PayrollItem, PONumber, PrintStatus, ProgressAmount, ProgressPercent, Quantity, QuantityAvailable, QuantityOnHand, QuantityOnSalesOrder, ReceivedQuantity, RefNumber, RunningBalance, SalesRep, SalesTaxCode, SerialOrLotNumber, ShipDate, ShipMethod, SourceName, SplitAccount, SSNOrTaxID, TaxLine, TaxTableVersion, Terms, TxnID, TxnNumber, TxnType, UnitPrice, UserEdit, ValueOnHand, WageBase, WageBaseTips -->
                        <IncludeColumn >ENUMTYPE</IncludeColumn> <!-- optional, may repeat -->
                        <IncludeSubcolumns >BOOLTYPE</IncludeSubcolumns> <!-- optional -->
                        <!-- ReportCalendar may have one of the following values: CalendarYear, FiscalYear, TaxYear -->
                        <ReportCalendar >ENUMTYPE</ReportCalendar> <!-- optional -->
                        <!-- ReturnRows may have one of the following values: ActiveOnly, NonZero, All -->
                        <ReturnRows >ENUMTYPE</ReturnRows> <!-- optional -->
                        <!-- ReturnColumns may have one of the following values: ActiveOnly, NonZero, All -->
                        <ReturnColumns >ENUMTYPE</ReturnColumns> <!-- optional -->
                </TimeReportQueryRq>

                <TimeReportQueryRs statusCode="INTTYPE" statusSeverity="STRTYPE" statusMessage="STRTYPE">
                        <ReportRet> <!-- optional -->
                                <ReportTitle >STRTYPE</ReportTitle> <!-- required -->
                                <ReportSubtitle >STRTYPE</ReportSubtitle> <!-- required -->
                                <!-- ReportBasis may have one of the following values: Accrual, Cash, None [DEFAULT] -->
                                <ReportBasis >ENUMTYPE</ReportBasis> <!-- optional -->
                                <NumRows >INTTYPE</NumRows> <!-- required -->
                                <NumColumns >INTTYPE</NumColumns> <!-- required -->
                                <NumColTitleRows >INTTYPE</NumColTitleRows> <!-- required -->
                                <ColDesc colID="INTTYPE" dataType="ENUMTYPE"> <!-- required, may repeat -->
                                        <ColTitle titleRow="INTTYPE" value="STRTYPE"> <!-- required, may repeat -->
                                        </ColTitle>
                                        <!-- ColType may have one of the following values: Account, Addr1, Addr2, Addr3, Addr4, Addr5, Aging, Amount, AmountDifference, AverageCost, BilledDate, BillingStatus, Blank, CalculatedAmount, Class, ClearedStatus, CostPrice, CreateDate, Credit, CustomField, Date, Debit, DeliveryDate, DueDate, Duration, EarliestReceiptDate, EstimateActive, FOB, IncomeSubjectToTax, Invoiced, IsAdjustment, Item, ItemDesc, ItemVendor, Label, LastModifiedBy, LatestOrPriorState, Memo, ModifiedTime, Name, NameAccountNumber, NameAddress, NameCity, NameContact, NameEmail, NameFax, NamePhone, NameState, NameZip, OpenBalance, OriginalAmount, PaidAmount, PaidStatus, PaidThroughDate, PaymentMethod, PayrollItem, Percent, PercentChange, PercentOfTotalRetail, PercentOfTotalValue, PhysicalCount, PONumber, PrintStatus, ProgressAmount, ProgressPercent, Quantity, QuantityAvailable, QuantityOnHand, QuantityOnOrder, QuantityOnPendingBuild, QuantityOnSalesOrder, ReceivedQuantity, RefNumber, ReorderPoint, RetailValueOnHand, RunningBalance, SalesPerWeek, SalesRep, SalesTaxCode, ShipDate, ShipMethod, ShipToAddr1, ShipToAddr2, ShipToAddr3, ShipToAddr4, ShipToAddr5, SONumber, SourceName, SplitAccount, SSNOrTaxID, SuggestedReorder, TaxLine, TaxTableVersion, Terms, Total, TxnID, TxnNumber, TxnType, UnitPrice, UserEdit, ValueOnHand, WageBase, WageBaseTips -->
                                        <ColType >ENUMTYPE</ColType> <!-- required -->
                                </ColDesc>
                                <ReportData> <!-- optional -->
                                        <!-- BEGIN OR -->
                                                <DataRow> <!-- optional -->
                                                        <RowData rowType="ENUMTYPE" value="STRTYPE"> <!-- optional -->
                                                        </RowData>
                                                        <ColData colID="INTTYPE" value="STRTYPE" dataType="ENUMTYPE"> <!-- optional, may repeat -->
                                                        </ColData>
                                                </DataRow>
                                        <!-- OR -->
                                                <TextRow rowNumber="INTTYPE" value="STRTYPE"> <!-- optional -->
                                                </TextRow>
                                        <!-- OR -->
                                                <SubtotalRow> <!-- optional -->
                                                        <RowData rowType="ENUMTYPE" value="STRTYPE"> <!-- optional -->
                                                        </RowData>
                                                        <ColData colID="INTTYPE" value="STRTYPE" dataType="ENUMTYPE"> <!-- optional, may repeat -->
                                                        </ColData>
                                                </SubtotalRow>
                                        <!-- OR -->
                                                <TotalRow> <!-- optional -->
                                                        <RowData rowType="ENUMTYPE" value="STRTYPE"> <!-- optional -->
                                                        </RowData>
                                                        <ColData colID="INTTYPE" value="STRTYPE" dataType="ENUMTYPE"> <!-- optional, may repeat -->
                                                        </ColData>
                                                </TotalRow>
                                        <!-- END OR -->
                                </ReportData>
                        </ReportRet>
                </TimeReportQueryRs>
        </QBXMLMsgsRq>
</QBXML>
```
## TimeTrackingQuery
The time-tracking transactions that are returned in this query include time tracking information that was entered into QuickBooks manually or gathered using the QuickBooks “Timer” or “Stopwatch.” Note that the QuickBooks Timer application can run on its own without QuickBooks, but the QuickBooks SDK cannot access the Timer data directly. The Timer data must be imported into QuickBooks before it is accessible via the SDK.)
### XMLOps
```
<?xml version="1.0" encoding="utf-8"?>
<?qbxml version="16.0"?>
<QBXML>
        <QBXMLMsgsRq onError="stopOnError">
                <TimeTrackingQueryRq metaData="ENUMTYPE" iterator="ENUMTYPE" iteratorID="UUIDTYPE">
                        <!-- BEGIN OR -->
                                <TxnID >IDTYPE</TxnID> <!-- optional, may repeat -->
                        <!-- OR -->
                                <MaxReturned >INTTYPE</MaxReturned> <!-- optional -->
                                <!-- BEGIN OR -->
                                        <ModifiedDateRangeFilter> <!-- optional -->
                                                <FromModifiedDate >DATETIMETYPE</FromModifiedDate> <!-- optional -->
                                                <ToModifiedDate >DATETIMETYPE</ToModifiedDate> <!-- optional -->
                                        </ModifiedDateRangeFilter>
                                <!-- OR -->
                                        <TxnDateRangeFilter> <!-- optional -->
                                                <!-- BEGIN OR -->
                                                        <FromTxnDate >DATETYPE</FromTxnDate> <!-- optional -->
                                                        <ToTxnDate >DATETYPE</ToTxnDate> <!-- optional -->
                                                <!-- OR -->
                                                        <!-- DateMacro may have one of the following values: All, Today, ThisWeek, ThisWeekToDate, ThisMonth, ThisMonthToDate, ThisCalendarQuarter, ThisCalendarQuarterToDate, ThisFiscalQuarter, ThisFiscalQuarterToDate, ThisCalendarYear, ThisCalendarYearToDate, ThisFiscalYear, ThisFiscalYearToDate, Yesterday, LastWeek, LastWeekToDate, LastMonth, LastMonthToDate, LastCalendarQuarter, LastCalendarQuarterToDate, LastFiscalQuarter, LastFiscalQuarterToDate, LastCalendarYear, LastCalendarYearToDate, LastFiscalYear, LastFiscalYearToDate, NextWeek, NextFourWeeks, NextMonth, NextCalendarQuarter, NextCalendarYear, NextFiscalQuarter, NextFiscalYear -->
                                                        <DateMacro >ENUMTYPE</DateMacro> <!-- optional -->
                                                <!-- END OR -->
                                        </TxnDateRangeFilter>
                                <!-- END OR -->
                                <TimeTrackingEntityFilter> <!-- optional -->
                                        <!-- BEGIN OR -->
                                                <ListID >IDTYPE</ListID> <!-- optional, may repeat -->
                                        <!-- OR -->
                                                <FullName >STRTYPE</FullName> <!-- optional, may repeat -->
                                        <!-- END OR -->
                                </TimeTrackingEntityFilter>
                        <!-- END OR -->
                        <IncludeRetElement >STRTYPE</IncludeRetElement> <!-- optional, may repeat -->
                </TimeTrackingQueryRq>

                <TimeTrackingQueryRs statusCode="INTTYPE" statusSeverity="STRTYPE" statusMessage="STRTYPE" retCount="INTTYPE" iteratorRemainingCount="INTTYPE" iteratorID="UUIDTYPE">
                        <TimeTrackingRet> <!-- optional, may repeat -->
                                <TxnID >IDTYPE</TxnID> <!-- required -->
                                <TimeCreated >DATETIMETYPE</TimeCreated> <!-- required -->
                                <TimeModified >DATETIMETYPE</TimeModified> <!-- required -->
                                <EditSequence >STRTYPE</EditSequence> <!-- required -->
                                <TxnNumber >INTTYPE</TxnNumber> <!-- optional -->
                                <TxnDate >DATETYPE</TxnDate> <!-- required -->
                                <EntityRef> <!-- required -->
                                        <ListID >IDTYPE</ListID> <!-- optional -->
                                        <FullName >STRTYPE</FullName> <!-- optional -->
                                </EntityRef>
                                <CustomerRef> <!-- optional -->
                                        <ListID >IDTYPE</ListID> <!-- optional -->
                                        <FullName >STRTYPE</FullName> <!-- optional -->
                                </CustomerRef>
                                <ItemServiceRef> <!-- optional -->
                                        <ListID >IDTYPE</ListID> <!-- optional -->
                                        <FullName >STRTYPE</FullName> <!-- optional -->
                                </ItemServiceRef>
                                <Duration >TIMEINTERVALTYPE</Duration> <!-- required -->
                                <ClassRef> <!-- optional -->
                                        <ListID >IDTYPE</ListID> <!-- optional -->
                                        <FullName >STRTYPE</FullName> <!-- optional -->
                                </ClassRef>
                                <PayrollItemWageRef> <!-- optional -->
                                        <ListID >IDTYPE</ListID> <!-- optional -->
                                        <FullName >STRTYPE</FullName> <!-- optional -->
                                </PayrollItemWageRef>
                                <Notes >STRTYPE</Notes> <!-- optional -->
                                <!-- BillableStatus may have one of the following values: Billable, NotBillable, HasBeenBilled -->
                                <BillableStatus >ENUMTYPE</BillableStatus> <!-- optional -->
                                <ExternalGUID >GUIDTYPE</ExternalGUID> <!-- optional -->
                                <IsBillable >BOOLTYPE</IsBillable> <!-- optional -->
                                <IsBilled >BOOLTYPE</IsBilled> <!-- optional -->
                        </TimeTrackingRet>
                </TimeTrackingQueryRs>
        </QBXMLMsgsRq>
</QBXML>
```
## ToDoQuery
A “to do”list is used in QuickBooks to keep track of tasks. Notice that the various Name filters refer to the Notes field in the ToDoQuery. So, by using these filters, you are searching the Notes.
### XMLOps
```
<?xml version="1.0" encoding="utf-8"?>
<?qbxml version="16.0"?>
<QBXML>
        <QBXMLMsgsRq onError="stopOnError">
                <ToDoQueryRq metaData="ENUMTYPE">
                        <!-- BEGIN OR -->
                                <ListID >IDTYPE</ListID> <!-- optional, may repeat -->
                        <!-- OR -->
                                <MaxReturned >INTTYPE</MaxReturned> <!-- optional -->
                                <!-- ActiveStatus may have one of the following values: ActiveOnly [DEFAULT], InactiveOnly, All -->
                                <ActiveStatus >ENUMTYPE</ActiveStatus> <!-- optional -->
                                <FromModifiedDate >DATETIMETYPE</FromModifiedDate> <!-- optional -->
                                <ToModifiedDate >DATETIMETYPE</ToModifiedDate> <!-- optional -->
                                <!-- BEGIN OR -->
                                        <NameFilter> <!-- optional -->
                                                <!-- MatchCriterion may have one of the following values: StartsWith, Contains, EndsWith -->
                                                <MatchCriterion >ENUMTYPE</MatchCriterion> <!-- required -->
                                                <Name >STRTYPE</Name> <!-- required -->
                                        </NameFilter>
                                <!-- OR -->
                                        <NameRangeFilter> <!-- optional -->
                                                <FromName >STRTYPE</FromName> <!-- optional -->
                                                <ToName >STRTYPE</ToName> <!-- optional -->
                                        </NameRangeFilter>
                                <!-- END OR -->
                                <!-- DoneStatus may have one of the following values: NotDoneOnly [DEFAULT], DoneOnly, All -->
                                <DoneStatus >ENUMTYPE</DoneStatus> <!-- optional -->
                        <!-- END OR -->
                        <IncludeRetElement >STRTYPE</IncludeRetElement> <!-- optional, may repeat -->
                </ToDoQueryRq>

                <ToDoQueryRs statusCode="INTTYPE" statusSeverity="STRTYPE" statusMessage="STRTYPE" retCount="INTTYPE">
                        <ToDoRet> <!-- optional, may repeat -->
                                <ListID >IDTYPE</ListID> <!-- required -->
                                <TimeCreated >DATETIMETYPE</TimeCreated> <!-- required -->
                                <TimeModified >DATETIMETYPE</TimeModified> <!-- required -->
                                <EditSequence >STRTYPE</EditSequence> <!-- required -->
                                <Notes >STRTYPE</Notes> <!-- required -->
                                <IsActive >BOOLTYPE</IsActive> <!-- optional -->
                                <!-- Type may have one of the following values: Task [DEFAULT], Call, Fax, Email, Meeting, Appointment -->
                                <Type >ENUMTYPE</Type> <!-- optional -->
                                <!-- Priority may have one of the following values: Low [DEFAULT], Medium, High -->
                                <Priority >ENUMTYPE</Priority> <!-- optional -->
                                <!-- BEGIN OR -->
                                        <CustomerRef> <!-- optional -->
                                                <ListID >IDTYPE</ListID> <!-- optional -->
                                                <FullName >STRTYPE</FullName> <!-- optional -->
                                        </CustomerRef>
                                <!-- OR -->
                                        <EmployeeRef> <!-- optional -->
                                                <ListID >IDTYPE</ListID> <!-- optional -->
                                                <FullName >STRTYPE</FullName> <!-- optional -->
                                        </EmployeeRef>
                                <!-- OR -->
                                        <LeadRef> <!-- optional -->
                                                <ListID >IDTYPE</ListID> <!-- optional -->
                                                <FullName >STRTYPE</FullName> <!-- optional -->
                                        </LeadRef>
                                <!-- OR -->
                                        <VendorRef> <!-- optional -->
                                                <ListID >IDTYPE</ListID> <!-- optional -->
                                                <FullName >STRTYPE</FullName> <!-- optional -->
                                        </VendorRef>
                                <!-- END OR -->
                                <IsDone >BOOLTYPE</IsDone> <!-- required -->
                                <ReminderDate >DATETYPE</ReminderDate> <!-- required -->
                                <ReminderTime >TIMEINTERVALTYPE</ReminderTime> <!-- optional -->
                        </ToDoRet>
                </ToDoQueryRs>
        </QBXMLMsgsRq>
</QBXML>
```
## TransactionQuery
TransactionQuery is a generic transaction query that provides functionality (e.g. filters) similar to the Advanced Find window in the QuickBooks UI. It allows you to search for transactions across different transaction types. In contrast to the other transaction-specific queries, the TransactionQuery only returns data common to all transactions, such as TxnID, type, dates, accountRef, and so on. This query does return condensed transactions.
Accordingly, if additional and more transaction-specific data is required, a subsequent call to the desired query can be used to get that transaction-specific data. For example, the TransactionQuery can be used to present all transactions in a certain date range, then the user can select a particular transaction, say an invoice transaction. In response to this choice, you could do an InvoiceQuery to pull up all of the invoice data, similar to QuickZoom in the QuickBooks UI.
Important
You should be aware that permissions are obeyed in this query. So, if you set the transaction type filter to “All” (or if you don’t set it at all), the query will be searching only those transaction types that are permissible types for the user currently logged in. Accordingly, if instead of “all,” you specify a transaction type that the currently logged in user is not permitted to access, you will get a runtime error, even if other permissible transaction types were specified as well.
Finally, the transaction query is subject to sensitive data access level restrictions and payroll subscription status.
### XMLOps
```
<?xml version="1.0" encoding="utf-8"?>
<?qbxml version="16.0"?>
<QBXML>
        <QBXMLMsgsRq onError="stopOnError">
                <TransactionQueryRq metaData="ENUMTYPE" iterator="ENUMTYPE" iteratorID="UUIDTYPE">
                        <!-- BEGIN OR -->
                                <TxnID >IDTYPE</TxnID> <!-- optional, may repeat -->
                        <!-- OR -->
                                <MaxReturned >INTTYPE</MaxReturned> <!-- optional -->
                                <!-- BEGIN OR -->
                                        <RefNumber >STRTYPE</RefNumber> <!-- optional, may repeat -->
                                <!-- OR -->
                                        <RefNumberCaseSensitive >STRTYPE</RefNumberCaseSensitive> <!-- optional, may repeat -->
                                <!-- OR -->
                                        <RefNumberFilter> <!-- optional -->
                                                <!-- MatchCriterion may have one of the following values: StartsWith, Contains, EndsWith -->
                                                <MatchCriterion >ENUMTYPE</MatchCriterion> <!-- required -->
                                                <RefNumber >STRTYPE</RefNumber> <!-- required -->
                                        </RefNumberFilter>
                                <!-- OR -->
                                        <RefNumberRangeFilter> <!-- optional -->
                                                <FromRefNumber >STRTYPE</FromRefNumber> <!-- optional -->
                                                <ToRefNumber >STRTYPE</ToRefNumber> <!-- optional -->
                                        </RefNumberRangeFilter>
                                <!-- END OR -->
                                <TransactionModifiedDateRangeFilter> <!-- optional -->
                                        <!-- BEGIN OR -->
                                                <FromModifiedDate >DATETIMETYPE</FromModifiedDate> <!-- optional -->
                                                <ToModifiedDate >DATETIMETYPE</ToModifiedDate> <!-- optional -->
                                        <!-- OR -->
                                                <!-- DateMacro may have one of the following values: All, Today, ThisWeek, ThisWeekToDate, ThisMonth, ThisMonthToDate, ThisCalendarQuarter, ThisCalendarQuarterToDate, ThisFiscalQuarter, ThisFiscalQuarterToDate, ThisCalendarYear, ThisCalendarYearToDate, ThisFiscalYear, ThisFiscalYearToDate, Yesterday, LastWeek, LastWeekToDate, LastMonth, LastMonthToDate, LastCalendarQuarter, LastCalendarQuarterToDate, LastFiscalQuarter, LastFiscalQuarterToDate, LastCalendarYear, LastCalendarYearToDate, LastFiscalYear, LastFiscalYearToDate, NextWeek, NextFourWeeks, NextMonth, NextCalendarQuarter, NextCalendarYear, NextFiscalQuarter, NextFiscalYear -->
                                                <DateMacro >ENUMTYPE</DateMacro> <!-- optional -->
                                        <!-- END OR -->
                                </TransactionModifiedDateRangeFilter>
                                <TransactionDateRangeFilter> <!-- optional -->
                                        <!-- BEGIN OR -->
                                                <FromTxnDate >DATETYPE</FromTxnDate> <!-- optional -->
                                                <ToTxnDate >DATETYPE</ToTxnDate> <!-- optional -->
                                        <!-- OR -->
                                                <!-- DateMacro may have one of the following values: All, Today, ThisWeek, ThisWeekToDate, ThisMonth, ThisMonthToDate, ThisCalendarQuarter, ThisCalendarQuarterToDate, ThisFiscalQuarter, ThisFiscalQuarterToDate, ThisCalendarYear, ThisCalendarYearToDate, ThisFiscalYear, ThisFiscalYearToDate, Yesterday, LastWeek, LastWeekToDate, LastMonth, LastMonthToDate, LastCalendarQuarter, LastCalendarQuarterToDate, LastFiscalQuarter, LastFiscalQuarterToDate, LastCalendarYear, LastCalendarYearToDate, LastFiscalYear, LastFiscalYearToDate, NextWeek, NextFourWeeks, NextMonth, NextCalendarQuarter, NextCalendarYear, NextFiscalQuarter, NextFiscalYear -->
                                                <DateMacro >ENUMTYPE</DateMacro> <!-- optional -->
                                        <!-- END OR -->
                                </TransactionDateRangeFilter>
                                <TransactionEntityFilter> <!-- optional -->
                                        <!-- BEGIN OR -->
                                                <!-- EntityTypeFilter may have one of the following values: Customer, Employee, OtherName, Vendor -->
                                                <EntityTypeFilter >ENUMTYPE</EntityTypeFilter> <!-- optional -->
                                        <!-- OR -->
                                                <ListID >IDTYPE</ListID> <!-- optional, may repeat -->
                                        <!-- OR -->
                                                <FullName >STRTYPE</FullName> <!-- optional, may repeat -->
                                        <!-- OR -->
                                                <ListIDWithChildren >IDTYPE</ListIDWithChildren> <!-- optional -->
                                        <!-- OR -->
                                                <FullNameWithChildren >STRTYPE</FullNameWithChildren> <!-- optional -->
                                        <!-- END OR -->
                                </TransactionEntityFilter>
                                <TransactionAccountFilter> <!-- optional -->
                                        <!-- BEGIN OR -->
                                                <!-- AccountTypeFilter may have one of the following values: AccountsPayable, AccountsReceivable, AllowedFor1099, APAndSalesTax, APOrCreditCard, ARAndAP, Asset, BalanceSheet, Bank, BankAndARAndAPAndUF, BankAndUF, CostOfSales, CreditCard, CurrentAsset, CurrentAssetAndExpense, CurrentLiability, Equity, EquityAndIncomeAndExpense, ExpenseAndOtherExpense, FixedAsset, IncomeAndExpense, IncomeAndOtherIncome, Liability, LiabilityAndEquity, LongTermLiability, NonPosting, OrdinaryExpense, OrdinaryIncome, OrdinaryIncomeAndCOGS, OrdinaryIncomeAndExpense, OtherAsset, OtherCurrentAsset, OtherCurrentLiability, OtherExpense, OtherIncome, OtherIncomeOrExpense -->
                                                <AccountTypeFilter >ENUMTYPE</AccountTypeFilter> <!-- optional -->
                                        <!-- OR -->
                                                <ListID >IDTYPE</ListID> <!-- optional, may repeat -->
                                        <!-- OR -->
                                                <FullName >STRTYPE</FullName> <!-- optional, may repeat -->
                                        <!-- OR -->
                                                <ListIDWithChildren >IDTYPE</ListIDWithChildren> <!-- optional -->
                                        <!-- OR -->
                                                <FullNameWithChildren >STRTYPE</FullNameWithChildren> <!-- optional -->
                                        <!-- END OR -->
                                </TransactionAccountFilter>
                                <TransactionItemFilter> <!-- optional -->
                                        <!-- BEGIN OR -->
                                                <!-- ItemTypeFilter may have one of the following values: AllExceptFixedAsset, Assembly, Discount, FixedAsset, Inventory, InventoryAndAssembly, NonInventory, OtherCharge, Payment, Sales, SalesTax, Service -->
                                                <ItemTypeFilter >ENUMTYPE</ItemTypeFilter> <!-- optional -->
                                        <!-- OR -->
                                                <ListID >IDTYPE</ListID> <!-- optional, may repeat -->
                                        <!-- OR -->
                                                <FullName >STRTYPE</FullName> <!-- optional, may repeat -->
                                        <!-- OR -->
                                                <ListIDWithChildren >IDTYPE</ListIDWithChildren> <!-- optional -->
                                        <!-- OR -->
                                                <FullNameWithChildren >STRTYPE</FullNameWithChildren> <!-- optional -->
                                        <!-- END OR -->
                                </TransactionItemFilter>
                                <TransactionClassFilter> <!-- optional -->
                                        <!-- BEGIN OR -->
                                                <ListID >IDTYPE</ListID> <!-- optional, may repeat -->
                                        <!-- OR -->
                                                <FullName >STRTYPE</FullName> <!-- optional, may repeat -->
                                        <!-- OR -->
                                                <ListIDWithChildren >IDTYPE</ListIDWithChildren> <!-- optional -->
                                        <!-- OR -->
                                                <FullNameWithChildren >STRTYPE</FullNameWithChildren> <!-- optional -->
                                        <!-- END OR -->
                                </TransactionClassFilter>
                                <TransactionTypeFilter> <!-- optional -->
                                        <!-- TxnTypeFilter may have one of the following values: All, ARRefundCreditCard, Bill, BillPaymentCheck, BillPaymentCreditCard, BuildAssembly, Charge, Check, CreditCardCharge, CreditCardCredit, CreditMemo, Deposit, Estimate, InventoryAdjustment, Invoice, ItemReceipt, JournalEntry, LiabilityAdjustment, Paycheck, PayrollLiabilityCheck, PurchaseOrder, ReceivePayment, SalesOrder, SalesReceipt, SalesTaxPaymentCheck, Transfer, VendorCredit, YTDAdjustment -->
                                        <TxnTypeFilter >ENUMTYPE</TxnTypeFilter> <!-- required, may repeat -->
                                </TransactionTypeFilter>
                                <!-- TransactionDetailLevelFilter may have one of the following values: All, SummaryOnly [DEFAULT], AllExceptSummary -->
                                <TransactionDetailLevelFilter >ENUMTYPE</TransactionDetailLevelFilter> <!-- optional -->
                                <!-- TransactionPostingStatusFilter may have one of the following values: Either [DEFAULT], NonPosting, Posting -->
                                <TransactionPostingStatusFilter >ENUMTYPE</TransactionPostingStatusFilter> <!-- optional -->
                                <!-- TransactionPaidStatusFilter may have one of the following values: Either [DEFAULT], Closed, Open -->
                                <TransactionPaidStatusFilter >ENUMTYPE</TransactionPaidStatusFilter> <!-- optional -->
                                <CurrencyFilter> <!-- optional -->
                                        <!-- BEGIN OR -->
                                                <ListID >IDTYPE</ListID> <!-- optional, may repeat -->
                                        <!-- OR -->
                                                <FullName >STRTYPE</FullName> <!-- optional, may repeat -->
                                        <!-- END OR -->
                                </CurrencyFilter>
                        <!-- END OR -->
                        <IncludeRetElement >STRTYPE</IncludeRetElement> <!-- optional, may repeat -->
                </TransactionQueryRq>

                <TransactionQueryRs statusCode="INTTYPE" statusSeverity="STRTYPE" statusMessage="STRTYPE" retCount="INTTYPE" iteratorRemainingCount="INTTYPE" iteratorID="UUIDTYPE">
                        <TransactionRet> <!-- optional, may repeat -->
                                <!-- TxnType may have one of the following values: ARRefundCreditCard, Bill, BillPaymentCheck, BillPaymentCreditCard, BuildAssembly, Charge, Check, CreditCardCharge, CreditCardCredit, CreditMemo, Deposit, Estimate, InventoryAdjustment, Invoice, ItemReceipt, JournalEntry, LiabilityAdjustment, Paycheck, PayrollLiabilityCheck, PurchaseOrder, ReceivePayment, SalesOrder, SalesReceipt, SalesTaxPaymentCheck, Transfer, VendorCredit, YTDAdjustment -->
                                <TxnType >ENUMTYPE</TxnType> <!-- optional -->
                                <TxnID >IDTYPE</TxnID> <!-- optional -->
                                <TxnLineID >IDTYPE</TxnLineID> <!-- optional -->
                                <TimeCreated >DATETIMETYPE</TimeCreated> <!-- optional -->
                                <TimeModified >DATETIMETYPE</TimeModified> <!-- optional -->
                                <EntityRef> <!-- optional -->
                                        <ListID >IDTYPE</ListID> <!-- optional -->
                                        <FullName >STRTYPE</FullName> <!-- optional -->
                                </EntityRef>
                                <AccountRef> <!-- optional -->
                                        <ListID >IDTYPE</ListID> <!-- optional -->
                                        <FullName >STRTYPE</FullName> <!-- optional -->
                                </AccountRef>
                                <TxnDate >DATETYPE</TxnDate> <!-- optional -->
                                <RefNumber >STRTYPE</RefNumber> <!-- optional -->
                                <Amount >AMTTYPE</Amount> <!-- optional -->
                                <CurrencyRef> <!-- optional -->
                                        <ListID >IDTYPE</ListID> <!-- optional -->
                                        <FullName >STRTYPE</FullName> <!-- optional -->
                                </CurrencyRef>
                                <ExchangeRate >FLOATTYPE</ExchangeRate> <!-- optional -->
                                <AmountInHomeCurrency >AMTTYPE</AmountInHomeCurrency> <!-- optional -->
                                <Memo >STRTYPE</Memo> <!-- optional -->
                        </TransactionRet>
                </TransactionQueryRs>
        </QBXMLMsgsRq>
</QBXML>
```
## TransferInventoryQuery
### XMLOps
```
<?xml version="1.0" encoding="utf-8"?>
<?qbxml version="16.0"?>
<QBXML>
    <QBXMLMsgsRq onError="stopOnError">
        <TransferInventoryQueryRq metaData="ENUMTYPE" iterator="ENUMTYPE" iteratorID="UUIDTYPE">
            <!-- BEGIN OR -->
                <TxnID >IDTYPE</TxnID> <!-- optional, may repeat -->
            <!-- OR -->
                <RefNumber >STRTYPE</RefNumber> <!-- optional, may repeat -->
            <!-- OR -->
                <RefNumberCaseSensitive >STRTYPE</RefNumberCaseSensitive> <!-- optional, may repeat -->
            <!-- OR -->
                <MaxReturned >INTTYPE</MaxReturned> <!-- optional -->
                <!-- BEGIN OR -->
                    <ModifiedDateRangeFilter> <!-- optional -->
                        <FromModifiedDate >DATETIMETYPE</FromModifiedDate> <!-- optional -->
                        <ToModifiedDate >DATETIMETYPE</ToModifiedDate> <!-- optional -->
                    </ModifiedDateRangeFilter>
                <!-- OR -->
                    <TxnDateRangeFilter> <!-- optional -->
                        <!-- BEGIN OR -->
                            <FromTxnDate >DATETYPE</FromTxnDate> <!-- optional -->
                            <ToTxnDate >DATETYPE</ToTxnDate> <!-- optional -->
                        <!-- OR -->
                            <!-- DateMacro may have one of the following values: All, Today, ThisWeek, ThisWeekToDate, ThisMonth, ThisMonthToDate, ThisCalendarQuarter, ThisCalendarQuarterToDate, ThisFiscalQuarter, ThisFiscalQuarterToDate, ThisCalendarYear, ThisCalendarYearToDate, ThisFiscalYear, ThisFiscalYearToDate, Yesterday, LastWeek, LastWeekToDate, LastMonth, LastMonthToDate, LastCalendarQuarter, LastCalendarQuarterToDate, LastFiscalQuarter, LastFiscalQuarterToDate, LastCalendarYear, LastCalendarYearToDate, LastFiscalYear, LastFiscalYearToDate, NextWeek, NextFourWeeks, NextMonth, NextCalendarQuarter, NextCalendarYear, NextFiscalQuarter, NextFiscalYear -->
                            <DateMacro >ENUMTYPE</DateMacro> <!-- optional -->
                        <!-- END OR -->
                    </TxnDateRangeFilter>
                <!-- END OR -->
                <EntityFilter> <!-- optional -->
                    <!-- BEGIN OR -->
                        <ListID >IDTYPE</ListID> <!-- optional, may repeat -->
                    <!-- OR -->
                        <FullName >STRTYPE</FullName> <!-- optional, may repeat -->
                    <!-- OR -->
                        <ListIDWithChildren >IDTYPE</ListIDWithChildren> <!-- optional -->
                    <!-- OR -->
                        <FullNameWithChildren >STRTYPE</FullNameWithChildren> <!-- optional -->
                    <!-- END OR -->
                </EntityFilter>
                <AccountFilter> <!-- optional -->
                    <!-- BEGIN OR -->
                        <ListID >IDTYPE</ListID> <!-- optional, may repeat -->
                    <!-- OR -->
                        <FullName >STRTYPE</FullName> <!-- optional, may repeat -->
                    <!-- OR -->
                        <ListIDWithChildren >IDTYPE</ListIDWithChildren> <!-- optional -->
                    <!-- OR -->
                        <FullNameWithChildren >STRTYPE</FullNameWithChildren> <!-- optional -->
                    <!-- END OR -->
                </AccountFilter>
                <!-- BEGIN OR -->
                    <RefNumberFilter> <!-- optional -->
                        <!-- MatchCriterion may have one of the following values: StartsWith, Contains, EndsWith -->
                        <MatchCriterion >ENUMTYPE</MatchCriterion> <!-- required -->
                        <RefNumber >STRTYPE</RefNumber> <!-- required -->
                    </RefNumberFilter>
                <!-- OR -->
                    <RefNumberRangeFilter> <!-- optional -->
                        <FromRefNumber >STRTYPE</FromRefNumber> <!-- optional -->
                        <ToRefNumber >STRTYPE</ToRefNumber> <!-- optional -->
                    </RefNumberRangeFilter>
                <!-- END OR -->
            <!-- OR -->
                <SiteFilter> <!-- optional -->
                    <!-- BEGIN OR -->
                        <ListID >IDTYPE</ListID> <!-- optional, may repeat -->
                    <!-- OR -->
                        <FullName >STRTYPE</FullName> <!-- optional, may repeat -->
                    <!-- END OR -->
                </SiteFilter>
            <!-- END OR -->
            <IncludeLineItems >BOOLTYPE</IncludeLineItems> <!-- optional -->
            <IncludeRetElement >STRTYPE</IncludeRetElement> <!-- optional, may repeat -->
        </TransferInventoryQueryRq>

        <TransferInventoryQueryRs statusCode="INTTYPE" statusSeverity="STRTYPE" statusMessage="STRTYPE" retCount="INTTYPE" iteratorRemainingCount="INTTYPE" iteratorID="UUIDTYPE">
            <TransferInventoryRet> <!-- optional, may repeat -->
                <TxnID >IDTYPE</TxnID> <!-- required -->
                <TimeCreated >DATETIMETYPE</TimeCreated> <!-- required -->
                <TimeModified >DATETIMETYPE</TimeModified> <!-- required -->
                <EditSequence >STRTYPE</EditSequence> <!-- required -->
                <TxnNumber >INTTYPE</TxnNumber> <!-- optional -->
                <TxnDate >DATETYPE</TxnDate> <!-- optional -->
                <RefNumber >STRTYPE</RefNumber> <!-- optional -->
                <FromInventorySiteRef> <!-- optional -->
                    <ListID >IDTYPE</ListID> <!-- optional -->
                    <FullName >STRTYPE</FullName> <!-- optional -->
                </FromInventorySiteRef>
                <ToInventorySiteRef> <!-- optional -->
                    <ListID >IDTYPE</ListID> <!-- optional -->
                    <FullName >STRTYPE</FullName> <!-- optional -->
                </ToInventorySiteRef>
                <Memo >STRTYPE</Memo> <!-- optional -->
                <ExternalGUID >GUIDTYPE</ExternalGUID> <!-- optional -->
                <TransferInventoryLineRet> <!-- optional, may repeat -->
                    <TxnLineID >IDTYPE</TxnLineID> <!-- required -->
                    <ItemRef> <!-- optional -->
                        <ListID >IDTYPE</ListID> <!-- optional -->
                        <FullName >STRTYPE</FullName> <!-- optional -->
                    </ItemRef>
                    <FromInventorySiteLocationRef> <!-- optional -->
                        <ListID >IDTYPE</ListID> <!-- optional -->
                        <FullName >STRTYPE</FullName> <!-- optional -->
                    </FromInventorySiteLocationRef>
                    <ToInventorySiteLocationRef> <!-- optional -->
                        <ListID >IDTYPE</ListID> <!-- optional -->
                        <FullName >STRTYPE</FullName> <!-- optional -->
                    </ToInventorySiteLocationRef>
                    <QuantityTransferred >QUANTYPE</QuantityTransferred> <!-- optional -->
                    <!-- BEGIN OR -->
                        <SerialNumber >STRTYPE</SerialNumber> <!-- optional -->
                    <!-- OR -->
                        <LotNumber >STRTYPE</LotNumber> <!-- optional -->
                    <!-- END OR -->
                                        <ExpirationDateForSerialLotNumber>STRTYPE</ExpirationDateForSerialLotNumber> <!-- optional -->
                </TransferInventoryLineRet>
            </TransferInventoryRet>
        </TransferInventoryQueryRs>
    </QBXMLMsgsRq>
</QBXML>
```
## TransferQuery
### XMLOps
```
<?xml version="1.0" encoding="utf-8"?>
<?qbxml version="16.0"?>
<QBXML>
        <QBXMLMsgsRq onError="stopOnError">
                <TransferQueryRq metaData="ENUMTYPE" iterator="ENUMTYPE" iteratorID="UUIDTYPE">
                        <!-- BEGIN OR -->
                                <TxnID >IDTYPE</TxnID> <!-- optional, may repeat -->
                        <!-- OR -->
                                <MaxReturned >INTTYPE</MaxReturned> <!-- optional -->
                                <!-- BEGIN OR -->
                                        <ModifiedDateRangeFilter> <!-- optional -->
                                                <FromModifiedDate >DATETIMETYPE</FromModifiedDate> <!-- optional -->
                                                <ToModifiedDate >DATETIMETYPE</ToModifiedDate> <!-- optional -->
                                        </ModifiedDateRangeFilter>
                                <!-- OR -->
                                        <TxnDateRangeFilter> <!-- optional -->
                                                <!-- BEGIN OR -->
                                                        <FromTxnDate >DATETYPE</FromTxnDate> <!-- optional -->
                                                        <ToTxnDate >DATETYPE</ToTxnDate> <!-- optional -->
                                                <!-- OR -->
                                                        <!-- DateMacro may have one of the following values: All, Today, ThisWeek, ThisWeekToDate, ThisMonth, ThisMonthToDate, ThisCalendarQuarter, ThisCalendarQuarterToDate, ThisFiscalQuarter, ThisFiscalQuarterToDate, ThisCalendarYear, ThisCalendarYearToDate, ThisFiscalYear, ThisFiscalYearToDate, Yesterday, LastWeek, LastWeekToDate, LastMonth, LastMonthToDate, LastCalendarQuarter, LastCalendarQuarterToDate, LastFiscalQuarter, LastFiscalQuarterToDate, LastCalendarYear, LastCalendarYearToDate, LastFiscalYear, LastFiscalYearToDate, NextWeek, NextFourWeeks, NextMonth, NextCalendarQuarter, NextCalendarYear, NextFiscalQuarter, NextFiscalYear -->
                                                        <DateMacro >ENUMTYPE</DateMacro> <!-- optional -->
                                                <!-- END OR -->
                                        </TxnDateRangeFilter>
                                <!-- END OR -->
                        <!-- END OR -->
                        <IncludeRetElement >STRTYPE</IncludeRetElement> <!-- optional, may repeat -->
                </TransferQueryRq>

                <TransferQueryRs statusCode="INTTYPE" statusSeverity="STRTYPE" statusMessage="STRTYPE" retCount="INTTYPE" iteratorRemainingCount="INTTYPE" iteratorID="UUIDTYPE">
                        <TransferRet> <!-- optional, may repeat -->
                                <TxnID >IDTYPE</TxnID> <!-- required -->
                                <TimeCreated >DATETIMETYPE</TimeCreated> <!-- required -->
                                <TimeModified >DATETIMETYPE</TimeModified> <!-- required -->
                                <EditSequence >STRTYPE</EditSequence> <!-- required -->
                                <TxnNumber >INTTYPE</TxnNumber> <!-- optional -->
                                <TxnDate >DATETYPE</TxnDate> <!-- optional -->
                                <TransferFromAccountRef> <!-- optional -->
                                        <ListID >IDTYPE</ListID> <!-- optional -->
                                        <FullName >STRTYPE</FullName> <!-- optional -->
                                </TransferFromAccountRef>
                                <FromAccountBalance >AMTTYPE</FromAccountBalance> <!-- optional -->
                                <TransferToAccountRef> <!-- optional -->
                                        <ListID >IDTYPE</ListID> <!-- optional -->
                                        <FullName >STRTYPE</FullName> <!-- optional -->
                                </TransferToAccountRef>
                                <ToAccountBalance >AMTTYPE</ToAccountBalance> <!-- optional -->
                                <ClassRef> <!-- optional -->
                                        <ListID >IDTYPE</ListID> <!-- optional -->
                                        <FullName >STRTYPE</FullName> <!-- optional -->
                                </ClassRef>
                                <Amount >AMTTYPE</Amount> <!-- optional -->
                                <Memo >STRTYPE</Memo> <!-- optional -->
                        </TransferRet>
                </TransferQueryRs>
        </QBXMLMsgsRq>
</QBXML>
```
## TxnDeletedQuery

A TxnDeletedQuery will return all transaction elements deleted within the last 90 days, grouped according to object type. (For example, if the request specifies TxnDelType elements of Bill and then Check, it will return all the Bill deletes first, then all the Check deletes.) By default, the records are returned in ascending order, according to the “real” delete time. For example:
•
If transaction A is deleted at 10 a.m. and B is deleted at 11 a.m., the query request will return A first, then B.
•
However, if the QuickBooks user moves the clock back before deleting B (for example, B is deleted at 9 a.m.), the query will still return first A then B, because B was deleted after A in “real” time.

### XMLOps
```
<?xml version="1.0" encoding="utf-8"?>
<?qbxml version="16.0"?>
<QBXML>
        <QBXMLMsgsRq onError="stopOnError">
                <TxnDeletedQueryRq metaData="ENUMTYPE">
                        <!-- TxnDelType may have one of the following values: ARRefundCreditCard, Bill, BillPaymentCheck, BillPaymentCreditCard, BuildAssembly, Charge, Check, CreditCardCharge, CreditCardCredit, CreditMemo, Deposit, Estimate, InventoryAdjustment, Invoice, ItemReceipt, JournalEntry, PayrollLiabilityAdjustment [PRIVATE], PayrollPriorPayment [PRIVATE], PayrollYearToDateAdjustment [PRIVATE], PurchaseOrder, ReceivePayment, SalesOrder, SalesReceipt, SalesTaxPaymentCheck, TimeTracking, TransferInventory, VehicleMileage, VendorCredit -->
                        <TxnDelType >ENUMTYPE</TxnDelType> <!-- required, may repeat -->
                        <DeletedDateRangeFilter> <!-- optional -->
                                <FromDeletedDate >DATETIMETYPE</FromDeletedDate> <!-- optional -->
                                <ToDeletedDate >DATETIMETYPE</ToDeletedDate> <!-- optional -->
                        </DeletedDateRangeFilter>
                        <IncludeRetElement >STRTYPE</IncludeRetElement> <!-- optional, may repeat -->
                </TxnDeletedQueryRq>

                <TxnDeletedQueryRs statusCode="INTTYPE" statusSeverity="STRTYPE" statusMessage="STRTYPE" retCount="INTTYPE">
                        <TxnDeletedRet> <!-- optional, may repeat -->
                                <!-- TxnDelType may have one of the following values: ARRefundCreditCard, Bill, BillPaymentCheck, BillPaymentCreditCard, BuildAssembly, Charge, Check, CreditCardCharge, CreditCardCredit, CreditMemo, Deposit, Estimate, InventoryAdjustment, Invoice, ItemReceipt, JournalEntry, PayrollLiabilityAdjustment [PRIVATE], PayrollPriorPayment [PRIVATE], PayrollYearToDateAdjustment [PRIVATE], PurchaseOrder, ReceivePayment, SalesOrder, SalesReceipt, SalesTaxPaymentCheck, TimeTracking, TransferInventory, VehicleMileage, VendorCredit -->
                                <TxnDelType >ENUMTYPE</TxnDelType> <!-- required -->
                                <TxnID >IDTYPE</TxnID> <!-- required -->
                                <TimeCreated >DATETIMETYPE</TimeCreated> <!-- required -->
                                <TimeDeleted >DATETIMETYPE</TimeDeleted> <!-- required -->
                                <RefNumber >STRTYPE</RefNumber> <!-- optional -->
                        </TxnDeletedRet>
                </TxnDeletedQueryRs>
        </QBXMLMsgsRq>
</QBXML>
```
## UIEventSubscriptionQuery
### XMLOps
```
<?xml version="1.0" encoding="utf-8"?>
<?qbxml version="16.0"?>
<QBXML>
        <QBXMLSubscriptionMsgsRq onError="stopOnError">
                <UIEventSubscriptionQueryRq>
                        <SubscriberID >GUIDTYPE</SubscriberID> <!-- required -->
                </UIEventSubscriptionQueryRq>

                <UIEventSubscriptionQueryRs statusCode="INTTYPE" statusSeverity="STRTYPE" statusMessage="STRTYPE">
                        <UIEventSubscriptionRet> <!-- optional -->
                                <SubscriberID >GUIDTYPE</SubscriberID> <!-- required -->
                                <TimeCreated >DATETIMETYPE</TimeCreated> <!-- required -->
                                <TimeLastProcessed >DATETIMETYPE</TimeLastProcessed> <!-- optional -->
                                <COMCallbackInfo> <!-- required -->
                                        <AppName >STRTYPE</AppName> <!-- required -->
                                        <!-- BEGIN OR -->
                                                <ProgID >STRTYPE</ProgID> <!-- optional -->
                                        <!-- OR -->
                                                <CLSID >GUIDTYPE</CLSID> <!-- optional -->
                                        <!-- END OR -->
                                </COMCallbackInfo>
                                <!-- DeliveryPolicy may have one of the following values: DeliverAlways, DeliverOnlyIfRunning -->
                                <DeliveryPolicy >ENUMTYPE</DeliveryPolicy> <!-- required -->
                                <CompanyFileEventSubscription> <!-- required -->
                                        <!-- CompanyFileEventOperation may have one of the following values: Close, Open -->
                                        <CompanyFileEventOperation >ENUMTYPE</CompanyFileEventOperation> <!-- required, may repeat -->
                                </CompanyFileEventSubscription>
                        </UIEventSubscriptionRet>
                </UIEventSubscriptionQueryRs>
        </QBXMLSubscriptionMsgsRq>
</QBXML>
```
## UIExtensionSubscriptionQuery
Queries for all UI extension event subscriptions that (a) match the specified SubscriberID, and (b) were originally created using the same qbXML spec version as the one used to make the subscription query. That is, if you make a qbXML 4.0 subscription query you will only get subscriptions originally made with qbXML 4.0! To get subscriptions made with qbXML 5.0, your subscription query must itself use qbXML 5.0.

The subscriberID you supply to this query is the one that was used to make the original event subscription, and which should have been written down by the person who made the subscription. (There is no way to get the SubscriberID if you don’t already know it.)

For details about the UI-extension feature, see Integrating with the QuickBooks UI.

This request must be invoked using the request processor method ProcessSubscription(), if you use qbXML. If you use QBFC, this request must be appended to an ISubscriptionMsgSetRequest object instantiated by the QBSessionManager method CreateSubscriptionMsgSetRequest() and invoked by the method DoSubscriptionRequests().
### XMLOps
```
<?xml version="1.0" encoding="utf-8"?>
<?qbxml version="16.0"?>
<QBXML>
        <QBXMLSubscriptionMsgsRq onError="stopOnError">
                <UIExtensionSubscriptionQueryRq>
                        <SubscriberID >GUIDTYPE</SubscriberID> <!-- required -->
                </UIExtensionSubscriptionQueryRq>

                <UIExtensionSubscriptionQueryRs statusCode="INTTYPE" statusSeverity="STRTYPE" statusMessage="STRTYPE">
                        <UIExtensionSubscriptionRet> <!-- optional -->
                                <SubscriberID >GUIDTYPE</SubscriberID> <!-- required -->
                                <TimeCreated >DATETIMETYPE</TimeCreated> <!-- required -->
                                <TimeLastProcessed >DATETIMETYPE</TimeLastProcessed> <!-- optional -->
                                <COMCallbackInfo> <!-- required -->
                                        <AppName >STRTYPE</AppName> <!-- required -->
                                        <!-- BEGIN OR -->
                                                <ProgID >STRTYPE</ProgID> <!-- optional -->
                                        <!-- OR -->
                                                <CLSID >GUIDTYPE</CLSID> <!-- optional -->
                                        <!-- END OR -->
                                </COMCallbackInfo>
                                <MenuExtensionSubscription> <!-- required -->
                                        <!-- AddToMenu may have one of the following values: File, Company, Customers, Vendors, Employees, Banking -->
                                        <AddToMenu >ENUMTYPE</AddToMenu> <!-- required -->
                                        <!-- BEGIN OR -->
                                                <Submenu> <!-- optional -->
                                                        <DisplayCondition> <!-- optional -->
                                                                <!-- VisibleIf may have one of the following values: AccountantCopyExists, AssemblyItemsEnabled, ClassesEnabled, EstimatesEnabled, HasCustomers, HasVendors, InventoryEnabled, IsAccountantCopy, MultiUserMode, PayrollEnabled, PriceLevelsEnabled, SalesOrdersEnabled, SalesTaxEnabled, TimeTrackingEnabled -->
                                                                <VisibleIf >ENUMTYPE</VisibleIf> <!-- optional, may repeat -->
                                                                <!-- VisibleIfNot may have one of the following values: AccountantCopyExists, AssemblyItemsEnabled, ClassesEnabled, EstimatesEnabled, HasCustomers, HasVendors, InventoryEnabled, IsAccountantCopy, MultiUserMode, PayrollEnabled, PriceLevelsEnabled, SalesOrdersEnabled, SalesTaxEnabled, TimeTrackingEnabled -->
                                                                <VisibleIfNot >ENUMTYPE</VisibleIfNot> <!-- optional, may repeat -->
                                                                <!-- EnabledIf may have one of the following values: AccountantCopyExists, AssemblyItemsEnabled, ClassesEnabled, EstimatesEnabled, HasCustomers, HasVendors, InventoryEnabled, IsAccountantCopy, MultiUserMode, PayrollEnabled, PriceLevelsEnabled, SalesOrdersEnabled, SalesTaxEnabled, TimeTrackingEnabled -->
                                                                <EnabledIf >ENUMTYPE</EnabledIf> <!-- optional, may repeat -->
                                                                <!-- EnabledIfNot may have one of the following values: AccountantCopyExists, AssemblyItemsEnabled, ClassesEnabled, EstimatesEnabled, HasCustomers, HasVendors, InventoryEnabled, IsAccountantCopy, MultiUserMode, PayrollEnabled, PriceLevelsEnabled, SalesOrdersEnabled, SalesTaxEnabled, TimeTrackingEnabled -->
                                                                <EnabledIfNot >ENUMTYPE</EnabledIfNot> <!-- optional, may repeat -->
                                                        </DisplayCondition>
                                                        <MenuItem> <!-- required, may repeat -->
                                                                <MenuText >STRTYPE</MenuText> <!-- required -->
                                                                <EventTag >STRTYPE</EventTag> <!-- required -->
                                                                <DisplayCondition> <!-- optional -->
                                                                        <!-- VisibleIf may have one of the following values: AccountantCopyExists, AssemblyItemsEnabled, ClassesEnabled, EstimatesEnabled, HasCustomers, HasVendors, InventoryEnabled, IsAccountantCopy, MultiUserMode, PayrollEnabled, PriceLevelsEnabled, SalesOrdersEnabled, SalesTaxEnabled, TimeTrackingEnabled -->
                                                                        <VisibleIf >ENUMTYPE</VisibleIf> <!-- optional, may repeat -->
                                                                        <!-- VisibleIfNot may have one of the following values: AccountantCopyExists, AssemblyItemsEnabled, ClassesEnabled, EstimatesEnabled, HasCustomers, HasVendors, InventoryEnabled, IsAccountantCopy, MultiUserMode, PayrollEnabled, PriceLevelsEnabled, SalesOrdersEnabled, SalesTaxEnabled, TimeTrackingEnabled -->
                                                                        <VisibleIfNot >ENUMTYPE</VisibleIfNot> <!-- optional, may repeat -->
                                                                        <!-- EnabledIf may have one of the following values: AccountantCopyExists, AssemblyItemsEnabled, ClassesEnabled, EstimatesEnabled, HasCustomers, HasVendors, InventoryEnabled, IsAccountantCopy, MultiUserMode, PayrollEnabled, PriceLevelsEnabled, SalesOrdersEnabled, SalesTaxEnabled, TimeTrackingEnabled -->
                                                                        <EnabledIf >ENUMTYPE</EnabledIf> <!-- optional, may repeat -->
                                                                        <!-- EnabledIfNot may have one of the following values: AccountantCopyExists, AssemblyItemsEnabled, ClassesEnabled, EstimatesEnabled, HasCustomers, HasVendors, InventoryEnabled, IsAccountantCopy, MultiUserMode, PayrollEnabled, PriceLevelsEnabled, SalesOrdersEnabled, SalesTaxEnabled, TimeTrackingEnabled -->
                                                                        <EnabledIfNot >ENUMTYPE</EnabledIfNot> <!-- optional, may repeat -->
                                                                </DisplayCondition>
                                                        </MenuItem>
                                                </Submenu>
                                        <!-- OR -->
                                                <MenuItem> <!-- optional -->
                                                        <MenuText >STRTYPE</MenuText> <!-- required -->
                                                        <EventTag >STRTYPE</EventTag> <!-- required -->
                                                        <DisplayCondition> <!-- optional -->
                                                                <!-- VisibleIf may have one of the following values: AccountantCopyExists, AssemblyItemsEnabled, ClassesEnabled, EstimatesEnabled, HasCustomers, HasVendors, InventoryEnabled, IsAccountantCopy, MultiUserMode, PayrollEnabled, PriceLevelsEnabled, SalesOrdersEnabled, SalesTaxEnabled, TimeTrackingEnabled -->
                                                                <VisibleIf >ENUMTYPE</VisibleIf> <!-- optional, may repeat -->
                                                                <!-- VisibleIfNot may have one of the following values: AccountantCopyExists, AssemblyItemsEnabled, ClassesEnabled, EstimatesEnabled, HasCustomers, HasVendors, InventoryEnabled, IsAccountantCopy, MultiUserMode, PayrollEnabled, PriceLevelsEnabled, SalesOrdersEnabled, SalesTaxEnabled, TimeTrackingEnabled -->
                                                                <VisibleIfNot >ENUMTYPE</VisibleIfNot> <!-- optional, may repeat -->
                                                                <!-- EnabledIf may have one of the following values: AccountantCopyExists, AssemblyItemsEnabled, ClassesEnabled, EstimatesEnabled, HasCustomers, HasVendors, InventoryEnabled, IsAccountantCopy, MultiUserMode, PayrollEnabled, PriceLevelsEnabled, SalesOrdersEnabled, SalesTaxEnabled, TimeTrackingEnabled -->
                                                                <EnabledIf >ENUMTYPE</EnabledIf> <!-- optional, may repeat -->
                                                                <!-- EnabledIfNot may have one of the following values: AccountantCopyExists, AssemblyItemsEnabled, ClassesEnabled, EstimatesEnabled, HasCustomers, HasVendors, InventoryEnabled, IsAccountantCopy, MultiUserMode, PayrollEnabled, PriceLevelsEnabled, SalesOrdersEnabled, SalesTaxEnabled, TimeTrackingEnabled -->
                                                                <EnabledIfNot >ENUMTYPE</EnabledIfNot> <!-- optional, may repeat -->
                                                        </DisplayCondition>
                                                </MenuItem>
                                        <!-- END OR -->
                                </MenuExtensionSubscription>
                        </UIExtensionSubscriptionRet>
                </UIExtensionSubscriptionQueryRs>
        </QBXMLSubscriptionMsgsRq>
</QBXML>
```
## UnitOfMeasureSetQuery
### XMLOps
```
<?xml version="1.0" encoding="utf-8"?>
<?qbxml version="16.0"?>
<QBXML>
        <QBXMLMsgsRq onError="stopOnError">
                <UnitOfMeasureSetQueryRq metaData="ENUMTYPE">
                        <!-- BEGIN OR -->
                                <ListID >IDTYPE</ListID> <!-- optional, may repeat -->
                        <!-- OR -->
                                <FullName >STRTYPE</FullName> <!-- optional, may repeat -->
                        <!-- OR -->
                                <MaxReturned >INTTYPE</MaxReturned> <!-- optional -->
                                <!-- ActiveStatus may have one of the following values: ActiveOnly [DEFAULT], InactiveOnly, All -->
                                <ActiveStatus >ENUMTYPE</ActiveStatus> <!-- optional -->
                                <FromModifiedDate >DATETIMETYPE</FromModifiedDate> <!-- optional -->
                                <ToModifiedDate >DATETIMETYPE</ToModifiedDate> <!-- optional -->
                                <!-- BEGIN OR -->
                                        <NameFilter> <!-- optional -->
                                                <!-- MatchCriterion may have one of the following values: StartsWith, Contains, EndsWith -->
                                                <MatchCriterion >ENUMTYPE</MatchCriterion> <!-- required -->
                                                <Name >STRTYPE</Name> <!-- required -->
                                        </NameFilter>
                                <!-- OR -->
                                        <NameRangeFilter> <!-- optional -->
                                                <FromName >STRTYPE</FromName> <!-- optional -->
                                                <ToName >STRTYPE</ToName> <!-- optional -->
                                        </NameRangeFilter>
                                <!-- END OR -->
                        <!-- END OR -->
                        <IncludeRetElement >STRTYPE</IncludeRetElement> <!-- optional, may repeat -->
                </UnitOfMeasureSetQueryRq>

                <UnitOfMeasureSetQueryRs statusCode="INTTYPE" statusSeverity="STRTYPE" statusMessage="STRTYPE" retCount="INTTYPE">
                        <UnitOfMeasureSetRet> <!-- optional, may repeat -->
                                <ListID >IDTYPE</ListID> <!-- optional -->
                                <TimeCreated >DATETIMETYPE</TimeCreated> <!-- optional -->
                                <TimeModified >DATETIMETYPE</TimeModified> <!-- optional -->
                                <EditSequence >STRTYPE</EditSequence> <!-- optional -->
                                <Name >STRTYPE</Name> <!-- optional -->
                                <IsActive >BOOLTYPE</IsActive> <!-- optional -->
                                <!-- UnitOfMeasureType may have one of the following values: Area, Count, Length, Other, Time, Volume, Weight -->
                                <UnitOfMeasureType >ENUMTYPE</UnitOfMeasureType> <!-- optional -->
                                <BaseUnit> <!-- optional -->
                                        <Name >STRTYPE</Name> <!-- required -->
                                        <Abbreviation >STRTYPE</Abbreviation> <!-- required -->
                                </BaseUnit>
                                <RelatedUnit> <!-- optional, may repeat -->
                                        <Name >STRTYPE</Name> <!-- required -->
                                        <Abbreviation >STRTYPE</Abbreviation> <!-- required -->
                                        <ConversionRatio >PRICETYPE</ConversionRatio> <!-- required -->
                                </RelatedUnit>
                                <DefaultUnit> <!-- optional, may repeat -->
                                        <!-- UnitUsedFor may have one of the following values: Purchase, Sales, Shipping -->
                                        <UnitUsedFor >ENUMTYPE</UnitUsedFor> <!-- required -->
                                        <Unit >STRTYPE</Unit> <!-- required -->
                                </DefaultUnit>
                        </UnitOfMeasureSetRet>
                </UnitOfMeasureSetQueryRs>
        </QBXMLMsgsRq>
</QBXML>
```
## VehicleMileageQuery
VehicleQuery is a transaction query that returns vehicle mileage transaction data for all vehicle mileage transactions that match the provided filter criteria. You can query by transaction ID, or by transaction date, or by date modified.

Note: If you use VehicleMileageQuery for app integration with Track Vehicle Mileage in QuickBooks Desktop, ask the customer to open Track Vehicle Mileage for the correct IRS rates. This change is applicable for QuickBooks Desktop 2023 and above.
### XMLOps
```
<?xml version="1.0" encoding="utf-8"?>
<?qbxml version="16.0"?>
<QBXML>
        <QBXMLMsgsRq onError="stopOnError">
                <VehicleMileageQueryRq metaData="ENUMTYPE" iterator="ENUMTYPE" iteratorID="UUIDTYPE">
                        <!-- BEGIN OR -->
                                <TxnID >IDTYPE</TxnID> <!-- optional, may repeat -->
                        <!-- OR -->
                                <MaxReturned >INTTYPE</MaxReturned> <!-- optional -->
                                <!-- BEGIN OR -->
                                        <ModifiedDateRangeFilter> <!-- optional -->
                                                <FromModifiedDate >DATETIMETYPE</FromModifiedDate> <!-- optional -->
                                                <ToModifiedDate >DATETIMETYPE</ToModifiedDate> <!-- optional -->
                                        </ModifiedDateRangeFilter>
                                <!-- OR -->
                                        <TxnDateRangeFilter> <!-- optional -->
                                                <!-- BEGIN OR -->
                                                        <FromTxnDate >DATETYPE</FromTxnDate> <!-- optional -->
                                                        <ToTxnDate >DATETYPE</ToTxnDate> <!-- optional -->
                                                <!-- OR -->
                                                        <!-- DateMacro may have one of the following values: All, Today, ThisWeek, ThisWeekToDate, ThisMonth, ThisMonthToDate, ThisCalendarQuarter, ThisCalendarQuarterToDate, ThisFiscalQuarter, ThisFiscalQuarterToDate, ThisCalendarYear, ThisCalendarYearToDate, ThisFiscalYear, ThisFiscalYearToDate, Yesterday, LastWeek, LastWeekToDate, LastMonth, LastMonthToDate, LastCalendarQuarter, LastCalendarQuarterToDate, LastFiscalQuarter, LastFiscalQuarterToDate, LastCalendarYear, LastCalendarYearToDate, LastFiscalYear, LastFiscalYearToDate, NextWeek, NextFourWeeks, NextMonth, NextCalendarQuarter, NextCalendarYear, NextFiscalQuarter, NextFiscalYear -->
                                                        <DateMacro >ENUMTYPE</DateMacro> <!-- optional -->
                                                <!-- END OR -->
                                        </TxnDateRangeFilter>
                                <!-- END OR -->
                        <!-- END OR -->
                        <IncludeRetElement >STRTYPE</IncludeRetElement> <!-- optional, may repeat -->
                </VehicleMileageQueryRq>

                <VehicleMileageQueryRs statusCode="INTTYPE" statusSeverity="STRTYPE" statusMessage="STRTYPE" retCount="INTTYPE" iteratorRemainingCount="INTTYPE" iteratorID="UUIDTYPE">
                        <VehicleMileageRet> <!-- optional, may repeat -->
                                <TxnID >IDTYPE</TxnID> <!-- optional -->
                                <TimeCreated >DATETIMETYPE</TimeCreated> <!-- optional -->
                                <TimeModified >DATETIMETYPE</TimeModified> <!-- optional -->
                                <EditSequence >STRTYPE</EditSequence> <!-- optional -->
                                <VehicleRef> <!-- optional -->
                                        <ListID >IDTYPE</ListID> <!-- optional -->
                                        <FullName >STRTYPE</FullName> <!-- optional -->
                                </VehicleRef>
                                <CustomerRef> <!-- optional -->
                                        <ListID >IDTYPE</ListID> <!-- optional -->
                                        <FullName >STRTYPE</FullName> <!-- optional -->
                                </CustomerRef>
                                <ItemRef> <!-- optional -->
                                        <ListID >IDTYPE</ListID> <!-- optional -->
                                        <FullName >STRTYPE</FullName> <!-- optional -->
                                </ItemRef>
                                <ClassRef> <!-- optional -->
                                        <ListID >IDTYPE</ListID> <!-- optional -->
                                        <FullName >STRTYPE</FullName> <!-- optional -->
                                </ClassRef>
                                <TripStartDate >DATETYPE</TripStartDate> <!-- optional -->
                                <TripEndDate >DATETYPE</TripEndDate> <!-- optional -->
                                <OdometerStart >QUANTYPE</OdometerStart> <!-- optional -->
                                <OdometerEnd >QUANTYPE</OdometerEnd> <!-- optional -->
                                <TotalMiles >QUANTYPE</TotalMiles> <!-- optional -->
                                <Notes >STRTYPE</Notes> <!-- optional -->
                                <!-- BillableStatus may have one of the following values: Billable, NotBillable, HasBeenBilled -->
                                <BillableStatus >ENUMTYPE</BillableStatus> <!-- optional -->
                                <StandardMileageRate >PERCENTTYPE</StandardMileageRate> <!-- optional -->
                                <StandardMileageTotalAmount >AMTTYPE</StandardMileageTotalAmount> <!-- optional -->
                                <BillableRate >PRICETYPE</BillableRate> <!-- optional -->
                                <BillableAmount >AMTTYPE</BillableAmount> <!-- optional -->
                        </VehicleMileageRet>
                </VehicleMileageQueryRs>
        </QBXMLMsgsRq>
</QBXML>
```
## VehicleQuery
### XMLOps
```
<?xml version="1.0" encoding="utf-8"?>
<?qbxml version="16.0"?>
<QBXML>
        <QBXMLMsgsRq onError="stopOnError">
                <VehicleQueryRq metaData="ENUMTYPE">
                        <!-- BEGIN OR -->
                                <ListID >IDTYPE</ListID> <!-- optional, may repeat -->
                        <!-- OR -->
                                <FullName >STRTYPE</FullName> <!-- optional, may repeat -->
                        <!-- OR -->
                                <MaxReturned >INTTYPE</MaxReturned> <!-- optional -->
                                <!-- ActiveStatus may have one of the following values: ActiveOnly [DEFAULT], InactiveOnly, All -->
                                <ActiveStatus >ENUMTYPE</ActiveStatus> <!-- optional -->
                                <FromModifiedDate >DATETIMETYPE</FromModifiedDate> <!-- optional -->
                                <ToModifiedDate >DATETIMETYPE</ToModifiedDate> <!-- optional -->
                                <!-- BEGIN OR -->
                                        <NameFilter> <!-- optional -->
                                                <!-- MatchCriterion may have one of the following values: StartsWith, Contains, EndsWith -->
                                                <MatchCriterion >ENUMTYPE</MatchCriterion> <!-- required -->
                                                <Name >STRTYPE</Name> <!-- required -->
                                        </NameFilter>
                                <!-- OR -->
                                        <NameRangeFilter> <!-- optional -->
                                                <FromName >STRTYPE</FromName> <!-- optional -->
                                                <ToName >STRTYPE</ToName> <!-- optional -->
                                        </NameRangeFilter>
                                <!-- END OR -->
                        <!-- END OR -->
                        <IncludeRetElement >STRTYPE</IncludeRetElement> <!-- optional, may repeat -->
                </VehicleQueryRq>

                <VehicleQueryRs statusCode="INTTYPE" statusSeverity="STRTYPE" statusMessage="STRTYPE" retCount="INTTYPE">
                        <VehicleRet> <!-- optional, may repeat -->
                                <ListID >IDTYPE</ListID> <!-- optional -->
                                <TimeCreated >DATETIMETYPE</TimeCreated> <!-- optional -->
                                <TimeModified >DATETIMETYPE</TimeModified> <!-- optional -->
                                <EditSequence >STRTYPE</EditSequence> <!-- optional -->
                                <Name >STRTYPE</Name> <!-- optional -->
                                <IsActive >BOOLTYPE</IsActive> <!-- optional -->
                                <Desc >STRTYPE</Desc> <!-- optional -->
                        </VehicleRet>
                </VehicleQueryRs>
        </QBXMLMsgsRq>
</QBXML>
```
## VendorCreditQuery
### XMLOps
```
<?xml version="1.0" encoding="utf-8"?>
<?qbxml version="16.0"?>
<QBXML>
        <QBXMLMsgsRq onError="stopOnError">
                <VendorCreditQueryRq metaData="ENUMTYPE" iterator="ENUMTYPE" iteratorID="UUIDTYPE">
                        <!-- BEGIN OR -->
                                <TxnID >IDTYPE</TxnID> <!-- optional, may repeat -->
                        <!-- OR -->
                                <RefNumber >STRTYPE</RefNumber> <!-- optional, may repeat -->
                        <!-- OR -->
                                <RefNumberCaseSensitive >STRTYPE</RefNumberCaseSensitive> <!-- optional, may repeat -->
                        <!-- OR -->
                                <MaxReturned >INTTYPE</MaxReturned> <!-- optional -->
                                <!-- BEGIN OR -->
                                        <ModifiedDateRangeFilter> <!-- optional -->
                                                <FromModifiedDate >DATETIMETYPE</FromModifiedDate> <!-- optional -->
                                                <ToModifiedDate >DATETIMETYPE</ToModifiedDate> <!-- optional -->
                                        </ModifiedDateRangeFilter>
                                <!-- OR -->
                                        <TxnDateRangeFilter> <!-- optional -->
                                                <!-- BEGIN OR -->
                                                        <FromTxnDate >DATETYPE</FromTxnDate> <!-- optional -->
                                                        <ToTxnDate >DATETYPE</ToTxnDate> <!-- optional -->
                                                <!-- OR -->
                                                        <!-- DateMacro may have one of the following values: All, Today, ThisWeek, ThisWeekToDate, ThisMonth, ThisMonthToDate, ThisCalendarQuarter, ThisCalendarQuarterToDate, ThisFiscalQuarter, ThisFiscalQuarterToDate, ThisCalendarYear, ThisCalendarYearToDate, ThisFiscalYear, ThisFiscalYearToDate, Yesterday, LastWeek, LastWeekToDate, LastMonth, LastMonthToDate, LastCalendarQuarter, LastCalendarQuarterToDate, LastFiscalQuarter, LastFiscalQuarterToDate, LastCalendarYear, LastCalendarYearToDate, LastFiscalYear, LastFiscalYearToDate, NextWeek, NextFourWeeks, NextMonth, NextCalendarQuarter, NextCalendarYear, NextFiscalQuarter, NextFiscalYear -->
                                                        <DateMacro >ENUMTYPE</DateMacro> <!-- optional -->
                                                <!-- END OR -->
                                        </TxnDateRangeFilter>
                                <!-- END OR -->
                                <EntityFilter> <!-- optional -->
                                        <!-- BEGIN OR -->
                                                <ListID >IDTYPE</ListID> <!-- optional, may repeat -->
                                        <!-- OR -->
                                                <FullName >STRTYPE</FullName> <!-- optional, may repeat -->
                                        <!-- OR -->
                                                <ListIDWithChildren >IDTYPE</ListIDWithChildren> <!-- optional -->
                                        <!-- OR -->
                                                <FullNameWithChildren >STRTYPE</FullNameWithChildren> <!-- optional -->
                                        <!-- END OR -->
                                </EntityFilter>
                                <AccountFilter> <!-- optional -->
                                        <!-- BEGIN OR -->
                                                <ListID >IDTYPE</ListID> <!-- optional, may repeat -->
                                        <!-- OR -->
                                                <FullName >STRTYPE</FullName> <!-- optional, may repeat -->
                                        <!-- OR -->
                                                <ListIDWithChildren >IDTYPE</ListIDWithChildren> <!-- optional -->
                                        <!-- OR -->
                                                <FullNameWithChildren >STRTYPE</FullNameWithChildren> <!-- optional -->
                                        <!-- END OR -->
                                </AccountFilter>
                                <!-- BEGIN OR -->
                                        <RefNumberFilter> <!-- optional -->
                                                <!-- MatchCriterion may have one of the following values: StartsWith, Contains, EndsWith -->
                                                <MatchCriterion >ENUMTYPE</MatchCriterion> <!-- required -->
                                                <RefNumber >STRTYPE</RefNumber> <!-- required -->
                                        </RefNumberFilter>
                                <!-- OR -->
                                        <RefNumberRangeFilter> <!-- optional -->
                                                <FromRefNumber >STRTYPE</FromRefNumber> <!-- optional -->
                                                <ToRefNumber >STRTYPE</ToRefNumber> <!-- optional -->
                                        </RefNumberRangeFilter>
                                <!-- END OR -->
                                <CurrencyFilter> <!-- optional -->
                                        <!-- BEGIN OR -->
                                                <ListID >IDTYPE</ListID> <!-- optional, may repeat -->
                                        <!-- OR -->
                                                <FullName >STRTYPE</FullName> <!-- optional, may repeat -->
                                        <!-- END OR -->
                                </CurrencyFilter>
                        <!-- END OR -->
                        <IncludeLineItems >BOOLTYPE</IncludeLineItems> <!-- optional -->
                        <IncludeLinkedTxns >BOOLTYPE</IncludeLinkedTxns> <!-- optional -->
                        <IncludeRetElement >STRTYPE</IncludeRetElement> <!-- optional, may repeat -->
                        <OwnerID >GUIDTYPE</OwnerID> <!-- optional, may repeat -->
                </VendorCreditQueryRq>

                <VendorCreditQueryRs statusCode="INTTYPE" statusSeverity="STRTYPE" statusMessage="STRTYPE" retCount="INTTYPE" iteratorRemainingCount="INTTYPE" iteratorID="UUIDTYPE">
                        <VendorCreditRet> <!-- optional, may repeat -->
                                <TxnID >IDTYPE</TxnID> <!-- required -->
                                <TimeCreated >DATETIMETYPE</TimeCreated> <!-- required -->
                                <TimeModified >DATETIMETYPE</TimeModified> <!-- required -->
                                <EditSequence >STRTYPE</EditSequence> <!-- required -->
                                <TxnNumber >INTTYPE</TxnNumber> <!-- optional -->
                                <VendorRef> <!-- required -->
                                        <ListID >IDTYPE</ListID> <!-- optional -->
                                        <FullName >STRTYPE</FullName> <!-- optional -->
                                </VendorRef>
                                <APAccountRef> <!-- optional -->
                                        <ListID >IDTYPE</ListID> <!-- optional -->
                                        <FullName >STRTYPE</FullName> <!-- optional -->
                                </APAccountRef>
                                <TxnDate >DATETYPE</TxnDate> <!-- required -->
                                <CreditAmount >AMTTYPE</CreditAmount> <!-- required -->
                                <CurrencyRef> <!-- optional -->
                                        <ListID >IDTYPE</ListID> <!-- optional -->
                                        <FullName >STRTYPE</FullName> <!-- optional -->
                                </CurrencyRef>
                                <ExchangeRate >FLOATTYPE</ExchangeRate> <!-- optional -->
                                <CreditAmountInHomeCurrency >AMTTYPE</CreditAmountInHomeCurrency> <!-- optional -->
                                <RefNumber >STRTYPE</RefNumber> <!-- optional -->
                                <Memo >STRTYPE</Memo> <!-- optional -->
                                <IsTaxIncluded >BOOLTYPE</IsTaxIncluded> <!-- optional -->
                                <SalesTaxCodeRef> <!-- optional -->
                                        <ListID >IDTYPE</ListID> <!-- optional -->
                                        <FullName >STRTYPE</FullName> <!-- optional -->
                                </SalesTaxCodeRef>
                                <ExternalGUID >GUIDTYPE</ExternalGUID> <!-- optional -->
                                <LinkedTxn> <!-- optional, may repeat -->
                                        <TxnID >IDTYPE</TxnID> <!-- required -->
                                        <!-- TxnType may have one of the following values: ARRefundCreditCard, Bill, BillPaymentCheck, BillPaymentCreditCard, BuildAssembly, Charge, Check, CreditCardCharge, CreditCardCredit, CreditMemo, Deposit, Estimate, InventoryAdjustment, Invoice, ItemReceipt, JournalEntry, LiabilityAdjustment, Paycheck, PayrollLiabilityCheck, PurchaseOrder, ReceivePayment, SalesOrder, SalesReceipt, SalesTaxPaymentCheck, Transfer, VendorCredit, YTDAdjustment -->
                                        <TxnType >ENUMTYPE</TxnType> <!-- required -->
                                        <TxnDate >DATETYPE</TxnDate> <!-- required -->
                                        <RefNumber >STRTYPE</RefNumber> <!-- optional -->
                                        <!-- LinkType may have one of the following values: AMTTYPE, QUANTYPE -->
                                        <LinkType >ENUMTYPE</LinkType> <!-- optional -->
                                        <Amount >AMTTYPE</Amount> <!-- required -->
                                </LinkedTxn>
                                <ExpenseLineRet> <!-- optional, may repeat -->
                                        <TxnLineID >IDTYPE</TxnLineID> <!-- required -->
                                        <AccountRef> <!-- optional -->
                                                <ListID >IDTYPE</ListID> <!-- optional -->
                                                <FullName >STRTYPE</FullName> <!-- optional -->
                                        </AccountRef>
                                        <Amount >AMTTYPE</Amount> <!-- optional -->
                                        <Memo >STRTYPE</Memo> <!-- optional -->
                                        <CustomerRef> <!-- optional -->
                                                <ListID >IDTYPE</ListID> <!-- optional -->
                                                <FullName >STRTYPE</FullName> <!-- optional -->
                                        </CustomerRef>
                                        <ClassRef> <!-- optional -->
                                                <ListID >IDTYPE</ListID> <!-- optional -->
                                                <FullName >STRTYPE</FullName> <!-- optional -->
                                        </ClassRef>
                                        <SalesTaxCodeRef> <!-- optional -->
                                                <ListID >IDTYPE</ListID> <!-- optional -->
                                                <FullName >STRTYPE</FullName> <!-- optional -->
                                        </SalesTaxCodeRef>
                                        <!-- BillableStatus may have one of the following values: Billable, NotBillable, HasBeenBilled -->
                                        <BillableStatus >ENUMTYPE</BillableStatus> <!-- optional -->
                                        <SalesRepRef> <!-- optional -->
                                                <ListID >IDTYPE</ListID> <!-- optional -->
                                                <FullName >STRTYPE</FullName> <!-- optional -->
                                        </SalesRepRef>
                                        <DataExtRet> <!-- optional, may repeat -->
                                                <OwnerID >GUIDTYPE</OwnerID> <!-- optional -->
                                                <DataExtName >STRTYPE</DataExtName> <!-- required -->
                                                <!-- DataExtType may have one of the following values: AMTTYPE, DATETIMETYPE, INTTYPE, PERCENTTYPE, PRICETYPE, QUANTYPE, STR1024TYPE, STR255TYPE -->
                                                <DataExtType >ENUMTYPE</DataExtType> <!-- required -->
                                                <DataExtValue >STRTYPE</DataExtValue> <!-- required -->
                                        </DataExtRet>
                                </ExpenseLineRet>
                                <!-- BEGIN OR -->
                                        <ItemLineRet> <!-- optional -->
                                                <TxnLineID >IDTYPE</TxnLineID> <!-- required -->
                                                <ItemRef> <!-- optional -->
                                                        <ListID >IDTYPE</ListID> <!-- optional -->
                                                        <FullName >STRTYPE</FullName> <!-- optional -->
                                                </ItemRef>
                                                <InventorySiteRef> <!-- optional -->
                                                        <ListID >IDTYPE</ListID> <!-- optional -->
                                                        <FullName >STRTYPE</FullName> <!-- optional -->
                                                </InventorySiteRef>
                                                <InventorySiteLocationRef> <!-- optional -->
                                                        <ListID >IDTYPE</ListID> <!-- optional -->
                                                        <FullName >STRTYPE</FullName> <!-- optional -->
                                                </InventorySiteLocationRef>
                                                <!-- BEGIN OR -->
                                                        <SerialNumber >STRTYPE</SerialNumber> <!-- optional -->
                                                <!-- OR -->
                                                        <LotNumber >STRTYPE</LotNumber> <!-- optional -->
                                                <!-- END OR -->
                                                <ExpirationDateForSerialLotNumber>STRTYPE</ExpirationDateForSerialLotNumber> <!-- optional -->
                                                <Desc >STRTYPE</Desc> <!-- optional -->
                                                <Quantity >QUANTYPE</Quantity> <!-- optional -->
                                                <UnitOfMeasure >STRTYPE</UnitOfMeasure> <!-- optional -->
                                                <OverrideUOMSetRef> <!-- optional -->
                                                        <ListID >IDTYPE</ListID> <!-- optional -->
                                                        <FullName >STRTYPE</FullName> <!-- optional -->
                                                </OverrideUOMSetRef>
                                                <Cost >PRICETYPE</Cost> <!-- optional -->
                                                <Amount >AMTTYPE</Amount> <!-- optional -->
                                                <CustomerRef> <!-- optional -->
                                                        <ListID >IDTYPE</ListID> <!-- optional -->
                                                        <FullName >STRTYPE</FullName> <!-- optional -->
                                                </CustomerRef>
                                                <ClassRef> <!-- optional -->
                                                        <ListID >IDTYPE</ListID> <!-- optional -->
                                                        <FullName >STRTYPE</FullName> <!-- optional -->
                                                </ClassRef>
                                                <SalesTaxCodeRef> <!-- optional -->
                                                        <ListID >IDTYPE</ListID> <!-- optional -->
                                                        <FullName >STRTYPE</FullName> <!-- optional -->
                                                </SalesTaxCodeRef>
                                                <!-- BillableStatus may have one of the following values: Billable, NotBillable, HasBeenBilled -->
                                                <BillableStatus >ENUMTYPE</BillableStatus> <!-- optional -->
                                                <SalesRepRef> <!-- optional -->
                                                        <ListID >IDTYPE</ListID> <!-- optional -->
                                                        <FullName >STRTYPE</FullName> <!-- optional -->
                                                </SalesRepRef>
                                                <DataExtRet> <!-- optional, may repeat -->
                                                        <OwnerID >GUIDTYPE</OwnerID> <!-- optional -->
                                                        <DataExtName >STRTYPE</DataExtName> <!-- required -->
                                                        <!-- DataExtType may have one of the following values: AMTTYPE, DATETIMETYPE, INTTYPE, PERCENTTYPE, PRICETYPE, QUANTYPE, STR1024TYPE, STR255TYPE -->
                                                        <DataExtType >ENUMTYPE</DataExtType> <!-- required -->
                                                        <DataExtValue >STRTYPE</DataExtValue> <!-- required -->
                                                </DataExtRet>
                                        </ItemLineRet>
                                <!-- OR -->
                                        <ItemGroupLineRet> <!-- optional -->
                                                <TxnLineID >IDTYPE</TxnLineID> <!-- required -->
                                                <ItemGroupRef> <!-- required -->
                                                        <ListID >IDTYPE</ListID> <!-- optional -->
                                                        <FullName >STRTYPE</FullName> <!-- optional -->
                                                </ItemGroupRef>
                                                <Desc >STRTYPE</Desc> <!-- optional -->
                                                <Quantity >QUANTYPE</Quantity> <!-- optional -->
                                                <UnitOfMeasure >STRTYPE</UnitOfMeasure> <!-- optional -->
                                                <OverrideUOMSetRef> <!-- optional -->
                                                        <ListID >IDTYPE</ListID> <!-- optional -->
                                                        <FullName >STRTYPE</FullName> <!-- optional -->
                                                </OverrideUOMSetRef>
                                                <TotalAmount >AMTTYPE</TotalAmount> <!-- required -->
                                                <ItemLineRet> <!-- optional, may repeat -->
                                                        <TxnLineID >IDTYPE</TxnLineID> <!-- required -->
                                                        <ItemRef> <!-- optional -->
                                                                <ListID >IDTYPE</ListID> <!-- optional -->
                                                                <FullName >STRTYPE</FullName> <!-- optional -->
                                                        </ItemRef>
                                                        <InventorySiteRef> <!-- optional -->
                                                                <ListID >IDTYPE</ListID> <!-- optional -->
                                                                <FullName >STRTYPE</FullName> <!-- optional -->
                                                        </InventorySiteRef>
                                                        <InventorySiteLocationRef> <!-- optional -->
                                                                <ListID >IDTYPE</ListID> <!-- optional -->
                                                                <FullName >STRTYPE</FullName> <!-- optional -->
                                                        </InventorySiteLocationRef>
                                                        <!-- BEGIN OR -->
                                                                <SerialNumber >STRTYPE</SerialNumber> <!-- optional -->
                                                        <!-- OR -->
                                                                <LotNumber >STRTYPE</LotNumber> <!-- optional -->
                                                        <!-- END OR -->
                                                        <ExpirationDateForSerialLotNumber>STRTYPE</ExpirationDateForSerialLotNumber> <!-- optional -->
                                                        <Desc >STRTYPE</Desc> <!-- optional -->
                                                        <Quantity >QUANTYPE</Quantity> <!-- optional -->
                                                        <UnitOfMeasure >STRTYPE</UnitOfMeasure> <!-- optional -->
                                                        <OverrideUOMSetRef> <!-- optional -->
                                                                <ListID >IDTYPE</ListID> <!-- optional -->
                                                                <FullName >STRTYPE</FullName> <!-- optional -->
                                                        </OverrideUOMSetRef>
                                                        <Cost >PRICETYPE</Cost> <!-- optional -->
                                                        <Amount >AMTTYPE</Amount> <!-- optional -->
                                                        <CustomerRef> <!-- optional -->
                                                                <ListID >IDTYPE</ListID> <!-- optional -->
                                                                <FullName >STRTYPE</FullName> <!-- optional -->
                                                        </CustomerRef>
                                                        <ClassRef> <!-- optional -->
                                                                <ListID >IDTYPE</ListID> <!-- optional -->
                                                                <FullName >STRTYPE</FullName> <!-- optional -->
                                                        </ClassRef>
                                                        <SalesTaxCodeRef> <!-- optional -->
                                                                <ListID >IDTYPE</ListID> <!-- optional -->
                                                                <FullName >STRTYPE</FullName> <!-- optional -->
                                                        </SalesTaxCodeRef>
                                                        <!-- BillableStatus may have one of the following values: Billable, NotBillable, HasBeenBilled -->
                                                        <BillableStatus >ENUMTYPE</BillableStatus> <!-- optional -->
                                                        <SalesRepRef> <!-- optional -->
                                                                <ListID >IDTYPE</ListID> <!-- optional -->
                                                                <FullName >STRTYPE</FullName> <!-- optional -->
                                                        </SalesRepRef>
                                                        <DataExtRet> <!-- optional, may repeat -->
                                                                <OwnerID >GUIDTYPE</OwnerID> <!-- optional -->
                                                                <DataExtName >STRTYPE</DataExtName> <!-- required -->
                                                                <!-- DataExtType may have one of the following values: AMTTYPE, DATETIMETYPE, INTTYPE, PERCENTTYPE, PRICETYPE, QUANTYPE, STR1024TYPE, STR255TYPE -->
                                                                <DataExtType >ENUMTYPE</DataExtType> <!-- required -->
                                                                <DataExtValue >STRTYPE</DataExtValue> <!-- required -->
                                                        </DataExtRet>
                                                </ItemLineRet>
                                                <DataExt> <!-- optional, may repeat -->
                                                        <OwnerID >GUIDTYPE</OwnerID> <!-- required -->
                                                        <DataExtName >STRTYPE</DataExtName> <!-- required -->
                                                        <DataExtValue >STRTYPE</DataExtValue> <!-- required -->
                                                </DataExt>
                                        </ItemGroupLineRet>
                                <!-- END OR -->
                                <OpenAmount >AMTTYPE</OpenAmount> <!-- optional -->
                                <DataExtRet> <!-- optional, may repeat -->
                                        <OwnerID >GUIDTYPE</OwnerID> <!-- optional -->
                                        <DataExtName >STRTYPE</DataExtName> <!-- required -->
                                        <!-- DataExtType may have one of the following values: AMTTYPE, DATETIMETYPE, INTTYPE, PERCENTTYPE, PRICETYPE, QUANTYPE, STR1024TYPE, STR255TYPE -->
                                        <DataExtType >ENUMTYPE</DataExtType> <!-- required -->
                                        <DataExtValue >STRTYPE</DataExtValue> <!-- required -->
                                </DataExtRet>
                        </VendorCreditRet>
                </VendorCreditQueryRs>
        </QBXMLMsgsRq>
</QBXML>
```
## VendorQuery
### XMLOps
```
<?xml version="1.0" encoding="utf-8"?>
<?qbxml version="16.0"?>
<QBXML>
        <QBXMLMsgsRq onError="stopOnError">
                <VendorQueryRq metaData="ENUMTYPE" iterator="ENUMTYPE" iteratorID="UUIDTYPE">
                        <!-- BEGIN OR -->
                                <ListID >IDTYPE</ListID> <!-- optional, may repeat -->
                        <!-- OR -->
                                <FullName >STRTYPE</FullName> <!-- optional, may repeat -->
                        <!-- OR -->
                                <MaxReturned >INTTYPE</MaxReturned> <!-- optional -->
                                <!-- ActiveStatus may have one of the following values: ActiveOnly [DEFAULT], InactiveOnly, All -->
                                <ActiveStatus >ENUMTYPE</ActiveStatus> <!-- optional -->
                                <FromModifiedDate >DATETIMETYPE</FromModifiedDate> <!-- optional -->
                                <ToModifiedDate >DATETIMETYPE</ToModifiedDate> <!-- optional -->
                                <!-- BEGIN OR -->
                                        <NameFilter> <!-- optional -->
                                                <!-- MatchCriterion may have one of the following values: StartsWith, Contains, EndsWith -->
                                                <MatchCriterion >ENUMTYPE</MatchCriterion> <!-- required -->
                                                <Name >STRTYPE</Name> <!-- required -->
                                        </NameFilter>
                                <!-- OR -->
                                        <NameRangeFilter> <!-- optional -->
                                                <FromName >STRTYPE</FromName> <!-- optional -->
                                                <ToName >STRTYPE</ToName> <!-- optional -->
                                        </NameRangeFilter>
                                <!-- END OR -->
                                <TotalBalanceFilter> <!-- optional -->
                                        <!-- Operator may have one of the following values: LessThan, LessThanEqual, Equal, GreaterThan, GreaterThanEqual -->
                                        <Operator >ENUMTYPE</Operator> <!-- required -->
                                        <Amount >AMTTYPE</Amount> <!-- required -->
                                </TotalBalanceFilter>
                                <CurrencyFilter> <!-- optional -->
                                        <!-- BEGIN OR -->
                                                <ListID >IDTYPE</ListID> <!-- optional, may repeat -->
                                        <!-- OR -->
                                                <FullName >STRTYPE</FullName> <!-- optional, may repeat -->
                                        <!-- END OR -->
                                </CurrencyFilter>
                                <ClassFilter> <!-- optional -->
                                        <!-- BEGIN OR -->
                                                <ListID >IDTYPE</ListID> <!-- optional, may repeat -->
                                        <!-- OR -->
                                                <FullName >STRTYPE</FullName> <!-- optional, may repeat -->
                                        <!-- OR -->
                                                <ListIDWithChildren >IDTYPE</ListIDWithChildren> <!-- optional -->
                                        <!-- OR -->
                                                <FullNameWithChildren >STRTYPE</FullNameWithChildren> <!-- optional -->
                                        <!-- END OR -->
                                </ClassFilter>
                        <!-- END OR -->
                        <IncludeRetElement >STRTYPE</IncludeRetElement> <!-- optional, may repeat -->
                        <OwnerID >GUIDTYPE</OwnerID> <!-- optional, may repeat -->
                </VendorQueryRq>

                <VendorQueryRs statusCode="INTTYPE" statusSeverity="STRTYPE" statusMessage="STRTYPE" retCount="INTTYPE" iteratorRemainingCount="INTTYPE" iteratorID="UUIDTYPE">
                        <VendorRet> <!-- optional, may repeat -->
                                <ListID >IDTYPE</ListID> <!-- required -->
                                <TimeCreated >DATETIMETYPE</TimeCreated> <!-- required -->
                                <TimeModified >DATETIMETYPE</TimeModified> <!-- required -->
                                <EditSequence >STRTYPE</EditSequence> <!-- required -->
                                <Name >STRTYPE</Name> <!-- required -->
                                <IsActive >BOOLTYPE</IsActive> <!-- optional -->
                                <ClassRef> <!-- optional -->
                                        <ListID >IDTYPE</ListID> <!-- optional -->
                                        <FullName >STRTYPE</FullName> <!-- optional -->
                                </ClassRef>
                                <IsTaxAgency >BOOLTYPE</IsTaxAgency> <!-- optional -->
                                <CompanyName >STRTYPE</CompanyName> <!-- optional -->
                                <Salutation >STRTYPE</Salutation> <!-- optional -->
                                <FirstName >STRTYPE</FirstName> <!-- optional -->
                                <MiddleName >STRTYPE</MiddleName> <!-- optional -->
                                <LastName >STRTYPE</LastName> <!-- optional -->
                                <JobTitle >STRTYPE</JobTitle> <!-- optional -->
                                <VendorAddress> <!-- optional -->
                                        <Addr1 >STRTYPE</Addr1> <!-- optional -->
                                        <Addr2 >STRTYPE</Addr2> <!-- optional -->
                                        <Addr3 >STRTYPE</Addr3> <!-- optional -->
                                        <Addr4 >STRTYPE</Addr4> <!-- optional -->
                                        <Addr5 >STRTYPE</Addr5> <!-- optional -->
                                        <City >STRTYPE</City> <!-- optional -->
                                        <State >STRTYPE</State> <!-- optional -->
                                        <PostalCode >STRTYPE</PostalCode> <!-- optional -->
                                        <Country >STRTYPE</Country> <!-- optional -->
                                        <Note >STRTYPE</Note> <!-- optional -->
                                </VendorAddress>
                                <VendorAddressBlock> <!-- optional -->
                                        <Addr1 >STRTYPE</Addr1> <!-- optional -->
                                        <Addr2 >STRTYPE</Addr2> <!-- optional -->
                                        <Addr3 >STRTYPE</Addr3> <!-- optional -->
                                        <Addr4 >STRTYPE</Addr4> <!-- optional -->
                                        <Addr5 >STRTYPE</Addr5> <!-- optional -->
                                </VendorAddressBlock>
                                <ShipAddress> <!-- optional -->
                                        <Addr1 >STRTYPE</Addr1> <!-- optional -->
                                        <Addr2 >STRTYPE</Addr2> <!-- optional -->
                                        <Addr3 >STRTYPE</Addr3> <!-- optional -->
                                        <Addr4 >STRTYPE</Addr4> <!-- optional -->
                                        <Addr5 >STRTYPE</Addr5> <!-- optional -->
                                        <City >STRTYPE</City> <!-- optional -->
                                        <State >STRTYPE</State> <!-- optional -->
                                        <PostalCode >STRTYPE</PostalCode> <!-- optional -->
                                        <Country >STRTYPE</Country> <!-- optional -->
                                        <Note >STRTYPE</Note> <!-- optional -->
                                </ShipAddress>
                                <Phone >STRTYPE</Phone> <!-- optional -->
                                <AltPhone >STRTYPE</AltPhone> <!-- optional -->
                                <Fax >STRTYPE</Fax> <!-- optional -->
                                <Email >STRTYPE</Email> <!-- optional -->
                                <Cc >STRTYPE</Cc> <!-- optional -->
                                <Contact >STRTYPE</Contact> <!-- optional -->
                                <AltContact >STRTYPE</AltContact> <!-- optional -->
                                <AdditionalContactRef> <!-- must occur 0 - 8 times -->
                                        <ContactName >STRTYPE</ContactName> <!-- required -->
                                        <ContactValue >STRTYPE</ContactValue> <!-- required -->
                                </AdditionalContactRef>
                                <ContactsRet> <!-- optional, may repeat -->
                                        <ListID >IDTYPE</ListID> <!-- required -->
                                        <TimeCreated >DATETIMETYPE</TimeCreated> <!-- required -->
                                        <TimeModified >DATETIMETYPE</TimeModified> <!-- required -->
                                        <EditSequence >STRTYPE</EditSequence> <!-- required -->
                                        <Contact >STRTYPE</Contact> <!-- optional -->
                                        <Salutation >STRTYPE</Salutation> <!-- optional -->
                                        <FirstName >STRTYPE</FirstName> <!-- required -->
                                        <MiddleName >STRTYPE</MiddleName> <!-- optional -->
                                        <LastName >STRTYPE</LastName> <!-- optional -->
                                        <JobTitle >STRTYPE</JobTitle> <!-- optional -->
                                        <AdditionalContactRef> <!-- must occur 0 - 5 times -->
                                                <ContactName >STRTYPE</ContactName> <!-- required -->
                                                <ContactValue >STRTYPE</ContactValue> <!-- required -->
                                        </AdditionalContactRef>
                                </ContactsRet>
                                <NameOnCheck >STRTYPE</NameOnCheck> <!-- optional -->
                                <AccountNumber >STRTYPE</AccountNumber> <!-- optional -->
                                <Notes >STRTYPE</Notes> <!-- optional -->
                                <AdditionalNotesRet> <!-- optional, may repeat -->
                                        <NoteID >INTTYPE</NoteID> <!-- required -->
                                        <Date >DATETYPE</Date> <!-- required -->
                                        <Note >STRTYPE</Note> <!-- required -->
                                </AdditionalNotesRet>
                                <VendorTypeRef> <!-- optional -->
                                        <ListID >IDTYPE</ListID> <!-- optional -->
                                        <FullName >STRTYPE</FullName> <!-- optional -->
                                </VendorTypeRef>
                                <TermsRef> <!-- optional -->
                                        <ListID >IDTYPE</ListID> <!-- optional -->
                                        <FullName >STRTYPE</FullName> <!-- optional -->
                                </TermsRef>
                                <CreditLimit >AMTTYPE</CreditLimit> <!-- optional -->
                                <VendorTaxIdent >STRTYPE</VendorTaxIdent> <!-- optional -->
                                <IsVendorEligibleFor1099 >BOOLTYPE</IsVendorEligibleFor1099> <!-- optional -->
                                <Balance >AMTTYPE</Balance> <!-- optional -->
                                <BillingRateRef> <!-- optional -->
                                        <ListID >IDTYPE</ListID> <!-- optional -->
                                        <FullName >STRTYPE</FullName> <!-- optional -->
                                </BillingRateRef>
                                <ExternalGUID >GUIDTYPE</ExternalGUID> <!-- optional -->
                                <SalesTaxCodeRef> <!-- optional -->
                                        <ListID >IDTYPE</ListID> <!-- optional -->
                                        <FullName >STRTYPE</FullName> <!-- optional -->
                                </SalesTaxCodeRef>
                                <!-- SalesTaxCountry may have one of the following values: Australia, Canada [DEFAULT], UK, US -->
                                <SalesTaxCountry >ENUMTYPE</SalesTaxCountry> <!-- optional -->
                                <IsSalesTaxAgency >BOOLTYPE</IsSalesTaxAgency> <!-- optional -->
                                <SalesTaxReturnRef> <!-- optional -->
                                        <ListID >IDTYPE</ListID> <!-- optional -->
                                        <FullName >STRTYPE</FullName> <!-- optional -->
                                </SalesTaxReturnRef>
                                <TaxRegistrationNumber >STRTYPE</TaxRegistrationNumber> <!-- optional -->
                                <!-- ReportingPeriod may have one of the following values: Monthly, Quarterly [DEFAULT] -->
                                <ReportingPeriod >ENUMTYPE</ReportingPeriod> <!-- optional -->
                                <IsTaxTrackedOnPurchases >BOOLTYPE</IsTaxTrackedOnPurchases> <!-- optional -->
                                <TaxOnPurchasesAccountRef> <!-- optional -->
                                        <ListID >IDTYPE</ListID> <!-- optional -->
                                        <FullName >STRTYPE</FullName> <!-- optional -->
                                </TaxOnPurchasesAccountRef>
                                <IsTaxTrackedOnSales >BOOLTYPE</IsTaxTrackedOnSales> <!-- optional -->
                                <TaxOnSalesAccountRef> <!-- optional -->
                                        <ListID >IDTYPE</ListID> <!-- optional -->
                                        <FullName >STRTYPE</FullName> <!-- optional -->
                                </TaxOnSalesAccountRef>
                                <IsTaxOnTax >BOOLTYPE</IsTaxOnTax> <!-- optional -->
                                <PrefillAccountRef> <!-- must occur 0 - 3 times -->
                                        <ListID >IDTYPE</ListID> <!-- optional -->
                                        <FullName >STRTYPE</FullName> <!-- optional -->
                                </PrefillAccountRef>
                                <CurrencyRef> <!-- optional -->
                                        <ListID >IDTYPE</ListID> <!-- optional -->
                                        <FullName >STRTYPE</FullName> <!-- optional -->
                                </CurrencyRef>
                                <DataExtRet> <!-- optional, may repeat -->
                                        <OwnerID >GUIDTYPE</OwnerID> <!-- optional -->
                                        <DataExtName >STRTYPE</DataExtName> <!-- required -->
                                        <!-- DataExtType may have one of the following values: AMTTYPE, DATETIMETYPE, INTTYPE, PERCENTTYPE, PRICETYPE, QUANTYPE, STR1024TYPE, STR255TYPE -->
                                        <DataExtType >ENUMTYPE</DataExtType> <!-- required -->
                                        <DataExtValue >STRTYPE</DataExtValue> <!-- required -->
                                </DataExtRet>
                        </VendorRet>
                </VendorQueryRs>
        </QBXMLMsgsRq>
</QBXML>
```
## VendorTypeQuery
### XMLOps
```
<?xml version="1.0" encoding="utf-8"?>
<?qbxml version="16.0"?>
<QBXML>
        <QBXMLMsgsRq onError="stopOnError">
                <VendorTypeQueryRq metaData="ENUMTYPE">
                        <!-- BEGIN OR -->
                                <ListID >IDTYPE</ListID> <!-- optional, may repeat -->
                        <!-- OR -->
                                <FullName >STRTYPE</FullName> <!-- optional, may repeat -->
                        <!-- OR -->
                                <MaxReturned >INTTYPE</MaxReturned> <!-- optional -->
                                <!-- ActiveStatus may have one of the following values: ActiveOnly [DEFAULT], InactiveOnly, All -->
                                <ActiveStatus >ENUMTYPE</ActiveStatus> <!-- optional -->
                                <FromModifiedDate >DATETIMETYPE</FromModifiedDate> <!-- optional -->
                                <ToModifiedDate >DATETIMETYPE</ToModifiedDate> <!-- optional -->
                                <!-- BEGIN OR -->
                                        <NameFilter> <!-- optional -->
                                                <!-- MatchCriterion may have one of the following values: StartsWith, Contains, EndsWith -->
                                                <MatchCriterion >ENUMTYPE</MatchCriterion> <!-- required -->
                                                <Name >STRTYPE</Name> <!-- required -->
                                        </NameFilter>
                                <!-- OR -->
                                        <NameRangeFilter> <!-- optional -->
                                                <FromName >STRTYPE</FromName> <!-- optional -->
                                                <ToName >STRTYPE</ToName> <!-- optional -->
                                        </NameRangeFilter>
                                <!-- END OR -->
                        <!-- END OR -->
                        <IncludeRetElement >STRTYPE</IncludeRetElement> <!-- optional, may repeat -->
                </VendorTypeQueryRq>

                <VendorTypeQueryRs statusCode="INTTYPE" statusSeverity="STRTYPE" statusMessage="STRTYPE" retCount="INTTYPE">
                        <VendorTypeRet> <!-- optional, may repeat -->
                                <ListID >IDTYPE</ListID> <!-- required -->
                                <TimeCreated >DATETIMETYPE</TimeCreated> <!-- required -->
                                <TimeModified >DATETIMETYPE</TimeModified> <!-- required -->
                                <EditSequence >STRTYPE</EditSequence> <!-- required -->
                                <Name >STRTYPE</Name> <!-- required -->
                                <FullName >STRTYPE</FullName> <!-- required -->
                                <IsActive >BOOLTYPE</IsActive> <!-- optional -->
                                <ParentRef> <!-- optional -->
                                        <ListID >IDTYPE</ListID> <!-- optional -->
                                        <FullName >STRTYPE</FullName> <!-- optional -->
                                </ParentRef>
                                <Sublevel >INTTYPE</Sublevel> <!-- required -->
                        </VendorTypeRet>
                </VendorTypeQueryRs>
        </QBXMLMsgsRq>
</QBXML>
```
## WorkersCompCodeQuery
Requires the company to be subscribed to Intuit Payroll service. Queries for the workers’ compensation codes specified in the query filter; you can filter by name, modified date, and effective date.
### XMLOps
```
<?xml version="1.0" encoding="utf-8"?>
<?qbxml version="16.0"?>
<QBXML>
        <QBXMLMsgsRq onError="stopOnError">
                <WorkersCompCodeQueryRq metaData="ENUMTYPE">
                        <!-- BEGIN OR -->
                                <ListID >IDTYPE</ListID> <!-- optional, may repeat -->
                        <!-- OR -->
                                <FullName >STRTYPE</FullName> <!-- optional, may repeat -->
                        <!-- OR -->
                                <MaxReturned >INTTYPE</MaxReturned> <!-- optional -->
                                <!-- ActiveStatus may have one of the following values: ActiveOnly [DEFAULT], InactiveOnly, All -->
                                <ActiveStatus >ENUMTYPE</ActiveStatus> <!-- optional -->
                                <FromModifiedDate >DATETIMETYPE</FromModifiedDate> <!-- optional -->
                                <ToModifiedDate >DATETIMETYPE</ToModifiedDate> <!-- optional -->
                                <!-- BEGIN OR -->
                                        <NameFilter> <!-- optional -->
                                                <!-- MatchCriterion may have one of the following values: StartsWith, Contains, EndsWith -->
                                                <MatchCriterion >ENUMTYPE</MatchCriterion> <!-- required -->
                                                <Name >STRTYPE</Name> <!-- required -->
                                        </NameFilter>
                                <!-- OR -->
                                        <NameRangeFilter> <!-- optional -->
                                                <FromName >STRTYPE</FromName> <!-- optional -->
                                                <ToName >STRTYPE</ToName> <!-- optional -->
                                        </NameRangeFilter>
                                <!-- END OR -->
                                <FromEffectiveDate >DATETYPE</FromEffectiveDate> <!-- optional -->
                                <ToEffectiveDate >DATETYPE</ToEffectiveDate> <!-- optional -->
                        <!-- END OR -->
                        <IncludeRetElement >STRTYPE</IncludeRetElement> <!-- optional, may repeat -->
                </WorkersCompCodeQueryRq>

                <WorkersCompCodeQueryRs statusCode="INTTYPE" statusSeverity="STRTYPE" statusMessage="STRTYPE" retCount="INTTYPE">
                        <WorkersCompCodeRet> <!-- optional, may repeat -->
                                <ListID >IDTYPE</ListID> <!-- optional -->
                                <TimeCreated >DATETIMETYPE</TimeCreated> <!-- optional -->
                                <TimeModified >DATETIMETYPE</TimeModified> <!-- optional -->
                                <EditSequence >STRTYPE</EditSequence> <!-- optional -->
                                <Name >STRTYPE</Name> <!-- optional -->
                                <IsActive >BOOLTYPE</IsActive> <!-- optional -->
                                <Desc >STRTYPE</Desc> <!-- optional -->
                                <CurrentRate >PRICETYPE</CurrentRate> <!-- optional -->
                                <CurrentEffectiveDate >DATETYPE</CurrentEffectiveDate> <!-- optional -->
                                <NextRate >PRICETYPE</NextRate> <!-- optional -->
                                <NextEffectiveDate >DATETYPE</NextEffectiveDate> <!-- optional -->
                                <RateHistory> <!-- optional, may repeat -->
                                        <Rate >PRICETYPE</Rate> <!-- required -->
                                        <EffectiveDate >DATETYPE</EffectiveDate> <!-- required -->
                                </RateHistory>
                        </WorkersCompCodeRet>
                </WorkersCompCodeQueryRs>
        </QBXMLMsgsRq>
</QBXML>
```
