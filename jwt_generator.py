import os
import time
import jwt

def generate_jwt(private_key, app_id):
    """
    Generates a JWT for GitHub App authentication.
    """
    payload = {
        "iat": int(time.time()),  # Issued at time
        "exp": int(time.time()) + (10 * 60),  # Expiration time (10 minutes)
        "iss": app_id  # GitHub App ID
    }

    # Generate the JWT
    return jwt.encode(payload, private_key, algorithm="RS256")
