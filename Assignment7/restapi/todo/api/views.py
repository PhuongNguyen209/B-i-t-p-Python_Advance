from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from rest_framework import permissions
from todo.models import Customer
from .serializers import CustomerSerializer

class CustomerListApiView(APIView):
    permission_classes = [permissions.IsAuthenticated]

    def get(self, request, *args, **kwargs):
        todos = Customer.objects.filter(user = request.user.id)
        serializer = CustomerSerializer(todos, many=True)
        return Response(serializer.data, status= status.HTTP_200_OK)

    def post(self, request, *args, **kwargs):
        data= {
            'name': request.data.get('name'),
            'age': request.data.get('age'),
            'address': request.data.get('address'),
            'tel': request.data.get('tel'),
            'completed': request.data.get('completed'),
            'user': request.user.id
        }
        serializer = CustomerSerializer(data=data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status= status.HTTP_201_CREATED)
        
        return Response(serializer.errors, status= status.HTTP_400_BAD_REQUEST)

class CustomerDetailApiView(APIView):
    permission_classes = [permissions.IsAuthenticated]

    def get_object(self, customer_id, user_id):
        try:
            return Customer.objects.get(id= customer_id, user= user_id)
        except Customer.DoesNotExist:
            return None

    def get(self, request, customer_id, *args, **kwargs):
        customer_instance = self.get_object(customer_id, request.user.id)
        if not customer_instance:
            return Response(
                {"res": "Object does not exists"},
                status= status.HTTP_400_BAD_REQUEST
            )
        
        serializer = CustomerSerializer(customer_instance)
        return Response(serializer.data, status= status.HTTP_200_OK)
    
    def put(self, request, customer_id, *args, **kwargs):
        customer_instance = self.get_object(customer_id, request.user.id)
        if not customer_instance:
            return Response(
                {"res": "Object does not exists"},
                status= status.HTTP_400_BAD_REQUEST
            )
        data= {
            'name': request.data.get('name'),
            'age': request.data.get('age'),
            'address': request.data.get('address'),
            'tel': request.data.get('tel'),
            'completed': request.data.get('completed'),
            'user': request.user.id
        }
        serializer = CustomerSerializer(instance= customer_instance, data=data, partial= True)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status= status.HTTP_200_OK)
        return Response(serializer.errors, status= status.HTTP_400_BAD_REQUEST)

    def delete(self, request, customer_id, *args, **kwargs):
        customer_instance = self.get_object(customer_id, request.user.id)
        if not customer_instance:
            return Response(
                {"res": "Object does not exists"},
                status= status.HTTP_400_BAD_REQUEST
            )
        customer_instance.delete()
        return Response(
                {"res": "Object deleted!"},
                status= status.HTTP_200_OK
            )