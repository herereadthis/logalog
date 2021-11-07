// Import dependencies
const jwt = require('jsonwebtoken');
const express = require('express');
const bcrypt = require('bcrypt');

// Dummy data
const users = [
    {
        email: 'foo@bar.com', 
        password: '$2b$15$zqY2Q4eOoGzFpZkHJz9HS.BSfXc/HM2E/yTWa1awFmTMgN2bE72Uu', 
        roles: ['admin', 'editor', 'viewer']
    }
];

// setup the express server router
const router = express.Router();

// On post
router.post('/', async (request, response) => {
    // Find the user
    const user = users.find(u => u.email === request.body.email);
    if (!user) {
        throw new Error('Invalid email or password.')
    };

    // Compare passwords
    const valid = await bcrypt.compare(request.body.password, user.password);
    if (!valid) {
        throw new Error('Invalid email or password.');
    }

    const token = jwt.sign({
        id: user._id,
        roles: user.roles,
    }, 'jwtPrivateKey', { expiresIn: '60m' });

    response.send({
        token
    });
});

// Export the router
module.exports = router;