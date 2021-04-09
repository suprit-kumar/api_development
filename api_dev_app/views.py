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

            if todo_name is None:
                response['message'] = 'Todo Required'
                raise Exception("Name not found")
            if todo_description is None:
                response['message'] = 'Description Required'
                raise Exception("Description not found")

            todo_obj = Todo.objects.create(todo_name=todo_name, todo_description=todo_description)
            payload = {'todo_id': todo_obj.id, 'todo_name': todo_obj.todo_name,
                       'todo_description': todo_obj.todo_description, }
            response['status'] = 200
            response['message'] = 'Your Todo is saved '
            response['data'] = payload

        except Exception as e:
            print("Exception -->", e)
        return Response(response)

    def delete(self, request):
        try:

            todo_id = request.GET.get('todo_id')
            if todo_id is None:
                response['message'] = 'Todo id Required'
                raise Exception("Todo id not found")
            try:
                todo_obj = Todo.objects.get(id=todo_id)
                todo_obj.delete()
                response['status'] = 200
                response['message'] = 'Todo Deleted'
            except Exception as e:
                response['message'] = 'Invalid Todo Id'

        except Exception as e:
            print("Exception -->", e)
        return Response(response)

    def update(self, request):
        try:
            data = request.data
            todo_id = data.get('todo_id')
            todo_name = data.get('todo_name')
            todo_description = data.get('todo_description')
            is_completed = data.get('is_completed')
            if todo_id is None:
                response['message'] = 'Todo id Required'
                raise Exception("Todo id not found")
            try:
                todo_obj = Todo.objects.get(id=todo_id)
                todo_obj.todo_name = todo_name
                todo_obj.todo_description = todo_description
                todo_obj.is_completed = is_completed
                todo_obj.save()
                response['status'] = 200
                response['message'] = 'Todo Updated'
            except Exception as e:
                response['message'] = 'Invalid Todo Id'

        except Exception as e:
            print("Exception -->", e)
        return Response(response)


TodoView = TodoView.as_view()
