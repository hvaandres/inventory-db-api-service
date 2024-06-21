import sys
import os
# Add the parent directory to the Python path
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))
from main import client, db_id, collection_device_id, bucket_id
from appwrite.services.databases import Databases
from appwrite.services.storage import Storage
import secrets

db = Databases(client)
storage = Storage(client)

# Define attributes for the collection
attributes_to_create = [
    {'key': 'device_name', 'size': 255, 'required': True},
    {'key': 'device_sku', 'size': 255, 'required': True},
    {'key': 'uvu_sku', 'size': 255, 'required': True},
    {'key': 'device_mac_address', 'size': 255, 'required': True},
    {'key': 'funding_source', 'size': 255, 'required': True},
    {'key': 'device_cost', 'size': 255, 'required': True},
    {'key': 'device_category', 'size': 255, 'required': True},
    {'key': 'serial_number', 'size': 255, 'required': True},
    {'key': 'inventory_status', 'size': 255, 'required': True}
]

# Check and create string attributes in the collection
for attr in attributes_to_create:
    try:
        # Check if attribute exists
        attribute_info = db.get_attribute(
            database_id=db_id,
            collection_id=collection_device_id,
            key=attr['key']
        )
        if attribute_info:
            print(f"Attribute '{attr['key']}' has been created already.")
        else:
            # Create attribute if it doesn't exist
            db.create_string_attribute(
                database_id=db_id,
                collection_id=collection_device_id,
                key=attr['key'],
                size=attr['size'],
                required=attr['required']
            )
            print(f"Attribute '{attr['key']}' was not found, created successfully.")
    
    except Exception as e:
        print(f"Failed to check or create attribute '{attr['key']}': {e}")

# Create a string attribute to store the file ID
try:
    # Check if attribute exists
    attribute_info = db.get_attribute(
        database_id=db_id,
        collection_id=collection_device_id,
        key='device_image_id'
    )
    if attribute_info:
        print("Attribute 'device_image_id' has been created already.")
    else:
        # Create attribute if it doesn't exist
        db.create_string_attribute(
            database_id=db_id,
            collection_id=collection_device_id,
            key='device_image_id',
            size=1024,
            required=True
        )
        print("Attribute 'device_image_id' was not found, created successfully.")

except Exception as e:
    print(f"Failed to check or create attribute 'device_image_id': {e}")

# Additional logic to handle file storage if required
try:
    # Replace with your file storage logic
    file_id = storage.create_file(
        bucket=bucket_id,
        data=b'File content example',  # Replace with your actual file content
        file_name='example.jpg',  # Replace with the actual file name
        content_type='image/jpeg',  # Replace with the actual content type
        encryption=False  # Set to True if you want encryption
    )
    print("File stored successfully with ID:", file_id)

    # Update the document in the database with the file ID
    document_id = secrets.token_hex(8)  # Generate a unique document ID
    db.create_document(
        database_id=db_id,
        collection_id=collection_device_id,
        data={
            'device_name': 'Device Name',
            'device_sku': 'Device SKU',
            'uvu_sku': 'UVU SKU',
            'device_mac_address': 'Device MAC Address',
            'funding_source': 'Funding Source',
            'device_cost': 'Device Cost',
            'device_category': 'Device Category',
            'serial_number': 'Serial Number',
            'inventory_status': 'Inventory Status',
            'device_image_id': file_id  # Assign the file ID to the device_image_id attribute
        }
    )
    print("Document created successfully with file reference.")

except Exception as e:
    print(f"Failed to store file or create document: {e}")