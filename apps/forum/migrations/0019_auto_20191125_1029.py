# Generated by Django 2.0.12 on 2019-11-25 10:29

from django.db import migrations, models
import uuid


class Migration(migrations.Migration):

    dependencies = [
        ('forum', '0018_auto_20190821_1126'),
    ]

    operations = [
        migrations.AlterField(
            model_name='priority',
            name='id',
            field=models.UUIDField(default=uuid.uuid4, primary_key=True, serialize=False),
        ),
    ]
