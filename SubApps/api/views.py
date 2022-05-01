from django.shortcuts import render
from django.http.response import JsonResponse
from rest_framework import status, permissions
from rest_framework.decorators import api_view, permission_classes
from rest_framework.response import Response
from .serializers import *
from .models import *


@api_view(['GET', 'POST'])
@permission_classes((permissions.AllowAny, ))
def BirthdayList(request):
    if request.method == 'GET':
        queryset = Birthday.objects.all()
        serializer = BirthdaySerializer(queryset,
                                        context={'request': request},
                                        many=True)
        return Response(serializer.data)

    elif request.method == 'POST':
        serializer = BirthdaySerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(status=status.HTTP_201_CREATED)

        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


# Create your views here.
@api_view(['GET', 'POST'])
@permission_classes((permissions.AllowAny, ))
def PasswordList(request):
    if request.method == 'GET':
        queryset = Password.objects.all()
        serializer = PasswordSerializer(queryset,
                                        context={'request': request},
                                        many=True)
        return Response(serializer.data)

    elif request.method == 'POST':
        serializer = PasswordSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(status=status.HTTP_201_CREATED)

        print(serializer.errors)

        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


@api_view(['GET', 'POST'])
@permission_classes((permissions.AllowAny, ))
def TodoList(request):
    if request.method == 'GET':
        queryset = Todo.objects.all()
        serializer = TodoSerializer(queryset,
                                    context={'request': request},
                                    many=True)
        return Response(serializer.data)

    elif request.method == 'POST':
        serializer = TodoSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(status=status.HTTP_201_CREATED)

        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


@api_view(['GET', 'DELETE', 'PATCH'])
@permission_classes((permissions.AllowAny, ))
def delTodo(request, pk):
    try:
        todo = Todo.objects.get(pk=pk)
    except:
        return JsonResponse({'message': "Todo doesn't exist"},
                            status=status.HTTP_404_NOT_FOUND)

    if request.method == 'DELETE':
        todo.delete()
        return JsonResponse({'message': "Todo deleted successfull"},
                            status=status.HTTP_204_NO_CONTENT)

    elif request.method == 'GET':

        serializer = TodoSerializer(todo, context={'request': request})
        return Response(serializer.data)

    elif request.method == 'PATCH':

        serializer = TodoSerializer(data=request.data, partial=True)
        if serializer.is_valid():
            serializer.save()
            return Response(status=status.HTTP_201_CREATED)

        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
