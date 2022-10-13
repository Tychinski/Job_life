import csv
import io
import os
import pandas as pd

from django.core.files.storage import default_storage
from Job_life.settings import BASE_DIR, MEDIA_ROOT
from main.models import *


class DataSerializer:
    """
    Класс для десериализации данных в структуру
    """
    def __init__(self, file_in_memory):
        self.file_in_memory = file_in_memory
        self.file_type = file_in_memory.name.split('.')[1]
        self.file_path = os.path.join(BASE_DIR, MEDIA_ROOT)

        self.skip_size = 0
        self.chunk_size = 4

    def save_file_to_media(self):
        try:
            file_name = default_storage.save(self.file_in_memory.name, self.file_in_memory)
        except Exception as e:
            print("Exception raised", e)
            raise Exception({"general_errors": "Error during file upload"})
        finally:
            self.file_path = os.path.join(self.file_path, file_name)

    def serializer(self):
        self.save_file_to_media()
        serializer = self._get_serializer(self.file_type)
        return serializer()

    def _get_serializer(self, file_format):
        if file_format == 'csv':
            return self._serialize_chunk_from_csv
        elif 'xls' in file_format:
            return self._serialize_from_excel

    @staticmethod
    def clean_dict(data):
        """Очищает словарь от всех невидимых символов"""

        return {key.strip(): item.strip() for key, item in data.items() if isinstance(item, str)}

    def _serialize_from_excel(self):
        pass

    def _serialize_chunk_from_csv(self):
        """Десериализует csv-файл в список из словарей"""
        data = pd.read_csv(self.file_path, delimiter=';',
                           chunksize=self.chunk_size,
                           skiprows=self.skip_size,
                           nrows=self.chunk_size,
                           encoding='utf-8-sig')
        self.skip_size += self.chunk_size

        data = pd.concat(data).drop('id', axis=1)

        return data.to_dict(orient='records')
