from django.contrib.auth.models import User
from django.forms.models import model_to_dict
from collections import OrderedDict
# serializer
from . serializers import (
    UserRegisterSerializer,
    UpdateProfileSerializer
)

# rest_framework
from rest_framework.authentication import TokenAuthentication
from rest_framework.authtoken.models import Token
from rest_framework.response import Response
from rest_framework import status
from rest_framework.decorators import (
    parser_classes,
    api_view
)
from rest_framework.parsers import (
    FormParser,
    MultiPartParser
)





@api_view(['POST'])
def user_register_view(request):
    username = request.data['username']
    if User.objects.filter(username__iexact=username).first():
        message = {"error":f'Username \'{username}\' already exists.'}
        return Response(message, status=status.HTTP_400_BAD_REQUEST)
    serializer = UserRegisterSerializer(data=request.data)
    if serializer.is_valid():
        serializer.save()
        message = {**serializer.data,'message':'Successfully registered'}
        return Response(message, status=status.HTTP_201_CREATED)
    return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


@api_view(['POST'])
def retrieve_token_view(request):
    username = request.data['username']
    user = User.objects.filter(username=username).first()
    if user:
        token = Token.objects.get_or_create(user=user)
        message = {'token':token[0].key, 'message':'Successfully authenticated'}
        return Response(message, status=status.HTTP_202_ACCEPTED)
    message = {'error':'Username or password did not match'}
    return Response(message, status=status.HTTP_401_UNAUTHORIZED)


@api_view(['PUT'])
@parser_classes([MultiPartParser, FormParser])
def user_update_profile_view(request, id):
    try:
        user = User.objects.get(id=id)
    except User.DoesNotExist:
        message = {'error': 'User does not exist.'}
        return Response(message, status=status.HTTP_400_BAD_REQUEST)
    data = OrderedDict()
    data.update(request.data)
    data['user'] = user.id
    serializer = UpdateProfileSerializer(user, data=data)
    if serializer.is_valid():
        serializer.save()
        message = {'message': 'Profile updated successfully.'}
        return Response(message, status=status.HTTP_202_ACCEPTED)
    return Response({**serializer.errors, 'message': 'Something went wrong'}, status=status.HTTP_400_BAD_REQUEST)


@api_view(['GET'])
def get_users_view(request):
    serializer = UserRegisterSerializer(User.objects.all(), many=True)
    users = [user['id'] for user in serializer.data]
    print(users)
    return Response(serializer.data)


@api_view(['GET'])
def user_detail_view(request, id):
    try:
        user = User.objects.get(id=id)
    except User.DoesNotExist :
        message = {'error': 'User does not exist.'}
        return Response(message, status=status.HTTP_400_BAD_REQUEST)
    serializer = UserRegisterSerializer(user)
    return Response(serializer.data)