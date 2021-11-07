// Using ExpressJS
const express = require('express');
const path = require('path');
const app = express();

app.use(express.json());
app.use(express.urlencoded({ extended: false }));

// PUT request to ./post
app.put('/post/:id',(req,res)=>{
    // Get the ID from the URL and display with the body
    res.json({
        id: req.params.id,
        title: req.body.title
    });
});

// Message to console if the result appears on port 5000
app.listen(5000,()=>console.log(`Server started on 5000`));