# Generated by Django 3.1.3 on 2020-12-02 05:01

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Amenity',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created', models.DateTimeField(auto_now_add=True)),
                ('updated', models.DateTimeField(auto_now=True)),
                ('name', models.CharField(max_length=80)),
            ],
            options={
                'verbose_name_plural': 'Amenities',
            },
        ),
        migrations.CreateModel(
            name='BedType',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created', models.DateTimeField(auto_now_add=True)),
                ('updated', models.DateTimeField(auto_now=True)),
                ('name', models.CharField(max_length=80)),
            ],
            options={
                'verbose_name': 'Bed Type',
                'ordering': ['name'],
            },
        ),
        migrations.CreateModel(
            name='RoomType',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created', models.DateTimeField(auto_now_add=True)),
                ('updated', models.DateTimeField(auto_now=True)),
                ('name', models.CharField(max_length=80)),
            ],
            options={
                'verbose_name': 'Room Type',
                'ordering': ['name'],
            },
        ),
        migrations.CreateModel(
            name='Room',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created', models.DateTimeField(auto_now_add=True)),
                ('updated', models.DateTimeField(auto_now=True)),
                ('room_number', models.CharField(max_length=5)),
                ('room_state', models.BooleanField(default=True)),
                ('amenities', models.ManyToManyField(blank=True, related_name='rooms', to='rooms.Amenity')),
                ('bed_type', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='rooms', to='rooms.bedtype')),
                ('room_type', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='rooms', to='rooms.roomtype')),
            ],
            options={
                'abstract': False,
            },
        ),
    ]
