from flask_mail import Message
from flask import render_template,current_app
from extension import mail



def send_email(
    subject,
    recipient,
    template,
    **kwargs
):

    html = render_template(
        template,
        **kwargs
    )

    msg = Message(
        subject,
        sender=current_app.config["MAIL_DEFAULT_SENDER"],
        recipients=[recipient]
    )

    msg.html = html

    mail.send(msg)