

def main():
    poetry = input('Do You want to use Poetry as dependency manager? [yN] ').strip().lower()

    postgres = input('Do You want to use dockerized PostgreSQL as Your Database? [yN] ').strip().lower()

    celery = input('Do You want to use dockerized Celery with Redis for Asynchronous tasks? [yN] ').strip().lower()

    jwt = input('Do You want to use JWT Authentication provided by "dj_rest_auth" package? [yN] ').strip().lower()

    project_name = input('How do You want to name the project? ').strip().lower()

    folder_name = input('How do You want to name the folder with Django code? ').strip().lower()


if __name__ == '__main__':
    main()
