from django.contrib import admin

# https://docs.djangoproject.com/en/1.8/ref/contrib/admin/#customizing-the-adminsite-class
from django.contrib.admin import AdminSite


# Register your models here.
from cart.models import Product
from cart.models import Customer
from cart.models import Orders
from cart.models import Store
from cart.models import BillingAddress
from cart.models import ShippingAddress








class ProductAdmin(admin.ModelAdmin):
	pass

admin.site.register(Product,ProductAdmin)



class StoreAdmin(admin.ModelAdmin):
	pass
admin.site.register(Store,StoreAdmin)


class OrdersAdmin(admin.ModelAdmin):
	pass
admin.site.register(Orders,OrdersAdmin)



class BillingAddressInline(admin.StackedInline):
	model = BillingAddress
	max_num=1


class ShippingAddressInline(admin.StackedInline):
	model = ShippingAddress
	max_num=1

class CustomerAdmin(admin.ModelAdmin):
	inlines = [
        BillingAddressInline,
        ShippingAddressInline,
    ]
admin.site.register(Customer,CustomerAdmin)




class MyAdminSite(AdminSite):
	site_header = 'Django Cart Lite Admin'
	index_title = 'UP here'
	index_template="cart/templates/admin/cart/index.html"

admin_site = MyAdminSite(name='myadmin')
admin_site.register(Product,ProductAdmin)
admin_site.register(Orders,OrdersAdmin)
admin_site.register(Customer,CustomerAdmin)
admin_site.register(Store,StoreAdmin)
