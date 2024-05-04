// Import the express library
const express = require('express');

// Create an express application
const app = express();

// Define a port number
const PORT = 3000;

// Middleware to parse JSON bodies (this is required for POST requests)
app.use(express.json());

// Define a route for GET requests to the root URL ('/')
app.get('/', (req, res) => {
    res.send('Hello, this is my quiz app!');
});

// Start the server on the defined PORT
app.listen(PORT, () => {
    console.log(`Server is running on http://localhost:${PORT}`);
});
