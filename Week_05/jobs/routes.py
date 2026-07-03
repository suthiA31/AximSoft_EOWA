from flask import (
    render_template,
    request,
    redirect,
    url_for,
    flash,
    current_app
)

from flask_login import (
    login_required,
    current_user
)

from jobs import jobs_bp

from extension import db

from models import (
    Job,
    Application,
    SavedJob
)

from utils.helper import save_resume
from utils.notifications import create_notification
from utils.email import send_email


@jobs_bp.route("/")
def all_jobs():

    search = request.args.get("search")

    if search:
        jobs = Job.query.filter(
            Job.title.contains(search)
        ).all()
    else:
        jobs = Job.query.all()

    return render_template(
        "jobs/jobs.html",
        jobs=jobs
    )


@jobs_bp.route("/<int:id>")
def job_details(id):

    job = Job.query.get_or_404(id)

    return render_template(
        "jobs/job_details.html",
        job=job
    )

@jobs_bp.route(
    "/apply/<int:job_id>",
    methods=["POST"]
)
@login_required
def apply_job(job_id):

    existing = Application.query.filter_by(
        user_id=current_user.id,
        job_id=job_id
    ).first()

    if existing:

        flash(
            "You have already applied for this job",
            "warning"
        )

        return redirect(
            url_for(
                "jobs.job_details",
                id=job_id
            )
        )

    resume = request.files.get("resume")

    filename = save_resume(
        resume,
        current_app.config["UPLOAD_FOLDER"]
    )

    application = Application(
        user_id=current_user.id,
        job_id=job_id,
        resume_file=filename
    )

    db.session.add(application)
    db.session.commit()

    create_notification(
        current_user.id,
        "Application submitted successfully"
    )

    job = Job.query.get(job_id)

    send_email(
        subject="Application Submitted",
        recipient=current_user.email,
        template="emails/application.html",
        user=current_user,
        application=application,
        job=job
    )

    flash(
        "Application Submitted Successfully",
        "success"
    )

    return redirect(
        url_for(
            "candidate.dashboard"
        )
    )

@jobs_bp.route(
    "/save/<int:job_id>"
)
@login_required
def save_job(job_id):

    existing = SavedJob.query.filter_by(
        user_id=current_user.id,
        job_id=job_id
    ).first()

    if existing:

        flash(
            "Job Already Saved",
            "warning"
        )

        return redirect(
            url_for(
                "jobs.job_details",
                id=job_id
            )
        )

    saved = SavedJob(
        user_id=current_user.id,
        job_id=job_id
    )

    db.session.add(saved)
    db.session.commit()

    flash(
        "Job Saved Successfully",
        "success"
    )

    return redirect(
        url_for(
            "jobs.job_details",
            id=job_id
        )
    )
@jobs_bp.route("/companies")
def companies():
    return render_template(
        "companies.html"
    )


@jobs_bp.route("/categories")
def categories():
    return render_template(
        "categories.html"
    )


@jobs_bp.route("/about")
def about():
    return render_template(
        "about.html"
    )