from django.urls import path
from comment.api.views import CommentCreatedAPIView,CommentListAPIView, CommentUpdateAPIView
app_name = "create"
urlpatterns = [
    path('create', CommentCreatedAPIView.as_view(), name='create'),
    path('list', CommentListAPIView.as_view(), name='list'),
    # path('delete/<pk>', CommentDeleteAPIView.as_view(), name='delete'),
    path('update/<pk>', CommentUpdateAPIView.as_view(), name='update')

]
