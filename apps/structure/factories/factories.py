import factory
from factory.django import DjangoModelFactory
from factory.declarations import Sequence, LazyFunction, LazyAttribute, SubFactory
from faker import Faker
import random
from datetime import date, timedelta

from ..models.university import Faculty, Department, Specialty, FacultyEmployee, DepartmentEmployee
from ..models.employees import Employee
from apps.users.models import User

fake = Faker('uz_UZ')  # Uzbek locale


class EmployeeFactory(DjangoModelFactory):
    """Employee model uchun Factory"""
    
    class Meta:
        model = Employee
        django_get_or_create = ('employee_id_number',)
    
    full_name = LazyFunction(lambda: fake.name())
    xmn_id = Sequence(lambda n: f"XMN{n:06d}")
    employee_id_number = Sequence(lambda n: f"EMP{n:06d}")
    meta_id = Sequence(lambda n: f"META{n:05d}")
    uzkadr_id = Sequence(lambda n: f"{n:04d}")
    
    gender = LazyFunction(lambda: random.choice([Employee.MALE, Employee.FEMALE]))
    year_of_enter = LazyFunction(lambda: str(random.randint(2010, 2024)))
    birthday = LazyFunction(
        lambda: fake.date_between(start_date=date(1960, 1, 1), end_date=date(1995, 12, 31))
    )
    email = LazyAttribute(lambda obj: f"{obj.full_name.lower().replace(' ', '.')}@adu.uz")
    phone = LazyFunction(lambda: f"+998{random.randint(900000000, 999999999)}")
    passport = LazyFunction(lambda: f"{fake.random_uppercase_letter()}{fake.random_uppercase_letter()}{random.randint(1000000, 9999999)}")
    address = LazyFunction(lambda: fake.address())
    citizenship = Employee.UZBEK
    age = LazyFunction(lambda: random.randint(25, 65))
    
    specialty = LazyFunction(lambda: random.choice([
        "Matematik", "Fizik", "Kimyogar", "Biologiyakonas", "Tarixchi", "Filolog", 
        "Iqtisodchi", "Muhandis", "Dasturchi", "Psixolog"
    ]))
    academicDegree = LazyFunction(lambda: random.choice([
        Employee.UNDEGREE, Employee.CANDIDATE_OF_SCIENCES, Employee.DOCTOR_OF_SCIENCES
    ]))
    academicRank = LazyFunction(lambda: random.choice([
        Employee.UNTITLED, Employee.DOTSENT, Employee.SENIOR_LECTURER, Employee.PROFESSOR
    ]))
    employmentForm = LazyFunction(lambda: random.choice([
        Employee.FULL, Employee.EXTERNAL, Employee.HOURLY
    ]))
    staffPosition = LazyFunction(lambda: random.choice([
        Employee.STAJYOR, Employee.ASISTENT, Employee.BIG_TEACHER, Employee.DOTSENT, Employee.PROFESSOR
    ]))
    employeeType = "teacher"
    is_foreign = False


class FacultyFactory(DjangoModelFactory):
    """Faculty model uchun Factory"""
    
    class Meta:
        model = Faculty
        django_get_or_create = ('code',)
    
    name = LazyFunction(lambda: random.choice([
        "Matematika fakulteti", "Fizika fakulteti", "Kimyo fakulteti", 
        "Biologiya fakulteti", "Tarix fakulteti", "Filologiya fakulteti",
        "Iqtisodiyot fakulteti", "Informatika fakulteti", "Psixologiya fakulteti",
        "Falsafa fakulteti", "Geografiya fakulteti", "Huquq fakulteti"
    ]))
    xmn_id = Sequence(lambda n: f"FAC{n:03d}")
    code = Sequence(lambda n: f"F{n:03d}")
    description = LazyFunction(lambda: fake.text(max_nb_chars=200))
    position = Sequence(lambda n: n)


class DepartmentFactory(DjangoModelFactory):
    """Department model uchun Factory"""
    
    class Meta:
        model = Department
        django_get_or_create = ('code',)
    
    name = LazyFunction(lambda: random.choice([
        "Oliy matematika kafedrasi", "Algebra kafedrasi", "Geometriya kafedrasi",
        "Fizika kafedrasi", "Umumiy fizika kafedrasi", "Nazariy fizika kafedrasi",
        "Kimyo kafedrasi", "Organik kimyo kafedrasi", "Noorganik kimyo kafedrasi",
        "Biologiya kafedrasi", "Botanika kafedrasi", "Zoologiya kafedrasi",
        "O'zbek adabiyoti kafedrasi", "Jahon adabiyoti kafedrasi", "Tilshunoslik kafedrasi"
    ]))
    xmn_id = Sequence(lambda n: f"DEP{n:03d}")
    code = Sequence(lambda n: f"D{n:03d}")
    faculty = SubFactory(FacultyFactory)
    description = LazyFunction(lambda: fake.text(max_nb_chars=200))
    position = Sequence(lambda n: n)


class SpecialtyFactory(DjangoModelFactory):
    """Specialty model uchun Factory"""
    
    class Meta:
        model = Specialty
        django_get_or_create = ('code',)
    
    name = LazyFunction(lambda: random.choice([
        "Amaliy matematika", "Matematik fizika", "Umumiy fizika", "Nazariy fizika",
        "Organik kimyo", "Noorganik kimyo", "Fizik kimyo", "Biologiya",
        "Botanika", "Zoologiya", "O'zbek tili va adabiyoti", "Ingliz tili",
        "Iqtisodiyot", "Buxgalteriya hisobi", "Informatika", "Dasturlash"
    ]))
    xmn_id = Sequence(lambda n: f"SPEC{n:03d}")
    code = Sequence(lambda n: f"S{n:05d}")
    faculty = SubFactory(FacultyFactory)
    department = SubFactory(DepartmentFactory)
    educationType = LazyFunction(lambda: random.choice([11, 12, 13, 14]))
    localityType = LazyFunction(lambda: random.choice([10, 11, 12, 13]))
    description = LazyFunction(lambda: fake.text(max_nb_chars=200))
    position = Sequence(lambda n: n)


class FacultyEmployeeFactory(DjangoModelFactory):
    """FacultyEmployee model uchun Factory"""
    
    class Meta:
        model = FacultyEmployee
    
    faculty = SubFactory(FacultyFactory)
    employee = SubFactory(EmployeeFactory)
    staffPosition = LazyFunction(lambda: random.choice([
        Employee.DEKAN, Employee.DEKAN_ASSISTANT, Employee.PROFESSOR, Employee.DOTSENT
    ]))


class DepartmentEmployeeFactory(DjangoModelFactory):
    """DepartmentEmployee model uchun Factory"""
    
    class Meta:
        model = DepartmentEmployee
    
    department = SubFactory(DepartmentFactory)
    employee = SubFactory(EmployeeFactory)
    position = LazyFunction(lambda: random.choice([
        Employee.DEPARTMENT_USER, Employee.PROFESSOR, Employee.DOTSENT, Employee.BIG_TEACHER
    ]))
