from django.contrib import admin 

# Register your models here.
from .models import Pracownik
from .models import Klient
from .models import Projekt
from .models import Zlecenie
from .models import Moja_Firma
from .models import Marszruta
from .models import Operacje_technologiczne
from imagekit.admin import AdminThumbnail #pakiet do tworzenia miniatur


admin.site.site_header = 'Panel Kadry - Kaczmarczyk'  #ustawia nagłówek zmiast "Django Administracja"
admin.site.site_title = 'Administracja MES Kaczmarczyk'

@admin.register(Moja_Firma)
class Moja_FirmaAdmin(admin.ModelAdmin):
	list_display = ('nazwa',)


@admin.register(Pracownik)
class PracownikAdmin(admin.ModelAdmin):
	list_display = ('aktywny', 'nazwisko', 'imie', 'nr_telefonu','rola', 'foto_display')
	list_filter = ('aktywny', 'bhp_wygasa', 'badania_wygasaja', 'rola', 'narodowosc')
	search_fields = ('nazwisko',)
	ordering = ('nazwisko',)
	foto_display = AdminThumbnail(image_field='foto_miniatura') #wyswietlanie miniatur w list_display
	foto_display.short_description = 'Fotografia'
	readonly_fields = ['foto_display']

@admin.register(Klient)
class KlientAdmin(admin.ModelAdmin):
	list_display = ('nazwa',)
	search_fields = ('nazwa',)
	ordering = ('nazwa',)
	readonly_fields = ['data_dodania']


@admin.register(Projekt)
class ProjektAdmin(admin.ModelAdmin):
	list_display = ('id', 'nazwa', 'get_customer_name', 'get_project_owner',)
	list_filter = ('klient', 'szef_projektu',)
	search_fields = ('nazwa',)
	ordering = ('nazwa',)
	readonly_fields = ['data_dodania']

	def get_customer_name(self, obj):  #metoda do pobrania nazwy klienta
		return obj.klient.nazwa
	get_customer_name.short_description = 'Klient'
	get_customer_name.admin_order_field = 'nazwa__klienta'

	def get_project_owner(self, obj):  #metoda do pobrania nazwiska właściciela projektu
		return obj.szef_projektu.nazwisko + obj.szef_projektu.imie
	get_project_owner.short_description = 'Właściciel'
	get_project_owner.admin_order_field = 'nazwisko__właściciela__projektu'


@admin.register(Zlecenie)
class ZlecenieAdmin(admin.ModelAdmin):
	list_display = ('id','nazwa', 'get_project_name')

	def get_project_name(self, obj):  #metoda do pobrania nazwy projektu
		return obj.nr_projektu.nazwa
	get_project_name.short_description = 'Projekt'
	get_project_name.admin_order_field = 'nazwa__projektu'


@admin.register(Marszruta)
class MarszrutaAdmin(admin.ModelAdmin):
	fields = ('nazwa', 'id',)             #ustawia kolejność w trybie edycji
	list_display = ('id', 'nazwa', 'get_order_name', 'get_operacja',)

	def get_order_name(self, obj):  #metoda do pobrania nr zlecenia
		return obj.zlecenie.id
	get_order_name.short_description = 'Zlecenie'
	get_order_name.admin_order_field = 'numer__zlecenia'

	def get_operacja(self, obj):                         # metoda pobiera liste operacji po symbolu
		return "\n".join([p.symbol for p in obj.operacja.all()])
	get_operacja.short_description = 'Operacje'
	get_operacja.admin_order_field = 'Operacje technologiczne'
	

@admin.register(Operacje_technologiczne)
class Operacje_technologiczneAdmin(admin.ModelAdmin):
	list_display = ('nazwa', 'symbol', 'czas_przezbrajania')
	