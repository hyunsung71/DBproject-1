# Generated by Django 3.1.3 on 2020-12-04 06:28

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('employees', '0001_initial'),
        ('rooms', '0001_initial'),
        ('complaints', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='complain_type',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('complain_type', models.CharField(max_length=100)),
            ],
        ),
        migrations.AlterField(
            model_name='complain',
            name='employee_ID',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='employees.employee'),
        ),
        migrations.AlterField(
            model_name='complain',
            name='room_number',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='rooms.room'),
        ),
        migrations.AlterField(
            model_name='complain',
            name='work_type',
            field=models.CharField(blank=True, choices=[('houseman', 'Houseman'), ('londry', 'Londry'), ('operator', 'Operator'), ('reception', 'Reception'), ('reservation', 'Reservation'), ('roommaid', 'Room maid'), ('other', 'Other')], max_length=20),
        ),
        migrations.AlterField(
            model_name='complain',
            name='complain_type',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='complaints.complain_type'),
        ),
    ]