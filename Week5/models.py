from datetime import datetime
#db is the SQLAlchemy object used to create database tables.
from extension import db
from flask_login import UserMixin


class User(UserMixin, db.Model):

    __tablename__ = "users"

    id = db.Column(
        db.Integer,
        primary_key=True
    )

    name = db.Column(
        db.String(100),
        nullable=False
    )

    email = db.Column(
        db.String(120),
        unique=True,
        nullable=False
    )

    password = db.Column(
        db.String(255),
        nullable=False
    )

    role = db.Column(
        db.String(20),
        nullable=False
    )

    profile_pic = db.Column(
        db.String(255)
    )

    resume = db.Column(
        db.String(255)
    )

    skills = db.Column(
        db.Text
    )

    experience = db.Column(
        db.Text
    )

    bio = db.Column(
        db.Text
    )

    is_verified = db.Column(
        db.Boolean,
        default=False
    )

    created_at = db.Column(
        db.DateTime,
        default=datetime.utcnow
    )
    company_name = db.Column(
        db.String(100)
    )


class Job(db.Model):

    __tablename__ = "jobs"

    id = db.Column(
        db.Integer,
        primary_key=True
    )

    company_name = db.Column(
        db.String(100)
    )

    title = db.Column(
        db.String(100)
    )

    location = db.Column(
        db.String(100)
    )

    experience = db.Column(
        db.String(50)
    )

    salary = db.Column(
        db.String(50)
    )

    skills = db.Column(
        db.Text
    )

    description = db.Column(
        db.Text
    )

    status = db.Column(
        db.String(20),
        default="Active"
    )

    posted_date = db.Column(
        db.DateTime,
        default=datetime.utcnow
    )

    employer_id = db.Column(
        db.Integer,
        db.ForeignKey("users.id")
    )

#Whenever a candidate applies for a job, one record is inserted.
class Application(db.Model):

    __tablename__ = "applications"
    user = db.relationship(
        "User",
        backref="applications"
    )

    job = db.relationship(
        "Job",
        backref="applications"
    )

    id = db.Column(
        db.Integer,
        primary_key=True
    )

    user_id = db.Column(
        db.Integer,
        db.ForeignKey("users.id")
    )

    job_id = db.Column(
        db.Integer,
        db.ForeignKey("jobs.id")
    )

    resume_file = db.Column(
        db.String(255)
    )

    status = db.Column(
        db.String(50),
        default="Applied"
    )

    applied_date = db.Column(
        db.DateTime,
        default=datetime.utcnow
    )
    user = db.relationship(
        "User",
        backref="applications"
    )
    job = db.relationship(
        "Job",
        backref="applications"
    )


class SavedJob(db.Model):

    __tablename__ = "saved_jobs"

    id = db.Column(
        db.Integer,
        primary_key=True
    )

    user_id = db.Column(
        db.Integer,
        db.ForeignKey("users.id")
    )

    job_id = db.Column(
        db.Integer,
        db.ForeignKey("jobs.id")
    )

    saved_date = db.Column(
        db.DateTime,
        default=datetime.utcnow
    )
    job = db.relationship(
        "Job",
        backref="saved_entries"
    )

    user = db.relationship(
        "User",
        backref="saved_jobs"
    )

class OTP(db.Model):

    __tablename__ = "otp"

    id = db.Column(
        db.Integer,
        primary_key=True
    )

    email = db.Column(
        db.String(120)
    )

    otp = db.Column(
        db.String(10)
    )

    created_at = db.Column(
        db.DateTime,
        default=datetime.utcnow
    )


class Notification(db.Model):

    __tablename__ = "notifications"

    id = db.Column(
        db.Integer,
        primary_key=True
    )

    user_id = db.Column(
        db.Integer,
        db.ForeignKey("users.id")
    )

    message = db.Column(
        db.Text
    )

    is_read = db.Column(
        db.Boolean,
        default=False
    )

    created_at = db.Column(
        db.DateTime,
        default=datetime.utcnow
    )


class Interview(db.Model):

    __tablename__ = "interviews"

    id = db.Column(
        db.Integer,
        primary_key=True
    )

    candidate_id = db.Column(
        db.Integer,
        db.ForeignKey("users.id")
    )

    job_id = db.Column(
        db.Integer,
        db.ForeignKey("jobs.id")
    )

    interview_date = db.Column(
        db.String(50)
    )

    interview_time = db.Column(
        db.String(50)
    )

    mode = db.Column(
        db.String(50)
    )

    status = db.Column(
        db.String(50),
        default="Scheduled"
    )
    #This means one user can have many interview
    candidate = db.relationship(
        "User",
        backref="scheduled_interviews"
    )

    job = db.relationship(
        "Job",
        backref="interviews"
    )
