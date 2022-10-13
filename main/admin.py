from django.contrib import admin
from .models import *
# Register your models here.


class AreaAdmin(admin.ModelAdmin):
    """Класс, описывающий настройки для модели Area в админке Django"""
    list_display = ('name',)


admin.site.register(Area, AreaAdmin)
admin.site.register(Fertility)
admin.site.register(Lifeextantion)
admin.site.register(Mortality)
admin.site.register(Years)
