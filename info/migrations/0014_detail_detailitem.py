# Generated by Django 2.1.2 on 2018-10-28 15:37

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('info', '0013_personalinfo_title'),
    ]

    operations = [
        migrations.CreateModel(
            name='Detail',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=64)),
                ('sort_order', models.IntegerField(default=0)),
            ],
        ),
        migrations.CreateModel(
            name='DetailItem',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('text', models.TextField()),
                ('sort_order', models.IntegerField(default=0)),
                ('detail', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='detailitems', to='info.Detail')),
            ],
        ),
    ]
