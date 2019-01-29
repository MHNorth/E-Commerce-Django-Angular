from django.contrib.auth.models import User
from rest_framework import serializers

class UserSerializer(serializers.HyperlinkedModelSerializer): # Hyperlinked serializer allows the use of primary keys and various other relationships
        class Meta:
                model = User
                fields = ('url', 'username', 'email')
