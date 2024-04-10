from jose import jwt

def generate_token(email):
    """
    Generate JWT token for authentication.
    """
    token = jwt.encode({"sub": email}, "secret_key", algorithm="HS256")
    return token
