from flask import Flask
from config import Config
import os

def create_app():
    app = Flask(__name__)
    app.config.from_object(Config)

    os.makedirs(app.config["PROFILE_UPLOAD_FOLDER"], exist_ok=True)
    os.makedirs(app.config["COURSE_UPLOAD_FOLDER"], exist_ok=True)

    from app.main import main_bp
    from app.auth import auth_bp
    from app.courses import courses_bp
    from app.dashboard import dashboard_bp
    from app.profile import profile_bp
    from app.admin import admin_bp

    app.register_blueprint(main_bp)
    app.register_blueprint(auth_bp, url_prefix="/auth")
    app.register_blueprint(courses_bp, url_prefix="/courses")
    app.register_blueprint(dashboard_bp, url_prefix="/dashboard")
    app.register_blueprint(profile_bp, url_prefix="/profile")
    app.register_blueprint(admin_bp, url_prefix="/admin")

    return app