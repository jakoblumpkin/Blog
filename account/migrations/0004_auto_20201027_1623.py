# Generated by Django 3.1 on 2020-10-27 21:23

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('account', '0003_section'),
    ]

    operations = [
        migrations.AlterField(
            model_name='section',
            name='comment',
            field=models.TextField(),
        ),
    ]
