# Generated by Django 4.0.3 on 2023-06-21 17:38

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('presentations', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='status',
            name='name',
            field=models.CharField(default='SUBMITTED', max_length=10),
        ),
    ]
