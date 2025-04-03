# Github-API
This repo is meant for exploring the github api features. Specially focusing on classroom resources related to the autograding feature. 
## Currently not working
Had several tests ran, but i'm having serious troubles with authentication and permissions. Github is not allowing the script to update check_runs from foreign repositories, it is throwing the following error message: 
```json
{
    "message": "Invalid app_id `15368` - check run can only be modified by the GitHub App that created it.", 
    "documentation_url": "https://docs.github.com/rest/checks/runs#update-a-check-run", 
    "status": "403"
    }
```