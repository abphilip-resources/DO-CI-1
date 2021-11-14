var request = new XMLHttpRequest();					// Create Request
url = 'https://hplussport.com/api/wrong'			// URL
request.open('GET', url);							// Open Request

request.onload = function() {						// Request loaded
	var response = request.response;				// Get Response
	console.log(response);							// Log Response
	var jsonData = JSON.parse(response);			// Parse to JSON
	console.log(jsonData);							// Log JSON
};
request.oneerror = function() {						// If Error
	console.log("Error Here!");						// Log Error
}

request.send();										// Send Request