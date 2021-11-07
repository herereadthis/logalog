// Import dependencies
const express = require('express');

// Import middlewares
const auth = require('../middleware/auth');
const roles = require('../middleware/roles');

// Dummy data
let messages = [
    {
        id: 1, 
        name: 'Lorem ipsum dolor', 
        content: 'Lorem ipsum dolor sit amet, consectetur adipiscing elit. Cras pretium nec ipsum nec elementum.'
    }
];

// Setup the router for express
const router = express.Router();

// route handlers

router.get('/', [auth, roles.viewer], (request, response) => {
    response.send({
        result: messages
    });
});

router.post('/', [auth, roles.editor], async (request, response) => {
    const {
        name,
        content
    } = request.body;
    // Make a new message and add it
    messages.push({
        id: messages.length + 1, 
        name,
        content
    });

    // Send response
    response.status(200).send({
        result: messages
    });
});

/** @todo not implemented */
// router.put('/', [auth, roles.editor], async (request, response) => {
//     response.status(200).send({
//         result: messages
//     });
// });

router.delete('/', [auth, roles.admin], async (request, response) => {
    // Delete the message
    messages = messages.filter((message) => {message.id !== request.body.id});

    response.status(200).send({
        result: messages
    });
});

// Export the router
module.exports = router;