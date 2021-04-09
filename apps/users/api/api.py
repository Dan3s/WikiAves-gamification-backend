from rest_framework import status
from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework.decorators import api_view
from apps.users.models import User
from apps.users.api.serializers.user_serializers import UserSerializer, UserListSerializer

@api_view(['GET', 'POST'])
def user_api_view(request): #Para usar las funciones se debe usar un Decorator
    
    #List
    if request.method == 'GET':
        users = User.objects.all().values('id', 'name', 'last_names', 'username', 'password', 'email', 'city', 'region') #consulta
        users_list_serializer = UserListSerializer(users, many = True)#Many true para decirle a serializador que no es solo un objeto
        return Response(users_list_serializer.data, status = status.HTTP_200_OK)

    #Created
    elif request.method == 'POST':
        users_serializer = UserSerializer(data = request.data)
        if users_serializer.is_valid():
            users_serializer.save()
            return Response({'message': 'Usuario creado correctamente'}, status = status.HTTP_201_CREATED)
        return Response(users_serializer.errors, status = status.HTTP_400_BAD_REQUEST)

@api_view(['GET', 'PUT', 'DELETE'])
def user_detail_view(request, pk=None):

#Consulta
    user = User.objects.filter(id = pk).first()
    
    #Validación
    if user: 
        #retrieve
        if request.method == 'GET':
            users_serializer = UserSerializer(user)
            return Response(users_serializer.data, status = status.HTTP_200_OK)
    #update
        elif request.method == 'PUT':
        
            users_serializer = UserSerializer(user, data = request.data)
            if users_serializer.is_valid():
                users_serializer.save()
                return Response(users_serializer.data, status = status.HTTP_200_OK)
            return Response(users_serializer.errors, status = status.HTTP_400_BAD_REQUEST)
    #delete
        elif request.method == 'DELETE':

            user.delete()
            return Response({'message': 'Eliminado'}, status = status.HTTP_200_OK)

    return Response({'message': 'No se ha encontrado el usuario'}, status = status.HTTP_400_BAD_REQUEST)

    


