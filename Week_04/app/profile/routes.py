from flask import (
    render_template,
    request,
    redirect,
    url_for,
    flash,
    session,

)

import os

from werkzeug.utils import secure_filename

from app.profile import profile_bp
from app.models.database import get_db


@profile_bp.route("/", methods=["GET", "POST"])
def profile():


    # LOGIN CHECK

    if "user_id" not in session:
        flash("Please login first")
        return redirect(url_for("auth.login"))

    conn = get_db()


    # UPDATE PROFILE (POST)

    if request.method == "POST":

        name = request.form["name"]
        email = request.form["email"]

        image = request.files.get("profile_image")

        filename = None


        # HANDLE IMAGE UPLOAD

        if image and image.filename:
            upload_folder = os.path.join(
                os.path.dirname(os.path.dirname(__file__)),
                "static",
                "uploads",
                "profiles"
            )

            os.makedirs(upload_folder, exist_ok=True)

            filename = secure_filename(image.filename)

            image_path = os.path.join(
                upload_folder,
                filename
            )

            image.save(image_path)

        # UPDATE USER INFO

        conn.execute(
            """
            UPDATE users
            SET name = ?, email = ?
            WHERE user_id = ?
            """,
            (name, email, session["user_id"])
        )

        # UPDATE PROFILE IMAGE (IF EXISTS)

        if filename:

            conn.execute(
                """
                UPDATE users
                SET profile_image = ?
                WHERE user_id = ?
                """,
                (filename, session["user_id"])
            )

            session["profile_image"] = filename

        conn.commit()


        # UPDATE SESSION

        session["user_name"] = name
        session["user_email"] = email

        conn.close()

        flash("Profile Updated Successfully!")

        return redirect(url_for("profile.profile"))



    user = conn.execute(
        """
        SELECT *
        FROM users
        WHERE user_id = ?
        """,
        (session["user_id"],)
    ).fetchone()


    # TOTAL ENROLLMENTS

    total_courses = conn.execute(
        """
        SELECT COUNT(*)
        FROM enrollments
        WHERE user_id = ?
        """,
        (session["user_id"],)
    ).fetchone()[0]


    # COMPLETED COURSES

    completed_courses = conn.execute(
        """
        SELECT COUNT(*)
        FROM enrollments
        WHERE user_id = ?
        AND progress_percentage = 100
        """,
        (session["user_id"],)
    ).fetchone()[0]

    conn.close()


    # RENDER PAGE

    return render_template(
        "profile/profile.html",
        user=user,
        total_courses=total_courses,
        completed_courses=completed_courses
    )