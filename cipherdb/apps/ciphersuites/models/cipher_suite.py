from django.db import models

from .key_exchange_algorithm import KeyExchangeAlgorithm
from .encryption_algorithm import EncryptionAlgorithm
from .message_authentication_code import MessageAuthenticationCode


class CipherSuite(models.Model):
    """
    A cipher suite is a named combination of authentication, encryption,
    message authentication code (MAC) and key exchange algorithms used to
    negotiate the security settings for a network connection using the
    Transport Layer Security (TLS) / Secure Sockets Layer (SSL) network
    protocol.

    https://www.iana.org/assignments/tls-parameters/tls-parameters.xhtml
    #tls-parameters-4
    """

    class Meta:
        app_label = 'ciphersuites'

    iana_name = models.CharField(
        max_length=200)

    key_exchange_algorithm = models.ForeignKey(
        KeyExchangeAlgorithm,
        null=True)

    encryption_algorithm = models.ForeignKey(
        EncryptionAlgorithm,
        null=True)

    message_authentication_code = models.ForeignKey(
        MessageAuthenticationCode,
        null=True)

    def __str__(self):
        return '{0}'.format(self.iana_name)
