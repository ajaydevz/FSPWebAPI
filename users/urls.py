from django.urls import path
from .views import UserList,UserDetails,MyTokenObtainPairView,UserRegister
from rest_framework_simplejwt.views import TokenRefreshView
from django.conf.urls.static import static
from django.conf import settings

urlpatterns = [
    path('token/', MyTokenObtainPairView.as_view(), name='token_obtain_pair'),
    path('token/refresh/', TokenRefreshView.as_view(), name='token_refresh'),
    


]+ static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)