from django.shortcuts import render

from django.http import HttpResponse
from kadry.models import Projekt
from kadry.models import Zlecenie
from kadry.models import Marszruta
from kadry.models import Operacje_technologiczne


def projektowanie(request):
	zlecenia = Zlecenie.objects.all()
	projekty = Projekt.objects.all()

	return render(request, 'projektant/projektowanie.html', {'zlecenia': zlecenia, 'projekty': projekty})


def projekty(request):
	projekty = Projekt.objects.all()
	return render(request, 'projektant/projekty.html', {'projekty': projekty})


def marszruty(request):
	marszruty = Marszruta.objects.all()
	operacje = Operacje_technologiczne.objects.all()

	return render(request, 'projektant/marszruty.html', {'marszruty': marszruty, 'operacje': operacje})