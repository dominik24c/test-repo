import os

from celery import Celery
from celery.schedules import crontab

os.environ.setdefault("DJANGO_SETTINGS_MODULE", "app.settings")

app = Celery("app")
app.config_from_object("django.conf:settings", namespace="CELERY")

app.conf.beat_schedule = {
    'print-message-ten-seconds': {
        'task': 'print_msg_main',  
        'schedule': 10.0,
        'args': ("Hello",) 
    },
    'print-time-twenty-seconds': {
        'task': 'print_time',  
        'schedule': 20.0, 
    },
    #Scheduler Name
    'calculate-forty-seconds': {
        'task': 'get_calculation',  
        'schedule': 40.0,
        'args': (10,20) 
    },

}

app.autodiscover_tasks()
