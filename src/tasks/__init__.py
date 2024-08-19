from celery import Celery
from tasks import celeryconfig
from tasks.utils import get_predict_tasks, get_load_tasks

__all__ = ["get_predict_tasks", "get_load_tasks"]

app = Celery()
app.config_from_object(celeryconfig)
