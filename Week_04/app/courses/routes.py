from flask import (
    render_template,
    request,
    redirect,
    url_for,
    flash,
    session
)

from app.courses import courses_bp
from app.models.database import get_db


# =========================
# COURSES LIST PAGE
# =========================
@courses_bp.route("/")
def courses():

    search = request.args.get("search", "")
    category = request.args.get("category", "")

    conn = get_db()

    query = """
        SELECT *
        FROM courses
        WHERE 1=1
    """

    params = []

    # -------------------------
    # SEARCH BY COURSE NAME
    # -------------------------
    if search:
        query += """
            AND course_name LIKE ?
        """
        params.append(f"%{search}%")

    # -------------------------
    # FILTER BY CATEGORY
    # -------------------------
    if category:
        query += """
            AND category = ?
        """
        params.append(category)

    # -------------------------
    # FETCH COURSES
    # -------------------------
    courses = conn.execute(
        query,
        params
    ).fetchall()

    # -------------------------
    # FETCH DISTINCT CATEGORIES
    # -------------------------
    categories = conn.execute(
        """
        SELECT DISTINCT category
        FROM courses
        """
    ).fetchall()

    conn.close()

    return render_template(
        "courses/courses.html",
        courses=courses,
        categories=categories,
        search=search,
        selected_category=category
    )


# =========================
# COURSE DETAILS PAGE
# =========================
@courses_bp.route("/details/<int:course_id>")

def course_details(course_id):

    conn = get_db()

    course = conn.execute(
        """
        SELECT *
        FROM courses
        WHERE course_id = ?
        """,
        (course_id,)
    ).fetchone()

    if course is None:
        conn.close()
        flash("Course not found")
        return redirect(url_for("courses.courses"))

    # -------------------------
    # CHECK IF USER ALREADY ENROLLED
    # -------------------------
    enrolled = False

    if "user_id" in session:

        existing = conn.execute(
            """
            SELECT *
            FROM enrollments
            WHERE user_id = ?
            AND course_id = ?
            """,
            (
                session["user_id"],
                course_id
            )
        ).fetchone()

        if existing:
            enrolled = True

    conn.close()

    return render_template(
        "courses/course_details.html",
        course=course,
        enrolled=enrolled
    )

# =========================
# ENROLL IN COURSE
# =========================
@courses_bp.route("/enroll/<int:course_id>")
def enroll(course_id):

    if "user_id" not in session:
        flash("Please login first")
        return redirect(url_for("auth.login"))

    user_id = session["user_id"]

    conn = get_db()

    # -------------------------
    # CHECK COURSE EXISTS
    # -------------------------
    course = conn.execute(
        """
        SELECT *
        FROM courses
        WHERE course_id = ?
        """,
        (course_id,)
    ).fetchone()

    if course is None:
        conn.close()
        flash("Course not found")
        return redirect(url_for("courses.courses"))

    # -------------------------
    # CHECK ALREADY ENROLLED
    # -------------------------
    existing = conn.execute(
        """
        SELECT *
        FROM enrollments
        WHERE user_id = ?
        AND course_id = ?
        """,
        (user_id, course_id)
    ).fetchone()

    if not existing:
        conn.execute(
            """
            INSERT INTO enrollments (
                user_id,
                course_id
            )
            VALUES (?, ?)
            """,
            (user_id, course_id)
        )

        conn.commit()
        flash("Course enrolled successfully!")

    else:
        flash("You are already enrolled in this course")

    conn.close()

    return redirect(url_for("dashboard.dashboard"))