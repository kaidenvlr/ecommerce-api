from django.views.decorators.csrf import csrf_exempt
from rest_framework import permissions, status
from rest_framework.decorators import api_view, permission_classes
from rest_framework.response import Response

from store.models import Review
from store.serializers import ReviewSerializer


@csrf_exempt
@api_view(('POST',))
@permission_classes((permissions.IsAuthenticated,))
def add_review(request):
    review_serializer = ReviewSerializer(data=request.data)
    if review_serializer.is_valid():
        review_serializer.save()

        review = Review.objects.get(id=review_serializer.data.get('id'))
        review.active = True
        review.save()

        return Response(review_serializer.data, status=status.HTTP_201_CREATED)
    return Response(review_serializer.errors, status=status.HTTP_400_BAD_REQUEST)


@api_view(('GET',))
@permission_classes((permissions.AllowAny,))
def get_all_review(request):
    review = Review.objects.all()
    review_serializer = ReviewSerializer(review, many=True)
    return Response(review_serializer.data, status=status.HTTP_200_OK)
