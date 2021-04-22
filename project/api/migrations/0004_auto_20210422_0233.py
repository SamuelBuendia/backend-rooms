# Generated by Django 2.2 on 2021-04-22 07:33

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0003_auto_20210422_0230'),
    ]

    operations = [
        migrations.AlterField(
            model_name='employee',
            name='name',
            field=models.CharField(max_length=255, unique=True),
        ),
        migrations.AlterField(
            model_name='historicalemployee',
            name='name',
            field=models.CharField(db_index=True, max_length=255),
        ),
    ]
