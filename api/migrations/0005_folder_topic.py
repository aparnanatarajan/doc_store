# Generated by Django 4.0 on 2022-01-09 23:18

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0004_rename_folder_id_document_folder_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='folder',
            name='topic',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, to='api.topic'),
        ),
    ]
