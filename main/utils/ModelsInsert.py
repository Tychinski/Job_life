from main.models import *


class ModelsInsert:
    def __init__(self, model_name):
        self.model_name = model_name

    def handle(self, serialized_data):
        handler = self.__get_insert_handler()
        return handler(serialized_data)

    def __get_insert_handler(self):
        if self.model_name == 'area':
            return self.__area_insert_handler

    def __area_insert_handler(self, serialized_data):
        entries = []
        for data_dict in serialized_data:
            entries.append(Area(**data_dict))
        Area.objects.bulk_create(entries)

    def __years_insert_handler(self, serialized_data):
        entries = []
        for data_dict in serialized_data:
            entries.append(Years(**data_dict))
        Years.objects.bulk_create(entries)

    def __mortality_insert_handler(self, serialized_data):
        for data_dict in serialized_data:
            pass
