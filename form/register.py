from flask import Blueprint

register_blueprint = Blueprint('register', __name__)

@register_blueprint.route("/register")
def register():
    return "Register Page"
