# Generated by Django 3.2.14 on 2022-07-27 04:25

from django.db import migrations, models
import uuid


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Takingone',
            fields=[
                ('id', models.UUIDField(default=uuid.uuid4, primary_key=True, serialize=False)),
                ('numberofone', models.IntegerField()),
                ('operatoscode', models.IntegerField()),
                ('sometag', models.CharField(max_length=200)),
                ('timezoneofone', models.CharField(help_text='Введите часоваой пояс в формате +/-число', max_length=10)),
            ],
        ),
        migrations.CreateModel(
            name='Wordsofmail',
            fields=[
                ('id', models.UUIDField(default=uuid.uuid4, primary_key=True, serialize=False)),
                ('content', models.TextField(max_length=140)),
                ('timetogo', models.TimeField(null=True)),
            ],
        ),
        migrations.CreateModel(
            name='Mailing',
            fields=[
                ('id', models.UUIDField(default=uuid.uuid4, primary_key=True, serialize=False)),
                ('name', models.CharField(max_length=100)),
                ('dateofstart', models.DateField()),
                ('dateofstop', models.DateField()),
                ('wordsofmail', models.ManyToManyField(null=True, to='catalog.Wordsofmail')),
            ],
        ),
    ]
