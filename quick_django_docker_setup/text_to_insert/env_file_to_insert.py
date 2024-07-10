def get_env_file_text(use_postgres: bool, use_celery: bool) -> str:
    text = """SECRET_KEY=django-insecure-(^*b^9afma4119+v*donkkox0cm9hduawhdai#$(*)
DEBUG=1
"""

    if use_postgres:
        text += """POSTGRES_DB=database
POSTGRES_USER=database
POSTGRES_PASSWORD=password
POSTGRES_HOST=database
POSTGRES_PORT=5432
"""

    if use_celery:
        text += """CELERY_BROKER_URL=redis://redis:6379/0
CELERY_RESULT_BACKEND=redis://redis:6379/0"""

    return text


def get_env_temp_file_text(use_postgres: bool, use_celery: bool) -> str:
    text = """SECRET_KEY={{change}}
DEBUG={{change}}
"""

    if use_postgres:
        text += """POSTGRES_DB={{change}}
POSTGRES_USER={{change}}
POSTGRES_PASSWORD={{change}}
POSTGRES_HOST={{change}}
POSTGRES_PORT=5432
"""

    if use_celery:
        text += """CELERY_BROKER_URL=redis://redis:6379/0
CELERY_RESULT_BACKEND=redis://redis:6379/0"""

    return text
