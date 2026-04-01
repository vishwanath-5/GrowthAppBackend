from rest_framework import viewsets
from .models import Progress
from .serializers import ProgressSerializer
from rest_framework.permissions import IsAuthenticated

class ProgressViewSet(viewsets.ModelViewSet):
    serializer_class = ProgressSerializer
    permission_classes = [IsAuthenticated]

    def get_queryset(self):
        return Progress.objects.filter(user=self.request.user)