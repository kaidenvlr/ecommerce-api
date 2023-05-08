from django.views.decorators.csrf import csrf_exempt
from rest_framework import status, permissions
from rest_framework.decorators import api_view, permission_classes
from rest_framework.response import Response

from store.models import Subcategory, Category, Brand, Product
from store.serializers import ProductSerializer, ProductImageSerializer


@csrf_exempt
@api_view(('POST',))
@permission_classes((permissions.IsAdminUser,))
def add_product(request):
    product_serializer = ProductSerializer(data=request.data)
    if product_serializer.is_valid():
        product_serializer.save()

        subcategory = Subcategory.objects.get(id=product_serializer.data.get('subcategory'))
        subcategory.active = True
        subcategory.save()

        subcategory.category.active = True
        subcategory.category.save()

        brand = Brand.objects.get(id=product_serializer.data.get('brand'))
        brand.active = True
        brand.save()

        return Response(product_serializer.data, status=status.HTTP_201_CREATED)
    return Response(product_serializer.errors, status=status.HTTP_400_BAD_REQUEST)


@api_view(('GET',))
@permission_classes((permissions.AllowAny,))
def get_one_product(request):
    try:
        product = Product.objects.get(id=request.query_params.get('id'))
    except Exception as error:
        return Response({'error': error}, status=status.HTTP_404_NOT_FOUND)

    serializer = ProductSerializer(product)
    return Response(serializer.data, status=status.HTTP_200_OK)


@api_view(('GET',))
@permission_classes((permissions.AllowAny,))
def get_all_products(request):
    products = Product.objects.all()
    serializer = ProductSerializer(products, many=True)
    return Response(serializer.data, status=status.HTTP_200_OK)


@api_view(('PUT',))
@permission_classes((permissions.IsAdminUser,))
def update_product(request):
    try:
        product = Product.objects.get(id=request.data.get('id'))
    except Exception as error:
        return Response({'error': error}, status=status.HTTP_404_NOT_FOUND)

    serializer = ProductSerializer(product, data=request.data)
    if serializer.is_valid():
        serializer.save()
        return Response(serializer.data, status=status.HTTP_202_ACCEPTED)
    return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


@api_view(('DELETE',))
@permission_classes((permissions.IsAdminUser,))
def delete_product(request):
    try:
        product = Product.objects.get(id=request.data.get('id'))
    except Exception as error:
        return Response({'error': error}, status=status.HTTP_404_NOT_FOUND)

    product.delete()
    return Response(status=status.HTTP_204_NO_CONTENT)


@csrf_exempt
@api_view(('POST',))
@permission_classes((permissions.IsAdminUser,))
def add_product_image(request):
    image_serializer = ProductImageSerializer(data=request.data)
    if image_serializer.is_valid():
        image_serializer.save()
        return Response(image_serializer.data, status=status.HTTP_201_CREATED)
    return Response(image_serializer.errors, status=status.HTTP_400_BAD_REQUEST)


@api_view(('DELETE',))
@permission_classes((permissions.IsAdminUser,))
def delete_product_images(request):
    try:
        product = Product.objects.get(id=request.data.get('id'))
        print(*product.image)
    except Exception as error:
        return Response({'error': error}, status=status.HTTP_404_NOT_FOUND)

    return Response({'message': 'check server console'}, status=status.HTTP_200_OK)
