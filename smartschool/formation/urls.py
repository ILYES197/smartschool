from django.urls import path
from . import views
<<<<<<< HEAD
=======
from .views import CommentListCreateAPIView
>>>>>>> 7cb928f279a365f5e97b4268eb287317d67d7e1e

urlpatterns = [
    path('formations/', views.get_all_formations,name='formations'),
   path('formations/<str:pk>/', views.get_by_id_formation,name='get_by_id_formation'),
<<<<<<< HEAD
=======
    path('comments/', CommentListCreateAPIView.as_view(), name='comment-list-create'),  # عرض وإنشاء التعليقات
>>>>>>> 7cb928f279a365f5e97b4268eb287317d67d7e1e
   
]