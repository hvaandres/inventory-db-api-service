from appwrite.client import Client
from appwrite.services.storage import Storage
import os
from dotenv import load_dotenv

# Load environment variables from a dedicated .env file
load_dotenv()

def get_appwrite_config():
    """
    Fetches Appwrite configuration details from environment variables.

    Raises:
        ValueError: If any required environment variable is missing.
    """
    required_vars = ["APPWRITE_ENDPOINT", "APPWRITE_PROJECT_ID", "APPWRITE_API_KEY", "APPWRITE_BUCKET_ID"]
    for var in required_vars:
        if not os.getenv(var):
            raise ValueError(f"Missing environment variable: {var}")

    return {
        "endpoint": os.getenv("APPWRITE_ENDPOINT"),
        "project": os.getenv("APPWRITE_PROJECT_ID"),
        "key": os.getenv("APPWRITE_API_KEY"),
        "bucket_id": os.getenv("APPWRITE_BUCKET_ID"),
    }

def list_bucket_files(config):
    """
    Initializes Appwrite client and lists files in the specified bucket.

    Args:
        config: A dictionary containing Appwrite configuration details.

    Prints:
        File URLs and names or informative messages depending on the outcome.

    Raises:
        Exception: If an error occurs while listing files.
    """
    client = Client()
    client.set_endpoint(config["endpoint"])  # Set Appwrite endpoint
    client.set_project(config["project"])    # Set Appwrite project ID
    client.set_key(config["key"])            # Set Appwrite API key

    storage = Storage(client)

    try:
        response = storage.list_files(bucket_id=config["bucket_id"])

        if "files" in response:
            files = response["files"]
            if len(files) > 0:
                print("Files in bucket:")
                for file in files:
                    file_id = file["$id"]
                    file_name = file["name"]
                    file_url = f"{config['endpoint']}/v1/storage/files/{file_id}/view"
                    print(f"File Name: {file_name}")
                    print(f"File URL: {file_url}")
            else:
                print("No files found in the bucket.")
        else:
            print("No 'files' key found in the response.")

    except Exception as e:
        print(f"Failed to list files: {str(e)}")
        # Implement more detailed logging here (e.g., logging the response object)

if __name__ == "__main__":
    try:
        config = get_appwrite_config()
        list_bucket_files(config)
    except ValueError as e:
        print(f"Error: {e}")
