import requests
from pprint import pprint 
import json


def auspost_estimate(to_postcode= '2000'):
	aus_post_key 	= 'fcf4be35-368d-4b33-9ecf-24fceed12baf'

	# Header params
	headers 		= {'auth-key' : aus_post_key }

	# Postage calculator URL

	url 			= 'https://auspost.com.au//api/v3/postage/domestic/service.json'

	# with service code 'AUS_PARCEL_REGULAR'
	url2 			= 'https://auspost.com.au/api/postage/parcel/domestic/calculate.json'

	# Query params

	from_postcode	= '3004'
	
	length			= '20'
	width			= '20'
	height			= '20'
	weight			= '5'

	# only for url 2
	service_code	= 'AUS_PARCEL_REGULAR'


	payload ={
							'from_postcode':from_postcode,
							'to_postcode':to_postcode,
						
							'length':length,
							'width':width,
							'height':height,
							'weight':weight,
							'service_code' : service_code
						}


	# Request 

	r = requests.get(url2,headers=headers,params=payload)

	if r.status_code is 200:
		js =  json.loads(r.content)

		result = js["postage_result"]["total_cost"]
	else:
		result = False

	return result