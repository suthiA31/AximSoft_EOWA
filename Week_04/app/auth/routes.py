from flask import (
    render_template,
    request,
    redirect,
    url_for,
    flash,
    session
)

from werkzeug.security import (
    generate_password_hash,
    check_password_hash
)

from app.auth import auth_bp
from app.models.database import get_db


@auth_bp.route("/register", methods=["GET", "POST"])
def register():

    if request.method == "POST":

        name = request.form["name"].strip()
        email = request.form["email"].strip()
        password = request.form["password"]

        # Validation
        if not name:
            flash("Name is required", "danger")
            return redirect(url_for("auth.register"))

        if not email:
            flash("Email is required", "danger")
            return redirect(url_for("auth.register"))

        if len(password) < 6:
            flash("Password must be at least 6 characters", "danger")
            return redirect(url_for("auth.register"))

        conn = get_db()

        # Check existing email
        existing_user = conn.execute(
            """
            SELECT *
            FROM users
            WHERE email = ?
            """,
            (email,)
        ).fetchone()

        if existing_user:
            flash("Email already exists", "warning")
            conn.close()
            return redirect(url_for("auth.register"))

        # HASH PASSWORD
        hashed_password = generate_password_hash(password)

        # Insert user
        conn.execute(
            """
            INSERT INTO users (
                name,
                email,
                password
            )
            VALUES (?, ?, ?)
            """,
            (
                name,
                email,
                hashed_password
            )
        )

        conn.commit()
        conn.close()

        flash("Registration successful. Please login.", "success")
        return redirect(url_for("auth.login"))

    return render_template("auth/register.html")


@auth_bp.route("/login", methods=["GET", "POST"])
def login():

    if request.method == "POST":

        email = request.form["email"].strip()
        password = request.form["password"]

        conn = get_db()

        user = conn.execute(
            """
            SELECT *
            FROM users
            WHERE email = ?
            """,
            (email,)
        ).fetchone()

        conn.close()

        if user and check_password_hash(user["password"], password):

            session.clear()
            session["user_id"] = user["user_id"]
            session["user_name"] = user["name"]
            session["user_email"] = user["email"]
            session["profile_image"] = user["profile_image"]

            # role will work after we add role column
            session["role"] = user["role"] if "role" in user.keys() else "student"

            flash("Login successful", "success")
            return redirect(url_for("main.home"))

        flash("Invalid email or password", "danger")

    return render_template("auth/login.html")

#LOGOUT
@auth_bp.route("/logout")
def logout():
    session.clear()
    flash("Logged out successfully", "info")
    return redirect(url_for("main.home"))