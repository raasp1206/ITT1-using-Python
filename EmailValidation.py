class InvalidEmailError(Exception):
    pass
def validate_email(email_str):
    try:
        if ' ' in email_str:
            raise InvalidEmailError
        if email_str.count('@') != 1:
            raise InvalidEmailError
        username, domain = email_str.split('@')
        if not username:
            raise InvalidEmailError
        if '.' not in domain:
            raise InvalidEmailError
        allowed_chars = set("abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ0123456789_.")
        for char in username:
            if char not in allowed_chars:
                raise InvalidEmailError
        print("VALID")
    except InvalidEmailError:
        print("INVALID")
    except ValueError:
        print("INVALID")
def run_tests():
    email=input("Enter the valid email:")
    validate_email(email)
run_tests()
