# Generated by Django 2.1.10 on 2019-12-12 17:16

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0002_auto_20191212_1658'),
    ]

    operations = [
        migrations.AlterUniqueTogether(
            name='appuser',
            unique_together={('user_name', 'birthday')},
        ),
    ]
