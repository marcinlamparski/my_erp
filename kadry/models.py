from django.db import models

# Create your models here.
from django.db import models
from django.utils import timezone
from django.contrib.auth.models import User

from PIL import Image #pakiet do obslugi zdjec
from imagekit.models import ImageSpecField #pakiet do obslugi zdjec
from imagekit.processors import ResizeToFill #pakiet do obslugi zdjec

from django import forms #pola formularzy html

from django.contrib.postgres.fields import ArrayField




class Moja_Firma(models.Model):
	nazwa = models.CharField(max_length=50)
	nip = models.CharField(max_length=12, help_text="NIP w formacie PLXXXXXXXXXX")
	data_dodania = models.DateTimeField(auto_now_add=True)


	class Meta:
		verbose_name_plural = "Moja Firma"


class Pracownik(models.Model):
	nazwisko = models.CharField(max_length=50)
	imie = models.CharField(max_length=50)
	pesel = models.CharField(max_length=11, null=True)
	AKTYWNY_CHOICES  = (
		(True, 'Aktywny'),
		(False, 'Niektywny')
		)
	aktywny = models.BooleanField(default=False)
	ROLA_CHOICES = (
		('PRO', 'Projektant'),
		('KP', 'Kierownik Produkcji'),
		('PP', 'Pracownik Produkcji'),
		('MON', 'Montażysta'),
		('KPR', 'Kierownik Projektu'),
		('DYR', 'Dyrektor'),
	)
	rola = models.CharField(max_length=3, choices=ROLA_CHOICES)
	data_dodania = models.DateTimeField(default=timezone.now)
	data_zatrudnienia = models.DateField(auto_now=False, null=True, blank=True)
	data_zwolnienia = models.DateField(auto_now=False, null=True, blank=True)
	data_urodzenia = models.DateField(auto_now=False, null=True, blank=True)
	wynagrodzenie_netto = models.DecimalField(max_digits=5, decimal_places=2,null=True)
	bhp_wygasa = models.DateField(auto_now=False, null=True, blank=True)
	badania_wygasaja = models.DateField(auto_now=False, null=True, blank=True)
	viza_wygasa = models.DateField(auto_now=False, null=True, blank=True)
	NARODOWOSC_CHOICES = (
		('PL', 'Polskie'),
		('UA', 'Ukraiśkie'),
		)
	narodowosc = models.CharField(max_length=2, choices=NARODOWOSC_CHOICES, verbose_name = 'narodowość')
	nr_paszportu = models.CharField(max_length=9, null=True, blank=True, help_text = 'W przypadku obcokrajowców', verbose_name = 'numer paszportu')
	nr_dowodu= models.CharField(max_length=9, null=True, verbose_name = 'numer dowodu')
	nr_telefonu = models.CharField(max_length=9, null=True, verbose_name = 'numer telefonu')
	email = models.EmailField(max_length=50, null=True, blank=True)
	notatki = models.TextField(null=True, blank=True)
	foto = models.ImageField(upload_to='foto', default='/foto/default_foto.jpeg')
	foto_miniatura = ImageSpecField(source='foto',
                                      processors=[ResizeToFill(30, 30)],
                                      format='JPEG',
                                      options={'quality': 50})

	class Meta:
		verbose_name_plural = "Pracownicy"


class Klient(models.Model):
	nazwa = models.CharField(max_length=50, unique=True)
	notatki = models.TextField(null=True, blank=True, help_text = 'Istotne informacje dotyczące klienta')
	data_dodania = models.DateTimeField(auto_now_add=True)

	class Meta:
		verbose_name_plural = "Klienci"


class Projekt(models.Model):
	nazwa = models.CharField(max_length=50)
	notatki = models.TextField(null=True, blank=True, help_text = 'Ważne informacje dotyczące projeku')
	klient = models.ForeignKey(Klient, on_delete=models.CASCADE, null=True)
	szef_projektu = models.ForeignKey(Pracownik, on_delete=models.CASCADE, null=True, verbose_name = 'szef projektu')
	data_dodania = models.DateTimeField(auto_now_add=True)
	ostatnia_modyfikacja = models.DateField(auto_now=True)
	
	class Meta:
		verbose_name_plural = "Projekty"

class Zlecenie(models.Model):
	#numer = models.CharField(max_length=50)
	nazwa = models.CharField(max_length=50)
	data_dodania = models.DateTimeField(auto_now_add=True)
	ostatnia_modyfikacja = models.DateField(auto_now=True)
	nr_projektu = models.ForeignKey(Projekt, on_delete=models.CASCADE, null=True)

	class Meta:
		verbose_name_plural = "Zlecenia"



class Operacje_technologiczne(models.Model):
	nazwa = models.CharField(max_length=50)
	symbol = models.CharField(max_length=3, help_text = 'Maksymalnie 3 znaki')
	czas_przezbrajania = models.PositiveSmallIntegerField(default=0, verbose_name='Czas przezbrajania maszyny', help_text = 'Jednostka - godzina')

	class Meta:
		verbose_name_plural = "Operacje"



class Marszruta(models.Model):
	nazwa = models.CharField(max_length=50)
	zlecenie = models.ForeignKey(Zlecenie, on_delete=models.CASCADE, null=True)
	operacja = models.ManyToManyField(Operacje_technologiczne)
	#czasy = ArrayField(
	#	ArrayField(
	#		models.IntegerField(default=0, null=True),
	#		size=8,
	#	),
	#	size=8,
	#)
	class Meta:
		verbose_name_plural = "Marszruty"
	