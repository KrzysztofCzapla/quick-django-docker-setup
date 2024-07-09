from celery import Celery
from django_project import DjangoProject
from dockerfile import Dockerfile
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
        Dockerfile(use_poetry=output["poetry"])
    ]
    steps_len = len(steps)

    for i, step in enumerate(steps):
        print_progress(iteration=i, total=steps_len, current_task=step)
        step.run()


if __name__ == "__main__":
    main()
