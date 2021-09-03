// Using ExpressJS
const express = require('express');
const path = require('path');
const app = express();

app.use(express.json());
app.use(express.urlencoded({ extended: false }));

app.delete('/check/:id',(req,res)=>{
    res.json({
        msg:`${req.params.id} deleted`
    });
});

// Message to console if the result appears on port 5000
app.listen(5000,()=>console.log(`Server started on 5000`));