from django import forms
from django.db.models import fields
from django.forms import ModelForm
from .models import Software

class SoftwareForm(ModelForm):
    class Meta:
        model = Software
        fields = ['idSoftware', 
                'nomSoftware',
                'descSoftware',
                'catSoftware']
        labels = {

            'idSoftware' : 'Ingrese el ID del Software',
            'nomSoftware' : 'Ingrese el Nombre del Software',
            'descSoftware' : 'Ingrese la Descripción del Software',
            'catSoftware' : 'Seleccione la Categoría del Software'

        }

        widgets = {

            'idSoftware' : forms.NumberInput(
                attrs={
                    'class' : 'form-control',
                    'placeholder' : 'id del software',
                    'id' : 'idsoft',
                    'style' : 'border-radius: 0px'
                }
            ),
            'nomSoftware' : forms.TextInput(
                attrs={
                    'class' : 'form-control',
                    'placeholder' : 'nombre del Software',
                    'id' : 'nomSoft',
                    'style' : 'border-radius: 0px'
                }
            ),
            'descSoftware' : forms.Textarea(
                attrs={
                    'class' : 'form-control',
                    'id' : 'descSoft',
                    'placeholder' : 'Ingrese una descipción del software',
                    'cols' : '95',
                    'rows' : '10',
                    'style' : 'border-radius: 0px'
                }
            ),
            'catSoftware' : forms.Select(
                attrs={
                    'class' : 'form-control',
                    'id' : 'catSoft',
                    'style' : 'border-radius: 0px'
                }
            )

        }