# Generated by Django 4.1 on 2022-12-02 21:54

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0005_task'),
    ]

    operations = [
        migrations.AddField(
            model_name='task',
            name='film',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, related_name='tasks', to='api.movie'),
        ),
    ]
