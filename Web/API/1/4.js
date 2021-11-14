URL = 'https://hplussport.com/api/products?qty=2&order=name'
// '?' --> Parameters after this
// '&' --> Connecting two parameters

var request = new XMLHttpRequest();					    // Create Request
request.open('GET', URL);							    // Open Request 
request.onload = function() {						    // Action once data received
	data = JSON.parse(request.response)					// Parse JSON
	console.log(data);	        						// Log Response
	
};
request.send()                                          // Send Request     