import sys
import os
# Add the parent directory to the Python path
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))
from main import client, db_id, collection_standard_users_id
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
    {'key': 'first_name', 'size': 255, 'required': True},
    {'key': 'last_name', 'size': 255, 'required': True},
    {'key': 'uvu_id', 'size': 255, 'required': True},
    {'key': 'email_address', 'size': 255, 'required': True},
    {'key': 'degree_program', 'size': 255, 'required': True},
    {'key': 'uvu_status', 'size': 255, 'required': True}
]

# Check and create string attributes in the collection
for attr in attributes_to_create:
    if attribute_exists(db, db_id, collection_standard_users_id, attr['key']):
        print(f"Attribute '{attr['key']}' has been created already.")
    else:
        try:
            db.create_string_attribute(
                database_id=db_id,
                collection_id=collection_standard_users_id,
                key=attr['key'],
                size=attr['size'],
                required=attr['required']
            )
            print(f"Attribute '{attr['key']}' was not found, created successfully.")
        except Exception as e:
            print(f"Failed to create attribute '{attr['key']}': {e}")
