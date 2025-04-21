from django.db import models

class UserProfile(models.Model):
    GENDER_CHOICES = [
        ('Male', 'Male'),
        ('Female', 'Female'),
        ('Other', 'Other'),
    ]

    DEPARTMENT_CHOICES = [
        ('Construction Workers', 'Construction Workers'),
        ('Textiles and Garments', 'Textiles and Garments'),
        ('Domestic Work and Housekeeping', 'Domestic Work and Housekeeping'),
        ('Retail and Sales', 'Retail and Sales'),
        ('Vendors', 'Vendors'),
        ('Security', 'Security'),
        ('Mining', 'Mining'),
        ('Factories', 'Factories'),
    ]

    VACCINE_CHOICES = [
        ('Yes', 'Yes'),
        ('No', 'No'),
    ]

    MARITAL_STATUS_CHOICES = [
        ('Single', 'Single'),
        ('Married', 'Married'),
        ('Divorced', 'Divorced'),
        ('Widowed', 'Widowed'),
    ]

    name = models.CharField(max_length=100)
    email = models.EmailField(unique=True)
    photo = models.ImageField(upload_to='profile_photos/', null=True, blank=True)
    dob = models.DateField()
    gender = models.CharField(max_length=10, choices=GENDER_CHOICES)
    address = models.TextField()
    state = models.CharField(max_length=100)
    contact = models.CharField(max_length=10)
    department = models.CharField(max_length=50, choices=DEPARTMENT_CHOICES)
    bank = models.CharField(max_length=30)
    current_location = models.CharField(max_length=100)
    working_state = models.CharField(max_length=100)
    location = models.CharField(max_length=100)
    experience = models.PositiveIntegerField()
    district = models.CharField(max_length=100)
    occupation = models.CharField(max_length=100)
    salary = models.PositiveIntegerField()
    vaccine = models.CharField(max_length=3, choices=VACCINE_CHOICES)
    employer = models.TextField()
    marital_status = models.CharField(max_length=10, choices=MARITAL_STATUS_CHOICES)

    def __str__(self):
        return self.name


class Complaint(models.Model):
    STATUS_CHOICES = [
        ('processing', 'Processing'),
        ('solved', 'Solved'),
    ]

    name = models.CharField(max_length=100)
    contact = models.CharField(max_length=10)
    email = models.EmailField()
    subject = models.CharField(max_length=200)
    message = models.TextField()
    date   = models.DateField(auto_now_add=True)
    status = models.CharField(max_length=20, choices=STATUS_CHOICES, default='processing')

    def __str__(self):
        return self.name


