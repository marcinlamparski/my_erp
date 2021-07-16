from django.db import models

# Create your models here.
from django.db import models
from django.utils import timezone
from django.contrib.auth.models import User

class Employee(models.Model):
	first_name = models.CharField(max_length=50)
	last_name = models.CharField(max_length=50)
	pesel = models.CharField(max_length=11, null=True)
	ROLE = (
		('PRO', 'Projektant'),
		('KP', 'Kierownik Produkcji'),
		('PP', 'Pracownik Produkcji'),
		('MON', 'Montażysta'),
		('KZ', 'Kadra Zarządzająca'),
	)
	data_dodania = models.DateTimeField(default=timezone.now)
	birth_date = models.DateField(auto_now=False, null=True, blank=True)
	salary_netto = models.DecimalField(max_digits=5, decimal_places=2,null=True)
	ohs_expires_date = models.DateField(auto_now=False, null=True, blank=True)
	health_exam_expires_date = models.DateField(auto_now=False, null=True, blank=True)
	viza_expires_date = models.DateField(auto_now=False, null=True, blank=True)
	nationality = (
		('PL', 'Polskie'),
		('UA', 'Ukraiśkie'),
		)
	passport_no = models.CharField(max_length=9, null=True)
	id_card_no = models.CharField(max_length=9, null=True)
	phone_no = models.CharField(max_length=9, null=True)
	email = models.EmailField(max_length=50, null=True)
	health_exam_file = models.FileField(null=True)
