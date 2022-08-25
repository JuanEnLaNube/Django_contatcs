from django.contrib import admin
from directorio.models import Contactos

# Register your models here.
class ContactosView(admin.ModelAdmin):
    list_display = ('nombre', 'telefono', 'email')

    list_filter = ('nombre',)

    fieldsets = (
        ('Foto', { 'fields': ('foto',)}),
        ('Infonrmacion General', { 'fields': ('nombre', 'telefono', 'email',)}),
    )

admin.site.register(Contactos, ContactosView)