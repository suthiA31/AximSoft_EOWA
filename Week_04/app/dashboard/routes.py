from flask import (
    render_template,
    session,
    redirect,
    url_for,
    flash
)

from app.dashboard import dashboard_bp
from app.models.database import get_db


# =========================
# DASHBOARD (DB DRIVEN)
# =========================
@dashboard_bp.route("/")
def dashboard():

    if "user_id" not in session:
        return redirect(url_for("auth.login"))

    conn = get_db()

    enrolled_courses = conn.execute(
        """
        SELECT 
            c.course_id,
            c.course_name,
            c.category,
            c.duration,
            e.progress_percentage
        FROM enrollments e
        JOIN courses c ON e.course_id = c.course_id
        WHERE e.user_id = ?
        """,
        (session["user_id"],)
    ).fetchall()

    total_courses = len(enrolled_courses)
    completed_courses = 0

    course_list = []

    for course in enrolled_courses:

        course_dict = dict(course)

        if course_dict["progress_percentage"] >= 100:
            completed_courses += 1

        course_list.append({
            "course_id": course_dict["course_id"],
            "course_name": course_dict["course_name"],
            "category": course_dict["category"],
            "duration": course_dict["duration"],
            "progress": course_dict["progress_percentage"]
        })

    conn.close()

    return render_template(
        "dashboard/dashboard.html",
        enrolled_courses=course_list,
        total_courses=total_courses,
        completed_courses=completed_courses
    )


# =========================
# UPDATE PROGRESS (DB ONLY)
# =========================
@dashboard_bp.route("/update-progress/<int:course_id>")
def update_progress(course_id):

    if "user_id" not in session:
        return redirect(url_for("auth.login"))

    conn = get_db()

    enrollment = conn.execute(
        """
        SELECT progress_percentage
        FROM enrollments
        WHERE user_id = ?
        AND course_id = ?
        """,
        (session["user_id"], course_id)
    ).fetchone()

    if not enrollment:
        flash("Enrollment not found", "danger")
        return redirect(url_for("dashboard.dashboard"))

    new_progress = min(enrollment["progress_percentage"] + 25, 100)

    conn.execute(
        """
        UPDATE enrollments
        SET progress_percentage = ?
        WHERE user_id = ?
        AND course_id = ?
        """,
        (new_progress, session["user_id"], course_id)
    )

    conn.commit()
    conn.close()

    flash("Progress updated successfully!", "success")

    return redirect(url_for("dashboard.dashboard"))