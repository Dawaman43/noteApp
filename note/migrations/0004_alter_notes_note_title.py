# Generated by Django 5.1.5 on 2025-02-19 07:48

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('note', '0003_notes_note_title'),
    ]

    operations = [
        migrations.AlterField(
            model_name='notes',
            name='note_title',
            field=models.CharField(max_length=100),
        ),
    ]
