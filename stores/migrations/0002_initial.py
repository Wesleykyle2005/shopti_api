# Generated by Django 5.2.1 on 2025-07-24 22:14

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('stores', '0001_initial'),
        ('users', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='store',
            name='location',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='users.location'),
        ),
        migrations.AddField(
            model_name='store',
            name='media',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='users.media'),
        ),
        migrations.AddField(
            model_name='storemetric',
            name='store',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='stores.store'),
        ),
    ]
