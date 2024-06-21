import sys
import os
# Add the parent directory to the Python path
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))
from main import client, db_id, collection_device_id, bucket_id
from appwrite.services.storage import Storage
import secrets

storage = Storage(client)

try:
    result = storage.create_bucket(
        bucket_id=secrets.token_hex(8),
        name="uvu_inventory_dgm",
        permissions=["write(\"any\")", "create(\"any\")", "read(\"any\")", "update(\"any\")"],  # Set permissions for read and write
        file_security=False,
        enabled=True,
        maximum_file_size=50,
        allowed_file_extensions=["png", "jpg", "jpeg", "svg", "gif"],
        encryption=True,
        antivirus=False,
        compression="gzip",

    )
    print('Bucket created successfully:')
    print(result)
except Exception as e:
    print(f"Error creating bucket: {str(e)}")

