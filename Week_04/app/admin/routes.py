import os

from flask import (
    render_template,
    request,
    redirect,
    url_for,
    flash,
    current_app
)

from werkzeug.utils import secure_filename

from app.admin import admin_bp
from app.models.database import get_db
from app.utils.decorators import admin_required



# ADMIN DASHBOARD / MANAGE COURSES
# =========================
@admin_bp.route("/courses")
@admin_required
def manage_courses():

    conn = get_db()

    courses = conn.execute(
        "SELECT * FROM courses"
    ).fetchall()

    conn.close()

    return render_template(
        "admin/manage_courses.html",
        courses=courses
    )



# ADD COURSE
# =========================
@admin_bp.route("/courses/add", methods=["GET", "POST"])
@admin_required
def add_course():

    if request.method == "POST":

        course_name = request.form["course_name"].strip()
        category = request.form["category"].strip()
        duration = request.form["duration"].strip()
        description = request.form["description"].strip()

        if not course_name or not category or not duration or not description:
            flash("All fields are required.", "danger")
            return redirect(url_for("admin.add_course"))

        image = request.files.get("course_image")
        filename = None

        if image and image.filename:
            filename = secure_filename(image.filename)

            upload_path = current_app.config["COURSE_UPLOAD_FOLDER"]

            os.makedirs(upload_path, exist_ok=True)

            image.save(
                os.path.join(upload_path, filename)
            )

        conn = get_db()

        conn.execute(
            """
            INSERT INTO courses
            (course_name, category, duration, description, image)
            VALUES (?, ?, ?, ?, ?)
            """,
            (
                course_name,
                category,
                duration,
                description,
                filename
            )
        )

        conn.commit()
        conn.close()

        flash("Course added successfully!", "success")
        return redirect(url_for("admin.manage_courses"))

    return render_template("admin/add_course.html")



# EDIT COURSE
# =========================
@admin_bp.route("/courses/edit/<int:course_id>", methods=["GET", "POST"])
@admin_required
def edit_course(course_id):

    conn = get_db()

    course = conn.execute(
        "SELECT * FROM courses WHERE course_id = ?",
        (course_id,)
    ).fetchone()

    if not course:
        conn.close()
        flash("Course not found.", "danger")
        return redirect(url_for("admin.manage_courses"))

    if request.method == "POST":

        course_name = request.form["course_name"].strip()
        category = request.form["category"].strip()
        duration = request.form["duration"].strip()
        description = request.form["description"].strip()

        if not course_name or not category or not duration or not description:
            conn.close()
            flash("All fields are required.", "danger")
            return redirect(url_for("admin.edit_course", course_id=course_id))

        image = request.files.get("course_image")
        filename = course["image"]

        if image and image.filename:
            filename = secure_filename(image.filename)

            upload_path = os.path.join(
                current_app.root_path,
                "static",
                "uploads",
                "courses"
            )

            os.makedirs(upload_path, exist_ok=True)

            image.save(
                os.path.join(upload_path, filename)
            )

        conn.execute(
            """
            UPDATE courses
            SET course_name = ?, category = ?, duration = ?, description = ?, image = ?
            WHERE course_id = ?
            """,
            (
                course_name,
                category,
                duration,
                description,
                filename,
                course_id
            )
        )

        conn.commit()
        conn.close()

        flash("Course updated successfully!", "success")
        return redirect(url_for("admin.manage_courses"))

    conn.close()

    return render_template(
        "admin/edit_course.html",
        course=course
    )



# DELETE COURSE

@admin_bp.route("/courses/delete/<int:course_id>", methods=["POST"])
@admin_required
def delete_course(course_id):

    conn = get_db()

    course = conn.execute(
        "SELECT * FROM courses WHERE course_id = ?",
        (course_id,)
    ).fetchone()

    if not course:
        conn.close()
        flash("Course not found.", "danger")
        return redirect(url_for("admin.manage_courses"))

    conn.execute(
        "DELETE FROM courses WHERE course_id = ?",
        (course_id,)
    )

    conn.commit()
    conn.close()

    flash("Course deleted successfully!", "success")
    return redirect(url_for("admin.manage_courses"))