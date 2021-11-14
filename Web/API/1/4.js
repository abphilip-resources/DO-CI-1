URL = 'https://hplussport.com/api/products?qty=2&order=name'
// '?' --> Parameters after this
// '&' --> Connecting two parameters

var request = new XMLHttpRequest();					    // Create Request
request.open('GET', URL);							    // Open Request 
request.onload = function() {						    // Action once data received
	data = JSON.parse(request.response)					// Parse JSON
	console.log(data);	        						// Log Response
	console.log(data[0].name);							// Log first item's name

	for(z in data) {									// Loop through data
		text = document.createElement('li');			// Create List element
		text.innerHTML = data[z].name;					// Set Element Content
		document.body.appendChild(text);				// Append Element to Body

		img = document.createElement('img');			// Create Image element
		img.setAttribute('src', data[z].image);			// Set Element Content
		document.body.appendChild(img);					// Append Element to Body
	}
};
request.send()                                          // Send Request     