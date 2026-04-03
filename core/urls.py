from django.contrib import admin
from django.urls import path, include
from rest_framework_simplejwt.views import TokenObtainPairView
from django.http import JsonResponse

def home(request):
    return JsonResponse({"status": "Backend running 🚀"})

urlpatterns = [
    path('', home),  # 👈 ADD THIS

    path('admin/', admin.site.urls),

    path('api/users/', include('users.urls')),
    path('api/tasks/', include('tasks.urls')),
    path('api/progress/', include('progress.urls')),
    path('api/token/', TokenObtainPairView.as_view(), name='token'),
]