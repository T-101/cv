# Generated by Django 2.1.2 on 2018-10-28 16:05

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('info', '0014_detail_detailitem'),
    ]

    operations = [
        migrations.AlterField(
            model_name='detailitem',
            name='detail',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='items', to='info.Detail'),
        ),
    ]
