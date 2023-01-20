from rest_framework import serializers
from .models import Women, Categories

class WomenSerilizers(serializers.ModelSerializer):
    class Meta:
        model = Women
        fields = '__all__'
