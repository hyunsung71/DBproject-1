# Generated by Django 3.1.3 on 2020-12-02 05:01

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Employee',
            fields=[
                ('e_ID', models.CharField(max_length=20, primary_key=True, serialize=False)),
                ('e_PW', models.CharField(max_length=20)),
                ('e_name', models.CharField(max_length=20)),
                ('e_gender', models.CharField(blank=True, choices=[('male', 'Male'), ('female', 'Female')], max_length=20)),
                ('e_work_type', models.CharField(blank=True, choices=[('houseman', 'Houseman'), ('londry', 'Londry'), ('operator', 'Operator'), ('reception', 'Reception'), ('reservation', 'Reservation'), ('roommaid', 'Room maid'), ('other', 'Other')], max_length=20)),
                ('e_birthdate', models.DateField(blank=True, null=True)),
                ('e_address', models.CharField(max_length=200)),
                ('e_salary', models.IntegerField(blank=True, null=True)),
                ('e_phone_number', models.CharField(max_length=100)),
            ],
        ),
    ]
