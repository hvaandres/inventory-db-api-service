from appwrite.client import Client
from dotenv import load_dotenv
import os


load_dotenv()

project_id = os.getenv('APPWRITE_PROJECT_ID')
api_key = os.getenv('APPWRITE_API_KEY')
db_id = os.getenv('APPWRITE_DB_ID')
collection_admin_users_id = os.getenv('APPWRITE_COLLECTION_ADMIN_USERS_ID')
Collection_standard_users_id = os.getenv('APPWRITE_COLLECTION_STANDARD_USERS_ID')

client = Client()

client = (client
          
    .set_endpoint('https://cloud.appwrite.io/v1') # Your API Endpoint
    .set_project(project_id) # Your project ID
    .set_key(api_key) # Your secret API key         
)

