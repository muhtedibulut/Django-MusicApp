import os
from celery import Celery

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'MusicApp.settings')

app = Celery('MusicApp')
app.config_from_object('django.conf:settings', namespace='CELERY')
app.autodiscover_tasks()

@app.task(bind=True)
def debug_task(self):
    print('Request: {0!r}'.format(self.request))


"""@app.task
def add(x, y):
    return print(str(x + y))"""


"""@app.task
def reverse(string):
    return string[::-1]"""
