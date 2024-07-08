from utils import create_django_project

def main():

    # poetry = input('Do You want to use Poetry as dependency manager? [yN] ').strip().lower()
    #
    # postgres = input('Do You want to use dockerized PostgreSQL as Your Database? [yN] ').strip().lower()
    #
    # celery = input('Do You want to use dockerized Celery with Redis for Asynchronous tasks? [yN] ').strip().lower()
    #
    # jwt = input('Do You want to use JWT Authentication provided by "dj_rest_auth" package? [yN] ').strip().lower()
    #
    # registration = input('Do You want to use registration provided by "dj_rest_auth" package? [yN] ').strip().lower()
    #
    # swagger = input('Do You want to use swagger as API Documentation? [yN] ').strip().lower()

    backend_folder = input('Do You want to put django code inside "backend" folder?  [yN] ').strip().lower()

    project_name = input('How do You want to name the project? ').strip().lower()

    create_django_project(backend_folder=backend_folder, project_name=project_name)


if __name__ == '__main__':
    main()
