from .views import ToolAPIView, ToolListAPIView, ToolRetrieveAPIView
from django.urls import path

app_name = 'parser'

urlpatterns = [
    path('parse/', ToolAPIView.as_view(), name='parse'),
    path('tools/', ToolListAPIView.as_view(), name='tools-list'),
    path('tools/<int:id>/', ToolRetrieveAPIView.as_view(), name='tools-retrieve'),
]