from django.contrib import admin

from .models import (CipherSuite, KeyExchangeAlgorithm, EncryptionAlgorithm,
                     MessageAuthenticationCode)


@admin.register(CipherSuite)
class CipherSuiteAdmin(admin.ModelAdmin):
    list_display = (
        'iana_name', 'key_exchange_algorithm', 'encryption_algorithm',
        'message_authentication_code')


@admin.register(KeyExchangeAlgorithm)
class KeyExchangeAlgorithm(admin.ModelAdmin):
    pass


@admin.register(EncryptionAlgorithm)
class EncryptionAlgorithm(admin.ModelAdmin):
    pass


@admin.register(MessageAuthenticationCode)
class MessageAuthenticationCode(admin.ModelAdmin):
    pass
