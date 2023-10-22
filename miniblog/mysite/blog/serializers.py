from rest_framework import serializers
from .models import Post
from rest_framework.authtoken.models import Token
from rest_framework.validators import UniqueValidator
from django.contrib.auth.password_validation import validate_password
from django.contrib.auth.models import User
from django.contrib.auth import authenticate

class PostSerializer(serializers.ModelSerializer):
    class Meta:
        model = Post
        fields = '__all__'

# 회원 가입
class RegisterSerializer(serializers.ModelSerializer):
    username = serializers.CharField(
        required = True, validators = [UniqueValidator(queryset=User.objects.all())] # ID 중복 검사
    )
    email = serializers.EmailField(
        required = True, validators = [UniqueValidator(queryset=User.objects.all())] # email 중복 검사
    )
    password = serializers.CharField(
        write_only = True,
        required = True,
        validators = [validate_password]
    )
    # 비밀번호 유효성 검사
    password2 = serializers.CharField(      
        write_only = True,      # 쓰기만 가능
        required = True         
    )

    class Meta:
        model = User
        fields = '__all__'
    
    def validate(self, attrs):
        if attrs['password'] != attrs['password']:
            raise serializers.ValidationError({'password': '비밀번호가 일치하지 않습니다.'})
        return attrs
    
    def create(self, validated_data):
        user = User.objects.create(
            username = validated_data['username'],
            email = validated_data['email']
        )
        user.set_password(validated_data['password']) # 비밀번호 암호화
        user.save()
        Token.objects.create(user=user) # user가 맞다면 토큰생성
        return user
    
# 로그인
class LoginSerializer(serializers.ModelSerializer):
    username = serializers.CharField(required=True)
    password = serializers.CharField(write_only=True, required=True)

    class Meta:
        model = User
        fields = ['username', 'password']
    
    def validate(self, data):
        print(data)
        user = authenticate(**data)
        print(user)
        if user:
            token = Token.objects.get(user=user)
            return token
        return serializers.ValidationError('유효하지 않은 로그인입니다.')