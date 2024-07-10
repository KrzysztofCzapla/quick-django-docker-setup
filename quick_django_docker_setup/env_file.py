from quick_django_docker_setup.text_to_insert.env_file_to_insert import get_env_file_text, get_env_temp_file_text
from quick_django_docker_setup.utils import create_file_and_insert, create_folder


class EnvFile:
    def __init__(self, use_postgres: bool, use_celery: bool, outer_foldername: str):
        self.env_filepath = f"./{outer_foldername}/config/.env"
        self.env_template_filepath = f"./{outer_foldername}/config/.env.template"
        self.outer_foldername = outer_foldername

        self.use_celery = use_celery
        self.use_postgres = use_postgres

    def create_config_folder(self):
        create_folder(f"{self.outer_foldername}/config")

    def insert_in_envs(self):
        create_file_and_insert(
            self.env_filepath, get_env_file_text(use_postgres=self.use_postgres, use_celery=self.use_celery)
        )

        create_file_and_insert(
            self.env_template_filepath, get_env_temp_file_text(use_postgres=self.use_postgres, use_celery=self.use_celery)
        )

    def run(self):
        self.create_config_folder()

        self.insert_in_envs()
