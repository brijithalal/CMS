import uuid
from django.db import models
from django.contrib.auth.models import AbstractUser

# 1. Role Table
# class Role(models.Model):
#     role_name = models.CharField(max_length=100, unique=True)
#     description = models.TextField()

#     def __str__(self):
#         return self.role_name

# 2. Department Table
class Department(models.Model):
    department_name = models.CharField(max_length=100, unique=True)
    description = models.TextField()
    is_active = models.BooleanField(default=True)
    base_salary = models.DecimalField(max_digits=10, decimal_places=2)

    def __str__(self):
        return self.department_name


# 3. Qualification Table
class Qualification(models.Model):
    qualification_name = models.CharField(max_length=100, unique=True)
    min_year_of_experience = models.PositiveIntegerField()
    description = models.TextField()

    def __str__(self):
        return self.qualification_name


# 4. Staff Table
class Staff(AbstractUser):
    # username = models.CharField(max_length=100, unique=True)
    # password = models.CharField(max_length=100)
    department = models.ForeignKey(Department, on_delete=models.SET_NULL, null=True)
    qualification = models.ForeignKey(Qualification, on_delete=models.SET_NULL, null=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    # first_name = models.CharField(max_length=100)
    # last_name = models.CharField(max_length=100)
    dob = models.DateField(null=True, blank=True)
    profile_image = models.ImageField(upload_to='clinic/images/')
    gender = models.CharField(max_length=20)
    contact = models.CharField(max_length=20)
    # email = models.EmailField(unique=True)
    # date_of_joining = models.DateField()
    # status = models.BooleanField(default=True)

    
    def __str__(self):
        return self.username


# 5. Work History Table
class WorkHistory(models.Model):
    staff = models.ForeignKey(Staff, on_delete=models.CASCADE)
    work_details = models.TextField()
    start_date = models.DateField()
    end_date = models.DateField()

    
    def __str__(self):
        return self.staff.username


# 6. Doctor Table
class Doctor(models.Model):
    staff = models.OneToOneField(Staff, on_delete=models.CASCADE)
    specialization = models.ManyToManyField(Qualification)
    doctor_code = models.CharField(max_length=50, unique=True)
    consultation_fee = models.DecimalField(max_digits=10, decimal_places=2)
    consultation_days = models.CharField(max_length=100)
    consultation_duration = models.PositiveIntegerField(default=15)  # 15 mins
    morning_start_time = models.TimeField()
    morning_end_time = models.TimeField()
    evening_start_time = models.TimeField()
    evening_end_time = models.TimeField()
    status = models.BooleanField(default=True)

    def generate_doctor_code(self):
        """
        Generate a unique receptionist code starting with 'R' followed by a unique identifier.
        """
        unique_id = uuid.uuid4().hex[:6].upper()  # First 6 characters of UUID for uniqueness
        return f"R{unique_id}"

    def save(self, *args, **kwargs):
        if not self.doctor_code:  # Only generate the code if it hasn't been set already
            self.doctor_code = self.generate_doctor_code()
        super(Doctor, self).save(*args, **kwargs)

    
    def __str__(self):
        return self.staff.username


# 7. Specialization Table
class Specialization(models.Model):
    qualification = models.ManyToManyField(Qualification)
    specialization_name = models.CharField(max_length=100)
    description = models.TextField()

    
    def __str__(self):
        return self.specialization_name


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

    def generate_patient_code(self):
        """
        Generate a unique receptionist code starting with 'R' followed by a unique identifier.
        """
        unique_id = uuid.uuid4().hex[:6].upper()  # First 6 characters of UUID for uniqueness
        return f"R{unique_id}"

    def save(self, *args, **kwargs):
        if not self.patient_code:  # Only generate the code if it hasn't been set already
            self.patient_code = self.generate_patient_code()
        super(Patient, self).save(*args, **kwargs)

    
    def __str__(self):
        return f"{self.first_name}{self.last_name}"


# 9. Appointment Table
class Appointment(models.Model):
    appointment_number = models.CharField(max_length=100, unique=True)
    patient = models.ForeignKey(Patient, on_delete=models.CASCADE)
    doctor = models.ForeignKey(Doctor, on_delete=models.CASCADE)
    appointment_date = models.DateField()
    time_slot = models.TimeField()
    status = models.CharField(max_length=50)  # Scheduled, Cancelled, Completed

    def __str__(self):
        return self.patient


# 10. Token Table
class Token(models.Model):
    patient = models.ForeignKey(Patient, on_delete=models.CASCADE)
    doctor = models.ForeignKey(Doctor, on_delete=models.CASCADE)
    token_number = models.CharField(max_length=100)
    status = models.CharField(max_length=50)  # Active, Expired

    def __str__(self):
        return f"{self.patient} {self.token_number}"



# 11. Billing Table
class Billing(models.Model):
    appointment = models.OneToOneField(Appointment, on_delete=models.CASCADE)
    billing_date = models.DateField()
    billing_time = models.TimeField()
    insurance_details = models.TextField()
    consultation_fee = models.DecimalField(max_digits=10, decimal_places=2)
    total_amount = models.DecimalField(max_digits=10, decimal_places=2)


    def __str__(self):
        return f"{self.appointment} {self.total_amount}"



# 12. Medicine Table
class Medicine(models.Model):
    name = models.CharField(max_length=100)
    manufacturer = models.CharField(max_length=100)
    dosage_instructions = models.TextField()
    medicine_type = models.CharField(max_length=100)

    def __str__(self):
        return self.name



# 13. Prescription Table
class Prescription(models.Model):
    appointment = models.ForeignKey(Appointment, on_delete=models.CASCADE)
    medicine = models.ManyToManyField(Medicine)
    dosage = models.CharField(max_length=100)
    duration = models.PositiveIntegerField()
    frequency = models.CharField(max_length=50)

    def __str__(self):
        return f"{self.appointment} {self.medicine}"


# 14. Salary Table
class Salary(models.Model):
    staff = models.ForeignKey(Staff, on_delete=models.CASCADE)
    experience_bonus = models.DecimalField(max_digits=10, decimal_places=2)
    specialization_bonus = models.DecimalField(max_digits=10, decimal_places=2)
    qualification_bonus = models.DecimalField(max_digits=10, decimal_places=2)
    total_salary = models.DecimalField(max_digits=10, decimal_places=2)
    salary_date = models.DateField()
    created_at = models.DateTimeField(auto_now_add=True)
    status = models.CharField(max_length=50)  # Active, Inactive

    def __str__(self):
        return f"{self.staff.username} {self.total_salary}"


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

    def __str__(self):
        return f"{self.appointment} {self.doctor}"


# 16. Note Table
class Note(models.Model):
    consultation = models.ForeignKey(Consultation, on_delete=models.CASCADE)
    doctor = models.ForeignKey(Doctor, on_delete=models.CASCADE)
    note_text = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.consultation


# 17. Patient File Table
class PatientFile(models.Model):
    patient = models.ForeignKey(Patient, on_delete=models.CASCADE)
    note = models.ForeignKey(Note, on_delete=models.CASCADE)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.patient


# 18. Receptionist Table
class Receptionist(models.Model):
    staff = models.OneToOneField(Staff, on_delete=models.CASCADE)
    receptionist_code = models.CharField(max_length=100,unique=True)
    years_of_experience = models.PositiveIntegerField()
    education_qualification = models.CharField(max_length=100)
    base_salary = models.DecimalField(max_digits=10, decimal_places=2)
    is_active = models.BooleanField(default=True)


    def generate_receptionist_code(self):
        """
        Generate a unique receptionist code starting with 'R' followed by a unique identifier.
        """
        unique_id = uuid.uuid4().hex[:6].upper()  # First 6 characters of UUID for uniqueness
        return f"R{unique_id}"

    def save(self, *args, **kwargs):
        if not self.receptionist_code:  # Only generate the code if it hasn't been set already
            self.receptionist_code = self.generate_receptionist_code()
        super(Receptionist, self).save(*args, **kwargs)

    def __str__(self):
        return self.staff

