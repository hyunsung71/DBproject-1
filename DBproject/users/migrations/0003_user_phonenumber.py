# Generated by Django 2.2.5 on 2020-11-25 07:16

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0002_auto_20201112_1544'),
    ]

    operations = [
        migrations.AddField(
            model_name='user',
            name='phoneNumber',
            field=models.CharField(default=0, max_length=20),
            preserve_default=False,
        ),
    ]
