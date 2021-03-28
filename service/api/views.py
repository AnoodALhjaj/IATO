from rest_framework import generics,viewsets
from ..models import Service, Customer ,  Notification , BigService, SmallService,CustomerBill,BookService,ServiceBookDetails,Tracking
from .serlizer import ServiceSerlizer, CustomerSerlizer , NotificationSerlizer , GroupSerlizer ,PermissionSerlizer, UserSerlizer,BigServiceSerlizer , SmallServiceSerlizer,CustomerBillSerlizer,ServiceBookDetailsSerlizer,BookServiceSerlizer,UserSerlizerEd,TrackingSerlizer,CustomerBillSignalSerlizer
from django.contrib.auth.models import Group,Permission,User
from rest_framework.response import Response    
from rest_framework import status
from rest_framework import filters



class CustomerBillSignalAPI(viewsets.ModelViewSet):
    
    queryset=CustomerBill.objects.all()
    serializer_class=CustomerBillSignalSerlizer

    
class TrackingAPI(viewsets.ModelViewSet):
    
    queryset=Tracking.objects.all().order_by("-id")
    serializer_class=TrackingSerlizer


class UserAPI(viewsets.ModelViewSet):
    
    queryset=User.objects.all()
    serializer_class=UserSerlizer

class UserEdAPI(viewsets.ModelViewSet):
    queryset=User.objects.all()
    serializer_class=UserSerlizerEd


class SmallServiceAPI(viewsets.ModelViewSet):
    queryset=SmallService.objects.all()
    serializer_class=SmallServiceSerlizer
    def create(self, request, *args, **kwargs):
        print(request.data)
        data = request.data
        many = isinstance(data, list)
        print (data, many)
        serializer = self.get_serializer(data=data, many=many)
        serializer.is_valid(raise_exception=True)
        self.perform_create(serializer)
        headers = self.get_success_headers(serializer.data)
        return Response(
                serializer.data,
                status=status.HTTP_201_CREATED,
                headers=headers
        )

class BigServiceAPI(viewsets.ModelViewSet):
    queryset=BigService.objects.all()
    serializer_class=BigServiceSerlizer
    def create(self, request, *args, **kwargs):
        print(request.data)
        data = request.data
        many = isinstance(data, list)
        print (data, many)
        serializer = self.get_serializer(data=data, many=many)
        serializer.is_valid(raise_exception=True)
        self.perform_create(serializer)
        headers = self.get_success_headers(serializer.data)
        return Response(
                serializer.data,
                status=status.HTTP_201_CREATED,
                headers=headers
        )

class GroupAPI(viewsets.ModelViewSet):
    queryset=Group.objects.all()
    serializer_class=GroupSerlizer


class PermissionAPI(viewsets.ModelViewSet):
    queryset=Permission.objects.all()
    serializer_class=PermissionSerlizer


class ServicesAPI(viewsets.ModelViewSet):
    queryset=Service.objects.all()
    serializer_class=ServiceSerlizer


class CustomerAPI(viewsets.ModelViewSet):
    queryset=Customer.objects.all()
    serializer_class=CustomerSerlizer





class NotifcationAPI(viewsets.ModelViewSet):
    queryset=Notification.objects.all()
    serializer_class=NotificationSerlizer



class CustomerBillAPI(viewsets.ModelViewSet):
    queryset=CustomerBill.objects.all().order_by("-id")
    serializer_class=CustomerBillSerlizer



class ServiceBookDetailsAPI(viewsets.ModelViewSet):
    queryset=ServiceBookDetails.objects.all().order_by("-id")
    serializer_class=ServiceBookDetailsSerlizer
    filter_backends = [filters.SearchFilter]
    search_fields = ['serv_smallserv_small_service', 'serv_bigserv_big_service']
    def create(self, request, *args, **kwargs):
        #data = request.data.get('items', request.data)
        
        data = request.data
        many = isinstance(data, list)
        #print (data, many)
        serializer = self.get_serializer(data=data, many=many)
        serializer.is_valid(raise_exception=True)
        self.perform_create(serializer)
        headers = self.get_success_headers(serializer.data)
        return Response(
                serializer.data,
                status=status.HTTP_201_CREATED,
                headers=headers
        )


class BookServiceAPI(viewsets.ModelViewSet):
    queryset=BookService.objects.all()
    serializer_class=BookServiceSerlizer