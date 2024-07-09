from text_to_insert.celery_to_insert import init_text, celery_to_insert
from text_to_insert.docker_compose_to_insert import dockerignore
from text_to_insert.dockerfile_to_insert import dockerfile_with_poetry, dockerfile_without_poetry
from utils import create_file_and_insert, create_folder


class Dockerfile:
    def __init__(self, use_postgres: bool, use_celery: bool):
        self.dockerfile_filepath = f"./deployment/docker/Dockerfile.py"

        self.use_postgres = use_postgres
        self.use_celery = use_celery

    def get_docker_compose_text(self):


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
