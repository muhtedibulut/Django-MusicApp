import os
from celery import Celery

os.environ.setdefault("DJANGO_SETTINGS_MODULE", "music_app.settings")

app = Celery(
    "music_app", backend="redis://localhost", broker="redis://localhost:6379/0"
)
app.config_from_object("django.conf:settings", namespace="CELERY")
app.autodiscover_tasks()


@app.task(bind=True)
def debug_task(self):
    print("Request: {0!r}".format(self.request))


@app.task
def reverse(string):
    return string[::-1]
