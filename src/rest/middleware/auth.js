// Import dependencies
const jwt = require('jsonwebtoken');

const auth = (request, response, next) => {
    const token = request.header('x-auth-token');

    if (!token) {
        return response.status(401).send({
            ok: false,
            error: 'Access denied. No token provided'
        });
    }

    try {
        const decoded = jwt.verify(token, 'jwtPrivateKey');
        response.user = decoded;
    } catch (error) {
        return response.status(401).send({
            ok: false,
            error: 'Token expired'
        });
    }

    next();
}

module.exports = auth;