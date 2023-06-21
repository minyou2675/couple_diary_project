# Generated by Django 4.2 on 2023-06-20 12:35

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('diary', '0005_alter_answer_author_alter_answer_question_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='schedule',
            name='author',
            field=models.ForeignKey(default=1, on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL),
            preserve_default=False,
        ),
    ]