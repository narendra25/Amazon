# Generated by Django 2.1.1 on 2018-10-29 18:03

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('ama', '0010_comments'),
    ]

    operations = [
        migrations.AlterField(
            model_name='comments',
            name='comment',
            field=models.CharField(max_length=10000),
        ),
    ]
