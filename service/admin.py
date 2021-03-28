from django.contrib import admin
from .models import Customer,Notification,BigService,Service,ServiceBookDetails,SmallService,BookService



admin.site.register(Customer)
admin.site.register(Notification)
admin.site.register(BigService)
admin.site.register(Service)
admin.site.register(SmallService)
admin.site.register(ServiceBookDetails)
admin.site.register(BookService)