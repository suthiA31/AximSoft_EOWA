from functools import wraps
from flask import session, flash, redirect, url_for

def admin_required(view_func):
    @wraps(view_func)
    def wrapper(*args, **kwargs):

        if "user_id" not in session:
            flash("Please login first.", "warning")
            return redirect(url_for("auth.login"))

        if session.get("role") != "admin":
            flash("You are not authorized to access admin panel.", "danger")
            return redirect(url_for("main.home"))

        return view_func(*args, **kwargs)

    return wrapper