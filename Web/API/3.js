URL = 'https://hplussport.com/api/products'			

// No. 1 --> XML Request
var request = new XMLHttpRequest();					    // Create Request
request.open('GET', URL);							    // Open Request 
request.onload = function() {						    // Action once data received
	console.log(JSON.parse(request.response));	        // Parse JSON and Log Response
};
request.send();                                         // Send Request              

// No. 2 --> jQuery & AJAX Request 
$.ajax ({                                               // Asynchronous JS And XML
	url: URL,                                                         
	success: function(response) {                       // Action once data received
		console.log(response)                           // Log Response
	}
})

// No. 3 --> Fetch Method Request
fetch(URL)                                              // Fetch and execute serially
.then(function(response) { return response.json(); })   // Return parsed JSON
.then(function(respData) { console.log(respData);  })   // Log Response