from rest_framework import viewsets
from rest_framework.viewsets import ModelViewSet

from .models import *
from .serializers import *


class BolimViewSet(viewsets.ModelViewSet):
    queryset = Bolim.objects.all()
    serializer_class = BolimSerializer


class TaomViewSet(viewsets.ModelViewSet):
    queryset = Taom.objects.all()
    serializer_class = TaomSerializer


class StolViewSet(viewsets.ModelViewSet):
    queryset = Stol.objects.all()
    serializer_class = StolSerializer


class BuyurtmaViewSet(viewsets.ModelViewSet):
    queryset = Buyurtma.objects.all()
    serializer_class = BuyurtmaSerializer

    def get_serializer_class(self):
        if self.action in ['list', 'retrieve']:
            return BuyurtmaSafeSerializer
        return self.serializer_class


class BTaomViewSet(viewsets.ModelViewSet):
    queryset = BTaom.objects.all()
    serializer_class = BTaomSerializer

    def get_serializer_class(self):
        if self.action in ['list', 'retrieve']:
            return BTaomSafeSerializer
        return self.serializer_class
