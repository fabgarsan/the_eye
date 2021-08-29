from django.db import models


class Application(models.Model):
    name = models.CharField(max_length=200)
    url = models.URLField()

    def __str__(self):
        return self.name


class Session(models.Model):
    application = models.ForeignKey(Application, related_name='sessions', on_delete=models.PROTECT)


class Event(models.Model):
    session = models.ForeignKey(Session, on_delete=models.PROTECT, related_name='events')
    category = models.CharField(max_length=200)
    name = models.CharField(max_length=200)
    data = models.JSONField()
    timestamp = models.DateTimeField()
