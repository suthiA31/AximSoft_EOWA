import random


def generate_otp():

    return str(
        random.randint(
            100000,
            999999
        )
    )


def verify_otp(
    entered_otp,
    stored_otp
):

    return entered_otp == stored_otp