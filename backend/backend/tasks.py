from .celery import app

from events.models import Application, Session, Event


@app.task
def save_event(data):
    data_body = data.get('data', None)
    host = data_body.get('host', None)
    if host:
        application = Application.objects.filter(url__icontains=host).first()
        if application:
            session_id = data.get('session_id')
            session, created = Session.objects.get_or_create(pk=session_id, application=application)
            data['session'] = session
            Event.objects.create(**data)
