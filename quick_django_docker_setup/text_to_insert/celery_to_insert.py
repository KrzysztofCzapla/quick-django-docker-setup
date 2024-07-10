def celery_to_insert(project_name: str) -> str:
    return f"""import os

from celery import Celery

# Set the default Django settings module for the 'celery' program.
os.environ.setdefault("DJANGO_SETTINGS_MODULE", "{project_name}.settings")

app = Celery("{project_name}")

# Using a string here means the worker doesn't have to serialize
# the configuration object to child processes.
# - namespace='CELERY' means all celery-related configuration keys
#   should have a `CELERY_` prefix.
app.config_from_object("django.conf:settings", namespace="CELERY")

# Load task modules from all registered Django apps.
app.autodiscover_tasks()

app.conf.beat_scheduler = "django_celery_beat.schedulers:DatabaseScheduler"
"""


init_text = """from .celery import app as celery_app

__all__ = ("celery_app",)
"""
