from github import Github
from dotenv import load_dotenv
import os
from installation_token_generator import get_installation_access_token
from jwt_generator import generate_jwt
def notify_classroom(final_score):
    # Load environment variables from the .env file
    load_dotenv()

    # Retrieve necessary values from environment variables
    private_key_path = os.getenv("PRIVATE_KEY_PATH")
    app_id = os.getenv("GITHUB_APP_ID")
    installation_id = os.getenv("INSTALLATION_ID")
    repo_name = os.getenv("GITHUB_REPOSITORY")
    check_run_id = os.getenv("CHECK_RUN_ID")

    # Check if all necessary environment variables are present
    if not private_key_path or not app_id or not installation_id or not repo_name or not check_run_id:
        print("Missing required environment variables.")
        return

    # Read the private key from file
    with open(private_key_path, 'r') as file:
        private_key = file.read()

    # Generate JWT
    jwt_token = generate_jwt(private_key, app_id)

    # Get the installation access token
    installation_access_token = get_installation_access_token(jwt_token, installation_id)

    if not installation_access_token:
        return

    # Create the GitHub client using the installation access token
    g = Github(installation_access_token)
    repo = g.get_repo(repo_name)

    # Retrieve the check run using the provided check_run_id
    check_run = repo.get_check_run(int(check_run_id))

    if not check_run:
        print("Check run not found.")
        return
    print(f"Check run ID: {check_run.id}")

    # Create a summary for the final grade
    text = f"Final Score: {final_score}/100"

    # Update the check run with the final score
    check_run.edit(
        name="Autograding",
        output={
            "title": "Autograding Result",
            "summary": text,
            "text": text,
            "annotations": [{
                "path": ".github",
                "start_line": 1,
                "end_line": 1,
                "annotation_level": "notice",
                "message": text,
                "title": "Autograding complete"
            }]
        }
    )

    print(f"Final grade updated: {final_score}/100")

if __name__ == "__main__":
    # Call the notify_classroom function with a sample score
    notify_classroom(95)
