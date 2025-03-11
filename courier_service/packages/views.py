from django.shortcuts import render
from rest_framework.decorators import api_view, permission_classes
from rest_framework.response import Response
from rest_framework import status
from .models import Package
from .serializers import PackageSerializer
from rest_framework.permissions import IsAuthenticated

@api_view(['GET', 'POST'])
@permission_classes([IsAuthenticated])
def package_list(request):
    if request.method == 'GET':
        packages = Package.objects.filter(is_deleted=False)
        serializer = PackageSerializer(packages, many=True)
        return Response(serializer.data)

    elif request.method == 'POST':
        serializer = PackageSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

@api_view(['GET', 'PUT', 'DELETE'])
@permission_classes([IsAuthenticated])
def package_detail(request, pk):
    try:
        package = Package.objects.get(pk=pk, is_deleted=False)
    except Package.DoesNotExist:
        return Response(status=status.HTTP_404_NOT_FOUND)

    if request.method == 'GET':
        serializer = PackageSerializer(package)
        return Response(serializer.data)

    elif request.method == 'PUT':
        serializer = PackageSerializer(package, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    elif request.method == 'DELETE':
        package.is_deleted = True
        package.save()
        return Response(status=status.HTTP_204_NO_CONTENT)
