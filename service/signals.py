
from django.db.models.signals import post_save,pre_save
from django.dispatch import receiver
from .models import CustomerBill , BigService,SmallService, ServiceBookDetails
import requests



@receiver(post_save,sender=CustomerBill)
def add_tracking(sender, instance, created,*args, **kwargs):
    print ('Tracking')
    if created:
        #instance.pk
        if(instance.user_id is not None):
            print ('this is an insert')
            myobj={"desc": "Insert number "+str(instance.id),"task": "CustomerBIll","table_id": instance.id,"username":instance.user_id.username, "user_id":instance.user_id.id}
            r = requests.post('http://127.0.0.1:8000/api/serAPI/TrackingAPI/', data = myobj)
            if r.status_code == 201:
                print ('Tracking insert Done')
                
        else:
            print("Insert mode user is not Define")
            # #http://127.0.0.1:8000/api/serAPI/CustomerBill/
            # myobj={ "user_id": instance.user_id}
            # r = requests.post('http://127.0.0.1:8000/api/serAPI/bill/5/'+str(instance.pk)+"/", data = myobj)
            # if r.status_code == 200:
            #     print ('Tracking insert Done')    
                

    else:
            print ('this is an update')
            myobj={"desc": "Updated invoice number "+str(instance.id),"task": "CustomerBIll","table_id": instance.id,"username":instance.user_id.username, "user_id":instance.user_id.id}
            r = requests.post('http://127.0.0.1:8000/api/serAPI/TrackingAPI/', data = myobj)
            if r.status_code == 200:
                
                print ('Tracking Update Done')

            
@receiver(pre_save,sender=SmallService)
def add_tracking_SmallService(sender, instance,*args, **kwargs):
    if not instance._state.adding:
        print("small Service Update")
        # oldservice=sender.objects.get(id=instance.id)
        # text="";
        # if instance.ser_name!=oldservice.ser_name:
        #     text+=" service name Change from "+instance.ser_name+" to "+oldservice.ser_name
        # if instance.ser_number!=oldservice.ser_number:
        #     text+=" service number Change from "+str(instance.ser_number)+" to "+str(oldservice.ser_number)
        # if instance.price!=oldservice.price:
        #     text+=" service price Change from "+str(instance.price)+" to "+str(oldservice.price)
        # if instance.dateServics!=oldservice.dateServics:
        #     text+=" service number Change from "+str(instance.dateServics)+" to "+str(oldservice.dateServics)
        # print(instance.id)
        # print(instance.pk)
        # id=int(instance.id)
        # #customer_bill_id_id
        # #Bill=ServiceBookDetails.objects.get(small_service_id=id)
        # b=ServiceBookDetails.objects.get(small_service_id=oldservice.id)
        # print(b)
        # Customer=CustomerBill.objects.get(id=Bill.customer_bill_id)
        # if CustomerBill.Condition is None:
        #     print ( 'User update is the same')
        #     print(Bill.user_id)
        #     myobj={"desc":text,"task": "SmallService","table_id": Customer.id,"username":Customer.user_id.username, "user_id":Customer.user_id.id}
        #     r = requests.post('http://127.0.0.1:8000/api/serAPI/TrackingAPI/', data = myobj)
        #     if r.status_code == 201:
        #         print ('Service Track Update Done')
        # else:
        #     print ( 'User updated is on the Conditions')


        
        
            


@receiver(pre_save,sender=BigService)
def add_tracking_BigService(sender, instance,*args, **kwargs):
    if not instance._state.adding:
        print("Service Update")

# @receiver(pre_delete, sender=Question)
# def Question_delete(sender, instance, **kwargs):
#     # Pass false so FileField doesn't save the model.
#     instance.img.delete(False)






# r = requests.get('http://127.0.0.1:8000/api/serAPI/SamllService/'+str(instance.pk)+"/")
#         if r.status_code == 200:
#                 data=r.json()
#                 print(data)
#                 print(data['customer_bill_id'])
#                 Customer=CustomerBill.objects.get(id=data['customer_bill_id'])
#                 if Customer.Condition is None:
#                     print ( 'User update is the same')
#                     print(data['user_id'])
#                     myobj={"desc":text,"task": "SmallService","table_id": Customer.id,"username":Customer.user_id.username, "user_id":Customer.user_id.id}
#                     r = requests.post('http://127.0.0.1:8000/api/serAPI/TrackingAPI/', data = myobj)
#                     if r.status_code == 201:
#                         print ('Service Track Update Done')
#                     else:
#                         print ( 'User updated is on the Conditions')