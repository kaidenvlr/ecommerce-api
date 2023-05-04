from django.views.decorators.csrf import csrf_exempt
from rest_framework import permissions, status
from rest_framework.decorators import api_view, permission_classes
from rest_framework.response import Response

from store.models import Subcategory
from store.serializers import SubcategorySerializer


# Subcategory
@csrf_exempt
@api_view(('POST',))
@permission_classes((permissions.IsAdminUser,))
def add_subcategory(request):
    subcategory_serializer = SubcategorySerializer(data=request.data)
    if subcategory_serializer.is_valid():
        subcategory_serializer.save()

        subcategory = Subcategory.objects.get(id=subcategory_serializer.data.get('id'))
        subcategory.active = True
        subcategory.category.active = True

        subcategory.category.save()
        subcategory.save()

        return Response(subcategory_serializer.data, status=status.HTTP_201_CREATED)
    return Response(subcategory_serializer.errors, status=status.HTTP_400_BAD_REQUEST)


@api_view(('GET',))
@permission_classes((permissions.AllowAny,))
def get_one_subcategory(request):
    try:
        subcategory = Subcategory.objects.get(id=request.query_params.get('id'))
    except Exception as error:
        return Response({'error': error}, status=status.HTTP_404_NOT_FOUND)

    subcategory_serializer = SubcategorySerializer(subcategory)
    return Response(subcategory_serializer.data, status=status.HTTP_200_OK)


@api_view(('GET',))
@permission_classes((permissions.AllowAny,))
def get_all_subcategories(request):
    subcategory = Subcategory.objects.all()
    subcategory_serializer = SubcategorySerializer(subcategory, many=True)
    return Response(subcategory_serializer.data, status=status.HTTP_200_OK)


@api_view(('PUT',))
@permission_classes((permissions.IsAdminUser,))
def update_subcategory(request):
    try:
        subcategory = Subcategory.objects.get(id=request.data.get('id'))
    except Exception as error:
        return Response({'error': error}, status=status.HTTP_404_NOT_FOUND)

    subcategory_serializer = SubcategorySerializer(subcategory, data=request.data)
    if subcategory_serializer.is_valid():
        subcategory_serializer.save()
        return Response(subcategory_serializer.data, status=status.HTTP_202_ACCEPTED)
    return Response(subcategory_serializer.errors, status=status.HTTP_400_BAD_REQUEST)


@api_view(('DELETE',))
@permission_classes((permissions.IsAdminUser,))
def delete_subcategory(request):
    try:
        subcategory = Subcategory.objects.get(id=request.data.get('id'))
    except Exception as error:
        return Response({'error': error}, status=status.HTTP_404_NOT_FOUND)

    subcategory.delete()
    return Response(status=status.HTTP_204_NO_CONTENT)

