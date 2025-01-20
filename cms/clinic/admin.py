from django.contrib import admin

from .models import Appointment, Billing, Consultation, Department, Doctor, Medicine, Note, Patient, PatientFile, Prescription, Qualification, Receptionist, Salary, Specialization, Staff, Token, WorkHistory

# Register your models here.


admin.site.register(Department)
admin.site.register(Qualification)
admin.site.register(Staff)
admin.site.register(WorkHistory)
# admin.site.register(Doctor)
admin.site.register(Specialization)
# admin.site.register(Patient)
admin.site.register(Appointment)
admin.site.register(Token)
admin.site.register(Billing)
admin.site.register(Medicine)
admin.site.register(Prescription)
admin.site.register(Salary)
admin.site.register(Consultation)
admin.site.register(Note)
admin.site.register(PatientFile)
# admin.site.register(Receptionist)

@admin.register(Doctor)
class DoctorAdmin(admin.ModelAdmin):
    readonly_fields = ('doctor_code',)  # Make doctor_code read-only
    # list_display = ('staff', 'doctor_code', 'specialization', 'status')


@admin.register(Receptionist)
class ReceptionistAdmin(admin.ModelAdmin):
    readonly_fields = ('receptionist_code',)  # Make doctor_code read-only
    # list_display = ('staff', 'doctor_code', 'specialization', 'status')


@admin.register(Patient)
class PatientAdmin(admin.ModelAdmin):
    readonly_fields = ('patient_code',)  # Make doctor_code read-only
    # list_display = ('staff', 'doctor_code', 'specialization', 'status')