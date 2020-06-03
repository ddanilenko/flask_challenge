"""Celery app module"""
from celery import Celery
from celery.utils.log import get_task_logger

logger = get_task_logger(__name__)


def create_celery_app(flask_app):
    """Configures celery app

    Args:
        app (object): Flask application object

    Returns:
        object: configured celery app object

    """
    celery = Celery("att")
    celery.conf.update(flask_app.config)

    TaskBase = celery.Task

    class AppContextTask(TaskBase):
        abstract = True

        def __call__(self, *args, **kwargs):
            with flask_app.app_context():
                return TaskBase.__call__(self, *args, **kwargs)

    celery.Task = AppContextTask

    celery.finalize()

    return celery
