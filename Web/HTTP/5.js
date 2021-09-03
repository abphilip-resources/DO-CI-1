// Using ExpressJS
const express = require('express');
const path = require('path');
const app = express();

app.use(express.json());
app.use(express.urlencoded({ extended: false }));

// Launching a static webpage from folder 'sample' in the current directory
app.use(express.static('sample'));

// Message to console if the result appears on port 5000
app.listen(5000,()=>console.log(`Server started on 5000`));