from flask_wtf import FlaskForm
from wtforms import (
    StringField,
    TextAreaField,
    SubmitField
)
from wtforms.validators import DataRequired


class JobForm(FlaskForm):

    company = StringField(
        "Company",
        validators=[DataRequired()]
    )

    title = StringField(
        "Job Title",
        validators=[DataRequired()]
    )

    location = StringField(
        "Location",
        validators=[DataRequired()]
    )

    experience = StringField(
        "Experience",
        validators=[DataRequired()]
    )

    salary = StringField(
        "Salary",
        validators=[DataRequired()]
    )

    skills = StringField(
        "Skills",
        validators=[DataRequired()]
    )

    description = TextAreaField(
        "Description",
        validators=[DataRequired()]
    )

    submit = SubmitField("Post Job")