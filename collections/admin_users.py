from main import client, db_id, collection_admin_users_id
from appwrite.services.databases import Databases
import secrets

db = Databases(client)

# Create a new collection

admin_users = db.create_collection(
    database_id = db_id,
    collection_id = secrets.token_hex(8),
    name = 'admin-users',
    permission = 'role:admin'
)

print(admin_users)