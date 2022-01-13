from django.db import models


class Topic(models.Model):
    id = models.BigAutoField(primary_key=True)
    name = models.CharField(max_length=100)

    class Meta:
        ordering = ['name']

    def __str__(self):
        return f"{self.name}"


class Folder(models.Model):
    id = models.BigAutoField(primary_key=True)
    name = models.CharField(max_length=100)
    topic = models.ManyToManyField('api.Topic', related_name='folder_related_topics')

    class Meta:
        ordering = ['name']

    def __str__(self):
        return f"{self.name}"


class Document(models.Model):
    id = models.BigAutoField(primary_key=True)
    name = models.CharField(max_length=50, null=False, blank=False)
    file = models.FileField(upload_to='docs/', null=False, blank=False)
    topic = models.ManyToManyField('api.Topic', related_name='doc_related_topics')
    folder = models.ForeignKey(Folder, on_delete=models.SET_NULL, blank=True, null=True)

    class Meta:
        ordering = ['name']

    def __str__(self):
        return f"{self.name}"
