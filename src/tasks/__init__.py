from celery import Celery
from tasks import celeryconfig
from tasks.utils import get_predict_tasks, get_load_tasks, get_load_result

__all__ = ["get_predict_tasks", "get_load_tasks", "get_load_result"]

app = Celery()
app.config_from_object(celeryconfig)
