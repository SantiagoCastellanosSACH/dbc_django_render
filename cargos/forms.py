from django import forms
from crispy_forms.helper import FormHelper
from crispy_forms.layout import Layout, Fieldset, Row, Column, Submit
from .models import Cargo

class CargoForm(forms.ModelForm):
    area = forms.CharField(label='Área')

    class Meta:
        model = Cargo
        fields = '__all__'

    def __init__(self, *args, **kwargs):
        super(CargoForm, self).__init__(*args, **kwargs)
        self.fields['nombre_cargo'].label = 'Nombre Posición'
        self.helper = FormHelper()
        self.helper.form_method = 'post'
        self.helper.add_input(Submit('submit', 'Crear', style='background-color: #003594;'))
        self.helper.layout = Layout(
            Fieldset(
                'INFORMACIÓN DEL CARGO',
                Row(
                    Column('nombre_cargo', css_class='form-group col-md-6 mb-3'),
                    Column('area', css_class='form-group col-md-6 mb-3'),
                ),
                css_class='seccion-container'
            ),
        )

class CargoEditForm(forms.ModelForm):
    area = forms.CharField(label='Área')


    class Meta:
        model = Cargo
        fields = '__all__'

    def __init__(self, *args, **kwargs):
        super(CargoEditForm, self).__init__(*args, **kwargs)
        self.fields['nombre_cargo'].label = 'Nombre Posición'
        self.helper = FormHelper()
        self.helper.form_method = 'post'
        self.helper.add_input(Submit('submit', 'Guardar cambios', style='background-color: #003594;'))
        self.helper.layout = Layout(
            Fieldset(
                'INFORMACIÓN DEL CARGO',
                Row(
                    Column('nombre_cargo', css_class='form-group col-md-6 mb-3'),
                    Column('area', css_class='form-group col-md-6 mb-3'),
                ),
                css_class='seccion-container'
            ),
        )

