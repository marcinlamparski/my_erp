# Generated by Django 3.2.5 on 2021-08-26 09:45

import django.contrib.postgres.fields
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('kadry', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='marszruta',
            name='czasy',
            field=django.contrib.postgres.fields.ArrayField(base_field=django.contrib.postgres.fields.ArrayField(base_field=models.IntegerField(default=0, null=True), size=8), default=0, size=8),
            preserve_default=False,
        ),
    ]
