from django import forms
from crispy_forms.helper import FormHelper
from crispy_forms.layout import Layout, Fieldset, Row, Column, Submit
from .models import PersonasSST
from personas.models import Persona  # Importa el modelo Persona

class PersonasSSTForm(forms.ModelForm):
    persona_SST = forms.ModelChoiceField(queryset=Persona.objects.all(), label='Persona')

    class Meta:
        model = PersonasSST
        fields = ['persona_SST', 'tipo_documento', 'nombre_documento', 'archivo']

    def __init__(self, *args, **kwargs):
        super(PersonasSSTForm, self).__init__(*args, **kwargs)
        self.helper = FormHelper()
        self.helper.form_method = 'post'
        self.helper.add_input(Submit('submit', 'Adjuntar', style='background-color: #003594;'))

        self.helper.layout = Layout(
            Fieldset(
                'DATOS DE LA PERSONA',
                Row(
                    Column('persona_SST', css_class='form-group col-md-4 mb-3'),
                    Column('tipo_documento', css_class='form-group col-md-4 mb-3'),
                    Column('nombre_documento', css_class='form-group col-md-4 mb-3'),
                ),
                Row(
                'archivo',
                ),
                css_class='seccion-container'
            )
        )

class EditarPersonasSSTForm(forms.ModelForm):
    class Meta:
        model = PersonasSST
        fields = ['persona_SST', 'tipo_documento', 'nombre_documento', 'archivo']

    def __init__(self, *args, **kwargs):
        super(EditarPersonasSSTForm, self).__init__(*args, **kwargs)
        self.helper = FormHelper()
        self.helper.form_method = 'post'
        self.helper.add_input(Submit('submit', 'Guardar cambios', style='background-color: #003594;'))

        self.helper.layout = Layout(
            Fieldset(
                'DATOS DE LA PERSONA',
                Row(
                    Column('persona_SST', css_class='form-group col-md-4 mb-3'),
                    Column('tipo_documento', css_class='form-group col-md-4 mb-3'),
                    Column('nombre_documento', css_class='form-group col-md-4 mb-3'),
                ),
                css_class='seccion-container'
            ),
            Fieldset(
                 'DOCUMENTO',
                'archivo',
                css_class='seccion-container adjuntos'
            )
        )