from django.contrib.auth.models import User
from django.contrib.auth.password_validation import validate_password
from rest_framework import serializers
from rest_framework.validators import UniqueValidator

from main.models import Buyer


class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = Buyer
        fields = ['user', 'number', 'avatar']
        depth = 1


class RegisterSerializer(serializers.ModelSerializer):
    email = serializers.EmailField(
        required=True,
        validators=[UniqueValidator(queryset=User.objects.all())]
    )
    password = serializers.CharField(
        write_only=True, required=True, validators=[validate_password])
    password2 = serializers.CharField(write_only=True, required=True)
    phone = serializers.CharField(write_only=True, required=False)
    avatar = serializers.ImageField(write_only=True, required=False)

    class Meta:
        model = User
        fields = ('password', 'password2',
                  'first_name', 'last_name',
                  'email', 'phone', 'avatar')
        extra_kwargs = {
            'first_name': {'required': True},
            'last_name': {'required': True}
        }

    def validate(self, attrs):
        if attrs['password'] != attrs['password2']:
            raise serializers.ValidationError(
                {"error": "Password fields didn't match."})
        return attrs

    def create(self, validated_data):
        user = User.objects.create(
            username=validated_data.get('email'),
            email=validated_data.get('email'),
            first_name=validated_data.get('first_name'),
            last_name=validated_data.get('last_name')
        )
        user.set_password(validated_data['password'])
        user.save()

        buyer = Buyer.objects.create(user=user)
        buyer.number = validated_data.get('phone')
        buyer.avatar = validated_data.get('avatar')
        buyer.save()

        return user


class ChangePasswordSerializer(serializers.Serializer):
    model = User

    old_password = serializers.CharField(required=True, validators=[validate_password])
    new_password = serializers.CharField(required=True, validators=[validate_password])
    new_password_2 = serializers.CharField(required=True)
