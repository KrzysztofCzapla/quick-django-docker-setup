from quick_django_docker_setup.celery import Celery
from quick_django_docker_setup.django_project import DjangoProject
from quick_django_docker_setup.docker_compose import DockerCompose
from quick_django_docker_setup.dockerfile import Dockerfile
from quick_django_docker_setup.env_file import EnvFile
from quick_django_docker_setup.package_manager import PackageManager
from quick_django_docker_setup.settings import Settings
from quick_django_docker_setup.utils import ask_questions


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
        Dockerfile(use_poetry=output["poetry"], outer_foldername=outer_folder_name),
        DockerCompose(
            use_postgres=output["postgres"],
            use_celery=output["celery"],
            outer_foldername=outer_folder_name,
            project_name=output["project_name"],
        ),
        PackageManager(
            use_postgres=output["postgres"],
            use_poetry=output["poetry"],
            use_jwt=output["jwt"],
            use_registration=output["registration"],
            use_celery=output["celery"],
            use_swagger=output["swagger"],
            project_name=output["project_name"],
            outer_foldername=outer_folder_name,
        ),
        EnvFile(
            use_postgres=output["postgres"],
            use_celery=output["celery"],
            outer_foldername=outer_folder_name,
        ),
    ]

    if output["celery"]:
        steps.append(
            Celery(
                outer_folder_name=outer_folder_name,
                inner_folder_name=output["project_name"],
            )
        )

    for step in steps:
        step.run()

    print("✨ Done ✨")


if __name__ == "__main__":
    main()
