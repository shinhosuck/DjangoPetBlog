from django.contrib.auth.forms import UserCreationForm 
from blog.models import Post
from django.contrib.auth.models import User

# serializer
from . serializers import PostSerializer

# rest_framework
from rest_framework.authentication import TokenAuthentication
from rest_framework.response import Response
from rest_framework import status
from rest_framework.parsers import (
    JSONParser,
    MultiPartParser,
    FormParser
)
from rest_framework.permissions import (
    AllowAny,
    IsAuthenticated
)
from rest_framework.decorators import (
    renderer_classes,
    parser_classes,
    authentication_classes,
    permission_classes,
    api_view
)




@api_view(['GET'])
@permission_classes([AllowAny])
def post_list_view(request):
    posts = Post.objects.all()
    serializer = PostSerializer(posts, many=True)
    return Response(serializer.data, status=status.HTTP_200_OK)


