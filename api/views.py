from django.http import HttpResponse, JsonResponse
from django.shortcuts import render
from rest_framework import status
from rest_framework.decorators import api_view
from rest_framework.parsers import JSONParser
from rest_framework.utils import json

from .forms import UploadDocForm, CreateTopicForm, CreateFolderForm
from .models import Document, Topic, Folder
from .serializers import DocumentSerializer, TopicSerializer, FolderSerializer, DocumentSearchSerializer


def docuploadview(request):
    if request.method == 'POST':
        form = UploadDocForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            return HttpResponse('The file is saved')
    else:
        form = UploadDocForm()
        context = {
            'form': form,
        }
    return render(request, 'UploadDoc.html', context)


@api_view(['GET'])
def listdocsview(request):
    if request.method == 'GET':
        documents = Document.objects.all()
        document_serializer = DocumentSerializer(documents, many=True)
        return JsonResponse(document_serializer.data, safe=False)
        # 'safe=False' for objects serialization
        return JsonResponse(document_serializer.errors, status=status.HTTP_400_BAD_REQUEST)


@api_view(['GET'])
def getdocview(request, name):
    if request.method == 'GET' or request.method == 'POST':
        print(f"doc name {name}")
        documents = Document.objects.filter(name__icontains=name)[:10]
        document_serializer = DocumentSerializer(documents, many=True)
        return JsonResponse(document_serializer.data, safe=False)
    else:
        return JsonResponse({'message': '{} No data found'}, status=status.HTTP_204_NO_CONTENT)


@api_view(['GET'])
def listtopicsview(request):
    if request.method == 'GET':
        topics = Topic.objects.all()
        topic_serializer = TopicSerializer(topics, many=True)
        return JsonResponse(topic_serializer.data, safe=False)


@api_view(['GET'])
def listfoldersview(request):
    if request.method == 'GET':
        folders = Folder.objects.all()
        folder_serializer = FolderSerializer(folders, many=True)
        return JsonResponse(folder_serializer.data, safe=False)

@api_view(['GET', 'POST'])
def createtopicview(request):
    if request.method == 'GET' or request.method == 'POST':
        topic = JSONParser().parse(request)
        topic_serializer = TopicSerializer(data=topic)
        if topic_serializer.is_valid():
            topic_serializer.save()
            return JsonResponse(topic_serializer.data, status=status.HTTP_201_CREATED)
    return JsonResponse(topic_serializer.errors, status=status.HTTP_400_BAD_REQUEST)

@api_view(['GET', 'POST'])
def createfolderview(request):
    if request.method == 'GET' or request.method == 'POST':
        folder = JSONParser().parse(request)
        folder_serializer = FolderSerializer(data=folder)
        if folder_serializer.is_valid():
            folder_serializer.save()
            return JsonResponse(folder_serializer.data, status=status.HTTP_201_CREATED)
    return JsonResponse(folder_serializer.errors, status=status.HTTP_400_BAD_REQUEST)


@api_view(['GET'])
def searchdocview(request):
    if request.method == 'GET':
        for key, value in request.GET.items():
            print(key)
            print(value)


    # if request.method == 'GET':
    # documents = Document.objects.filter(name__icontains=name)[:10]
    # document_serializer = DocumentSearchSerializer(documents, many=True)
    # return JsonResponse(document_serializer.data, safe=False)
    return JsonResponse({'message': '{} No data found'}, status=status.HTTP_204_NO_CONTENT)
