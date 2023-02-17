from django.urls import include, path
from users.views import UserViewSet
from rest_framework.routers import SimpleRouter

from rest_framework_simplejwt.views import TokenObtainPairView, TokenRefreshView

# Register user router
users_router = SimpleRouter()
users_router.register('users', UserViewSet, basename='user')

urlpatterns = [
    path('', include(users_router.urls)),

    path('auth/', include('djoser.urls')),
    path('auth/', include('djoser.urls.jwt')),

    path('token/', TokenObtainPairView.as_view()),
    path('token/refresh/', TokenRefreshView.as_view()),
]

