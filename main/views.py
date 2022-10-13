import csv
import io

from django.shortcuts import render, HttpResponse, HttpResponseRedirect
from django.core.files.storage import default_storage
from django.apps import apps
from .forms import InsertForm
from .utils.DataSerializer import DataSerializer
from .utils.ModelsInsert import ModelsInsert

def is_ajax(request):
    return request.META.get('HTTP_X_REQUESTED_WITH') == 'XMLHttpRequest'


def index(request):
    """Главная страница проекта"""
    return render(request, 'main/main_index.html')


def data_page(request):
    """Страница для добавления данных в БД"""
    if request.method == "GET":
        form = InsertForm()
        context = {"models": {}, "form": form}

        # Словарь всех моделей из БД
        models = apps.all_models['main']

        # Формируем контекст для страницы
        for model, value in models.items():
            context["models"].setdefault(model,
                                         [item.name for item in value._meta.concrete_fields if item.name != "id"])
        return render(request, 'main/data_insert.html', context)
    if request.method == "POST":
        serializer = DataSerializer(request.FILES['file_field'])
        dict_data = serializer.serializer()
        model_insert = ModelsInsert(request.POST['model'])
        model_insert.handle(dict_data)
        return HttpResponseRedirect('/insert')
