from django.urls import path
from . import views
from .views import CommentListCreateAPIView

urlpatterns = [
    path('formations/', views.get_all_formations,name='formations'),
   path('formations/<str:pk>/', views.get_by_id_formation,name='get_by_id_formation'),
    path('comments/', CommentListCreateAPIView.as_view(), name='comment-list-create'),  # عرض وإنشاء التعليقات
   
]