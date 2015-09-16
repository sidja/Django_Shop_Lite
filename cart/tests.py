from django.test import TestCase

from django.test import Client
from cart.models import Product





class CartTest(TestCase):
	
	def setUp(self):
		#Add product to cart
		Product.objects.create(id='1',name='Unicorn Machine',text='Great stuff',image='',url='',unit_price='2000',stock='12',slug='')


	def test_add_item(self):
		c = Client() 
		c.get('/products/',  follow=True)
		# add product to cart
		response = c.post('/add_to_cart/', {'quantity': '1', 'product_id':'1'}, follow=True)
		
		self.assertEqual(response.status_code, 200)
		
		self.assertIn(b'Cart', response.content)

	def test_remove_item(self):
		c = Client() 
	
		# add product to cart
		response = c.post('/add_to_cart/', {'quantity': '1', 'product_id':'1'}, follow=True)

		# remove product from cart
		remove_item_response = c.get('/remove_from_cart/1', follow=True)	

		self.assertEqual(remove_item_response.status_code, 200)
		

class ProductsTest(TestCase):
	""" Author Test """

	def test_form(self):
		c = Client() 
		response = c.get('/products/',  follow=True)
		
		self.assertEqual(response.status_code, 200)
		self.assertIn(b'Products', response.content)
