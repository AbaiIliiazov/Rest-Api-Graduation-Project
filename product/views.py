from rest_framework import status
from django_filters.rest_framework import DjangoFilterBackend
from rest_framework.permissions import IsAuthenticated
from rest_framework.viewsets import ModelViewSet
from product.filters import ProductFilter
from product.models import Product
from product.serializers import ProductSerializer
from rest_framework.response import Response
from django.http import Http404

class ProductViewSet(ModelViewSet):
    queryset = Product.objects.all()
    serializer_class = ProductSerializer
    filter_backends = [DjangoFilterBackend]
    filterset_class = ProductFilter

    def get_permissions(self):
        if self.action in ['create','update', 'partial_update','destroy']:
            return [IsAuthenticated()]
        return []

    def destroy(self, request, *args, **kwargs):
        try:
            instance = self.get_object()
            self.perform_destroy(instance)
        except Http404:
            return Response ({'Error': 'product not found'}, status = status.HTTP_404_NOT_FOUND)

        return Response({'Success':'Product deleted'}, status = status.HTTP_204_NO_CONTENT)