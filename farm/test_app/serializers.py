from rest_framework.serializers import ModelSerializer
from palm.models import Gcg, Anode
from django.contrib.auth import get_user_model
class GcgSerializer(ModelSerializer):
    class Meta:
        model = Gcg
        fields = '__all__'
class UserSerializer(ModelSerializer):
    class Meta:
        model = get_user_model()
        fields = '__all__'
class AnodeSerializer(ModelSerializer):
    class Meta:
        model = Anode
        fields = '__all__'