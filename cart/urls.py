from django.conf.urls import url

from . import views
from views import ProductList, CategoriesList, ProductDetail, \
  CheckoutCustomerView, CheckoutBillingAddressView,           \
  CheckoutShippingAddressView, CheckoutPaymentMethodView,     \
  CheckoutPaymentPageView



urlpatterns = [


	url(r'^$', views.index, name='index'),
  #url(r'^$', ProductList.as_view(), name='product_list'),
 
  url(r'^products/$', ProductList.as_view(), name='product_list'),
  #url(r'^categories/$', CategoriesList.as_view(), name='category_list'),
   url(r'^products/(?P<slug>[-\w]+)/$', ProductDetail.as_view(), name='product_detail'),
   url(r'^add_to_cart/$', views.add_to_cart, name='add_to_cart'),
   
   url(r'^show_cart_icon/$', views.show_cart_icon, name='show_cart_icon'),
   url(r'^cart/$', views.get_cart, name='cart'),
	 url(r'^get_cart_block/$', views.get_cart_block, name='get_cart_block'),
   url(r'^remove_from_cart/(?P<product_id>[0-9]+)/$', views.remove_from_cart, name='remove_from_cart'),
   url(r'update_cart/$', views.update_cart_items, name='update_cart'),
   url(r'get_shipping/$', views.get_shipping, name='get_shipping'),
   
   url(r'^checkout/$',views.CheckoutCustomerFunc, name='checkout'),
  # url(r'^checkout/$',CheckoutCustomerView.as_view(), name='checkout'),
   url(r'^checkout/billing$',CheckoutBillingAddressView.as_view(), name='checkout_billing'),
   url(r'^checkout/shipping$',CheckoutShippingAddressView.as_view(), name='checkout_shipping'),
   url(r'^checkout/payment_method$',CheckoutPaymentMethodView.as_view(), name='checkout_payment_method'),
   url(r'^checkout/payment$',CheckoutPaymentPageView.as_view(), name='checkout_payment'),
   url(r'^checkout/thankyou$',views.thankyou, name='checkout_thankyou'),

   


   # Experiemental -- IGNORE 
   url(r'^crispy/$',views.crispy_test, name='crispy'),
    
    #url(r'^categories/$', CategoriesList.as_view(), name='category_list'),
    #url(r'^products/$', ProductList.as_view(), name='product_list'),
   # url(r'^products/(?P<slug>[-\w]+)/$', ProductDetail.as_view(), name='product_detail'),
   ## url(r'^test$', views.sesh_test, name='sesh_test'),
    #url(r'^add_to_cart/$', views.add_to_cart, name='add_to_cart_first'),
   # url(r'^add_to_cart/$', views.add_to_cart, name='add_to_cart'),
   	#url(r'^cart$', GetCartListView.as_view(), name='cart'),
	#url(r'^cart$', views.get_cart, name='cart'),
	#url(r'^remove_from_cart/(?P<product_id>[0-9]+)/$', views.remove_from_cart, name='remove_from_cart'),


]