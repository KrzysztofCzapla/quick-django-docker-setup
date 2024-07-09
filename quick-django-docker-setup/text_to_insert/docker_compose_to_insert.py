dockerignore = """**/.git
**/.gitignore
**/.vscode
**/coverage
**/.env
**/.aws
**/.ssh
Dockerfile
README.md
docker-compose.yml
**/.DS_Store
**/venv
**/env"""

def get_backend_service_text(use_postgres: bool, outer_foldername: str) -> str:
    text = f"""services:
  backend:
    container_name: backend
    build:
      context: ./
      dockerfile: ./deployment/docker/Dockerfile
    command: python manage.py runserver 0.0.0.0:8000
    volumes:
      - ./{outer_foldername}/:/{outer_foldername}
    ports:
      - 8000:8000
    env_file:
      - ./{outer_foldername}/config/.env"""

    if use_postgres:
        text += """    depends_on:
      - database"""

    return text

def get_database_service_text(outer_foldername: str) -> str:
    return f"""  database:
    container_name: database
    image: postgis/postgis:15-3.3-alpine
    env_file:
      - ./{outer_foldername}/config/.env
    volumes:
      - postgres-data:/var/lib/postgresql/data/
      """

def get_celery_service_text(use_postgres: bool, outer_foldername: str) -> str:
    if use_postgres:
        database_text = """
              - database"""
    else:
        database_text = ""

    return f"""  redis:
    container_name: redis
    image: redis:alpine
    env_file:
      - ./{outer_foldername}/config/.env
    expose:
      - 6379

  celery-worker:
    container_name: celery-worker
    build:
      context: ./
      dockerfile: ./deployment/docker/Dockerfile
    command: celery -A college_enrolment_system worker -l info
    volumes:
      - ./{outer_foldername}/:/{outer_foldername}
    env_file:
      - ./{outer_foldername}/config/.env
    depends_on:
      - redis{database_text}

  celery-beat:
    container_name: celery-beat
    build:
      context: ./
      dockerfile: ./deployment/docker/Dockerfile
    command: celery -A college_enrolment_system beat -l info
    volumes:
      - ./{outer_foldername}/:/{outer_foldername}
    env_file:
      - ./{outer_foldername}/config/.env
    depends_on:
      - redis
      - celery-worker{database_text}"""


def get_volume_text() -> str:
    return """
volumes:
  postgres-data:"""
