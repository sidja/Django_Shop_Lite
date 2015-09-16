from django.db import models

# Create your models here.
from django.db import models
from django.template.defaultfilters import slugify

from changuito.models import Item, Cart

# Django Tagitt
from taggit.managers import TaggableManager


# Create your models here.
class Categories(models.Model):

	id				= models.AutoField(primary_key=True, default=1)
	name 			= models.CharField(max_length=255)
	image 			= models. ImageField(upload_to='static/', blank=True, null=True)
	url				= models.URLField(max_length=1024, blank=True, null=True)


class Product(models.Model):

	id				= models.AutoField(primary_key=True)
	name 			= models.CharField(max_length=255)
	text			= models.CharField(max_length=255 , blank=True)
	image			= models.CharField(max_length=1024, blank=True)
	url				= models.URLField(max_length=1024, blank=True)
	unit_price		= models.IntegerField(default=0)
	stock			= models.IntegerField(default=0)
	slug 			= models.SlugField(unique=True,blank=True,)
	weight			= models.PositiveIntegerField(default=1)
	length 			= models.PositiveIntegerField(default=10)
	width			= models.PositiveIntegerField(default=10)
	height			= models.PositiveIntegerField(default=10)

	tags = TaggableManager()


	def save(self, *args, **kwargs):
		# converts name field into a slug by using slugify
		self.slug = slugify(self.name)
		super(Product, self).save(*args, **kwargs)

	def get_absolute_url(self):
		from django.core.urlresolvers import reverse
		return reverse("product_detail", kwargs={"slug": self.slug})

	def __str__(self):

			return ' '.join([
					self.name,
					
			])

	class Meta:
		managed = True

class Person(models.Model):

    first_name      = models.CharField(max_length=255, blank=False)
    last_name       = models.CharField(max_length=255, blank=False)
    email           = models.CharField(max_length=255, blank=False)

    def __str__(self):

        return ' '.join([
                self.first_name,
                self.last_name,
        ])
    class Meta:
    	abstract = True



class Address(models.Model):
    address1        = models.CharField(max_length=255, blank=False)
    address2        = models.CharField(max_length=255, blank=True)
    suburb          = models.CharField(max_length=255, blank=False)
    city            = models.CharField(max_length=255, blank=False)
    postcode        = models.CharField(max_length=255, blank=False)
    phone           = models.CharField(max_length=255, blank=False)

    class Meta:
    	abstract 	= True




class Customer(Person):


	def __str__(self):

		return ' '.join([
		        self.first_name,
		        self.last_name,
		])

	

	class Meta:
		verbose_name = 'customer'
        verbose_name_plural = 'customers'
         

class BillingAddress(Address,Person):

	customer		= models.ForeignKey(Customer)

	Person._meta.get_field('email').blank 			= True
	Person._meta.get_field('email').default 		= ""
	Person._meta.get_field('first_name').default	= ""
	Person._meta.get_field('last_name').default 	= ""

	class Meta:
		abstract 			= False
		verbose_name 		= 'BillingAddress'

class ShippingAddress(Address,Person):

	customer		= models.ForeignKey(Customer)
	
	Person._meta.get_field('email').blank = True

	business_name	= models.CharField(max_length=255, blank=True)

	class Meta:
		abstract			= False
		verbose_name 		= 'ShippingAddress'




class Orders(models.Model):

	
	customer_id			= models.ForeignKey(Customer)
	cart_id				= models.ForeignKey(Cart)
	submit_date 		= models.DateTimeField(auto_now=True)
	#customer_ip			= models.GenericIPAddressField()
	status				= models.CharField(max_length=255, blank=False,default='inactive')
	payment_proccessed	= models.BooleanField(blank=False,default=False,editable=True)
	total_amount		= models.PositiveIntegerField()
	weight				= models.PositiveIntegerField(null=True)

	class Meta:
		verbose_name = 'Order'
        verbose_name_plural = 'Orders'

class Store(Address):

	name 				= models.CharField(max_length=255, blank=True)
	abn					= models.PositiveIntegerField()
	

	def __str__(self):

		return ' '.join([
                self.name,
                
        ])