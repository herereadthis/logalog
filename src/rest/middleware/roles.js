const admin = (request, res, next) => {
    if (!request.user.roles.includes("admin")) {
        return res.status(403).send({
        ok: false,
        error: "Access denied."
    });
}

    next();
};

const editor = (request, res, next) => {
    if (!request.user.roles.includes("editor")) {
        return res.status(403).send({
        ok: false,
        error: "Access denied."
    });
}

    next();
};

const viewer = (request, res, next) => {
    if (!request.user.roles.includes("viewer")) {
        return res.status(403).send({
        ok: false,
        error: "Access denied."
    });
}

    next();
};

module.exports = { admin, editor, viewer };