from text_to_insert.celery_to_insert import init_text, celery_to_insert
from text_to_insert.dockerfile_to_insert import dockerfile_with_poetry, dockerfile_without_poetry
from utils import create_file_and_insert, create_folder


class Dockerfile:
    def __init__(self, use_poetry: bool):
        self.dockerfile_filepath = f"./deployment/docker/Dockerfile.py"

        self.use_poetry = use_poetry

    def create_deployment_and_docker_folders(self):
        create_folder("deployment")
        create_folder("deployment/docker")

    def insert_in_dockerfile(self):
        text_to_insert = dockerfile_with_poetry if self.use_poetry else dockerfile_without_poetry

        create_file_and_insert(
            self.dockerfile_filepath, text_to_insert
        )

    def run(self):
        self.create_deployment_and_docker_folders()

        self.insert_in_dockerfile()
