# Generated by Django 4.2 on 2023-06-21 05:58

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0003_user_first'),
    ]

    operations = [
        migrations.AlterField(
            model_name='user',
            name='first',
            field=models.DateField(verbose_name='우리가 처음 사귀게 된 날'),
        ),
    ]
