# Generated by Django 5.1.2 on 2024-10-22 13:33

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('mypage', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='creativereser',
            name='end_time',
            field=models.TimeField(blank=True, null=True),
        ),
    ]
