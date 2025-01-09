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
