from rest_framework.routers import DefaultRouter
from rest_framework.authtoken import views

from django.urls import include, path

from .views import PostViewSet, CommentViewSet, GroupViewSet


app_name = 'posts'

v1_router = DefaultRouter()

v1_router.register('posts', PostViewSet)
v1_router.register(r'posts/(?P<post_id>\d+)/comments',
                   CommentViewSet, basename='posts')
v1_router.register('groups', GroupViewSet)

urlpatterns = [
    path('v1/api-token-auth/', views.obtain_auth_token),
    path('v1/', include(v1_router.urls)),
]
