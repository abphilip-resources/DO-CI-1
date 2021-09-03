// Using ExpressJS
const express = require('express');
const path = require('path');
const app = express();

app.use(express.json());
app.use(express.urlencoded({ extended: false }));

// GET request to the root of the server
app.get('/',(req,res)=>{
    // Display host parameter of the HTTP request header
    res.send(req.header('host'));});
    
// Message to console if the result appears on port 5000
app.listen(5000,()=>console.log(`Server started on 5000`));