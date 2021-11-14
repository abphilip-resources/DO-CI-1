var request = new XMLHttpRequest();
url = 'https://hplussport.com/api/products'
request.open('GET', url);

request.onload = function() {
	var response = request.response;
	console.log(typeof response);
	var jsonData = JSON.parse(response);
	console.log(typeof jsonData);
};
request.oneerror = function() {
	console.log("Error Here!");
}

request.send();

var car = {
	make: "Honda",
	model: "City",
	year: 2014,
	honk: function() { 
		alert("Beep beep"); 
	},
	driver: { 
		name: "Allen", 
		license: "TN" 
	}
 };
 console.log(car.make);
 console.log(car.driver.name);