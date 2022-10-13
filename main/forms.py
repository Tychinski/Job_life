from django import forms
from django.apps import apps


class InsertForm(forms.Form):
    MODELS_LIST = apps.all_models['main'].keys()
    MODELS = zip(MODELS_LIST, MODELS_LIST)
    TYPES = ((0, 'Выберите тип добавления'),
             (1, 'csv/excel'),
             (2, 'ввести самому'))

    model = forms.ChoiceField(choices=MODELS,
                              label='')
    insert_type = forms.ChoiceField(choices=TYPES, label='')
    file_field = forms.FileField(label='')

