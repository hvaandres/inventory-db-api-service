from main import client, db_id, collection_admin_users_id
from appwrite.services.databases import Databases
import secrets

db = Databases(client)

# Create a new Database

def create_db():
    try:
        result = db.create(
        database_id=secrets.token_hex(8),
        name = 'inventory-dgm'
        )

        print(result)
    except Exception as e:
        print(f"An error occurred: {e}")
        print(f"Endpoint: {client.endpoint}")
        print(f"Project ID: {client.headers['x-appwrite-project']}")
        print(f"API Key: {client.headers['x-appwrite-key']}")
# Test the function
create_db()