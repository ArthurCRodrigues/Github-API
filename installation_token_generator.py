import requests

def get_installation_access_token(jwt_token, installation_id):
    """
    Get the installation access token using the JWT.
    """
    url = f'https://api.github.com/app/installations/{installation_id}/access_tokens'
    headers = {
        'Authorization': f'Bearer {jwt_token}',
        'Accept': 'application/vnd.github.v3+json'
    }

    response = requests.post(url, headers=headers)

    if response.status_code == 201:
        return response.json()['token']
    else:
        print("Failed to get installation access token:", response.json())
        return None
