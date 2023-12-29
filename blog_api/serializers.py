from django.contrib.auth.models import User
from rest_framework import serializers
from rest_framework.authtoken.models import Token
from blog.models import Post, Topic
from users.models import Profile




class TopicSerializer(serializers.ModelSerializer):
    class Meta:
        model = Topic 
        fields = '__all__'


class PostSerializer(serializers.ModelSerializer):
    topic = serializers.CharField(source='topic.name')
    author = serializers.CharField(source='author.username')
    class Meta:
        model = Post 
        fields = '__all__'


class UserRegisterSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = '__all__'

        extra_kwargs = {
            'password':{
                'write_only': True,
                'required': True
            }
        }

    def create(self, validated_data):
        user = User.objects.create_user(**validated_data)
        Token.objects.create(user=user)
        return user
    

class UpdateProfileSerializer(serializers.ModelSerializer):
    class Meta:
        model = Profile
        fields = '__all__'

    
    def update(self, instance, validated_data):
        instance.username = validated_data.get('username', instance.username)
        instance.first_name = validated_data.get('first_name', instance.first_name)
        instance.last_name = validated_data.get('last_name', instance.last_name)
        instance.email = validated_data.get('email', instance.email)
        instance.save()

        profile = Profile.objects.filter(user__id=instance.id).first()
        profile.image = validated_data.get('image')
        profile.username = instance.username
        profile.first_name = instance.first_name
        profile.last_name = instance.last_name
        profile.email = instance.email
        profile.save()
        return instance