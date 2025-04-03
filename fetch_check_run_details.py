import requests 
def get_check_run_details(repo_name, check_run_id, installation_access_token):
    """
    Fetch the details of a check run to inspect the `app_id`.
    """
    url = f'https://api.github.com/repos/{repo_name}/check-runs/{check_run_id}'
    headers = {
        'Authorization': f'token {installation_access_token}',
        'Accept': 'application/vnd.github.v3+json'
    }

    response = requests.get(url, headers=headers)

    if response.status_code == 200:
        check_run = response.json()
        print(f"Check Run ID: {check_run['id']}")
        print(f"App ID: {check_run['app']['id']}")  # The app_id that created the check run
        return check_run
    else:
        print(f"Failed to fetch check run details: {response.status_code}")
        return None
