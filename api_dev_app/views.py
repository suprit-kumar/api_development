from django.shortcuts import render
from rest_framework.response import Response
from rest_framework.decorators import api_view
from .serializers import ProductSerializer
from .models import *
from rest_framework.views import APIView


# Create your views here.


@api_view(['GET'])
def apiOverview(request):
    api_urls = {
        'List': '/product-list/',
        'Detail View': '/product-detail/<int:id>',
        'Create': '/product-create/',
        'Update': '/product-update/<int:id>',
        'Delete': '/product-delete/<int:id>',
    }

    return Response(api_urls)


@api_view(['GET'])
def showAll(request):
    products = Product.objects.all()
    serializer = ProductSerializer(products, many=True)
    return Response(serializer.data)


@api_view(['GET'])
def viewProduct(request, pk):
    product = Product.objects.get(id=pk)
    serializer = ProductSerializer(product, many=False)
    return Response(serializer.data)


@api_view(['POST'])
def createProduct(request):
    serializer = ProductSerializer(data=request.data)
    if serializer.is_valid():
        serializer.save()
    return Response(serializer.data)


@api_view(['POST'])
def updateProduct(request, pk):
    product = Product.objects.get(id=pk)
    serializer = ProductSerializer(instance=product, data=request.data)
    if serializer.is_valid():
        serializer.save()
    return Response(serializer.data)


@api_view(['GET'])
def deleteProduct(request, pk):
    product = Product.objects.get(id=pk)
    product.delete()
    return Response({'success': 'Item deleted successfully'})


response = {}
response['status'] = 500
response['message'] = 'Something Went Wrong'

class TodoView(APIView):
    def get(self, request):

        try:
            todo_objs = Todo.objects.all()
            payload = []
            for obj in todo_objs:
                payload.append({
                    'todo_name': obj.todo_name,
                    'todo_description': obj.todo_description,
                    'is_completed': obj.is_completed,
                })
            response['status'] = 200
            response['message'] = 'All Todos'
            response['data'] = payload
        except Exception as e:
            print("Exception -->", e)
        return Response(response)

    def post(self, request):
        try:
            data = request.data

            todo_name = data.get('todo_name')
            todo_description = data.get('todo_description')
            print(todo_name)
            print(todo_description)

            response['status'] = 200
            response['message'] = 'Your Todo is saved '

        except Exception as e:
            print("Exception -->", e)
        return Response(response)

    def delete(self, request):
        pass

    def update(self, request):
        pass


TodoView = TodoView.as_view()