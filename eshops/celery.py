import os
from celery import Celery

os.environ.setdefault("DJANGO_SETTINGS_MODULE", "eshops.settings")

app = Celery("eshops")

# Tell Celery to use settings.py with `CELERY_` prefix
app.config_from_object("django.conf:settings", namespace="CELERY")

# Auto-discover tasks in all installed apps
app.autodiscover_tasks()
