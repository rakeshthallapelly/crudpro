from django.db import models
GENDER_CHOICES = (
    ('Male', 'Male'),
    ('Female', 'Female')
)

class Patient(models.Model):


	first_name=models.CharField(max_length=24)
	middle_name=models.CharField(max_length=24)
	last_name=models.CharField(max_length=24)
	DOB=models.DateField(max_length=24)
	qualification=models.CharField(max_length=50)
	gender = models.CharField(choices=GENDER_CHOICES, max_length=6)
	reson_for_visit=models.TextField()


	
    
