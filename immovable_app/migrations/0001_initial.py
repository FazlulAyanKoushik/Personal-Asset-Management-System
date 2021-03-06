# Generated by Django 3.1.5 on 2021-01-27 09:15

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Other',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('date_of_acquisition', models.DateField()),
                ('owner', models.CharField(max_length=200)),
                ('class_and_location', models.CharField(max_length=200)),
                ('details', models.CharField(max_length=1000)),
                ('how_acquired_and_value', models.CharField(max_length=1000)),
                ('source_of_money', models.CharField(max_length=1000)),
                ('opinon', models.CharField(max_length=1000)),
                ('notesfile', models.FileField(blank=True, null=True, upload_to='immovable-files/')),
                ('is_confirm', models.BooleanField(default=False)),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='+', to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='Land',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('date_of_acquisition', models.DateField()),
                ('owner', models.CharField(max_length=200)),
                ('class_and_location', models.CharField(max_length=200)),
                ('details', models.CharField(max_length=1000)),
                ('how_acquired_and_value', models.CharField(max_length=1000)),
                ('source_of_money', models.CharField(max_length=1000)),
                ('opinon', models.CharField(max_length=1000)),
                ('notesfile', models.FileField(upload_to='immovable-files/')),
                ('is_confirm', models.BooleanField(default=False)),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='Homestead',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('date_of_acquisition', models.DateField()),
                ('owner', models.CharField(max_length=200)),
                ('class_and_location', models.CharField(max_length=200)),
                ('details', models.CharField(max_length=1000)),
                ('how_acquired_and_value', models.CharField(max_length=1000)),
                ('source_of_money', models.CharField(max_length=1000)),
                ('opinon', models.CharField(max_length=1000)),
                ('notesfile', models.FileField(blank=True, null=True, upload_to='immovable-files/')),
                ('is_confirm', models.BooleanField(default=False)),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='BusinessFirm',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('date_of_acquisition', models.DateField()),
                ('owner', models.CharField(max_length=200)),
                ('class_and_location', models.CharField(max_length=200)),
                ('details', models.CharField(max_length=1000)),
                ('how_acquired_and_value', models.CharField(max_length=1000)),
                ('source_of_money', models.CharField(max_length=1000)),
                ('opinon', models.CharField(max_length=1000)),
                ('notesfile', models.FileField(blank=True, null=True, upload_to='immovable-files/')),
                ('is_confirm', models.BooleanField(default=False)),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='Building',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('date_of_acquisition', models.DateField()),
                ('owner', models.CharField(max_length=200)),
                ('class_and_location', models.CharField(max_length=200)),
                ('details', models.CharField(max_length=1000)),
                ('how_acquired_and_value', models.CharField(max_length=1000)),
                ('source_of_money', models.CharField(max_length=1000)),
                ('opinon', models.CharField(max_length=1000)),
                ('notesfile', models.FileField(blank=True, null=True, upload_to='immovable-files/')),
                ('is_confirm', models.BooleanField(default=False)),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]
