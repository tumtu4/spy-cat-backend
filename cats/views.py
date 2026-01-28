from rest_framework import viewsets
from .models import Cat
from .serializers import CatSerializer, CatSalaryUpdateSerializer


class CatViewSet(viewsets.ModelViewSet):
    queryset = Cat.objects.all()

    def get_serializer_class(self):
        if self.action in ['update', 'partial_update']:
            return CatSalaryUpdateSerializer
        return CatSerializer

