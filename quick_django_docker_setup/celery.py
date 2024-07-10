from quick_django_docker_setup.text_to_insert.celery_to_insert import (
    init_text,
    celery_to_insert,
)
from quick_django_docker_setup.utils import insert_text_at_line, create_file_and_insert


class Celery:
    def __init__(self, outer_folder_name: str, inner_folder_name: str):
        self.inner_folder_name = inner_folder_name
        self.celery_filepath = f"./{outer_folder_name}/{inner_folder_name}/celery.py"
        self.init_filepath = f"./{outer_folder_name}/{inner_folder_name}/__init__.py"

    def insert_in_init(self):
        insert_text_at_line(self.init_filepath, 0, init_text)

    def insert_in_celery(self):
        create_file_and_insert(
            self.celery_filepath, celery_to_insert(self.inner_folder_name)
        )

    def run(self):
        self.insert_in_init()

        self.insert_in_celery()
