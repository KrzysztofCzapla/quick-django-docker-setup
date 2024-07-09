print(123)
#
CELERY_RESULT_BACKEND = "django-db"
CELERY_CACHE_BACKEND = "default"

CACHES = {
    "default": {
        "BACKEND": "django.core.cache.backends.db.DatabaseCache",
        "LOCATION": "my_cache_table",
    }
}
123
#
print(321)
