from flask import (
    render_template,
    request,
    redirect,
    url_for,
    flash
)

from flask_login import (
    login_required,
    current_user
)

from employer import employer_bp

from extension import db

from models import (
    Job,
    Application,
    Interview,
    Notification
)

from utils.notifications import create_notification


# ------------------------
# Employer Dashboard
# ------------------------

@employer_bp.route("/dashboard")
@login_required
def dashboard():

    if current_user.role != "employer":
        flash("Access Denied", "danger")
        return redirect(url_for("candidate.dashboard"))

    jobs = Job.query.filter_by(
        employer_id=current_user.id
    ).all()

    total_jobs = len(jobs)

    total_applications = sum(
        len(job.applications)
        for job in jobs
    )

    total_candidates = len({
        app.user_id
        for job in jobs
        for app in job.applications
    })

    return render_template(
        "employer/dashboard.html",
        jobs=jobs,
        total_jobs=total_jobs,
        total_applications=total_applications,
        total_candidates=total_candidates
    )


# ------------------------
# Post Job
# ------------------------

@employer_bp.route(
    "/post-job",
    methods=["GET", "POST"]
)
@login_required
def post_job():

    if current_user.role != "employer":
        flash("Access Denied", "danger")
        return redirect(url_for("candidate.dashboard"))

    if request.method == "POST":
        job = Job(
            company_name=current_user.company_name,
            title=request.form.get("title"),
            location=request.form.get("location"),
            experience=request.form.get("experience"),
            salary=request.form.get("salary"),
            skills=request.form.get("skills"),
            description=request.form.get("description"),
            employer_id=current_user.id
        )

        db.session.add(job)
        db.session.commit()

        flash("Job Posted Successfully", "success")

        return redirect(
            url_for("employer.dashboard")
        )

    return render_template(
        "employer/post_job.html"
    )


# ------------------------
# View Job
# ------------------------

@employer_bp.route("/view-job/<int:job_id>")
@login_required
def view_job(job_id):

    job = Job.query.get_or_404(job_id)

    return render_template(
        "employer/view_job.html",
        job=job,
        total_applications=len(job.applications),
        shortlisted=0,
        interviews=len(job.interviews)
    )


# ------------------------
# Edit Job
# ------------------------

@employer_bp.route(
    "/edit-job/<int:job_id>",
    methods=["GET", "POST"]
)
@login_required
def edit_job(job_id):

    job = Job.query.get_or_404(job_id)

    if request.method == "POST":

        job.company_name = request.form["company"]
        job.title = request.form["title"]
        job.location = request.form["location"]
        job.experience = request.form["experience"]
        job.salary = request.form["salary"]
        job.skills = request.form["skills"]
        job.description = request.form["description"]

        db.session.commit()

        flash("Job Updated Successfully", "success")

        return redirect(
            url_for("employer.dashboard")
        )

    return render_template(
        "employer/edit_job.html",
        job=job
    )


# ------------------------
# Delete Job
# ------------------------

@employer_bp.route("/delete-job/<int:job_id>")
@login_required
def delete_job(job_id):

    job = Job.query.get_or_404(job_id)

    db.session.delete(job)
    db.session.commit()

    flash("Job Deleted Successfully", "success")

    return redirect(
        url_for("employer.dashboard")
    )


# ------------------------
# View Applicants
# ------------------------

@employer_bp.route("/applicants/<int:job_id>")
@login_required
def view_applicants(job_id):

    applications = Application.query.filter_by(
        job_id=job_id
    ).all()

    return render_template(
        "employer/applicants.html",
        applications=applications
    )


# ------------------------
# Schedule Interview
# ------------------------

@employer_bp.route(
    "/schedule-interview/<int:application_id>",
    methods=["GET", "POST"]
)
@login_required
def schedule_interview(application_id):

    application = Application.query.get_or_404(application_id)

    if request.method == "POST":

        # create interview entry
        interview = Interview(
            candidate_id=application.user_id,
            job_id=application.job_id,
            interview_date=request.form["date"],
            interview_time=request.form["time"],
            mode=request.form["mode"]
        )

        db.session.add(interview)

        # ✅ IMPORTANT: update status
        application.status = "Interview Scheduled"

        db.session.commit()

        # notification
        create_notification(
            application.user_id,
            "Your interview has been scheduled."
        )

        flash("Interview Scheduled Successfully", "success")

        return redirect(
            url_for("employer.view_applicants",
            job_id=application.job_id)
        )

    return render_template("employer/schedule_interview.html")


# ------------------------
# Notifications
# ------------------------

@employer_bp.route("/notifications")
@login_required
def notifications():

    notifications = Notification.query.filter_by(
        user_id=current_user.id
    ).order_by(
        Notification.created_at.desc()
    ).all()

    return render_template(
        "employer/notifications.html",
        notifications=notifications
    )


# ------------------------
# Employer Profile
# ------------------------

@employer_bp.route("/profile")
@login_required
def profile():

    return render_template(
        "employer/profile.html"
    )


# ------------------------
# Edit Profile
# ------------------------

@employer_bp.route(
    "/edit-profile",
    methods=["GET", "POST"]
)
@login_required
def edit_profile():

    if request.method == "POST":

        current_user.name = request.form["name"]
        current_user.skills = request.form["skills"]
        current_user.experience = request.form["experience"]
        current_user.bio = request.form["bio"]

        db.session.commit()

        flash(
            "Profile Updated Successfully",
            "success"
        )

        return redirect(
            url_for("employer.profile")
        )

    return render_template(
        "employer/edit_profile.html"
    )


@employer_bp.route("/resume/<filename>")
@login_required
def view_resume(filename):
    return render_template(
        "employer/view_resume.html",
        filename=filename
    )