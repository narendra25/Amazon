# Generated by Django 2.1.1 on 2018-10-29 10:50

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('ama', '0004_auto_20181029_1619'),
    ]

    operations = [
        migrations.RenameField(
            model_name='paymentprocesses',
            old_name='pcno',
            new_name='customercno',
        ),
    ]