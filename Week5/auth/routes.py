from flask import (
    render_template,
    redirect,
    url_for,
    flash,
    session,
    request
)
from sqlalchemy.exc import IntegrityError
from werkzeug.security import (
    generate_password_hash,
    check_password_hash
)

from flask_login import (
    login_user,
    logout_user,
    login_required
)

from auth import auth_bp
from auth.forms import (
    RegisterForm,
    LoginForm
)

from extension import db
from models import User

from utils.otp import (
    generate_otp,
    verify_otp
)

from utils.email import send_email

#route registers a new user.
@auth_bp.route("/register", methods=["GET", "POST"])
def register():

    form = RegisterForm()

    if form.validate_on_submit():

        existing = User.query.filter_by(
            email=form.email.data
        ).first()

        if existing:
            flash("Email already exists", "danger")
            return redirect(url_for("auth.register"))

        otp = generate_otp()

        session["register_otp"] = otp

        session["register_data"] = {
            "name": form.name.data,
            "email": form.email.data,
            "password": generate_password_hash(
                form.password.data
            ),
            "role": form.role.data
        }

        send_email(
            subject="CareerHub Registration OTP",
            recipient=form.email.data,
            template="emails/otp_email.html",
            otp=otp
        )

        flash("OTP sent to your email.", "info")

        return redirect(
            url_for("auth.verify_register_otp")
        )

    return render_template(
        "register.html",
        form=form
    )


@auth_bp.route(
    "/verify-register-otp",
    methods=["GET", "POST"]
)
def verify_register_otp():

    if request.method == "POST":

        entered_otp = request.form.get("otp")

        if verify_otp(
            entered_otp,
            session.get("register_otp")
        ):

            data = session.get("register_data")

            existing = User.query.filter_by(
                email=data["email"]
            ).first()

            if existing:
                flash("Email already registered.", "danger")
                return redirect(url_for("auth.login"))

            user = User(
                name=data["name"],
                email=data["email"],
                password=data["password"],
                role=data["role"]
            )
            #prevents duplicate email entries if two registration requests happen simultaneously.
            try:
                db.session.add(user)
                db.session.commit()

            except IntegrityError:
                db.session.rollback()
                flash("Email already exists.", "danger")
                return redirect(url_for("auth.register"))
            send_email(
                subject="Welcome To CareerHub",
                recipient=user.email,
                template="emails/welcome.html",
                user=user
            )

            session.pop("register_otp", None)
            session.pop("register_data", None)

            flash("Registration Successful.", "success")

            return redirect(
                url_for("auth.login")
            )

        flash("Invalid OTP.", "danger")

    return render_template("verify_otp.html")


@auth_bp.route("/login", methods=["GET", "POST"])
def login():

    form = LoginForm()

    if form.validate_on_submit():

        user = User.query.filter_by(
            email=form.email.data
        ).first()

        if user and check_password_hash(
            user.password,
            form.password.data
        ):

            otp = generate_otp()

            session["login_otp"] = otp
            session["user_id"] = user.id

            send_email(
                subject="CareerHub Login OTP",
                recipient=user.email,
                template="emails/otp_email.html",
                otp=otp
            )

            flash("OTP sent to your email.", "info")

            return redirect(
                url_for("auth.verify_login_otp")
            )

        flash("Invalid Email or Password.", "danger")

    return render_template(
        "login.html",
        form=form
    )


@auth_bp.route(
    "/verify-login-otp",
    methods=["GET", "POST"]
)
def verify_login_otp():

    if request.method == "POST":

        entered_otp = request.form.get("otp")

        if verify_otp(
            entered_otp,
            session.get("login_otp")
        ):

            user = User.query.get(
                session.get("user_id")
            )

            login_user(user)

            send_email(
                subject="New Login Alert",
                recipient=user.email,
                template="emails/login_alert.html",
                user=user
            )

            session.pop("login_otp", None)
            session.pop("user_id", None)

            flash("Login Successful.", "success")

            if user.role == "employer":
                return redirect(
                    url_for("employer.dashboard")
                )

            return redirect(
                url_for("candidate.dashboard")
            )

        flash("Invalid OTP.", "danger")

    return render_template("verify_otp.html")


@auth_bp.route("/logout")
@login_required
def logout():

    logout_user()

    flash("Logged Out Successfully.", "info")

    return redirect(
        url_for("auth.login")
    )