# import enum 
from enum import Enum

# create anum for week days
class WeekDaysEnum(Enum):
    MONDAY = "Monday"
    TUESDAY = "Tuesday"
    WEDNESDAY = "Wednesday"
    THURSDAY = "Thursday"
    FRIDAY = "Friday"
    SATURDAY = "Saturday"
    SUNDAY = "Sunday"
    # create a method to get all days
    @classmethod
    def get_all_days(cls):
        return [day.value for day in cls]
    
    @classmethod
    def choices(cls):
        return [(day.value, day.name) for day in cls]
    

class MenuItemEnum(Enum):
    CHARTER = "charter" # universitet nizomi
    HISTORY = "history" # universitet tarixi
    UNIVERSITY_COUNCIL = "council" # universitet kengashi
    SCIENTIFIC_COUNCIL = "scientific_council" # ilmiy kengash
    
    @classmethod
    def choices(cls):
        return [(item.value, item.name) for item in cls]
    