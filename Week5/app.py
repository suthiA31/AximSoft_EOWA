from flask import (
    Flask,
    render_template
)

from config import Config

from extension import (
    db,
    login_manager,
    mail,
    migrate
)

from models import (
    User,
    Job
)


def create_app():

    app = Flask(__name__)

    app.config.from_object(Config)
    app.config["UPLOAD_FOLDER"] = "static/uploads/profile"
    #initialization Flask Extention
    db.init_app(app)
    login_manager.init_app(app)
    mail.init_app(app)
    migrate.init_app(app, db)

    login_manager.login_view = "auth.login"

    from auth.routes import auth_bp
    from jobs.routes import jobs_bp
    from candidate.routes import candidate_bp
    from employer.routes import employer_bp
    #Bluprints,every module has its own routes
    app.register_blueprint(auth_bp)
    app.register_blueprint(jobs_bp)
    app.register_blueprint(candidate_bp)
    app.register_blueprint(employer_bp)

    @app.route("/")
    def home():
         #latest  6 jobs
        jobs = Job.query.order_by(
            Job.id.desc()
        ).limit(6).all()

        return render_template(
            "index.html",
            jobs=jobs
        )

    return app

#Whenever a user logs in, Flask uses this function to retrieve the user from the database using their ID.
@login_manager.user_loader
def load_user(user_id):
    return User.query.get(int(user_id))


app = create_app()

if __name__ == "__main__":
    app.run(debug=True)