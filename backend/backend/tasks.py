from django.core.mail import EmailMessage

from .celery import app

from events.models import Application, Session, Event


@app.task
def save_event(data):
    data_body = data.get('data', None)
    host = data_body.get('host', None)
    if host:
        application = Application.objects.filter(url__icontains=host).first()
        if not application and 'www.consumeraffairs.com' in host:
            application = Application.objects.create(name='Consumer Affairs', url='www.consumeraffairs.com')
        if application:
            session_id = data.get('session_id')
            session, created = Session.objects.get_or_create(pk=session_id, application=application)
            data['session'] = session
            Event.objects.create(**data)
        else:
            send_email_save_event_error.delay(f'The host {host} is not in the list of allowed hosts')
    else:
        send_email_save_event_error.delay('No host has been set in the request')


@app.task
def send_email_save_event_error(body_message):
    email = EmailMessage(
        subject='Error saving and event!',
        body=body_message,
        to=['reporting.error@theeye.com']
    )
    email.send()
