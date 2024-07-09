from text_to_insert.celery_to_insert import init_text, celery_to_insert
from text_to_insert.docker_compose_to_insert import dockerignore, get_backend_service_text, get_database_service_text, \
    get_celery_service_text, get_volume_text
from text_to_insert.dockerfile_to_insert import dockerfile_with_poetry, dockerfile_without_poetry
from utils import create_file_and_insert, create_folder


class Dockerfile:
    def __init__(self, use_postgres: bool, use_celery: bool, outer_foldername: str):
        self.dockerfile_filepath = f"./deployment/docker/Dockerfile.py"
        self.outer_foldername = outer_foldername

        self.use_postgres = use_postgres
        self.use_celery = use_celery

    def get_docker_compose_text(self):
        text = get_backend_service_text(use_postgres=self.use_postgres, outer_foldername=self.outer_foldername)

        if self.use_postgres: text += get_database_service_text(outer_foldername=self.outer_foldername)

        if self.use_celery: text += get_celery_service_text(use_postgres=self.use_postgres, outer_foldername=self.outer_foldername)

        if self.use_postgres: text += get_volume_text()

        return text

    def setup_docker_compose(self):
        create_file_and_insert(
            "docker-compose.yml", self.get_docker_compose_text()
        )

    def setup_docker_ignore(self):
        create_file_and_insert(
            ".dockerignore", dockerignore
        )

    def run(self):
        self.set_up_docker_ignore()

        self.setup_docker_compose()
