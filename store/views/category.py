from django.views.decorators.csrf import csrf_exempt
from rest_framework import permissions, status
from rest_framework.decorators import api_view, permission_classes
from rest_framework.response import Response

from store.models import Category
from store.serializers import CategorySerializer


# Category
@csrf_exempt
@api_view(('POST',))
@permission_classes((permissions.IsAdminUser,))
def add_category(request):
    serializer = CategorySerializer(data=request.data)
    if serializer.is_valid():
        serializer.save()

        category = Category.objects.get(id=serializer.data.get('id'))
        category.active = True
        category.save()

        return Response(serializer.data, status=status.HTTP_201_CREATED)
    return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


@api_view(('GET',))
@permission_classes((permissions.AllowAny,))
def get_one_category(request):
    try:
        category = Category.objects.get(id=request.query_params.get('id'))
    except Exception as error:
        return Response({'error': error}, status=status.HTTP_404_NOT_FOUND)

    serializer = CategorySerializer(category)
    return Response(serializer.data, status=status.HTTP_200_OK)


@api_view(('GET',))
@permission_classes((permissions.AllowAny,))
def get_all_categories(request):
    category = Category.objects.all()
    serializer = CategorySerializer(category, many=True)
    return Response(serializer.data, status=status.HTTP_200_OK)


@api_view(('PUT',))
@permission_classes((permissions.IsAdminUser,))
def update_category(request):
    try:
        category = Category.objects.get(id=request.data.get('id'))
    except Exception as error:
        return Response({'error': error}, status=status.HTTP_404_NOT_FOUND)

    serializer = CategorySerializer(category, data=request.data)
    if serializer.is_valid():
        serializer.save()
        return Response(serializer.data, status=status.HTTP_202_ACCEPTED)
    return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


@api_view(('DELETE',))
@permission_classes((permissions.IsAdminUser,))
def delete_category(request):
    try:
        category = Category.objects.get(id=request.data.get('id'))
    except Exception as error:
        return Response({'error': error}, status=status.HTTP_404_NOT_FOUND)

    category.delete()
    return Response(status=status.HTTP_204_NO_CONTENT)
