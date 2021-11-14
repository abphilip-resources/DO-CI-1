// Using ExpressJS
const express = require('express');
const path = require('path');
const app = express();

app.use(express.json());
app.use(express.urlencoded({ extended: false }));

// POST request to ./contact
app.post('/contact',(req,res)=>{
    // If no value, send alert and stop execution with status code 400
    if(!req.body.name) {
        return res.status(400).send('Name is required');
    }
    // If value, send message with status code 201
    res.status(201).send(`Thank You ${req.body.name}`);
});

// POST request to ./login
app.post('/login',(req,res)=>{
    // If no value, send alert and stop execution with status code 400
    if(!req.header('x-auth-token')) {
        return res.status(400).send('No Token');
    }
    // If wrong value, send alert and stop execution with status code 401
    if(req.header('x-auth-token')!=='12345') {
        return res.status(401).send('Not Authorized');
    }
    // If correct value, send confirmation message
    res.send(`Authorized`);
});

// Message to console if the result appears on port 5000
app.listen(5000,()=>console.log(`Server started on 5000`));