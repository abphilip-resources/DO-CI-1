// No. 1
var sad = {
    name: "Allen",
    age: 20,     
    address: {
        city: "Bangalore",
        country: "India"
    },
    Schools:["BBHS","DPS"]      
};
console.log(sad.address.city)

// No. 2
var output='';
var people = [
    {
        name: "Allen",
        age: 20         
    },
    {
        name: "Is",
        age: 1          
    },
    {
        name: "Sad",
        age: 2         
    }
];
for(var z=0; z<people.length; z++){
    console.log(people[z].age);
    output+='<li>'+people[z].name+'</li>';
}
document.getElementById('people').innerHTML = output;
sad = JSON.stringify(sad);
sad = JSON.parse(sad);

// No. 3
var x = new XMLHttpRequest();
x.onreadystatechange = function() {
    if (x.readyState == 4 && x.status == 200) {
        console.log(x.responseText);
    }
    x.open("GET","1.json",true);
    x.send();
}