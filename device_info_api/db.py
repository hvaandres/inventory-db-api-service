import sys
import os
# Add the parent directory to the Python path
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))
from main import client, db_id, collection_device_id
from appwrite.services.databases import Databases
from datetime import datetime
import secrets

db = Databases(client)

class CRUD:
    def __init__(self):
        self.db = Databases(client)  # Initialize Databases object with client

        self.db_id = db_id
        self.collection_device_id = collection_device_id

    def list_devices(self):
        result = self.db.list_documents(
            database_id=self.db_id,
            collection_id=self.collection_device_id
        )
        documents = result.get("documents", [])
        return documents

    # def create_device(self, data: dict):
    #     # Ensure 'created_at' is added to 'data' if it's included in the model
    #     if 'created_at' in data and isinstance(data['created_at'], datetime):
    #         data['created_at'] = data['created_at'].isoformat()
    #     else:
    #         data['created_at'] = datetime.utcnow().isoformat()

    #     # Create document with a generated ID
    #     result = self.db.create_document(
    #         database_id=self.db_id,
    #         collection_id=self.collection_device_id,
    #         document_id=secrets.token_hex(8),
    #         data=data
    #     )
    #     return result

    def create_device(self, data: dict):
        result = db.create_document(
            database_id=self.db_id,
            collection_id=self.collection_device_id,
            document_id=secrets.token_hex(8),
            data=data
        )
        return result

    def retrieve_device(self, document_id: str):
        result = self.db.get_document(
            database_id=self.db_id,
            collection_id=self.collection_device_id,
            document_id=document_id
        )
        return result

    def update_device(self, document_id: str, data: dict):
        # Convert datetime to ISO format string if present
        if 'created_at' in data and isinstance(data['created_at'], datetime):
            data['created_at'] = data['created_at'].isoformat()
        result = self.db.update_document(
            database_id=self.db_id,
            collection_id=self.collection_device_id,
            document_id=document_id,
            data=data
        )
        return result

    def delete_device(self, document_id: str):
        result = self.db.delete_document(
            database_id=self.db_id,
            collection_id=self.collection_device_id,
            document_id=document_id
        )
        return result