from rest_framework import serializers
from django.contrib.auth import get_user_model


User = get_user_model()


class CustomUserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ('id', 'username', 'email', 'first_name', 'last_name', 'password')
        extra_kwargs = {'password': {'write_only': True}}

    def create(self, validated_data):
        user = User.objects.create_user(**validated_data)
        user.save()
        return user


class AccessTokenSerializer(serializers.Serializer):
    access_token = serializers.CharField(write_only=True)


class UpdateUserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ['first_name', 'last_name', 'profile_picture']  # Only allow updating these fields

    def update(self, instance, validated_data):
        # if not instance.is_email_verified:
        #     raise serializers.ValidationError('Email is not verified.')

        instance.first_name = validated_data.get('first_name', instance.first_name) if validated_data.get('first_name') else instance.first_name
        instance.last_name = validated_data.get('last_name', instance.last_name) if validated_data.get('last_name') else instance.last_name

        # Handle profile picture update
        profile_picture = validated_data.get('profile_picture', None)
        if profile_picture:
            instance.profile_picture = profile_picture

        instance.save()
        return instance


class LogoutSerializer(serializers.Serializer):
    pass


class AuthSerializer(serializers.Serializer):
    code = serializers.CharField(required=False)
    error = serializers.CharField(required=False)


class GoogleLoginSerializer(serializers.Serializer):
    access_token = serializers.CharField(required=True)
