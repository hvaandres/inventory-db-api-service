import sys
import os
# Add the parent directory to the Python path
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

from main import client, db_id, collection_standard_users_id
from appwrite.services.databases import Databases
import secrets

db = Databases(client)

# Define attributes for the collection

standard_users_attributes = db.create_string_attribute (
    database_id = db_id,
    collection_id = collection_standard_users_id,
    key = 'first_name',
    size = 255,
    required = True
)

standard_users_attributes = db.create_string_attribute (
    database_id = db_id,
    collection_id = collection_standard_users_id,
    key = 'last_name',
    size = 255,
    required = True
)

standard_users_attributes = db.create_string_attribute (
    database_id = db_id,
    collection_id = collection_standard_users_id,
    key = 'uvu_id',
    size = 255,
    required = True
)

standard_users_attributes = db.create_string_attribute (
    database_id = db_id,
    collection_id = collection_standard_users_id,
    key = 'email_address',
    size = 255,
    required = True
)

standard_users_attributes = db.create_string_attribute (
    database_id = db_id,
    collection_id = collection_standard_users_id,
    key = 'degree_program',
    size = 255,
    required = True
)

standard_users_attributes = db.create_string_attribute (
    database_id = db_id,
    collection_id = collection_standard_users_id,
    key = 'uvu_status',
    size = 255,
    required = True,
)

print(standard_users_attributes)