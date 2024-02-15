from rest_framework import serializers
from django.contrib.auth.models import User
from wallets_app.models import Wallet


class UserSerializer(serializers.ModelSerializer):
    """
    Serializer for User model
    """
    wallets = serializers.PrimaryKeyRelatedField(many=True, queryset=Wallet.objects.all())

    class Meta:
        model = User
        fields = ('id', 'username', 'email', "password", "wallets")
        extra_kwargs = {'password': {'write_only': True}}

    def create(self, validated_data):
        user = User(
            email=validated_data['email'],
            username=validated_data['username']
        )
        user.set_password(validated_data['password'])
        user.save()
        return user