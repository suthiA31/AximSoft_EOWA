from flask import render_template,request,flash,url_for,redirect
from flask_login import login_required, current_user
from extension import db
from candidate import candidate_bp


from models import (
    Application,
    SavedJob,
    Notification,
    Interview,

)
import os

from werkzeug.utils import secure_filename

from flask import current_app


@candidate_bp.route("/dashboard")
@login_required
def dashboard():

    total_applied = Application.query.filter_by(
        user_id=current_user.id
    ).count()

    saved_jobs = SavedJob.query.filter_by(
        user_id=current_user.id
    ).count()

    notifications = Notification.query.filter_by(
        user_id=current_user.id
    ).count()

    recent_applications = Application.query.filter_by(
        user_id=current_user.id
    ).order_by(
        Application.id.desc()
    ).limit(5).all()

    recent_saved_jobs = SavedJob.query.filter_by(
        user_id=current_user.id
    ).order_by(
        SavedJob.id.desc()
    ).limit(5).all()

    return render_template(
        "candidates/dashboard.html",
        total_applied=total_applied,
        saved_jobs=saved_jobs,
        notifications=notifications,
        recent_applications=recent_applications,
        recent_saved_jobs=recent_saved_jobs
    )

@candidate_bp.route("/notifications")
@login_required
def notifications():

    notifications = Notification.query.filter_by(
        user_id=current_user.id
    ).order_by(
        Notification.created_at.desc()
    ).all()

    return render_template(
        "candidates/notifications.html",
        notifications=notifications
    )
@candidate_bp.route("/applied-jobs")
@login_required
def applied_jobs():

    applications = Application.query.filter_by(
        user_id=current_user.id
    ).all()

    return render_template(
        "candidates/applied_jobs.html",
        applications=applications
    )


@candidate_bp.route("/saved-jobs")
@login_required
def saved_jobs():

    saved_jobs = SavedJob.query.filter_by(
        user_id=current_user.id
    ).all()

    return render_template(
        "candidates/saved_jobs.html",
        saved_jobs=saved_jobs
    )
@candidate_bp.route("/interviews")
@login_required
def interviews():

    interviews = Interview.query.filter_by(
        candidate_id=current_user.id
    ).all()

    return render_template(
        "candidates/interviews.html",
        interviews=interviews
    )
@candidate_bp.route("/profile")
@login_required
def profile():

    return render_template(
        "profile.html"
    )
@candidate_bp.route("/edit-profile", methods=["GET", "POST"])
@login_required
def edit_profile():
    profile_file = request.files.get("profile_pic")
    resume_file = request.files.get("resume")
    if profile_file and profile_file.filename:
        filename = secure_filename(profile_file.filename)

        profile_file.save(
            os.path.join(
                current_app.config["UPLOAD_FOLDER"],
                filename
            )
        )

        current_user.profile_pic = filename
    if resume_file and resume_file.filename:
        filename = secure_filename(resume_file.filename)

        resume_file.save(
            os.path.join(
                current_app.config["UPLOAD_FOLDER"],
                filename
            )
        )

        current_user.resume = filename

    if request.method == "POST":

        current_user.name = request.form.get("name")
        current_user.skills = request.form.get("skills")
        current_user.experience = request.form.get("experience")
        current_user.bio = request.form.get("bio")




        db.session.commit()

        flash("Profile Updated Successfully", "success")

        return redirect(url_for("candidate.profile"))

    return render_template("candidates/edit_profile.html")