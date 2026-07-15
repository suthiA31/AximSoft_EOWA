from flask_wtf import FlaskForm
from wtforms import (
    StringField,
    PasswordField,
    SubmitField,
    SelectField
)

from wtforms.validators import (
    DataRequired,
    Email,
    Length
)


class RegisterForm(FlaskForm):

    name = StringField(
        "Name",
        validators=[DataRequired()]
    )

    email = StringField(
        "Email",
        validators=[
            DataRequired(),
            Email()
        ]
    )

    password = PasswordField(
        "Password",
        validators=[
            DataRequired(),
            Length(min=6)
        ]
    )

    role = SelectField(
        "Role",
        choices=[
            ("candidate", "Candidate"),
            ("employer", "Employer")
        ]
    )

    submit = SubmitField("Register")


class LoginForm(FlaskForm):

    email = StringField(
        "Email",
        validators=[
            DataRequired(),
            Email()
        ]
    )

    password = PasswordField(
        "Password",
        validators=[DataRequired()]
    )

    submit = SubmitField("Login")