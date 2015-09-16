from django.shortcuts import render

# Create your views here.

from django.shortcuts import render
#Basic 
from datetime import datetime
from django.http import HttpResponse
# Views
from django.views.generic import  ListView , DetailView # View,TemplateView,
from django.shortcuts import render_to_response

#Response
from django.http import HttpResponseRedirect
from django.core.urlresolvers import reverse_lazy, reverse

from models import Categories, Product

from changuito.models import Item
from changuito.proxy import CartProxy


from changuito.proxy import CartProxy

#Forms
from django.views.generic.edit import FormView
from forms import CheckoutForm, CheckoutFormCustomerName, CheckoutFormBilling,\
 CheckoutFormShipping, ChekoutPaymentMethodForm,CheckoutCCForm
from crispy_forms_test import MessageForm
# Context
from django.template import RequestContext

from django.shortcuts import get_object_or_404
import json 

#CSRF manually update
from django.template.context_processors import csrf

# Shipping

from cart.utility import auspost_estimate

def index(request):
	return render_to_response('cart/test.html',)



class ProductList(ListView):
		model = Product
		
		
		def get_context_data(self, **kwargs):

			context = super(ProductList, self).get_context_data(**kwargs)
			context['cart'] = CartProxy(self.request)
			return context
			


class CategoriesList(ListView):
		model = Categories


class CategoryProductList(ListView):
		pass

class ProductDetail(DetailView):
		model = Product
		slug_field ='slug'

		def get_context_data(self, **kwargs):
			
			context = super(ProductDetail, self).get_context_data(**kwargs)
			context['cart'] = CartProxy(self.request)
			return context

def add_to_cart(request):
	if request.method =='POST':
		
		quantity 		= request.POST.get('quantity', False)
		product_id 		= request.POST.get('product_id', False)

		
		product = get_object_or_404(Product, id=product_id)
		cart = request.cart 
		cart.add(product, product.unit_price, int(quantity))
		#print Product.objects.filter(id=product_id).get_absolute_url()
		print
		print product.get_absolute_url()
		print
		#return HttpResponseRedirect(reverse('show_cart_icon'))
		return HttpResponseRedirect(product.get_absolute_url())
		#return render_to_response('shop/cart.html', request=request)

def update_cart_items(request):
	if request.method =='POST':
		
		
				
		# Get JS array in JSON string format
		cart_items = request.POST.getlist('cart_itm')
		
		print request.POST.getlist('csrfmiddlewaretoken')

		# 'cart_items' object has JSON values in unicode 
		#  below line converts cleans this up into a string
		clean_cart_items_string = json.dumps(json.JSONDecoder().decode(cart_items[0].encode('utf8')))
		
		# Converts string into JSON list/dictionary 
		cart_item_data = json.loads(clean_cart_items_string)
		
		
		#cart_items_list = [(item['quantity'],item['product_id'])for item in cart_item_data]
		
		print [(item['quantity'],item['product_id'])for item in cart_item_data]
		
		cart = request.cart

		# 	Traverses through JSON list to 
		#  	into a list with quantity and product_id from dictionary  

		for item in cart_item_data:
			product = get_object_or_404(Product, id=item['product_id'])
			cart.update(product, int(item['quantity']))
			
		# Updates cart 
		#for items in cart_items_list:

		
	return HttpResponseRedirect(reverse('get_cart_block'))


def show_cart_icon(request):
	return render_to_response('cart/cart_icon.html', dict(cart=CartProxy(request)),context_instance=RequestContext(request))



def get_cart(request):
    return render_to_response('cart/cart.html', dict(cart=CartProxy(request)),context_instance=RequestContext(request))


def remove_from_cart(request, product_id):
	cart = request.cart 
	cart.remove_item(product_id)

	return HttpResponseRedirect(reverse('get_cart_block'))

def get_cart_block(request):
	return render_to_response('cart/cart_block.html', dict(cart=CartProxy(request)))


def checkout(request):

	form = CheckoutFormCustomerName()


	return render_to_response('cart/checkout.html',{'form':form}, RequestContext(request))

def crispy_test(request):
    # This view is missing all form handling logic for simplicity of the example
    return render(request, 'cart/crispy_test.html', {'form': MessageForm()})


### Testing out forms here

def CheckoutCustomerFunc(request):
	 
	context = RequestContext(request)
		
	if request.method == 'POST':
		form = CheckoutFormCustomerName(request.POST, request.FILES)
		if form.is_valid(): # is the form valid?
			#form.save(commit=True) # yes? save to database
			return reverse_lazy('checkout_billing')
		else:
			print form.errors # no? display errors to end user
	else:
		form = CheckoutFormCustomerName()
	return render_to_response('cart/checkout.html', {'form': form}, context)



def get_shipping(request):
	if request.method == 'POST':
		shippin_to 		= request.POST.get('shippin_to', False)
		
		#print "shipping to "+str(shippin_to)

		shipping_result = auspost_estimate(shippin_to)

		#print shipping_result

		if shipping_result :
			estimate = '<b> Estimated Shipping : <i class="fa fa-usd">{}</b>'.format(shipping_result)	
		else:
			estimate = "<b> Please enter a valid postcode</b>"

	return HttpResponse(estimate) 




class CheckoutCustomerView(FormView):
	template_name = 'cart/checkout.html'
	form_class = CheckoutFormCustomerName

	success_url = reverse_lazy('checkout_billing')

	def form_valid(self, form):
		return super(CheckoutCustomerView, self).form_valid(form)

	#def get_form_kwargs(self):
	#	kwargs = super(CheckoutCustomerView, self).get_form_kwargs()
	#	kwargs['request'] = RequestContext(self.request)
	#	return kwargs


class CheckoutBillingAddressView(FormView):
	template_name = 'cart/checkout.html'
	form_class = CheckoutFormBilling

	success_url = reverse_lazy('checkout_shipping')

	#def get_form_kwargs(self):
	#    kwargs = super(CheckoutBillingAddressView, self).get_form_kwargs()
	#    kwargs['request'] = RequestContext(self.request)
	#    return kwargs


class CheckoutShippingAddressView(FormView):
	template_name = 'cart/checkout.html'
	form_class = CheckoutFormShipping

	success_url = reverse_lazy('checkout_payment_method')

	

class CheckoutPaymentMethodView(FormView):
	template_name = 'cart/checkout.html'
	form_class = ChekoutPaymentMethodForm

	success_url = reverse_lazy('checkout_payment')

	


class CheckoutPaymentPageView(FormView):
	template_name = 'cart/checkout.html'
	form_class = CheckoutCCForm

	success_url = reverse_lazy('checkout_thankyou')

	

def thankyou(request):
	 return render(request, 'cart/thankyou.html', {'form': MessageForm()})