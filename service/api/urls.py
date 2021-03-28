
from django.urls import path,include
from .views import ServicesAPI,CustomerAPI  ,NotifcationAPI , PermissionAPI ,GroupAPI,UserAPI,SmallServiceAPI , BigServiceAPI,CustomerBillAPI,ServiceBookDetailsAPI,BookServiceAPI,UserEdAPI,TrackingAPI
from rest_framework.routers import DefaultRouter

router=DefaultRouter()
router.register(r"serviceDisplay",ServicesAPI)
router.register(r"customer",CustomerAPI)
router.register(r"Notification",NotifcationAPI)
router.register(r"Group",GroupAPI)
router.register(r"Permission",PermissionAPI)
router.register(r"Users",UserAPI)
router.register(r"SamllService",SmallServiceAPI)
router.register(r"BigService",BigServiceAPI)
router.register(r"CustomerBill",CustomerBillAPI)
router.register(r"ServiceBookDetails",ServiceBookDetailsAPI)
router.register(r"BookService",BookServiceAPI)
router.register(r"UserEd",UserEdAPI)
router.register(r"TrackingAPI",TrackingAPI)


urlpatterns = [
        path("serAPI/",include(router.urls)),
   
   # path("service/",ServicesAPI.as_view(),name="Services")
]
