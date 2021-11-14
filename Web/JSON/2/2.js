var request = new XMLHttpRequest();
url = 'https://hplussport.com/api/wrong'
request.open('GET', url);

request.onload = function() {
	var response = request.response;
	console.log(response);
	var jsonData = JSON.parse(response);
	console.log(jsonData);
};
request.oneerror = function() {
	console.log("Error Here!");
}

request.send();