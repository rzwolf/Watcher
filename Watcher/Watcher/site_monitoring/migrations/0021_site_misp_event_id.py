# Generated by Django 3.0.7 on 2020-06-08 15:59

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('site_monitoring', '0020_site_the_hive_case_id'),
    ]

    operations = [
        migrations.AddField(
            model_name='site',
            name='misp_event_id',
            field=models.IntegerField(blank=True, null=True, unique=True),
        ),
    ]
