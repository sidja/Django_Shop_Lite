from django import forms

from crispy_forms.helper import FormHelper
from crispy_forms.layout import Layout, Div, Submit, HTML, Button, Row, Field
from crispy_forms.bootstrap import AppendedText, PrependedText, FormActions

#validation
from django.core.exceptions import ValidationError




class CheckoutForm(forms.Form):

	first_name 				= forms.CharField(max_length=100)
	last_name				= forms.CharField(max_length=100)
	email					= forms.EmailField()
	
	billing_address1		= forms.CharField(label='Address', max_length=100, required=True)
	billing_address2		= forms.CharField(label='', max_length=100, required=False)
	billing_suburb			= forms.CharField(label='Suburb', max_length=100, required=True)
	billing_state			= forms.CharField(label='State', max_length=100, required=True)
	billing_postcode		= forms.CharField(label='Postcode', max_length=100, required=True)
	billing_phone			= forms.CharField(label='Phone', max_length=100, required=True)


	shipping_address1		= forms.CharField(label='Address', max_length=100, required=True)
	shipping_address2		= forms.CharField(label='', max_length=100, required=False)
	shipping_suburb			= forms.CharField(label='Suburb', max_length=100, required=True)
	shipping_state			= forms.CharField(label='State', max_length=100, required=True)
	shipping_postcode		= forms.CharField(label='Postcode', max_length=100, required=True)
	shipping_phone			= forms.CharField(label='Phone', max_length=100, required=True)


	helper 					= FormHelper()
	helper.form_class 		= 'form-horizontal'
	helper.form_action 		= 'checkout_thankyou'
	
	helper.layout 			= Layout(

		Field('first_name', 		css_class='input-xlarge, form-control'),
		Field('last_name',			css_class='input-xlarge, form-control'),
		Field('email',				css_class='input-xlarge, form-control'),
		Field('billing_address1',	css_class='input-xlarge, form-control'),
		
		Field('billing_suburb',		css_class='input-xlarge, form-control'),
		Field('billing_state',		css_class='input-xlarge, form-control'),
		Field('billing_postcode',	css_class='input-xlarge, form-control'),
		Field('billing_phone',		css_class='input-xlarge, form-control'),
		

		FormActions(
		   
		    Submit('save_changes', 'Save Details', 	css_class="btn-primary checkout_form_name_btn"),
		    Submit('cancel', 'Cancel', 				css_class="checkout_form_name_btn"),
		
		)

    	)


class CheckoutFormCustomerName(forms.Form):

	def validate_even(value):
		if value % 2 != 0:
			raise ValidationError('%s is not an even number' % value)

	first_name 				= forms.CharField(max_length=100)
	last_name				= forms.CharField(max_length=100, validators=[validate_even])
	email					= forms.EmailField()

	helper 					= FormHelper()
	helper.form_class 		= 'form-horizontal'
	helper.form_action 		= 'checkout_billing'
	helper.layout 			= Layout(

			HTML("""

            		<p> Please enter your details <strong></strong></p>
        
        		"""),


			Field('first_name', 	css_class='input-xlarge, form-control', required=True),
			
			Field('last_name',		css_class='input-xlarge, form-control', required=True),
			Field('email',			css_class='input-xlarge, form-control', required=True),

			FormActions(
		    
		    Submit('save_changes', 'Save Details', 	css_class="btn-primary checkout_form_name_btn"),
		    Submit('cancel', 'Cancel', 				css_class="checkout_form_name_btn"),
		)

		)




class CheckoutFormBilling(forms.Form):
	
	billing_address1		= forms.CharField(label='Address', max_length=100, required=True)
	billing_address2		= forms.CharField(label='', max_length=100, required=False)
	billing_suburb			= forms.CharField(label='Suburb', max_length=100, required=True)
	billing_state			= forms.CharField(label='State', max_length=100, required=True)
	billing_postcode		= forms.CharField(label='Postcode', max_length=100, required=True)
	billing_phone			= forms.CharField(label='Phone', max_length=100, required=True)

	helper 					= FormHelper()
	helper.form_class 		= 'form-horizontal'
	helper.form_action 		= 'checkout_shipping'
	helper.form_show_errors = False


	helper.layout = Layout(

			HTML("""
            	
            		<p> <strong>Billing Address</strong></p>
       		 
       		 	"""),
			
			Field('billing_address1', 	css_class='input-xlarge, form-control', required=True, ),
			Field('billing_suburb',		css_class='input-xlarge, form-control', required=True),
			Field('billing_state',		css_class='input-xlarge, form-control', required=True),
			Field('billing_postcode',	css_class='input-xlarge, form-control'),
			Field('billing_phone',		css_class='input-xlarge, form-control', oninvalid="this.setCustomValidity('Please Enter phone number')", required=True),

			FormActions(
		    Submit('save_changes', 'Save Details', css_class="btn-primary checkout_form_name_btn"),
		    Submit('cancel', 'Cancel', css_class="checkout_form_name_btn"),
		)

		)

class CheckoutFormShipping(forms.Form):

	shipping_first_name 	= forms.CharField(label='First Name', max_length=100)
	shipping_last_name		= forms.CharField(label='Last Name', max_length=100)
	shipping_email			= forms.EmailField()
	shipping_address1		= forms.CharField(label='Address', max_length=100, required=True)
	shipping_address2		= forms.CharField(label='', max_length=100, required=False)
	shipping_suburb			= forms.CharField(label='Suburb', max_length=100, required=True)
	shipping_state			= forms.CharField(label='State', max_length=100, required=True)
	shipping_postcode		= forms.CharField(label='Postcode', max_length=100, required=True)
	shipping_phone			= forms.CharField(label='Phone', max_length=100, required=True)

	helper 					= FormHelper()
	helper.form_class 		= 'form-horizontal'
	helper.form_action	 	= 'checkout_payment_method'
	helper.form_show_errors = False


	helper.layout 			= Layout(

			HTML("""

            		<p> <strong>Shipping Address</strong></p>

       			 """),


			Field('shipping_address1', 	css_class='input-xlarge, form-control'),
			Field('shipping_suburb',	css_class='input-xlarge, form-control'),
			Field('shipping_state',		css_class='input-xlarge, form-control'),
			Field('shipping_postcode',	css_class='input-xlarge, form-control'),
			Field('shipping_phone',		css_class='input-xlarge, form-control', help_text="Phone goes here"),

			FormActions(

		    Submit('save_changes', 'Save Details', 	css_class="btn-primary checkout_form_name_btn"),
		    Submit('cancel', 'Cancel', 				css_class="checkout_form_name_btn"),
			
					)

		)

class ChekoutPaymentMethodForm(forms.Form):

	CHOICES=[
				('select1','select 1'),
        		('select2','select 2')
        	]

	payment_method	= forms.ChoiceField(

							choices=CHOICES, 
							widget=forms.RadioSelect()
					)

	
	helper 					= FormHelper()
	helper.form_class 		= 'form-horizontal'
	helper.form_action 		= 'checkout_payment'
	helper.form_show_errors = False


	helper.layout 			= Layout(

			HTML("""

            		<p> <strong>Payment Method</strong></p>

       			 """),


			Field('payment_method', 	css_class='input-xlarge'),
			

			FormActions(

		    	Submit('save_changes', 'Save Details', 	css_class="btn-primary checkout_form_name_btn"),
		    	Submit('cancel', 'Cancel', 				css_class="checkout_form_name_btn"),
			
			)

		)

class CheckoutCCForm(forms.Form):
	card_name				= forms.CharField(label='Full Name', max_length=100, required=True)
	card_number				= forms.CharField(max_length=16, required=True)
	card_expiry_date		= forms.DateField(label='Expiry Date', input_formats=['%m%y'], required=True)
	cvv						= forms.CharField(label='CVV', max_length=3, required=True)

	helper 					= FormHelper()
	helper.form_class 		= 'form-horizontal'
	helper.form_action 		= 'checkout_thankyou'
	helper.form_show_errors = False


	helper.layout = Layout(

			HTML("""

            		<p> <strong>Make Payment</strong></p>

       		 	"""),

			Field('card_name', 			css_class='input-xlarge, form-control'),
			Field('card_number', 		css_class='input-xlarge, form-control'),
			Field('card_expiry_date', 	css_class='input-xlarge, form-control'),
			Field('cvv', 				css_class='input-xlarge, form-control'),

			FormActions(

		    Submit('save_changes', 'Save Details', 	css_class="btn-primary checkout_form_name_btn"),
		    Submit('cancel', 'Cancel', 				css_class="checkout_form_name_btn"),
		)

		)