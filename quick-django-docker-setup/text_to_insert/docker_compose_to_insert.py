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

def get_backend_service_text(use_postgres: bool) -> str:
    text = """  backend:
    container_name: backend
    build:
      context: ./
      dockerfile: ./deployment/docker/Dockerfile
    command: python manage.py runserver 0.0.0.0:8000
    volumes:
      - ./backend/:/backend
    ports:
      - 8000:8000
    env_file:
      - ./backend/config/.env"""

    if use_postgres:
        text += """    depends_on:
      - database"""

    return text

def get_database_service_text() -> str:
    return """  database:
    container_name: database
    image: postgis/postgis:15-3.3-alpine
    env_file:
      - ./backend/config/.env
    volumes:
      - postgres-data:/var/lib/postgresql/data/"""

def get_celery_service_text(use_postgres: bool) -> str:
    