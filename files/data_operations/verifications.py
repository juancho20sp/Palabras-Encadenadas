import re

def validate_email(email: str) -> bool:
    """
    This is a function that validates if the email entered is valid.

    :param email: Email entered by the user.
    :return: True if the email is valid, False otherwise.
    """
    regex_email = '^\w+([\.-]?\w+)*@\w+([\.-]?\w+)*(\.\w{2,3})+$'

    if re.search(regex_email, email):
        return True
    else:
        return False
