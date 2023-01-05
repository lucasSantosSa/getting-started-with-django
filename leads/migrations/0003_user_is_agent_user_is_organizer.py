# Generated by Django 4.1.4 on 2022-12-27 05:06

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('leads', '0002_userprofile_agent_organization'),
    ]

    operations = [
        migrations.AddField(
            model_name='user',
            name='is_agent',
            field=models.BooleanField(default=False),
        ),
        migrations.AddField(
            model_name='user',
            name='is_organizer',
            field=models.BooleanField(default=True),
        ),
    ]
