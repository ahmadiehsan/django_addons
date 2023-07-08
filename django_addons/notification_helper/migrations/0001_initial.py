# Generated by Django 4.1.4 on 2023-01-02 11:32

import uuid

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = []

    operations = [
        migrations.CreateModel(
            name='EmailLog',
            fields=[
                ('id', models.UUIDField(default=uuid.uuid4, editable=False, primary_key=True, serialize=False)),
                ('create_time', models.DateTimeField(auto_now_add=True, verbose_name='Create Time')),
                ('update_time', models.DateTimeField(auto_now=True, verbose_name='Update Time')),
                ('subject', models.CharField(max_length=255, verbose_name='Subject')),
                ('html_message', models.TextField(verbose_name='HTML Message')),
            ],
            options={
                'verbose_name': 'Email Log',
                'verbose_name_plural': 'Email Logs',
                'ordering': ('-create_time',),
                'get_latest_by': ('create_time',),
                'abstract': False,
            },
        ),
        migrations.CreateModel(
            name='EmailRecipientLog',
            fields=[
                ('id', models.UUIDField(default=uuid.uuid4, editable=False, primary_key=True, serialize=False)),
                ('create_time', models.DateTimeField(auto_now_add=True, verbose_name='Create Time')),
                ('update_time', models.DateTimeField(auto_now=True, verbose_name='Update Time')),
                ('recipient', models.EmailField(max_length=254, verbose_name='Recipient')),
                (
                    'email_log',
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.CASCADE,
                        to='notification_helper.emaillog',
                        verbose_name='Recipient',
                    ),
                ),
            ],
            options={'ordering': ('-create_time',), 'get_latest_by': ('create_time',), 'abstract': False},
        ),
    ]