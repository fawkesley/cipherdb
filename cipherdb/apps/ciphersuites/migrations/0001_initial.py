# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='CipherSuite',
            fields=[
                ('id', models.AutoField(auto_created=True, verbose_name='ID', serialize=False, primary_key=True)),
                ('iana_name', models.CharField(max_length=200)),
            ],
        ),
        migrations.CreateModel(
            name='EncryptionAlgorithm',
            fields=[
                ('id', models.AutoField(auto_created=True, verbose_name='ID', serialize=False, primary_key=True)),
                ('name', models.CharField(max_length=200)),
            ],
        ),
        migrations.CreateModel(
            name='KeyExchangeAlgorithm',
            fields=[
                ('id', models.AutoField(auto_created=True, verbose_name='ID', serialize=False, primary_key=True)),
                ('name', models.CharField(max_length=200)),
            ],
        ),
        migrations.CreateModel(
            name='MessageAuthenticationCode',
            fields=[
                ('id', models.AutoField(auto_created=True, verbose_name='ID', serialize=False, primary_key=True)),
                ('name', models.CharField(max_length=200)),
            ],
        ),
        migrations.AddField(
            model_name='ciphersuite',
            name='encryption_algorithm',
            field=models.ForeignKey(null=True, to='ciphersuites.EncryptionAlgorithm'),
        ),
        migrations.AddField(
            model_name='ciphersuite',
            name='key_exchange_algorithm',
            field=models.ForeignKey(null=True, to='ciphersuites.KeyExchangeAlgorithm'),
        ),
        migrations.AddField(
            model_name='ciphersuite',
            name='message_authentication_code',
            field=models.ForeignKey(null=True, to='ciphersuites.MessageAuthenticationCode'),
        ),
    ]
