# Generated by Django 5.1.1 on 2024-09-19 07:34

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('courses', '0008_lesson_order'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='lesson',
            options={'ordering': ['order']},
        ),
    ]
