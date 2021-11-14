URL = 'https://hplussport.com/api/products?qty=2&order=name'
// '?' --> Parameters after this
// '&' --> Connecting two parameters

var request = new XMLHttpRequest();					    // Create Request
request.open('GET', URL);							    // Open Request 
request.onload = function() {						    // Action once data received
	data = JSON.parse(request.response)					// Parse JSON
	console.log(data);	        						// Log Response
	console.log(data[0].name);							// Access Data via console

	page = document.createElement('li');				// Create Element
	page.innerHTML = data[0].name;						// Set Element Content
	document.body.appendChild(page);					// Append Element to Body
};
request.send()                                          // Send Request     