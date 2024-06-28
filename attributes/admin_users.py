import sys
import os
# Add the parent directory to the Python path
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))
from main import client, db_id, collection_admin_users_id
from appwrite.services.databases import Databases

db = Databases(client)

# Function to check if an attribute exists
def attribute_exists(db, database_id, collection_id, key):
    attributes = db.list_attributes(database_id, collection_id)
    for attribute in attributes['attributes']:
        if attribute['key'] == key:
            return True
    return False

# Define attributes for the collection
attributes = [
    {'key': 'first_name', 'size': 255, 'required': True},
    {'key': 'last_name', 'size': 255, 'required': True},
    {'key': 'uvu_id', 'size': 255, 'required': True},
    {'key': 'title_name', 'size': 255, 'required': True},
    {'key': 'department_name', 'size': 255, 'required': True},
    {'key': 'manager_name', 'size': 255, 'required': True},
    {'key': 'user_email', 'size': 255, 'required': True}
]

# Loop through attributes and create them if they do not exist
for attr in attributes:
    if attribute_exists(db, db_id, collection_admin_users_id, attr['key']):
        print(f"You already created the attribute '{attr['key']}'")
    else:
        print(f"Attribute '{attr['key']}' is not created yet. Creating this attribute now.")
        db.create_string_attribute(
            database_id=db_id,
            collection_id=collection_admin_users_id,
            key=attr['key'],
            size=attr['size'],
            required=attr['required']
        )
