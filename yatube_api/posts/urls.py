from rest_framework.routers import DefaultRouter
from rest_framework.authtoken import views

from django.urls import include, path

from .views import PostViewSet, CommentViewSet, GroupViewSet


app_name = 'posts'

router = DefaultRouter()

router.register('api/v1/posts', PostViewSet)
router.register(r'api/v1/posts/(?P<post_id>\d+)/comments',
                CommentViewSet, basename='posts')
router.register('api/v1/groups', GroupViewSet)

urlpatterns = [
    path('api/v1/api-token-auth/', views.obtain_auth_token),
    path('', include(router.urls)),
]
