# import enum 
from enum import Enum
from django.utils.translation import gettext_lazy as _

# create anum for week days
class WeekDaysEnum(Enum):
    MONDAY = "monday"
    TUESDAY = "tuesday"
    WEDNESDAY = "wednesday"
    THURSDAY = "thursday"
    FRIDAY = "friday"
    SATURDAY = "saturday"
    SUNDAY = "sunday"
    
    # create a method to get all days
    @classmethod
    def get_all_days(cls):
        return [day.value for day in cls]
    
    @classmethod
    def choices(cls):
        return [
            (cls.MONDAY.value, _("Dushanba")),
            (cls.TUESDAY.value, _("Seshanba")),
            (cls.WEDNESDAY.value, _("Chorshanba")),
            (cls.THURSDAY.value, _("Payshanba")),
            (cls.FRIDAY.value, _("Juma")),
            (cls.SATURDAY.value, _("Shanba")),
            (cls.SUNDAY.value, _("Yakshanba")),
        ]
    

class MenuItemEnum(Enum):
    STRUCTURE = "structure"
    CHARTER = "charter" # universitet nizomi
    HISTORY = "history" # universitet tarixi
    UNIVERSITY_COUNCIL = "council" # universitet kengashi
    UNIVERSITY_PRESS_SECRETARY = "press-secretary" # ilmiy kengash
    STUDENTS_GIFTED = "gifted"
    STUDENTS_TUTION_FEE = "tuition-fee"
    STUDENTS_MANAGEMENT = "management"
    STUDENTS_EXAMS = "state-exams"
    STUDENTS_EMPLOYMENT = "employment"
    EDUCATION_DATA = "data"
    EDUCATION_REPORT = "reports"
    EDUCATION_COLLEAGE_FACULTY = "faculty"
    SDG_INFO = "sdg-info"
    SDG_REPORTS = "sdg-reports"
    GREEN_UNIVERSITY_CONCEPT = "concept"
    GREEN_ACTIVE_STUDENTS = "active-students"
    LEGAL_DOCUMENTS = "legal-documents"
    PRACTICAL_ACTIVITIES = "practical-activities"
    LEGAL_ACTS = "legal-acts"
    ADMISSION_GUIDE = "guide"
    ADMISSION_INTERNATIONAL = "international"
    ADMISSION_DISTANCE = "distance"
    ADMISSION_DORMITORIES = "dormitories"

    @classmethod
    def choices(cls):
        return [(item.value, item.name) for item in cls]


class DivisionTypeEnum(Enum):
    CENTER_DEPARTMENT = "centers-and-departments"  # Markaz/Bo'lim
    TECHNICAL_LYCEUM = "institutions"    # Texnikum/Litsey
    FORM_OF_EDUCATION = "forms-of-education"                    
    SCIENTIFIC_ACTIVITY = "scientific-activity"
    INTERNATION_RELATION = "international-relations"
    FINANCIAL_ACTIVITY = "financial-activity"
    INTERNATION_STUDENT = "international"
    GRADUATES = "graduates"
    ADMISSION_BACHELOR = "bachelor"
    ADMISSION_MASTER = "master"
    ADMISSION_DOCTORATE = "doctoral"
    ADMISSION_REGULATION = "regulations"
    
    
    
    @classmethod
    def choices(cls):
        return [(item.value, item.name) for item in cls]
