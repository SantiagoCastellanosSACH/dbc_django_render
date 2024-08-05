from django.utils import timezone
from django import forms
from crispy_forms.helper import FormHelper
from crispy_forms.layout import Layout, Fieldset, Row, Column, Submit
from .models import Contrato, Persona
from django.utils.html import format_html
from django.forms.widgets import Select

class EmpleadoSelectWidget(Select):
    def create_option(self, name, value, label, selected, index, subindex=None, attrs=None):
        option = super().create_option(name, value, label, selected, index, subindex=subindex, attrs=attrs)
        if value:
            empleado = Persona.objects.get(pk=value)
            option['label'] = format_html('{} ({})', empleado.nombre_persona, empleado.numero_documento_persona)
        return option

class ContratoForm(forms.ModelForm):
    empleado = forms.ModelChoiceField(queryset=Persona.objects.all())

    class Meta:
        model = Contrato
        fields = '__all__'
        exclude = ['fecha_creacion_contrato', 'fecha_carga_adjunto_contrato']
        labels = {
            'razón_social': 'Razón Social',
            'nit_empresa': 'NIT de la Empresa',
            'ubicacion': 'Ubicación',
            'direccion_notificacion_judicial': 'Dirección de Notificación Judicial',
            'nombre_representante_legal': 'Nombre',
            'cargo_representante_legal': 'Cargo',
            'tipo_doc_representante_legal': 'Tipo de Documento',
            'numero_doc_representante_legal': 'Número de Documento',
            'lugar_expedicion_doc_representante_legal': 'Lugar de Expedición',
            'correo_representante_legal': 'Correo',
            'celular_representante_legal': 'Celular',
            'empleado': 'Empleado',
            'tipo_contrato': 'Tipo de Contrato',
            'cargo_contrato': 'Cargo en el Contrato',
            'salario': 'Salario',
            'duracion_contrato': 'Duración del Contrato',
            'fecha_inicio': 'Fecha de Inicio',
            'fecha_terminacion': 'Fecha de Terminación',
            'fecha_pre_aviso': 'Fecha de Pre-aviso',
            'estado': 'Estado',
            'adjunto_contrato': 'Adjunto del Contrato',
            'adjunto_preaviso': 'Adjunto del Pre-aviso',
        }
    
    def __init__(self, *args, **kwargs):
        super(ContratoForm, self).__init__(*args, **kwargs)
        self.helper = FormHelper()
        self.helper.form_method = 'post'
        self.helper.add_input(Submit('submit', 'Crear', style='background-color: #003594;'))

        self.fields['salario'].widget = forms.TextInput(attrs={
            'id': 'id_salario',
            'type': 'text',
            'maxlength': '15'
        })

        self.fields['razón_social'].widget.attrs['readonly'] = True
        self.fields['nit_empresa'].widget.attrs['readonly'] = True
        self.fields['ubicacion'].widget.attrs['readonly'] = True
        self.fields['direccion_notificacion_judicial'].widget.attrs['readonly'] = True
        self.fields['nombre_representante_legal'].widget.attrs['readonly'] = True
        self.fields['cargo_representante_legal'].widget.attrs['readonly'] = True
        self.fields['tipo_doc_representante_legal'].widget.attrs['readonly'] = True
        self.fields['numero_doc_representante_legal'].widget.attrs['readonly'] = True
        self.fields['lugar_expedicion_doc_representante_legal'].widget.attrs['readonly'] = True
        self.fields['correo_representante_legal'].widget.attrs['readonly'] = True
        self.fields['celular_representante_legal'].widget.attrs['readonly'] = True

        self.helper.layout = Layout(
            Fieldset(
                'DATOS DE LA EMPRESA',
                Row(
                    Column('razón_social', css_class='form-group col-md-4 mb-3'),
                    Column('nit_empresa', css_class='form-group col-md-4 mb-3'),
                    Column('ubicacion', css_class='form-group col-md-4 mb-3'),
                ),
                Row(
                    Column('direccion_notificacion_judicial', css_class='form-group col-md-4 mb-3'),
                ),
                css_class='seccion-container'
            ),

            Fieldset (
                'DATOS DEL REPRESENTANTE LEGAL',
                Row(
                    Column('nombre_representante_legal', css_class='form-group col-md-4 mb-3'),
                    Column('cargo_representante_legal', css_class='form-group col-md-4 mb-3'),
                    Column('tipo_doc_representante_legal', css_class='form-group col-md-4 mb-3'),
                ),
            Row(
                    Column('numero_doc_representante_legal', css_class='form-group col-md-4 mb-3'),
                    Column('lugar_expedicion_doc_representante_legal', css_class='form-group col-md-4 mb-3'),
                    Column('correo_representante_legal', css_class='form-group col-md-4 mb-3'),
                ),
            Row(
                    Column('celular_representante_legal', css_class='form-group col-md-4 mb-3'),
                ),
            css_class='seccion-container'
            ),
            Fieldset(
                'DATOS DEL EMPLEADO',
                'empleado',
                css_class='seccion-container'
            ),
            Fieldset(
                'DATOS DEL CONTRATO',
                Row(
                    Column('tipo_contrato', css_class='form-group col-md-4 mb-3'),
                    Column('cargo_contrato', css_class='form-group col-md-4 mb-3'),
                    Column('salario', id='salario'),
                ),
                Row(
                    Column('duracion_contrato', css_class='form-group col-md-4 mb-3'),
                    Column('fecha_inicio', css_class='form-group col-md-4 mb-3'),
                    Column('fecha_terminacion', css_class='form-group col-md-4 mb-3'),
                ),
                Row(
                    Column('fecha_pre_aviso', css_class='form-group col-md-4 mb-3'),
                    Column('estado', css_class='form-group col-md-4 mb-3'),
                ),
                css_class='seccion-container'
            ),
            Fieldset(
                'CONTRATO',
                'adjunto_contrato',
                css_class='seccion-container adjuntos'
            ),
            Row(
                Column('fecha_carga_adjunto_contrato', css_class='form-group col-md-4 mb-3', style="display:none;"),
            )
        )
        self.fields['fecha_inicio'].widget.attrs['class'] = 'datepicker'
        self.fields['fecha_terminacion'].widget.attrs['class'] = 'datepicker'
        self.fields['fecha_pre_aviso'].widget.attrs['class'] = 'datepicker'
        self.fields['fecha_inicio'].widget.attrs['readonly'] = True
        self.fields['fecha_terminacion'].widget.attrs['readonly'] = True
        self.fields['fecha_pre_aviso'].widget.attrs['readonly'] = True

        if not self.instance.pk:
            del self.fields['adjunto_preaviso']

    def clean_salario(self):
        salario = self.cleaned_data['salario']
        salario = salario.replace('.', '')
        return salario
    

class ContratoEditForm(forms.ModelForm):
    class Meta:
        model = Contrato
        fields = '__all__'
        exclude = ['fecha_publicacion_preaviso']
        labels = {
            'razón_social': 'Razón Social',
            'nit_empresa': 'NIT de la Empresa',
            'ubicacion': 'Ubicación',
            'direccion_notificacion_judicial': 'Dirección de Notificación Judicial',
            'nombre_representante_legal': 'Nombre',
            'cargo_representante_legal': 'Cargo',
            'tipo_doc_representante_legal': 'Tipo de Documento',
            'numero_doc_representante_legal': 'Número de Documento',
            'lugar_expedicion_doc_representante_legal': 'Lugar de Expedición',
            'correo_representante_legal': 'Correo',
            'celular_representante_legal': 'Celular',
            'empleado': 'Empleado',
            'tipo_contrato': 'Tipo de Contrato',
            'cargo_contrato': 'Cargo en el Contrato',
            'salario': 'Salario',
            'duracion_contrato': 'Duración del Contrato',
            'fecha_inicio': 'Fecha de Inicio',
            'fecha_terminacion': 'Fecha de Terminación',
            'fecha_pre_aviso': 'Fecha de Pre-aviso',
            'estado': 'Estado',
            'adjunto_contrato': 'Adjunto del Contrato',
            'adjunto_preaviso': 'Adjunto del Pre-aviso',
        }

    def __init__(self, *args, **kwargs):
        super(ContratoEditForm, self).__init__(*args, **kwargs)
        self.helper = FormHelper()
        self.helper.form_method = 'post'
        self.helper.add_input(Submit('submit', 'Guardar cambios'))
        
        self.fields['razón_social'].widget.attrs['readonly'] = True
        self.fields['nit_empresa'].widget.attrs['readonly'] = True
        self.fields['ubicacion'].widget.attrs['readonly'] = True
        self.fields['direccion_notificacion_judicial'].widget.attrs['readonly'] = True
        self.fields['nombre_representante_legal'].widget.attrs['readonly'] = True
        self.fields['cargo_representante_legal'].widget.attrs['readonly'] = True
        self.fields['tipo_doc_representante_legal'].widget.attrs['readonly'] = True
        self.fields['numero_doc_representante_legal'].widget.attrs['readonly'] = True
        self.fields['lugar_expedicion_doc_representante_legal'].widget.attrs['readonly'] = True
        self.fields['correo_representante_legal'].widget.attrs['readonly'] = True
        self.fields['celular_representante_legal'].widget.attrs['readonly'] = True

        self.helper.layout = Layout(
            Fieldset(
                'DATOS DE LA EMPRESA',
                Row(
                    Column('razón_social', css_class='form-group col-md-4 mb-3'),
                    Column('nit_empresa', css_class='form-group col-md-4 mb-3'),
                    Column('ubicacion', css_class='form-group col-md-4 mb-3'),
                ),
                Row(
                    Column('direccion_notificacion_judicial', css_class='form-group col-md-4 mb-3'),
                ),
                css_class='seccion-container'
            ),

            Fieldset (
                'DATOS DEL REPRESENTANTE LEGAL',
                Row(
                    Column('nombre_representante_legal', css_class='form-group col-md-4 mb-3'),
                    Column('cargo_representante_legal', css_class='form-group col-md-4 mb-3'),
                    Column('tipo_doc_representante_legal', css_class='form-group col-md-4 mb-3'),
                ),
            Row(
                    Column('numero_doc_representante_legal', css_class='form-group col-md-4 mb-3'),
                    Column('lugar_expedicion_doc_representante_legal', css_class='form-group col-md-4 mb-3'),
                    Column('correo_representante_legal', css_class='form-group col-md-4 mb-3'),
                ),
            Row(
                    Column('celular_representante_legal', css_class='form-group col-md-4 mb-3'),
                ),
            css_class='seccion-container'
            ),
            Fieldset(
                'DATOS DEL EMPLEADO',
                'empleado',
                css_class='seccion-container'
            ),
            Fieldset(
                'DATOS DEL CONTRATO',
                Row(
                    Column('tipo_contrato', css_class='form-group col-md-4 mb-3'),
                    Column('cargo_contrato', css_class='form-group col-md-4 mb-3'),
                    Column('salario', css_class='form-group col-md-4 mb-3'),
                ),
                Row(
                    Column('duracion_contrato', css_class='form-group col-md-4 mb-3'),
                    Column('fecha_inicio', css_class='form-group col-md-4 mb-3'),
                    Column('fecha_terminacion', css_class='form-group col-md-4 mb-3'),
                ),
                Row(
                    Column('fecha_pre_aviso', css_class='form-group col-md-4 mb-3'),
                    Column('estado', css_class='form-group col-md-4 mb-3'),
                ),
                css_class='seccion-container'
            ),
            Fieldset(
                'CONTRATO',
                'adjunto_contrato',
                css_class='seccion-container adjuntos'
            ),
            Fieldset(
                'PRE-AVISO',
                'adjunto_preaviso',
                css_class='seccion-container adjuntos'
            ),
                Row(
                    Column('fecha_carga_adjunto_contrato', css_class='form-group col-md-4 mb-3', style="display:none;"),
                    Column('fecha_publicacion_preaviso', css_class='form-group col-md-4 mb-3', style="display:none;")
                )
            )
        self.fields['fecha_inicio'].widget.attrs['class'] = 'datepicker'
        self.fields['fecha_terminacion'].widget.attrs['class'] = 'datepicker'
        self.fields['fecha_pre_aviso'].widget.attrs['class'] = 'datepicker'
        self.fields['fecha_inicio'].widget.attrs['readonly'] = True
        self.fields['fecha_terminacion'].widget.attrs['readonly'] = True
        self.fields['fecha_pre_aviso'].widget.attrs['readonly'] = True

    def save(self, commit=True):
        contrato = super(ContratoEditForm, self).save(commit=False)
        if self.cleaned_data.get('adjunto_preaviso'):
            contrato.fecha_publicacion_preaviso = timezone.now().date()
        if commit:
            contrato.save()
        return contrato