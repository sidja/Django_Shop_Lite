

$('#pro_detail_add').on('submit', function(event){
    event.preventDefault();


    console.log("form submitted!")  // sanity check
   
    add_to_cart();



    
});

function add_to_cart() {
    console.log("create post is working!") // sanity check
    console.log($('#post-text').val())
     alert("Product has been added to cart2");




};





function remove_cart_item(itm) {

	
	var base_url = window.location.origin;
	var remove_link = base_url+"/remove_from_cart/"+itm; 

	
   
    $.ajax({
			  method: "GET",
			  url: remove_link,
			  success: function(data) {
  				
  				$('#cart_block').html(data);
  				
  				}
			})
			  .done(function( msg ) {
			   
  				
  			});

};




$('#update_cart_button').on('click', function(event){
    event.preventDefault();


    //console.log("form submitted!")  // sanity check

  

    var cart_items = [];

    $( "input[id*='cart_qty_item']" ).each(function(){

    	

			 var person = 	{
          					  	product_id: $(this).attr("productid"),
            					quantity:$(this).val()
        					}

        	 cart_items.push(person);

	});



	var base_url = window.location.origin;
	var update_link = base_url+"/update_cart/"; 
	var csrf_tk = $('#csrfmiddlewaretoken').val()

	//alert(update_link);

	 update_cart(update_link,csrf_tk,cart_items);

	
  
    
});


function update_cart(update_link,csrf_tk,cart_items){





	$.ajax({
			  method: "POST",
			  url: update_link,

			  data : 	{
			   				'csrfmiddlewaretoken' : csrftoken2 ,
			   				cart_itm : JSON.stringify(cart_items),
			   			},
			  success: function(data) {
  				
  				//$('#cart_block').html(data);
  				
  				
  				var cart_form_inner = $(data).find("#cart_form_inner")

  				var cart_total  = $(data).find("#cart_total")

  				$('#cart_total').html(cart_total);
  				$('#cart_form_inner').html(cart_form_inner);


  				  console.log($('#cart_form_inner').html(cart_form_inner));
  				 location.reload();

  				},

  				error : function(xhr,errmsg,err) {
          	  // $('#results').html("<div class='alert-box alert radius' data-alert>Oops! We have encountered an error: "+errmsg+
              //  " <a href='#' class='close'>&times;</a></div>"); // add the error to the dom

			// provide a bit more info about the error to the console
            console.log(xhr.status + ": " + xhr.responseText); 
        }
			});
			  
  		
}





$('#shipping_form_submit').on('click', function(event){
    event.preventDefault();

    var base_url = window.location.origin;
    var get_shipping_url = base_url+"/get_shipping/"


    $.ajax({
			  method: "POST",
			  url: get_shipping_url,

			  data : 	{
			   				'csrfmiddlewaretoken' : csrftoken2 ,
			   				shippin_to : $('#shipping_to_postcode').val(),
			   			},
			  success: function(data) {
  				
  				//$('#cart_block').html(data);

  				$('#shipping_estimate').html(data);
  				
  				
  				
  		
  				},

  				error : function(xhr,errmsg,err) {
          	  
            console.log(xhr.status + ": " + xhr.responseText); 
        }
			});
			  

});





// using jQuery
function getCookie(name) {
    var cookieValue = null;
    if (document.cookie && document.cookie != '') {
        var cookies = document.cookie.split(';');
        for (var i = 0; i < cookies.length; i++) {
            var cookie = jQuery.trim(cookies[i]);
            // Does this cookie string begin with the name we want?
            if (cookie.substring(0, name.length + 1) == (name + '=')) {
                cookieValue = decodeURIComponent(cookie.substring(name.length + 1));
                break;
            }
        }
    }
    return cookieValue;
}
var csrftoken2 = getCookie('csrftoken');


function csrfSafeMethod(method) {
    // these HTTP methods do not require CSRF protection
    return (/^(GET|HEAD|OPTIONS|TRACE)$/.test(method));
}
$.ajaxSetup({
    beforeSend: function(xhr, settings) {
        if (!csrfSafeMethod(settings.type) && !this.crossDomain) {
            xhr.setRequestHeader("X-CSRFToken", csrftoken2);
        }
    }
});



function isInt(value) {
  return !isNaN(value) && 
         parseInt(Number(value)) == value && 
         !isNaN(parseInt(value, 10));
}


