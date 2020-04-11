def validate_int(n):
    is_valid = True
    try:
        int(n)
    except ValueError:
        is_valid = False
    return is_valid
