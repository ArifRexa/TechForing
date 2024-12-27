from django.urls import path
from comments.views import CommentViewSet

urlpatterns = [
    path('', CommentViewSet.as_view({'get': 'list', 'post': 'create'})),
    path('<int:pk>/', CommentViewSet.as_view({'get': 'retrieve', 'put': 'update', 'delete': 'destroy'}))
]
