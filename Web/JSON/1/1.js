// No. 1 --> Single output to Console
var me = {                                          // Create Object me
    name: "Allen",                                  // String property
    age: 20,                                        // Number property
    address: {                                      // Object property
        city: "Bangalore",
        country: "India"
    },
    Schools:["BBHS","DPS"]                          // Array property
};
console.log(me.address.city)                        // Output: Bangalore

// No. 2 --> Multiple outputs to Console
var output='';
var people = [                                      // Create Array people
    {
        name: "Allen",
        age: 20         
    },
    {
        name: "Ben",
        age: 50          
    },
    {
        name: "Philipose",
        age: 90         
    }
];
for(var z=0; z<people.length; z++){
    console.log(people[z].age);                     // Output: 20, 50, 90
    output+='<li>'+people[z].name+'</li>';          // Display on page
}
document.getElementById('people').innerHTML = output;
me = JSON.stringify(me);                            // Convert to JSON
me = JSON.parse(me);                                // Convert to Object

// No. 3 --> AJAX with JSON
var x = new XMLHttpRequest();                   
x.onreadystatechange = function() {
    if (this.readyState == 4 && this.status == 200) {  
        var r = JSON.parse(x.responseText);
        var crowd = r.crowd;

        var output = '';
        for(var z=0; z<crowd.length; z++){
            console.log(crowd[z].age);              // Output: 90, 50, 20
            output+='<li>'+crowd[z].name+'</li>';   // Display on page
        }
        document.getElementById("crowd").innerHTML = output;         
    }
};
x.open("GET","1.json",true);                        // GET Request to 1.json
x.send();                                           // Send Request

// Data types in JSON --> Boolean, Array, String, Object, Number, NULL