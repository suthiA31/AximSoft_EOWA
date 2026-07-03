import os

BASE_DIR = os.path.abspath(os.path.dirname(__file__))

class Config:
    SECRET_KEY = os.environ.get("SECRET_KEY", "learnhub-secret-key")

    DATABASE = os.path.join(
        BASE_DIR,
        "instance",
        "database.db"
    )

    PROFILE_UPLOAD_FOLDER = os.path.join(
        BASE_DIR,
        "app",
        "static",
        "uploads",
        "profiles"
    )

    COURSE_UPLOAD_FOLDER = os.path.join(
        BASE_DIR,
        "app",
        "static",
        "uploads",
        "courses"
    )