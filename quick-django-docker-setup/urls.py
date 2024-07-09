from text_to_insert.urls_to_insert import imports, schema_view, swagger_path
from utils import insert_text_at_line, change_text_at_line


class Urls:
    def __init__(
        self,
        use_jwt: bool,
        use_registration: bool,
        use_swagger: bool,
        outer_folder_name: str,
        inner_folder_name: str,
    ):
        self.use_jwt = use_jwt
        self.use_registration = use_registration
        self.use_swagger = use_swagger
        self.inner_folder_name = inner_folder_name
        self.filepath = f"./{outer_folder_name}/{inner_folder_name}/urls.py"

        self.important_lines = {"imports_last_line": 19, "patterns_last_line": 22}

    def insert_text_in_urls(self, line: int, text: str):
        insert_text_at_line(self.filepath, line, text)

    def change_text_in_urls(self, line: int, text: str):
        change_text_at_line(self.filepath, line, text)

    def add_to_important_lines(self, number: int = 1):
        for key in self.important_lines:
            self.important_lines[key] += number

    def add_imports(self):
        self.change_text_in_urls(18, "from django.urls import include, path")

        if self.use_swagger:
            self.insert_text_in_urls(self.important_lines["imports_last_line"], imports)
            self.add_to_important_lines(3)

    def add_schema_view(self):
        self.insert_text_in_urls(self.important_lines["imports_last_line"], schema_view)
        self.change_text_in_urls(25, f'        title="{self.inner_folder_name}",')
        self.add_to_important_lines(13)

    def add_paths(self):
        if self.use_jwt:
            self.insert_text_in_urls(
                self.important_lines["imports_last_line"],
                '    path("auth/", include("dj_rest_auth.urls")),',
            )
            self.add_to_important_lines()

        if self.use_registration:
            self.insert_text_in_urls(
                self.important_lines["imports_last_line"],
                '    path("auth/registration/", include("dj_rest_auth.registration.urls")),',
            )
            self.add_to_important_lines()

        if self.use_swagger:
            self.insert_text_in_urls(
                self.important_lines["imports_last_line"], swagger_path
            )
            self.add_to_important_lines(5)

    def run(self):
        self.add_imports()

        if self.use_swagger:
            self.add_schema_view()

        self.add_paths()
