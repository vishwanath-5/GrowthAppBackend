from rest_framework import viewsets, permissions
from .models import Task
from .serializers import TaskSerializer


class TaskViewSet(viewsets.ModelViewSet):
    serializer_class = TaskSerializer
    permission_classes = [permissions.IsAuthenticated]

    # 🔐 Only logged-in user's tasks
    def get_queryset(self):
        return Task.objects.filter(user=self.request.user)

    # ➕ Assign task to logged-in user automatically
    def perform_create(self, serializer):
        serializer.save(user=self.request.user)