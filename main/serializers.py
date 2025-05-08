from rest_framework import serializers

from .models import *


class BolimSerializer(serializers.ModelSerializer):
    class Meta:
        model = Bolim
        fields = '__all__'


class TaomSerializer(serializers.ModelSerializer):
    class Meta:
        model = Taom
        fields = '__all__'


class StolSerializer(serializers.ModelSerializer):
    class Meta:
        model = Stol
        fields = '__all__'


class BTaomSafeSerializer(serializers.ModelSerializer):
    taom = TaomSerializer(read_only=True, many=False)

    class Meta:
        model = BTaom
        fields = '__all__'


class BTaomSerializer(serializers.ModelSerializer):
    class Meta:
        model = BTaom
        fields = '__all__'


class BuyurtmaSafeSerializer(serializers.ModelSerializer):
    taomlar = BTaomSerializer(read_only=True, many=True)

    class Meta:
        model = Buyurtma
        fields = ['id', 'izoh', 'sana', 'hisoblandi', 'tolandi', 'taomlar']


class BuyurtmaSerializer(serializers.ModelSerializer):
    class Meta:
        model = Buyurtma
        fields = '__all__'