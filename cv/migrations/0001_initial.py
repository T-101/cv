# Generated by Django 2.1.1 on 2018-09-19 01:00

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Employer',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=255)),
                ('description', models.CharField(blank=True, max_length=255, null=True)),
                ('url', models.URLField(blank=True, null=True)),
                ('visible', models.BooleanField(default=True)),
            ],
        ),
        migrations.CreateModel(
            name='Employment',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('date_start', models.DateField()),
                ('date_end', models.DateField(blank=True, null=True)),
                ('internship', models.BooleanField(default=False)),
                ('visible', models.BooleanField(default=True)),
                ('employer', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='cv.Employer')),
            ],
        ),
        migrations.CreateModel(
            name='EmploymentTask',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=255)),
                ('sort_index', models.IntegerField(default=0)),
                ('visible', models.BooleanField(default=True)),
                ('employment', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='cv.Employment')),
            ],
        ),
        migrations.CreateModel(
            name='ExternalLink',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('url', models.URLField()),
                ('title', models.CharField(max_length=255)),
            ],
        ),
        migrations.CreateModel(
            name='PersonalEmail',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('address', models.EmailField(max_length=254)),
            ],
        ),
        migrations.CreateModel(
            name='PersonalInfo',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('real_name', models.CharField(max_length=255)),
                ('nick_name', models.CharField(blank=True, max_length=255, null=True)),
            ],
        ),
        migrations.CreateModel(
            name='PersonalPhoneNumber',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('number', models.CharField(max_length=32)),
                ('type', models.CharField(choices=[('Home', 0), ('Work', 1), ('Mobile', 2), ('Fax', 3), ('Beeper', 4), ('Other', 5)], max_length=32)),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='phonenumbers', to='cv.PersonalInfo')),
            ],
        ),
        migrations.AddField(
            model_name='personalemail',
            name='user',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='emails', to='cv.PersonalInfo'),
        ),
    ]
