from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework import status
from .models import Product, Review
from .serializers import ReviewListSerializer, ProductListSerializer

@api_view(['GET'])
def get_product(request):
    product=Product.objects.all()
    data = ProductListSerializer(product,many=True).data
    return Response(data=data)

@api_view(['GET'])
def get_review(request, id):
    try :
        product1 = Review.objects.get(id=id)
    except Review.DoesNotExist:
        return Response(data ={'massage': 'Product not found'})
    data = ReviewListSerializer(product1).data
    return  Response(data=data)