import os
import subprocess
import sys
import shutil
import venv


class DjangoProject:
    def __init__(self, project_name: str, backend_folder: bool):
        self.env_path = os.path.join(os.getcwd(), "temp_env")
        self.project_name = project_name
        self.backend_folder = backend_folder

    def django_is_installed(self):
        try:
            subprocess.check_call(
                [sys.executable, "-m", "django", "--version"],
                stdout=subprocess.DEVNULL,
                stderr=subprocess.DEVNULL,
            )
            return True
        except subprocess.CalledProcessError:
            return False

    def create_virtualenv(self):
        venv.create(self.env_path, with_pip=True)

    def install_django_in_venv(self):
        pip_path = os.path.join(self.env_path, "Scripts", "pip.exe")
        subprocess.check_call(
            [pip_path, "install", "django"],
            stdout=subprocess.DEVNULL,
            stderr=subprocess.DEVNULL,
        )

    def execute_django_command_in_venv(self):
        self.create_virtualenv()
        self.install_django_in_venv()

        python_path = os.path.join(self.env_path, "Scripts", "python.exe")
        subprocess.check_call(
            [python_path, "-m", "django", "startproject", self.project_name]
        )

        shutil.rmtree(self.env_path)

    def execute_django_command(self):
        subprocess.check_call(
            [sys.executable, "-m", "django", "startproject", self.project_name]
        )

    def rename_outer_folder(self):
        os.rename("./" + self.project_name, "./backend")

    def run(self):
        if self.django_is_installed():
            self.execute_django_command()
        else:
            self.execute_django_command_in_venv()

        if self.backend_folder:
            self.rename_outer_folder()

    def __str__(self):
        return "Django Files"
