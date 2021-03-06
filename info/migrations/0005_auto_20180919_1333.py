# Generated by Django 2.1.1 on 2018-09-19 13:33

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('info', '0004_auto_20180919_0145'),
    ]

    operations = [
        migrations.AddField(
            model_name='externallink',
            name='user',
            field=models.ForeignKey(default=None, on_delete=django.db.models.deletion.CASCADE, related_name='external_links', to='info.PersonalInfo'),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='externallink',
            name='title',
            field=models.CharField(blank=True, max_length=255, null=True),
        ),
    ]
