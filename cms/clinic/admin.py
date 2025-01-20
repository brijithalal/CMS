from django.contrib import admin

from .models import Appointment, Billing, Consultation, Department, Doctor, Medicine, Note, Patient, PatientFile, Prescription, Qualification, Receptionist, Salary, Specialization, Staff, Token, WorkHistory

# Register your models here.


admin.site.register(Department)
admin.site.register(Qualification)
admin.site.register(Staff)
admin.site.register(WorkHistory)
admin.site.register(Doctor)
admin.site.register(Specialization)
admin.site.register(Patient)
admin.site.register(Appointment)
admin.site.register(Token)
admin.site.register(Billing)
admin.site.register(Medicine)
admin.site.register(Prescription)
admin.site.register(Salary)
admin.site.register(Consultation)
admin.site.register(Note)
admin.site.register(PatientFile)
admin.site.register(Receptionist)