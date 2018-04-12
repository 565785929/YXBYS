# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='studentdb',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('XXMC', models.CharField(max_length=40)),
                ('XM', models.CharField(max_length=8)),
                ('KSH', models.CharField(max_length=18)),
                ('XB', models.CharField(max_length=2)),
                ('MZ', models.CharField(max_length=10)),
                ('ZZMM', models.CharField(max_length=10)),
                ('RXSJ', models.CharField(max_length=8)),
                ('BYSJ', models.CharField(max_length=8)),
                ('XZ', models.CharField(max_length=4)),
                ('XLCC', models.CharField(max_length=14)),
                ('ZYMC', models.CharField(max_length=40)),
                ('BZ', models.CharField(max_length=40)),
            ],
            options={
                'ordering': ('XM',),
            },
        ),
    ]
