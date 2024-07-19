# forms.py
from django import forms
from crispy_forms.helper import FormHelper
from crispy_forms.layout import Layout, Fieldset, Row, Column, Submit
from .models import EmpresaSST

class EmpresaSSTForm(forms.ModelForm):
    class Meta:
        model = EmpresaSST
        fields = ['nombre_documento', 'tipo_documento', 'archivo']

    def __init__(self, *args, **kwargs):
        super(EmpresaSSTForm, self).__init__(*args, **kwargs)
        self.helper = FormHelper()
        self.helper.form_method = 'post'
        self.helper.add_input(Submit('submit', 'Adjuntar', style='background-color: #003594;'))

        self.helper.layout = Layout(
            Fieldset(
                'DOCUMENTOS SST EMPRESARIALES',
                Row(
                    Column('nombre_documento', css_class='form-group col-md-4 mb-3'),
                    Column('tipo_documento', css_class='form-group col-md-4 mb-3'),
                ),
                Row(
                    Column('archivo', css_class='form-group col-md-4 mb-3'),
                ),
                css_class='seccion-container'
            )
        )

class EditarEmpresaSSTForm(forms.ModelForm):

    class Meta:
        model = EmpresaSST
        fields = ['nombre_documento', 'tipo_documento', 'archivo']

    def __init__(self, *args, **kwargs):
        super(EditarEmpresaSSTForm, self).__init__(*args, **kwargs)
        self.helper = FormHelper()
        self.helper.form_method = 'post'
        self.helper.add_input(Submit('submit', 'Guardar cambios', style='background-color: #003594;'))

        self.helper.layout = Layout(
            Fieldset(
                'DATOS DE LA EMPRESA',
                Row(
                    Column('nombre_documento', css_class='form-group col-md-4 mb-3'),
                    Column('tipo_documento', css_class='form-group col-md-4 mb-3'),
                ),
                css_class='seccion-container'
            ),
            Fieldset(
                'DOCUMENTO',
                'archivo',
                css_class='seccion-container adjuntos'
            )
        )
