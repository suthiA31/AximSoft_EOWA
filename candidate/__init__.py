from flask import Blueprint

candidate_bp = Blueprint(
    "candidate",
    __name__,
    url_prefix="/candidate"
)