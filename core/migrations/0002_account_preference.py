# Generated by Django 3.2.9 on 2024-05-06 20:20

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='account',
            name='preference',
            field=models.ForeignKey(default=None, on_delete=django.db.models.deletion.CASCADE, to='core.preferences'),
        ),
    ]
