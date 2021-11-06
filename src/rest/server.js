const express = require('express');

// Setup the express server
const app = express();
const port = 3001;

// Import middlewares
app.use(express.json());

// Routes
const authRouter = require('./routes/auth');
const messagesRouter = require('./routes/messages');

app.use('/api/messages', messagesRouter);
app.use('/api/auth', authRouter);

// Start the server
app.listen(port, () => {
  console.log(`Listening on port ${port}...`);
});