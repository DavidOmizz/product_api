# from django.http import HttpResponse

# from rest_framework.decorators import api_view
# from rest_framework.response import Response

# from app.models import *
# from . serializers import *

# @api_view(['POST','GET'])
# def AddListCategory(request):
#     if request.method == 'POST':
#         serializer = CategorySerializer(data= request.data)
#         if serializer.is_valid():
#             serializer.save()
#         return Response({
#             'message':'Category added successfully',
#             'category': serializer.data
#         })
#     elif request.method == 'GET':
#         category = Category.objects.all()
#         serializer = CategorySerializer(category, many=True)
#         return Response({
#             'message':'List of categories added successfully',
#             'categories': serializer.data
#         })
    
#     else:
#         return Response({
#             'message':'Wrong call'
#         })


# @api_view(['POST','GET'])
# def Tags(request):
#     if request.method == 'POST':
#         serializer = TagSerializer(data = request.data)
#         if serializer.is_valid():
#             serializer.save()
#         return Response({
#             'message':'Tag added successfully',
#             'tag': serializer.data
#         })
#     elif request.method == 'GET':
#         tag = Tag.objects.all()
#         serializer = TagSerializer(tag, many=True)
#         return Response({
#             'message':'List of tags added successfully',
#             'tag': serializer.data
#         })

# @api_view(['GET'])
# def ListProduct(request):
#     # person = {
#     #     'name':'John',
#     #     'email':'john@example.com'
#     # }
#     product = Product.objects.all()
#     serializer = ProductSerializer(product, many=True)
#     return Response({
#         'message':'List of products',
#         'product': serializer.data,
#         'status': 200
#     })

# @api_view(['POST'])
# def AddProdcut(request):
#     serializer = ProductSerializer(data= request.data)
#     if serializer.is_valid():
#         serializer.save()
#     return Response({
#         'message': 'Product added successfully',
#         'product': serializer.data
#     })


from django.http import HttpResponse
from rest_framework.decorators import api_view, APIView
from rest_framework.response import Response
from rest_framework import status  # Import status codes
from rest_framework.viewsets import ModelViewSet

from app.models import Category, Tag, Product  # Import model classes
from .serializers import CategorySerializer, TagSerializer, ProductSerializer, TagSerial

@api_view(['POST', 'GET'])
def AddListCategory(request):
    if request.method == 'POST':
        serializer = CategorySerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response({'message': 'Category added successfully', 'category': serializer.data}, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    
    elif request.method == 'GET':
        categories = Category.objects.all()
        serializer = CategorySerializer(categories, many=True)
        return Response({'message': 'List of categories added successfully', 'categories': serializer.data}, status=status.HTTP_200_OK)
    
    else:
        return Response({'message': 'Wrong call'}, status=status.HTTP_405_METHOD_NOT_ALLOWED)

class TagViewset(ModelViewSet):
    queryset = Tag.objects.all()
    serializer_class = TagSerializer

@api_view(['POST', 'GET'])
def Tags(request):
    if request.method == 'POST':
        serializer = TagSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response({'message': 'Tag added successfully', 'tag': serializer.data}, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    
    if request.method == 'GET':
        tags = Tag.objects.all()
        serializer = TagSerializer(tags, many=True)
        return Response({'message': 'List of tags added successfully', 'tags': serializer.data}, status=status.HTTP_200_OK)


class TagView(APIView):
    serializer_class = TagSerializer
    def get(self,request):
        tags = Tag.objects.all().values()
        return Response(tags)
    
    def post(self,request):
        serializer_obj = TagSerial(data= request.data)
        if(serializer_obj.is_valid()):
            Tag.objects.create(name = serializer_obj.data.get('name'))
        tags = Tag.objects.all().filter(name=request.data['name']).values()
        return Response(tags)

@api_view(['GET','POST'])
def Products(request):
    if request.method == 'GET':
        products = Product.objects.all()
        serializer = ProductSerializer(products, many=True)
        return Response({'message': 'List of products', 'products': serializer.data}, status=status.HTTP_200_OK)
    
    elif request.method == 'POST':
        serializer = ProductSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response({'message': 'Product added successfully', 'products': serializer.data}, status= status.HTTP_201_CREATED)
        return Response(serializer.errors, status= status.HTTP_400_BAD_REQUEST)

# @api_view(['GET','PUT','DELETE'])
# def product_detail(request,id):
#     product = Product.objects.get(pk=id)
#     if request.method == 'GET':
#         serilizer = ProductSerializer(product)
#         return Response({'Product':serilizer.data}, status=status.HTTP_200_OK)
    
#     if request.method == 'PUT':
#         serializer = ProductSerializer(product, data = request.data)
#         if serializer.is_valid():
#             serializer.save()
#             return Response(serializer.data)
@api_view(['GET', 'PUT', 'DELETE'])
def product_detail(request, id):
    try:
        product = Product.objects.get(pk=id)
    except Product.DoesNotExist:
        return Response({'message': 'Product not found'}, status=status.HTTP_404_NOT_FOUND)

    if request.method == 'GET':
        serializer = ProductSerializer(product)
        return Response({'Product': serializer.data}, status=status.HTTP_200_OK)

    elif request.method == 'PUT':
        serializer = ProductSerializer(product, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response({'message': 'Product updated successfully', 'product': serializer.data}, status=status.HTTP_200_OK)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    elif request.method == 'DELETE':
        product.delete()
        return Response({'message': 'Product deleted successfully'}, status=status.HTTP_204_NO_CONTENT)

@api_view(['GET','PUT'])      
def tags_detail(request,id):
    try:
        tag = Tag.objects.get(pk=id)
    except Tag.DoesNotExist:
        return Response({'message': 'Tag not found'}, status=status.HTTP_404_NOT_FOUND)


    if request.method == 'GET':
        serializer = TagSerializer(tag)
        return Response({'Tag': serializer.data}, status=status.HTTP_200_OK)
    if request.method == 'PUT':
        serializer = TagSerializer(tag, data = request.data)
        if serializer.is_valid():
            serializer.save()
            return Response({'Tags updated': serializer.data}, status=status.HTTP_201_CREATED)



# @api_view(['POST'])
# def AddProduct(request):
#     serializer = ProductSerializer(data=request.data)
#     if serializer.is_valid():
#         serializer.save()
#         return Response({'message': 'Product added successfully', 'product': serializer.data}, status=status.HTTP_201_CREATED)
#     return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

