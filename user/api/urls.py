from django.urls import path
from .views import CurrentUserAPIView,CustomObtainAuthToken
from django.conf.urls import url

urlpatterns = [
       url(r'authenticate/', CustomObtainAuthToken.as_view()),
    path("user/",CurrentUserAPIView.as_view(),name="CurrentUser"),       
]
