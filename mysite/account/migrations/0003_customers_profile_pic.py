# Generated by Django 2.2 on 2020-05-07 11:16

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('account', '0002_auto_20200506_1541'),
    ]

    operations = [
        migrations.AddField(
            model_name='customers',
            name='profile_pic',
            field=models.ImageField(blank=True, null=True, upload_to=''),
        ),
    ]
