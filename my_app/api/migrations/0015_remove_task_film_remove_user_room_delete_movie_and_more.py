# Generated by Django 4.1 on 2022-12-03 16:59

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0014_alter_user_room'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='task',
            name='film',
        ),
        migrations.RemoveField(
            model_name='user',
            name='room',
        ),
        migrations.DeleteModel(
            name='Movie',
        ),
        migrations.DeleteModel(
            name='Task',
        ),
    ]
