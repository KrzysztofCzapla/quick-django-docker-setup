from text_to_insert.dockerfile_to_insert import get_dockerfile_without_poetry, get_dockerfile_without_poetry
from utils import create_file_and_insert, create_folder


class EnvFile:
    def __init__(self, use_postgres: bool, use_poetry: bool, outer_foldername: str):
        self.env_filepath = f"./{outer_foldername}/config/.env"
        self.env_template_filepath = f"./{outer_foldername}/config/.env.template"
        self.outer_foldername = outer_foldername

        self.use_poetry = use_poetry
        self.use_postgres = use_postgres

    def create_config_folder(self):
        create_folder(f"{self.outer_foldername}/config")

    def insert_in_dockerfile(self):
        text_to_insert = get_dockerfile_without_poetry(self.outer_foldername) if self.use_poetry else get_dockerfile_without_poetry(self.outer_foldername)

        create_file_and_insert(
            self.dockerfile_filepath, text_to_insert
        )

    def run(self):
        self.create_config_folder()

        self.insert_in_dockerfile()
