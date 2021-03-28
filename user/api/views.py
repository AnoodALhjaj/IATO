
from rest_framework import generics;
from rest_framework.response import Response
from .serlizers import UserDisplaySerlizer,UserLoginSerlizer
from django.contrib.auth.models import  User
from rest_framework.permissions import IsAuthenticated,IsAuthenticatedOrReadOnly
from rest_framework.authtoken.models import Token
#from django.contrib.auth import authenticate
from rest_framework.authtoken.views import ObtainAuthToken
import requests
class CurrentUserAPIView(generics.ListCreateAPIView):
    queryset=User.objects.all()
    serializer_class=UserDisplaySerlizer
  #  permission_classes= (IsAuthenticated,)


# class LoginUser(generics.ListCreateAPIView):
#     serializer_class=UserLoginSerlizer
#     def get_queryset(self):
#         user = authenticate(username=self.request.username,password=self.request.password)
#         if user is not None:
#             print(user);
#             token = Token.objects.create(user=self.request.user);
#             print (token.key);
#             user = User.objects.get(id=token.user_id);
#             print(user);
#             return Response({'token': token.key, 'id': token.user_id,'username':user.username,"Name":user.first_name})
#         # A backend authenticated the credentials
#         else: print("fsf");

class CustomObtainAuthToken(ObtainAuthToken):
    def post(self, request, *args, **kwargs):
        response = super(CustomObtainAuthToken, self).post(request, *args, **kwargs)
        token = Token.objects.get(key=response.data['token'])
        user = User.objects.get(id=token.user_id);
        r = requests.get('http://127.0.0.1:8000/api/serAPI/UserEd/'+str(token.user_id)+"/")
        if r.status_code == 200:
              data=r.json()
              return Response({'token': token.key, 'id': token.user_id,'username':user.username,"Name":user.first_name,"Group":data['groups'][0]})



    