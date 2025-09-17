from modeltranslation.translator import TranslationOptions, register

from apps.structure.models import (
    Divisions, 
    MenuItem, 
    Document, 
    DivisionDocument, 
    Employee,
    HomePageText,
    UniversityBaseInfo,
    Department,
    Faculty,
    Specialty

)
@register(Divisions)
class DivisionsTranslationOptions(TranslationOptions):
    fields = ('name', 'content',)

@register(MenuItem)
class MenuItemTranslationOptions(TranslationOptions):
    fields = ('title', 'content',)

@register(Document)
class DocumentTranslationOptions(TranslationOptions):
    fields = ('name',)

@register(DivisionDocument)
class DivisionDocumentTranslationOptions(TranslationOptions):
    fields = ('name',)

@register(Employee)
class EmployeeTranslationOptions(TranslationOptions):
    fields = ('task', 'employeeRank',)


@register(HomePageText)
class HomePageTextTranslationOptions(TranslationOptions):
    fields = ('description',)

@register(UniversityBaseInfo)
class UniversityBaseInfoTranslationOptions(TranslationOptions):
    fields = ('about', 'address',)

@register(Department)
class DepartmentTranslationOptions(TranslationOptions):
    fields = ('name', 'description',)
    
@register(Faculty)
class FacultyTranslationOptions(TranslationOptions):
    fields = ('name', 'description',)

@register(Specialty)
class SpecialtyTranslationOptions(TranslationOptions):
    fields = ('name', 'description',)
