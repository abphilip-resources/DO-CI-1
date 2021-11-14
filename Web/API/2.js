URL = 'https://hplussport.com/api/wrong'			

var request = new XMLHttpRequest();					// Create Request
request.open('GET', URL);							// Open Request

request.onload = function() {						// Action once data received
	var response = request.response;				// Get Response
	console.log(response);							// Log Response
	var jsonData = JSON.parse(response);			// Parse to JSON
	console.log(jsonData);							// Log JSON
};

request.onerror = function() {						// If Error
	console.log("Error Here!");						// Log Error
};

request.send();										// Send Request