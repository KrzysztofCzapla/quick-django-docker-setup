import subprocess
import sys
import shutil
from utils import create_file_and_insert


class PackageManager:
    def __init__(
            self,
            use_postgres: bool,
            use_poetry: bool,
            use_jwt: bool,
            use_registration: bool,
            use_celery: bool,
            use_swagger: bool,
            project_name: str,
            outer_foldername: str
    ):
        self.project_name = project_name
        self.outer_foldername = outer_foldername

        self.use_poetry = use_poetry
        self.use_postgres = use_postgres
        self.use_jwt = use_jwt
        self.use_registration = use_registration
        self.use_celery = use_celery
        self.use_swagger = use_swagger

    def check_poetry_installed(self):
        try:
            subprocess.run(
                [sys.executable, '-m', 'pip', 'show', 'poetry'],
                check=True,
                stdout=subprocess.DEVNULL,
                stderr=subprocess.DEVNULL
            )
            return True
        except subprocess.CalledProcessError:
            return False

    def install_poetry(self):
        subprocess.run(
            [sys.executable, '-m', 'pip', 'install', 'poetry'],
            check=True,
            stdout=subprocess.DEVNULL,
            stderr=subprocess.DEVNULL
        )

    def uninstall_poetry(self):
        subprocess.run(
            [sys.executable, '-m', 'pip', 'uninstall', '-y', 'poetry'],
            check=True,
            stdout=subprocess.DEVNULL,
            stderr=subprocess.DEVNULL
        )

    def get_dependencies(self):
        dependencies = ["django", "django-environ", "djangorestframework"]

        if self.use_postgres: dependencies.extend(["psycopg2-binary"])
        if self.use_jwt: dependencies.extend(["djangorestframework-simplejwt", "dj-rest-auth"])
        if self.use_registration: dependencies.extend(["dj-rest-auth[with_social]"])
        if self.use_celery: dependencies.extend(["celery[redis]", "django-celery-beat"])
        if self.use_swagger: dependencies.extend(["drf-yasg"])

        return dependencies

    def poetry_install_dependencies(self):
        subprocess.run(
            ["poetry", "init"],
            check=True,
            stdout=subprocess.DEVNULL,
            stderr=subprocess.DEVNULL
        )

        subprocess.run(
            ["poetry", "add"] + self.get_dependencies(),
            check=True,
            stdout=subprocess.DEVNULL,
            stderr=subprocess.DEVNULL
        )

        # copy poetry file into subfolder
        shutil.move("pyproject.toml", f"./{self.outer_foldername}/pyproject.toml")
        shutil.move("poetry.lock", f"./{self.outer_foldername}/poetry.lock")

    def run_requirements(self):
        text = "\n".join(dependency for dependency in self.get_dependencies())

        create_file_and_insert("requirements.txt", text)

    def run_poetry(self):
        if self.check_poetry_installed():
            self.poetry_install_dependencies()
        else:
            self.install_poetry()
            self.poetry_install_dependencies()
            self.uninstall_poetry()

    def run(self):
        if self.use_poetry:
            self.run_poetry()
        else:
            self.run_requirements()


