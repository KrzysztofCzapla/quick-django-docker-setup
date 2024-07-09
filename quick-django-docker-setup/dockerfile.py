from text_to_insert.dockerfile_to_insert import get_dockerfile_without_poetry, get_dockerfile_with_poetry
from utils import create_file_and_insert, create_folder


class Dockerfile:
    def __init__(self, use_poetry: bool, outer_foldername: str):
        self.dockerfile_filepath = f"./deployment/docker/Dockerfile"
        self.outer_foldername = outer_foldername

        self.use_poetry = use_poetry

    def create_deployment_and_docker_folders(self):
        create_folder("deployment")
        create_folder("deployment/docker")

    def insert_in_dockerfile(self):
        text_to_insert = get_dockerfile_with_poetry(self.outer_foldername) if self.use_poetry else get_dockerfile_without_poetry(self.outer_foldername)

        create_file_and_insert(
            self.dockerfile_filepath, text_to_insert
        )

    def run(self):
        self.create_deployment_and_docker_folders()

        self.insert_in_dockerfile()
