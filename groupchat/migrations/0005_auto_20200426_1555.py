# Generated by Django 3.0.5 on 2020-04-26 15:55

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('groupchat', '0004_auto_20200426_1554'),
    ]

    operations = [
        migrations.AlterField(
            model_name='room',
            name='messages',
            field=models.CharField(max_length=10000),
        ),
        migrations.AlterField(
            model_name='room',
            name='username',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL),
        ),
    ]
