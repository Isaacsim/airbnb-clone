# Generated by Django 3.0.7 on 2020-06-17 11:33

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('rooms', '0008_auto_20200612_2300'),
    ]

    operations = [
        migrations.AddField(
            model_name='room',
            name='super_host',
            field=models.BooleanField(default=False),
        ),
    ]