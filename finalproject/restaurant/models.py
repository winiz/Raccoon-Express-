from django.db import models
from django.utils import timezone
from django.contrib.auth.models import User
from django.db.models.signals import post_save
from django.dispatch import receiver
from menu.models import menu

class Table (models.Model):
	Table = models.IntegerField(default=0)
	Code = models.CharField(max_length=20)

class Restaurant (models.Model):
    Name = models.CharField(max_length=100)
    Location = models.CharField(max_length=100)

class Order(models.Model):
    CREATED = 'CREATED'
    SENT_TO_KITCHEN = 'SENT TO KITCHEN'
    STARTED = 'STARTED'
    READY = 'READY'
    SERVED = 'SERVED'
    COMPLETED = 'COMPLETED'
    STATUS_CHOICES = (
        (CREATED, 'Order created'),
        (SENT_TO_KITCHEN, 'Order sent to kitchen'),
        (STARTED, 'Order started'),
        (READY, 'Order ready to be served'),
        (SERVED, 'Order served'),
        (COMPLETED, 'Order completed')
    )
    Code = models.CharField(max_length=20)
    Table = models.IntegerField(default=0)
    Restaurant = models.ForeignKey(Restaurant, default=1)
    Status= models.CharField(max_length=15, choices=STATUS_CHOICES, default=CREATED,)
    StartTime = models.DateTimeField(default=timezone.now)

class Alert(models.Model):
    Order = models.ForeignKey(Order)
    Message = models.CharField(max_length=500)
    Resolved = models.BooleanField(default=0)

class UserType(models.Model):
    user = models.OneToOneField(User,on_delete=models.CASCADE)
    is_customer = models.BooleanField(default=True)
    is_kitchen = models.BooleanField(default=False)
    is_server = models.BooleanField(default=False)
    restaurant = models.ForeignKey(Restaurant, blank=True, null=True)
    # Override the __unicode__() method to return something meaningful!
    def __unicode__(self):
        return self.user.username

@receiver(post_save, sender=User)
def create_usertype(sender,instance,created, **kwargs):
	if created:
		UserType.objects.create(user=instance)

@receiver(post_save, sender=User)
def save_usertype(sender,instance,created, **kwargs):
	if created:
		instance.usertype.save()

class OrderedMenuItems(models.Model):
	order_id = models.ForeignKey(Order)
	#table_id = models.ForeignKey(Order)
	item_name = models.ForeignKey(menu, null=True)
	num_items = models.IntegerField(default=0)
	notes = models.TextField(max_length=500, null=True)
	#def __str__(self):
		#return self.item_name
		#return self.item_name

class Payment(models.Model):
	pay_id = models.ForeignKey(Order)
	total = models.PositiveIntegerField(default=0)
	def __str__(self):
		return self.pay_id
