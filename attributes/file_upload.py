import sys
import os
# Add the parent directory to the Python path
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

from main import client, db_id, collection_file_upload
from appwrite.services.databases import Databases
import secrets

db = Databases(client)

# Define attributes for the collection

standard_users_attributes = db.create_string_attribute (
    database_id = db_id,
    collection_id = collection_file_upload,
    key = 'file_name',
    size = 255,
    required = True
)

standard_users_attributes = db.create_string_attribute (
    database_id = db_id,
    collection_id = collection_file_upload,
    key = 'file_url',
    size = 255,
    required = True
)



standard_users_attributes = db.create_string_attribute (
    database_id = db_id,
    collection_id = collection_file_upload,
    key = 'file_size',
    size = 255,
    required = True
)

standard_users_attributes = db.create_string_attribute (
    database_id = db_id,
    collection_id = collection_file_upload,
    key = 'file_description',
    size = 255,
    required = True
)

standard_users_attributes = db.create_string_attribute (
    database_id = db_id,
    collection_id = collection_file_upload,
    key = 'device_name',
    size = 255,
    required = True
)

standard_users_attributes = db.create_string_attribute (
    database_id = db_id,
    collection_id = collection_file_upload,
    key = 'device_department',
    size = 255,
    required = True
)

standard_users_attributes = db.create_string_attribute (
    database_id = db_id,
    collection_id = collection_file_upload,
    key = 'user_upload',
    size = 255,
    required = True,
)

standard_users_attributes = db.create_string_attribute (
    database_id = db_id,
    collection_id = collection_file_upload,
    key = 'upload_date',
    size = 255,
    required = True,
)

print(standard_users_attributes)