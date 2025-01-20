from django.db import models

# 1. Role Table
class Role(models.Model):
    role_name = models.CharField(max_length=100, unique=True)
    description = models.TextField()

    def __str__(self):
        return self.role_name


# 2. Department Table
class Department(models.Model):
    department_name = models.CharField(max_length=100, unique=True)
    description = models.TextField()
    is_active = models.BooleanField(default=True)
    base_salary = models.DecimalField(max_digits=10, decimal_places=2)


# 3. Qualification Table
class Qualification(models.Model):
    qualification_name = models.CharField(max_length=100, unique=True)
    min_year_of_experience = models.PositiveIntegerField()
    description = models.TextField()


# 4. User Table
class User(models.Model):
    username = models.CharField(max_length=100, unique=True)
    password = models.CharField(max_length=100)
    department = models.ForeignKey(Department, on_delete=models.SET_NULL, null=True)
    role = models.ForeignKey(Role, on_delete=models.CASCADE)
    qualification = models.ForeignKey(Qualification, on_delete=models.SET_NULL, null=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    first_name = models.CharField(max_length=100)
    last_name = models.CharField(max_length=100)
    dob = models.DateField()
    gender = models.CharField(max_length=20)
    contact = models.CharField(max_length=20)
    email = models.EmailField(unique=True)
    date_of_joining = models.DateField()
    status = models.BooleanField(default=True)


# 5. Work History Table
class WorkHistory(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    work_details = models.TextField()
    start_date = models.DateField()
    end_date = models.DateField()


# 6. Doctor Table
class Doctor(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    specialization = models.ForeignKey(Qualification, on_delete=models.CASCADE)
    doctor_code = models.CharField(max_length=50, unique=True)
    consultation_fee = models.DecimalField(max_digits=10, decimal_places=2)
    consultation_days = models.CharField(max_length=100)
    consultation_duration = models.PositiveIntegerField(default=15)  # 15 mins
    morning_start_time = models.TimeField()
    morning_end_time = models.TimeField()
    evening_start_time = models.TimeField()
    evening_end_time = models.TimeField()
    status = models.BooleanField(default=True)


# 7. Specialization Table
class Specialization(models.Model):
    qualification = models.ForeignKey(Qualification, on_delete=models.CASCADE)
    specialization_name = models.CharField(max_length=100)
    description = models.TextField()


# 8. Patient Table
class Patient(models.Model):
    patient_code = models.CharField(max_length=50, unique=True)
    blood_group = models.CharField(max_length=10)
    first_name = models.CharField(max_length=100)
    last_name = models.CharField(max_length=100)
    contact = models.CharField(max_length=20)
    email = models.EmailField(unique=True)
    insurance_provider = models.CharField(max_length=100)
    insurance_number = models.CharField(max_length=50)
    insurance_validity = models.DateField()
    gender = models.CharField(max_length=20)
    dob = models.DateField()
    address = models.TextField()


# 9. Appointment Table
class Appointment(models.Model):
    appointment_number = models.CharField(max_length=100, unique=True)
    patient = models.ForeignKey(Patient, on_delete=models.CASCADE)
    doctor = models.ForeignKey(Doctor, on_delete=models.CASCADE)
    appointment_date = models.DateField()
    time_slot = models.TimeField()
    status = models.CharField(max_length=50)  # Scheduled, Cancelled, Completed


# 10. Token Table
class Token(models.Model):
    patient = models.ForeignKey(Patient, on_delete=models.CASCADE)
    doctor = models.ForeignKey(Doctor, on_delete=models.CASCADE)
    token_number = models.CharField(max_length=100)
    status = models.CharField(max_length=50)  # Active, Expired


# 11. Billing Table
class Billing(models.Model):
    appointment = models.OneToOneField(Appointment, on_delete=models.CASCADE)
    billing_date = models.DateField()
    billing_time = models.TimeField()
    insurance_details = models.TextField()
    consultation_fee = models.DecimalField(max_digits=10, decimal_places=2)
    total_amount = models.DecimalField(max_digits=10, decimal_places=2)


# 12. Medicine Table
class Medicine(models.Model):
    name = models.CharField(max_length=100)
    manufacturer = models.CharField(max_length=100)
    dosage_instructions = models.TextField()
    medicine_type = models.CharField(max_length=100)


# 13. Prescription Table
class Prescription(models.Model):
    appointment = models.ForeignKey(Appointment, on_delete=models.CASCADE)
    medicine = models.ForeignKey(Medicine, on_delete=models.CASCADE)
    dosage = models.CharField(max_length=100)
    duration = models.PositiveIntegerField()
    frequency = models.CharField(max_length=50)


# 14. Salary Table
class Salary(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    experience_bonus = models.DecimalField(max_digits=10, decimal_places=2)
    specialization_bonus = models.DecimalField(max_digits=10, decimal_places=2)
    qualification_bonus = models.DecimalField(max_digits=10, decimal_places=2)
    total_salary = models.DecimalField(max_digits=10, decimal_places=2)
    salary_date = models.DateField()
    created_at = models.DateTimeField(auto_now_add=True)
    status = models.CharField(max_length=50)  # Active, Inactive


# 15. Consultation Table
class Consultation(models.Model):
    appointment = models.ForeignKey(Appointment, on_delete=models.CASCADE)
    doctor = models.ForeignKey(Doctor, on_delete=models.CASCADE)
    patient = models.ForeignKey(Patient, on_delete=models.CASCADE)
    symptoms = models.TextField()
    diagnosis = models.TextField()
    consultation_date = models.DateField()
    test_name = models.CharField(max_length=100)
    created_at = models.DateTimeField(auto_now_add=True)


# 16. Note Table
class Note(models.Model):
    consultation = models.ForeignKey(Consultation, on_delete=models.CASCADE)
    doctor = models.ForeignKey(Doctor, on_delete=models.CASCADE)
    note_text = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)


# 17. Patient File Table
class PatientFile(models.Model):
    patient = models.ForeignKey(Patient, on_delete=models.CASCADE)
    note = models.ForeignKey(Note, on_delete=models.CASCADE)
    created_at = models.DateTimeField(auto_now_add=True)


# 18. Receptionist Table
class Receptionist(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    receptionist_code = models.CharField(max_length=100, unique=True)
    years_of_experience = models.PositiveIntegerField()
    education_qualification = models.CharField(max_length=100)
    base_salary = models.DecimalField(max_digits=10, decimal_places=2)
    is_active = models.BooleanField(default=True)

