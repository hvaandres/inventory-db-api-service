import sys
import os
# Add the parent directory to the Python path
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))
from main import client, db_id, collection_admin_users_id
from appwrite.services.databases import Databases
import secrets

db = Databases(client)


# Define attributes for the collection

admin_users_attributes = db.create_string_attribute (
    database_id = db_id,
    collection_id = collection_admin_users_id,
    key = 'first_name',
    size = 255,
    required = True
)

admin_users_attributes = db.create_string_attribute (
    database_id = db_id,
    collection_id = collection_admin_users_id,
    key = 'last_name',
    size = 255,
    required = True
)

admin_users_attributes = db.create_string_attribute (
    database_id = db_id,
    collection_id = collection_admin_users_id,
    key = 'uvu_id',
    size = 255,
    required = True
)

admin_users_attributes = db.create_string_attribute (
    database_id = db_id,
    collection_id = collection_admin_users_id,
    key = 'title_name',
    size = 255,
    required = True
)

admin_users_attributes = db.create_string_attribute (
    database_id = db_id,
    collection_id = collection_admin_users_id,
    key = 'department_name',
    size = 255,
    required = True
)

admin_users_attributes = db.create_string_attribute (
    database_id = db_id,
    collection_id = collection_admin_users_id,
    key = 'manager_name',
    size = 255,
    required = True
)

print(admin_users_attributes)