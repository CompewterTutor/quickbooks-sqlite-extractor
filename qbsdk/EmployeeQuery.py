from enum import Enum
from typing import List, Optional
from datetime import datetime
from lxml import etree
from sqlalchemy import create_engine, Column, String, DateTime, Boolean, Integer, Float
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker
from isodate import parse_duration

Base = declarative_base()

class MatchCriterion(Enum):
    STARTS_WITH = "StartsWith"
    CONTAINS = "Contains"
    ENDS_WITH = "EndsWith"

class ActiveStatus(Enum):
    ACTIVE_ONLY = "ActiveOnly"
    INACTIVE_ONLY = "InactiveOnly"
    ALL = "All"

class EmployeeQueryRq:
    def __init__(self, list_id: Optional[List[str]] = None, full_name: Optional[List[str]] = None, max_returned: Optional[int] = None,
                 active_status: Optional[ActiveStatus] = None, from_modified_date: Optional[datetime] = None, to_modified_date: Optional[datetime] = None,
                 name_filter: Optional[MatchCriterion] = None, name_range_filter: Optional[MatchCriterion] = None, include_ret_element: Optional[List[str]] = None,
                 owner_id: Optional[List[str]] = None):
        self.list_id = list_id
        self.full_name = full_name
        self.max_returned = max_returned
        self.active_status = active_status
        self.from_modified_date = from_modified_date
        self.to_modified_date = to_modified_date
        self.name_filter = name_filter
        self.name_range_filter = name_range_filter
        self.include_ret_element = include_ret_element
        self.owner_id = owner_id

    def to_xml(self) -> str:
        xml = f'''<?xml version="1.0" encoding="utf-8"?>
<?qbxml version="16.0"?>
<QBXML>
    <QBXMLMsgsRq onError="stopOnError">
        <EmployeeQueryRq>
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
                <MatchCriterion>{self.name_filter.value}</MatchCriterion>
                <Name>{self.name_filter}</Name>
            </NameFilter>
            '''
        if self.name_range_filter:
            xml += f'''
            <NameRangeFilter>
                <MatchCriterion>{self.name_range_filter.value}</MatchCriterion>
                <Name>{self.name_range_filter}</Name>
            </NameRangeFilter>
            '''
        if self.include_ret_element:
            for element in self.include_ret_element:
                xml += f'<IncludeRetElement>{element}</IncludeRetElement>'
        if self.owner_id:
            for owner_id in self.owner_id:
                xml += f'<OwnerID>{owner_id}</OwnerID>'
        xml += '''
        </EmployeeQueryRq>
    </QBXMLMsgsRq>
</QBXML>
        '''
        return xml

    def from_response_xml(self, response_xml: str):
        root = etree.fromstring(response_xml.encode('utf-8'))
        employee_rets = root.findall('.//EmployeeRet')
        self.employees = [EmployeeRet.from_xml(etree.tostring(employee_ret)) for employee_ret in employee_rets]
        self.employees = [employee for employee in self.employees if employee is not None]

class EmployeeRet(Base):
    __tablename__ = 'EmployeeRet'

    list_id = Column(String, primary_key=True)
    time_created = Column(DateTime)
    time_modified = Column(DateTime)
    edit_sequence = Column(String)
    name = Column(String)
    is_active = Column(Boolean, nullable=True)
    salutation = Column(String, nullable=True)
    first_name = Column(String, nullable=True)
    middle_name = Column(String, nullable=True)
    last_name = Column(String, nullable=True)
    job_title = Column(String, nullable=True)
    supervisor_list_id = Column(String, nullable=True)
    supervisor_full_name = Column(String, nullable=True)
    department = Column(String, nullable=True)
    description = Column(String, nullable=True)
    target_bonus = Column(Float, nullable=True)
    addr1 = Column(String, nullable=True)
    addr2 = Column(String, nullable=True)
    city = Column(String, nullable=True)
    state = Column(String, nullable=True)
    postal_code = Column(String, nullable=True)
    print_as = Column(String, nullable=True)
    phone = Column(String, nullable=True)
    mobile = Column(String, nullable=True)
    pager = Column(String, nullable=True)
    pager_pin = Column(String, nullable=True)
    alt_phone = Column(String, nullable=True)
    fax = Column(String, nullable=True)
    ssn = Column(String, nullable=True)
    email = Column(String, nullable=True)
    contact_name = Column(String, nullable=True)
    contact_value = Column(String, nullable=True)
    emergency_contact_name = Column(String, nullable=True)
    emergency_contact_value = Column(String, nullable=True)
    relation = Column(String, nullable=True)
    employee_type = Column(String, nullable=True)
    part_or_full_time = Column(String, nullable=True)
    exempt = Column(String, nullable=True)
    key_employee = Column(String, nullable=True)
    gender = Column(String, nullable=True)
    hired_date = Column(DateTime, nullable=True)
    original_hire_date = Column(DateTime, nullable=True)
    adjusted_service_date = Column(DateTime, nullable=True)
    released_date = Column(DateTime, nullable=True)
    birth_date = Column(DateTime, nullable=True)
    us_citizen = Column(String, nullable=True)
    ethnicity = Column(String, nullable=True)
    disabled = Column(String, nullable=True)
    disability_desc = Column(String, nullable=True)
    on_file = Column(String, nullable=True)
    work_auth_expire_date = Column(DateTime, nullable=True)
    us_veteran = Column(String, nullable=True)
    military_status = Column(String, nullable=True)
    account_number = Column(String, nullable=True)
    notes = Column(String, nullable=True)
    additional_notes = Column(String, nullable=True)
    billing_rate_list_id = Column(String, nullable=True)
    billing_rate_full_name = Column(String, nullable=True)
    pay_period = Column(String, nullable=True)
    class_list_id = Column(String, nullable=True)
    class_full_name = Column(String, nullable=True)
    clear_earnings = Column(Boolean, nullable=True)
    earnings_list_id = Column(String, nullable=True)
    earnings_full_name = Column(String, nullable=True)
    rate = Column(Float, nullable=True)
    rate_percent = Column(Float, nullable=True)
    is_using_time_data_to_create_paychecks = Column(Boolean, nullable=True)
    use_time_data_to_create_paychecks = Column(String, nullable=True)
    sick_hours_available = Column(Float, nullable=True)
    sick_hours_accrual_period = Column(String, nullable=True)
    sick_hours_accrued = Column(Float, nullable=True)
    sick_hours_maximum = Column(Float, nullable=True)
    is_resetting_hours_each_new_year = Column(Boolean, nullable=True)
    sick_hours_used = Column(Float, nullable=True)
    sick_hours_accrual_start_date = Column(DateTime, nullable=True)
    vacation_hours_available = Column(Float, nullable=True)
    vacation_hours_accrual_period = Column(String, nullable=True)
    vacation_hours_accrued = Column(Float, nullable=True)
    vacation_hours_maximum = Column(Float, nullable=True)
    is_resetting_vacation_hours_each_new_year = Column(Boolean, nullable=True)
    vacation_hours_used = Column(Float, nullable=True)
    vacation_hours_accrual_start_date = Column(DateTime, nullable=True)
    external_guid = Column(String, nullable=True)

    @staticmethod
    def from_xml(xml_str: str):
        root = etree.fromstring(xml_str)
        employee_ret = root if root.tag == 'EmployeeRet' else root.find('.//EmployeeRet')
        if employee_ret is None:
            return None

        def get_text(element, tag):
            child = element.find(tag)
            return child.text if child is not None else None

        def parse_duration_to_hours(duration_str):
            if duration_str:
                duration = parse_duration(duration_str)
                return duration.total_seconds() / 3600  # Convert seconds to hours
            return None

        return EmployeeRet(
            list_id=get_text(employee_ret, 'ListID'),
            time_created=datetime.fromisoformat(get_text(employee_ret, 'TimeCreated')) if get_text(employee_ret, 'TimeCreated') else None,
            time_modified=datetime.fromisoformat(get_text(employee_ret, 'TimeModified')) if get_text(employee_ret, 'TimeModified') else None,
            edit_sequence=get_text(employee_ret, 'EditSequence'),
            name=get_text(employee_ret, 'Name'),
            is_active=get_text(employee_ret, 'IsActive') == 'true' if get_text(employee_ret, 'IsActive') else None,
            salutation=get_text(employee_ret, 'Salutation'),
            first_name=get_text(employee_ret, 'FirstName'),
            middle_name=get_text(employee_ret, 'MiddleName'),
            last_name=get_text(employee_ret, 'LastName'),
            job_title=get_text(employee_ret, 'JobTitle'),
            supervisor_list_id=get_text(employee_ret, 'SupervisorRef/ListID'),
            supervisor_full_name=get_text(employee_ret, 'SupervisorRef/FullName'),
            department=get_text(employee_ret, 'Department'),
            description=get_text(employee_ret, 'Description'),
            target_bonus=float(get_text(employee_ret, 'TargetBonus')) if get_text(employee_ret, 'TargetBonus') else None,
            addr1=get_text(employee_ret, 'EmployeeAddress/Addr1'),
            addr2=get_text(employee_ret, 'EmployeeAddress/Addr2'),
            city=get_text(employee_ret, 'EmployeeAddress/City'),
            state=get_text(employee_ret, 'EmployeeAddress/State'),
            postal_code=get_text(employee_ret, 'EmployeeAddress/PostalCode'),
            print_as=get_text(employee_ret, 'PrintAs'),
            phone=get_text(employee_ret, 'Phone'),
            mobile=get_text(employee_ret, 'Mobile'),
            pager=get_text(employee_ret, 'Pager'),
            pager_pin=get_text(employee_ret, 'PagerPIN'),
            alt_phone=get_text(employee_ret, 'AltPhone'),
            fax=get_text(employee_ret, 'Fax'),
            ssn=get_text(employee_ret, 'SSN'),
            email=get_text(employee_ret, 'Email'),
            contact_name=get_text(employee_ret, 'AdditionalContactRef/ContactName'),
            contact_value=get_text(employee_ret, 'AdditionalContactRef/ContactValue'),
            emergency_contact_name=get_text(employee_ret, 'EmergencyContacts/PrimaryContact/ContactName'),
            emergency_contact_value=get_text(employee_ret, 'EmergencyContacts/PrimaryContact/ContactValue'),
            relation=get_text(employee_ret, 'EmergencyContacts/PrimaryContact/Relation'),
            employee_type=get_text(employee_ret, 'EmployeeType'),
            part_or_full_time=get_text(employee_ret, 'PartOrFullTime'),
            exempt=get_text(employee_ret, 'Exempt'),
            key_employee=get_text(employee_ret, 'KeyEmployee'),
            gender=get_text(employee_ret, 'Gender'),
            hired_date=datetime.fromisoformat(get_text(employee_ret, 'HiredDate')) if get_text(employee_ret, 'HiredDate') else None,
            original_hire_date=datetime.fromisoformat(get_text(employee_ret, 'OriginalHireDate')) if get_text(employee_ret, 'OriginalHireDate') else None,
            adjusted_service_date=datetime.fromisoformat(get_text(employee_ret, 'AdjustedServiceDate')) if get_text(employee_ret, 'AdjustedServiceDate') else None,
            released_date=datetime.fromisoformat(get_text(employee_ret, 'ReleasedDate')) if get_text(employee_ret, 'ReleasedDate') else None,
            birth_date=datetime.fromisoformat(get_text(employee_ret, 'BirthDate')) if get_text(employee_ret, 'BirthDate') else None,
            us_citizen=get_text(employee_ret, 'USCitizen'),
            ethnicity=get_text(employee_ret, 'Ethnicity'),
            disabled=get_text(employee_ret, 'Disabled'),
            disability_desc=get_text(employee_ret, 'DisabilityDesc'),
            on_file=get_text(employee_ret, 'OnFile'),
            work_auth_expire_date=datetime.fromisoformat(get_text(employee_ret, 'WorkAuthExpireDate')) if get_text(employee_ret, 'WorkAuthExpireDate') else None,
            us_veteran=get_text(employee_ret, 'USVeteran'),
            military_status=get_text(employee_ret, 'MilitaryStatus'),
            account_number=get_text(employee_ret, 'AccountNumber'),
            notes=get_text(employee_ret, 'Notes'),
            additional_notes=get_text(employee_ret, 'AdditionalNotesRet/Note'),
            billing_rate_list_id=get_text(employee_ret, 'BillingRateRef/ListID'),
            billing_rate_full_name=get_text(employee_ret, 'BillingRateRef/FullName'),
            pay_period=get_text(employee_ret, 'EmployeePayrollInfo/PayPeriod'),
            class_list_id=get_text(employee_ret, 'EmployeePayrollInfo/ClassRef/ListID'),
            class_full_name=get_text(employee_ret, 'EmployeePayrollInfo/ClassRef/FullName'),
            clear_earnings=get_text(employee_ret, 'EmployeePayrollInfo/ClearEarnings') == 'true' if get_text(employee_ret, 'EmployeePayrollInfo/ClearEarnings') else None,
            earnings_list_id=get_text(employee_ret, 'EmployeePayrollInfo/Earnings/PayrollItemWageRef/ListID'),
            earnings_full_name=get_text(employee_ret, 'EmployeePayrollInfo/Earnings/PayrollItemWageRef/FullName'),
            rate=float(get_text(employee_ret, 'EmployeePayrollInfo/Earnings/Rate')) if get_text(employee_ret, 'EmployeePayrollInfo/Earnings/Rate') else None,
            rate_percent=float(get_text(employee_ret, 'EmployeePayrollInfo/Earnings/RatePercent')) if get_text(employee_ret, 'EmployeePayrollInfo/Earnings/RatePercent') else None,
            is_using_time_data_to_create_paychecks=get_text(employee_ret, 'EmployeePayrollInfo/IsUsingTimeDataToCreatePaychecks') == 'true' if get_text(employee_ret, 'EmployeePayrollInfo/IsUsingTimeDataToCreatePaychecks') else None,
            use_time_data_to_create_paychecks=get_text(employee_ret, 'EmployeePayrollInfo/UseTimeDataToCreatePaychecks'),
            sick_hours_available=parse_duration_to_hours(get_text(employee_ret, 'EmployeePayrollInfo/SickHours/HoursAvailable')),
            sick_hours_accrual_period=get_text(employee_ret, 'EmployeePayrollInfo/SickHours/AccrualPeriod'),
            sick_hours_accrued=parse_duration_to_hours(get_text(employee_ret, 'EmployeePayrollInfo/SickHours/HoursAccrued')),
            sick_hours_maximum=parse_duration_to_hours(get_text(employee_ret, 'EmployeePayrollInfo/SickHours/MaximumHours')),
            is_resetting_hours_each_new_year=get_text(employee_ret, 'EmployeePayrollInfo/SickHours/IsResettingHoursEachNewYear') == 'true' if get_text(employee_ret, 'EmployeePayrollInfo/SickHours/IsResettingHoursEachNewYear') else None,
            sick_hours_used=parse_duration_to_hours(get_text(employee_ret, 'EmployeePayrollInfo/SickHours/HoursUsed')),
            sick_hours_accrual_start_date=datetime.fromisoformat(get_text(employee_ret, 'EmployeePayrollInfo/SickHours/AccrualStartDate')) if get_text(employee_ret, 'EmployeePayrollInfo/SickHours/AccrualStartDate') else None,
            vacation_hours_available=parse_duration_to_hours(get_text(employee_ret, 'EmployeePayrollInfo/VacationHours/HoursAvailable')),
            vacation_hours_accrual_period=get_text(employee_ret, 'EmployeePayrollInfo/VacationHours/AccrualPeriod'),
            vacation_hours_accrued=parse_duration_to_hours(get_text(employee_ret, 'EmployeePayrollInfo/VacationHours/HoursAccrued')),
            vacation_hours_maximum=parse_duration_to_hours(get_text(employee_ret, 'EmployeePayrollInfo/VacationHours/MaximumHours')),
            is_resetting_vacation_hours_each_new_year=get_text(employee_ret, 'EmployeePayrollInfo/VacationHours/IsResettingHoursEachNewYear') == 'true' if get_text(employee_ret, 'EmployeePayrollInfo/VacationHours/IsResettingHoursEachNewYear') else None,
            vacation_hours_used=parse_duration_to_hours(get_text(employee_ret, 'EmployeePayrollInfo/VacationHours/HoursUsed')),
            vacation_hours_accrual_start_date=datetime.fromisoformat(get_text(employee_ret, 'EmployeePayrollInfo/VacationHours/AccrualStartDate')) if get_text(employee_ret, 'EmployeePayrollInfo/VacationHours/AccrualStartDate') else None,
            external_guid=get_text(employee_ret, 'ExternalGUID')
        )

class EmployeeQueryRs:
    def __init__(self, status_code: int, status_severity: str, status_message: str, ret_count: int, employee_ret: Optional[List[EmployeeRet]] = None):
        self.status_code = status_code
        self.status_severity = status_severity
        self.status_message = status_message
        self.ret_count = ret_count
        self.employee_ret = employee_ret

def create_employee_table_if_not_exists(engine):
    Base.metadata.create_all(engine)

def generate_employee_query_xml(query: EmployeeQueryRq) -> str:
    xml = f'''<?xml version="1.0" encoding="utf-8"?>
<?qbxml version="16.0"?>
<QBXML>
    <QBXMLMsgsRq onError="stopOnError">
        <EmployeeQueryRq>
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
            <MatchCriterion>{query.name_filter.value}</MatchCriterion>
            <Name>{query.name_filter}</Name>
        </NameFilter>
        '''
    if query.name_range_filter:
        xml += f'''
        <NameRangeFilter>
            <MatchCriterion>{query.name_range_filter.value}</MatchCriterion>
            <Name>{query.name_range_filter}</Name>
        </NameRangeFilter>
        '''
    if query.include_ret_element:
        for element in query.include_ret_element:
            xml += f'<IncludeRetElement>{element}</IncludeRetElement>'
    if query.owner_id:
        for owner_id in query.owner_id:
            xml += f'<OwnerID>{owner_id}</OwnerID>'
    xml += '''
        </EmployeeQueryRq>
    </QBXMLMsgsRq>
</QBXML>
    '''
    return xml
