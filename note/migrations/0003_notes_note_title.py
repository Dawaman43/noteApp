# Generated by Django 5.1.5 on 2025-02-19 07:40

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('note', '0002_alter_notes_options'),
    ]

    operations = [
        migrations.AddField(
            model_name='notes',
            name='note_title',
            field=models.TextField(default=1, max_length=100),
            preserve_default=False,
        ),
    ]
