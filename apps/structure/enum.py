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
    
