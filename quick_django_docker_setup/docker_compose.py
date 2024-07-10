from quick_django_docker_setup.text_to_insert.docker_compose_to_insert import dockerignore, get_backend_service_text, get_database_service_text, \
    get_celery_service_text, get_volume_text
from quick_django_docker_setup.utils import create_file_and_insert


class DockerCompose:
    def __init__(self, use_postgres: bool, use_celery: bool, outer_foldername: str, project_name: str):
        self.dockerfile_filepath = f"./deployment/docker/Dockerfile.py"
        self.outer_foldername = outer_foldername
        self.project_name = project_name

        self.use_postgres = use_postgres
        self.use_celery = use_celery

    def get_docker_compose_text(self):
        text = get_backend_service_text(use_postgres=self.use_postgres, outer_foldername=self.outer_foldername)

        if self.use_postgres: text += get_database_service_text(outer_foldername=self.outer_foldername)

        if self.use_celery: text += get_celery_service_text(use_postgres=self.use_postgres, outer_foldername=self.outer_foldername, project_name=self.project_name)

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
        self.setup_docker_ignore()

        self.setup_docker_compose()
