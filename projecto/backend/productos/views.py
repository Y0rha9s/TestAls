from rest_framework import viewsets, status
from rest_framework.response import Response
from rest_framework.parsers import MultiPartParser, FormParser, JSONParser
from .models import Producto
from .serializers import ProductoSerializer

class ProductoViewSet(viewsets.ModelViewSet):
    """
    ViewSet para manejar todas las operaciones CRUD de productos
    """
    queryset = Producto.objects.all().order_by('-created_at')
    serializer_class = ProductoSerializer
    parser_classes = [MultiPartParser, FormParser, JSONParser]
    
    def list(self, request):
        """Listar todos los productos"""
        queryset = self.get_queryset()
        serializer = self.get_serializer(queryset, many=True, context={'request': request})
        return Response({
            'success': True,
            'count': len(serializer.data),
            'data': serializer.data
        })
    
    def create(self, request):
        """Crear un nuevo producto"""
        serializer = self.get_serializer(data=request.data, context={'request': request})
        if serializer.is_valid():
            producto = serializer.save()
            return Response({
                'success': True,
                'message': 'Producto creado exitosamente',
                'data': serializer.data
            }, status=status.HTTP_201_CREATED)
        return Response({
            'success': False,
            'errors': serializer.errors
        }, status=status.HTTP_400_BAD_REQUEST)