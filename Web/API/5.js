URL = 'https://api.giphy.com/v1/gifs/random'		// API URL
API = '?api_key=w6MeEQcX9y2Og8QCbhx4zvTg1K3qcJ6A'	// API Key
TAG = '&tag=cat&rating=g'							// API Parameters

var request = new XMLHttpRequest();					// Create Request
request.open('GET', URL+API+TAG);					// Send Request

request.onload = function() {						// Action once data received
	data = JSON.parse(request.response)				// Parse JSON
	console.log(data);								// Log Response
	org = data.data.images.original.url;			// Get Original URL
	console.log(org);								// Log Original URL

	gif = document.createElement('img');			// Create Image element
	gif.setAttribute('src', org);					// Set Element Content
	document.body.appendChild(gif);					// Append Element to Body
};

request.send();										// Send Request	