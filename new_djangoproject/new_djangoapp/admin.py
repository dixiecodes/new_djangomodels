from django.contrib import admin
from .models import School, Student, Faculty, Department, Grade, Certificate_Type

# Register your models here.
# This builds the administrative site
#password

admin.site.register(School)
admin.site.register(Student)
admin.site.register(Faculty)
admin.site.register(Department)
admin.site.register(Grade)
admin.site.register(Certificate_Type)



