from celery import Celery
from django_project import DjangoProject
from docker_compose import DockerCompose
from dockerfile import Dockerfile
from env_file import EnvFile
from package_manager import PackageManager
from settings import Settings
from utils import ask_questions, print_progress


def main():

    output = ask_questions()

    outer_folder_name = (
        "backend" if output["backend_folder"] else output["project_name"]
    )

    steps = [
        DjangoProject(
            backend_folder=output["backend_folder"], project_name=output["project_name"]
        ),
        Settings(
            use_postgres=output["postgres"],
            use_jwt=output["jwt"],
            use_registration=output["registration"],
            use_celery=output["celery"],
            use_swagger=output["swagger"],
            outer_folder_name=outer_folder_name,
            inner_folder_name=output["project_name"],
        ),
        Celery(outer_folder_name=outer_folder_name, inner_folder_name=output["project_name"],),
        Dockerfile(use_poetry=output["poetry"], outer_foldername=outer_folder_name),
        DockerCompose(use_postgres=output["postgres"], use_celery=output["celery"], outer_foldername=outer_folder_name),
        PackageManager(
            use_postgres=output["postgres"],
            use_poetry=output["poetry"],
            use_jwt=output["jwt"],
            use_registration=output["registration"],
            use_celery=output["celery"],
            use_swagger=output["swagger"],
            project_name=output["project_name"],
            outer_foldername=outer_folder_name),
        EnvFile(use_postgres=output["postgres"], use_celery=output["celery"], outer_foldername=outer_folder_name)
    ]
    steps_len = len(steps)

    for i, step in enumerate(steps):
        print_progress(iteration=i, total=steps_len, current_task=step)
        step.run()

    print("✨ Done ✨")


if __name__ == "__main__":
    main()
