from rest_framework import serializers

from api.models import Document, Topic, Folder


class DocumentSerializer(serializers.ModelSerializer):
    class Meta:
        model = Document
        fields = ('name',
                  'file',
                  'topic',
                  'folder')


class TopicSerializer(serializers.ModelSerializer):
    class Meta:
        model = Topic
        fields = ('id',
                  'name')


class FolderSerializer(serializers.ModelSerializer):
    class Meta:
        model = Folder
        fields = ('id',
                  'name',
                  'topic')


class DocumentSearchSerializer(serializers.ModelSerializer):
    topic = TopicSerializer(many=True, read_only=True)

    class Meta:
        model = Document
        fields = ('id',
                  'name',
                  'file',
                  'topic',
                  'folder')
