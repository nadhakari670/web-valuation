# Generated by Django 2.1.1 on 2019-03-13 03:01

from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('main', '0014_auto_20190312_2035'),
    ]

    operations = [
        migrations.AddField(
            model_name='evaluator',
            name='user',
            field=models.OneToOneField(default='none', on_delete='cascade', to=settings.AUTH_USER_MODEL),
            preserve_default=False,
        ),
    ]
