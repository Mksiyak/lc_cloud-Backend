# Generated by Django 2.2.6 on 2019-10-30 13:21

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0007_instance_slave_id'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='instance',
            name='slave_id',
        ),
    ]