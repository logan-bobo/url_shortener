from django.urls import path, include

urlpatterns = [
    path('', include('shortening_service.urls')),
]
