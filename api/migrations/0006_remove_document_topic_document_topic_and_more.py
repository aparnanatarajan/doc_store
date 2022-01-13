# Generated by Django 4.0 on 2022-01-10 16:25

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0005_folder_topic'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='document',
            name='topic',
        ),
        migrations.AddField(
            model_name='document',
            name='topic',
            field=models.ManyToManyField(related_name='doc_related_topics', to='api.Topic'),
        ),
        migrations.RemoveField(
            model_name='folder',
            name='topic',
        ),
        migrations.AddField(
            model_name='folder',
            name='topic',
            field=models.ManyToManyField(related_name='folder_related_topics', to='api.Topic'),
        ),
    ]