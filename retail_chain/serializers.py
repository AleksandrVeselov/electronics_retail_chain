from rest_framework import serializers

from retail_chain.models import Link


class LinkSerializer(serializers.ModelSerializer):
    """Сериализатор для модели звена сети"""
    class Meta:
        model = Link  # модель
        fields = '__all__'  # Поля для отображения
