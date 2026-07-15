from flask import Blueprint

employer_bp = Blueprint(
    "employer",
    __name__,
    url_prefix="/employer"
)