from functools import wraps

from flask import (
    flash,
    redirect,
    url_for
)

from flask_login import (
    current_user
)


def employer_required(func):

    @wraps(func)
    def wrapper(*args, **kwargs):

        if current_user.role != "employer":

            flash(
                "Employer access only",
                "danger"
            )

            return redirect(
                url_for("jobs.all_jobs")
            )

        return func(*args, **kwargs)

    return wrapper


def candidate_required(func):

    @wraps(func)
    def wrapper(*args, **kwargs):

        if current_user.role != "candidate":

            flash(
                "Candidate access only",
                "danger"
            )

            return redirect(
                url_for("jobs.all_jobs")
            )

        return func(*args, **kwargs)

    return wrapper