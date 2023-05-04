from django.views.decorators.csrf import csrf_exempt
from rest_framework import permissions, status
from rest_framework.decorators import api_view, permission_classes
from rest_framework.response import Response

from store.models import Brand
from store.serializers import BrandSerializer


# Category
@csrf_exempt
@api_view(('POST',))
@permission_classes((permissions.IsAdminUser,))
def add_category(request):
    brand_serializer = BrandSerializer(data=request.data)
    if brand_serializer.is_valid():
        brand_serializer.save()

        brand = Brand.objects.get(id=brand_serializer.data.get('id'))
        brand.active = True
        brand.save()

        return Response(brand_serializer.data, status=status.HTTP_201_CREATED)
    return Response(brand_serializer.errors, status=status.HTTP_400_BAD_REQUEST)


@api_view(('GET',))
@permission_classes((permissions.AllowAny,))
def get_one_category(request):
    try:
        brand = Brand.objects.get(id=request.query_params.get('id'))
    except Exception as error:
        return Response({'error': error}, status=status.HTTP_404_NOT_FOUND)

    brand_serializer = BrandSerializer(brand)
    return Response(brand_serializer.data, status=status.HTTP_200_OK)


@api_view(('GET',))
@permission_classes((permissions.AllowAny,))
def get_all_categories(request):
    brand = Brand.objects.all()
    brand_serializer = BrandSerializer(brand, many=True)
    return Response(brand_serializer.data, status=status.HTTP_200_OK)


@api_view(('PUT',))
@permission_classes((permissions.IsAdminUser,))
def update_category(request):
    try:
        brand = Brand.objects.get(id=request.data.get('id'))
    except Exception as error:
        return Response({'error': error}, status=status.HTTP_404_NOT_FOUND)

    brand_serializer = BrandSerializer(brand, data=request.data)
    if brand_serializer.is_valid():
        brand_serializer.save()
        return Response(brand_serializer.data, status=status.HTTP_202_ACCEPTED)
    return Response(brand_serializer.errors, status=status.HTTP_400_BAD_REQUEST)


@api_view(('DELETE',))
@permission_classes((permissions.IsAdminUser,))
def delete_category(request):
    try:
        brand = Brand.objects.get(id=request.data.get('id'))
    except Exception as error:
        return Response({'error': error}, status=status.HTTP_404_NOT_FOUND)

    brand.delete()
    return Response(status=status.HTTP_204_NO_CONTENT)
