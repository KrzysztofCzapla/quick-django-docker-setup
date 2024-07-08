import subprocess

def create_django_project(backend_folder: bool, project_name: str):
    result = subprocess.run(["dir"], shell=True, capture_output=True, text=True)

    print(result.stdout)