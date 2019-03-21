# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('auditlog', '0008_logentry_affected_user'),
    ]

    operations = [
        migrations.AlterField(
            model_name='logentry',
            name='actor',
            field=models.ForeignKey(blank=True, db_constraint=False, null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='+', to=settings.AUTH_USER_MODEL, verbose_name='actor'),
        ),
        migrations.AlterField(
            model_name='logentry',
            name='affected_user',
            field=models.ForeignKey(blank=True, db_constraint=False, null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='affecting_log_entries', to=settings.AUTH_USER_MODEL, verbose_name='affected user'),
        ),
    ]
