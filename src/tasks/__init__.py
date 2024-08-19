from celery import Celery
from tasks import celeryconfig

app = Celery()
app.config_from_object(celeryconfig)


# broker="pyamqp://guest@localhost//",
# backend="db+postgresql://myuser:mypassword@localhost:5432/mydatabase",
