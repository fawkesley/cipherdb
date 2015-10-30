from django.db import models


class MessageAuthenticationCode(models.Model):

    class Meta:
        app_label = 'ciphersuites'

    name = models.CharField(
        max_length=200)

    def __str__(self):
        return '{0}'.format(self.name)
