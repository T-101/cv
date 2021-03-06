# Generated by Django 2.1.1 on 2018-09-24 21:59

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('cv', '0004_auto_20180924_2158'),
    ]

    operations = [
        migrations.AlterField(
            model_name='employment',
            name='date_end_display_resolution',
            field=models.CharField(choices=[('%Y', 'Year'), ('%Y-%m', 'Month'), ('%M-%m-%d', 'Day')], default=('%M-%m-%d', 'Day'), max_length=8),
        ),
        migrations.AlterField(
            model_name='employment',
            name='date_start_display_resolution',
            field=models.CharField(choices=[('%Y', 'Year'), ('%Y-%m', 'Month'), ('%M-%m-%d', 'Day')], default=('%M-%m-%d', 'Day'), max_length=8),
        ),
    ]
