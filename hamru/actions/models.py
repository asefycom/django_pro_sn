from django.db import models
from django.conf import settings


class Action(models.Model):
    user = models.ForeignKey(settings.AUTH_USER_MODEL,
                             related_name='actions',
                             db_index=True,
                             on_delete=models.CASCADE)
    verb = models.CharField(max_length=255)
    created = models.DateTimeField(auto_now_add=True,
                                   db_index=True)

    class Meta:
        ordering = ('-created',)
