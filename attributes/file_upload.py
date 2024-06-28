import sys
import os
# Add the parent directory to the Python path
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))
from main import client, db_id, collection_file_upload
from appwrite.services.databases import Databases

db = Databases(client)

# Function to check if an attribute exists
def attribute_exists(db, database_id, collection_id, key):
    try:
        attribute_info = db.get_attribute(database_id, collection_id, key)
        return attribute_info is not None
    except:
        return False

# Define attributes for the collection
attributes_to_create = [
    {'key': 'file_name', 'size': 255, 'required': True},
    {'key': 'file_url', 'size': 255, 'required': True},
    {'key': 'file_size', 'size': 255, 'required': True},
    {'key': 'file_description', 'size': 255, 'required': True},
    {'key': 'device_name', 'size': 255, 'required': True},
    {'key': 'device_department', 'size': 255, 'required': True},
    {'key': 'user_upload', 'size': 255, 'required': True},
    {'key': 'upload_date', 'size': 255, 'required': True}
]

# Check and create string attributes in the collection
for attr in attributes_to_create:
    if attribute_exists(db, db_id, collection_file_upload, attr['key']):
        print(f"Attribute '{attr['key']}' has been created already.")
    else:
        try:
            db.create_string_attribute(
                database_id=db_id,
                collection_id=collection_file_upload,
                key=attr['key'],
                size=attr['size'],
                required=attr['required']
            )
            print(f"Attribute '{attr['key']}' was not found, created successfully.")
        except Exception as e:
            print(f"Failed to create attribute '{attr['key']}': {e}")
