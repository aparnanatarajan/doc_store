from django.forms import ModelForm
from django import forms
from api.models import Document, Topic, Folder


class UploadDocForm(ModelForm):
    class Meta:
        model = Document
        fields = ('id', 'name', 'file', 'folder', 'topic')


class CreateTopicForm(ModelForm):
    class Meta:
        model = Topic
        fields = ('id', 'name')


class CreateFolderForm(ModelForm):
    class Meta:
        model = Folder
        fields = ('id', 'name', 'topic')
