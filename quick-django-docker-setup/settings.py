from settings_to_insert import postgres_db, rest_framework_jwt, rest_framework_no_jwt, jwt, registration, celery, \
    swagger
from utils import insert_text_at_line, change_text_at_line


class Settings:
    def __init__(self, use_postgres: bool, use_jwt: bool, use_registration: bool, use_celery: bool, use_swagger: bool,
                 outer_folder_name: str, inner_folder_name: str):
        self.use_postgres = use_postgres
        self.use_jwt = use_jwt
        self.use_registration = use_registration
        self.use_celery = use_celery
        self.use_swagger = use_swagger
        self.filepath = f"./{outer_folder_name}/{inner_folder_name}/settings.py"

        # lines positions after environ
        self.installed_apps_ending_line = 43
        self.middleware_ending_line = 53
        self.db_engine_line = 81
        self.db_name_line = 82
        self.db_last_line = 83
        self.last_line = 127

        self.important_lines = [self.installed_apps_ending_line, self.middleware_ending_line,
                                self.db_engine_line, self.db_name_line, self.db_last_line, self.last_line]

    def insert_text_in_settings(self, line: int, text: str):
        insert_text_at_line(self.filepath, line, text)

    def change_text_in_settings(self, line: int, text: str):
        change_text_at_line(self.filepath, line, text)

    def add_to_important_lines(self, number: int = 1):
        for line in self.important_lines:
            line += 1

    def environ_on_secret_and_debug(self):
        self.insert_text_in_settings(14, "import environ")
        self.insert_text_in_settings(19, "env = environ.Env()")
        self.insert_text_in_settings(20, 'environ.Env.read_env("config/.env")')
        self.change_text_in_settings(26, 'SECRET_KEY = env("SECRET_KEY")')
        self.change_text_in_settings(29, 'DEBUG = env("DEBUG")')

    def edit_installed_apps(self):
        apps_list = ["rest_framework"]
        if self.use_jwt: apps_list.extend(["rest_framework.authtoken", "dj_rest_auth"])
        if self.use_registration: apps_list.extend(["allauth", "allauth.account", "allauth.socialaccount", "dj_rest_auth.registration"])
        if self.use_swagger: apps_list.append("drf_yasg")
        if self.use_celery: apps_list.append("django_celery_beat")

        for app in apps_list:
            app_name = f"    '{app}',"
            self.insert_text_in_settings(self.installed_apps_ending_line, app_name)
            self.add_to_important_lines()

    def add_postgres(self):
        self.change_text_in_settings(self.db_engine_line, '        "ENGINE": "django.db.backends.postgresql"')
        self.change_text_in_settings(self.db_name_line, '        "NAME": env("POSTGRES_DB"),')
        self.add_to_important_lines(2)

        self.insert_text_in_settings(self.db_last_line, postgres_db)
        self.add_to_important_lines(4)

    def add_rest_framework(self):
        if self.use_jwt:
            self.insert_text_in_settings(self.last_line, rest_framework_jwt)
            self.add_to_important_lines(3)
        else:
            self.insert_text_in_settings(self.last_line, rest_framework_no_jwt)
            self.add_to_important_lines(6)

    def add_jwt(self):
        self.insert_text_in_settings(self.last_line, jwt)
        self.add_to_important_lines(5)

    def add_registration(self):
        self.insert_text_in_settings(self.last_line, registration)
        self.add_to_important_lines(3)

    def add_celery(self):
        self.insert_text_in_settings(self.last_line, celery)
        self.add_to_important_lines(10)

    def add_swagger(self):
        self.insert_text_in_settings(self.last_line, swagger)
        self.add_to_important_lines(1)

    def run(self):
        self.environ_on_secret_and_debug()
        self.edit_installed_apps()

        if self.use_postgres: self.add_postgres()

        self.add_rest_framework()

        if self.use_jwt: self.add_jwt()

        if self.use_registration: self.add_registration()

        if self.use_celery: self.add_celery()

        if self.use_swagger: self.use_swagger()

