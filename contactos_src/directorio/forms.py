from directorio.models import Contactos
from django import forms 

class ContactosForm(forms.ModelForm):

    class Meta:
        model = Contactos
        
        fields = (
            'foto','nombre', 'telefono', 'email',
        )

        labels = {
            'foto':'Fotografía',
        }
