const admin = (request, response, next) => {
    if (!request.user.roles.includes("admin")) {
        return response.status(403).send({
            error: "Access denied."
        });
    }

    next();
};

const editor = (request, response, next) => {
    if (!request.user.roles.includes("editor")) {
        return response.status(403).send({
            error: "Access denied."
        });
    }

    next();
};

const viewer = (request, response, next) => {
    if (!request.user.roles.includes("viewer")) {
        return response.status(403).send({
            error: "Access denied."
        });
    }

    next();
};

module.exports = {
    admin,
    editor,
    viewer
};