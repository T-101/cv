# Generated by Django 2.1.2 on 2018-10-28 15:23

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('info', '0012_auto_20181028_1512'),
    ]

    operations = [
        migrations.AddField(
            model_name='personalinfo',
            name='title',
            field=models.CharField(default='Insert jobtitle here', max_length=255),
            preserve_default=False,
        ),
    ]
