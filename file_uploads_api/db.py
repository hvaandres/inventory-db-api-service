import sys
import os
# Add the parent directory to the Python path
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

from main import client, db_id, collection_file_upload
from appwrite.services.databases import Databases
import secrets

db = Databases(client)
collection_file_upload = os.getenv('APPWRITE_COLLECTION_FILE_UPLOAD')

class CRUD:
    def __init__(self):
        self.db_id = db_id
        self.collection_file_upload = collection_file_upload

    def list_standard_files(self):
        result = db.list_documents(
            database_id=self.db_id,
            collection_id=self.collection_file_upload
        )
        return result
    
    def create_standard_file(self, data: dict):
        result = db.create_document(
            database_id=self.db_id,
            collection_id=self.collection_file_upload,
            document_id=secrets.token_hex(8),
            data=data
        )
        return result
    
    def retrieve_standard_file(self, document_id: str):
        result = db.get_document(
            database_id=self.db_id,
            collection_id=self.collection_file_upload,
            document_id=document_id
        )
        return result
    
    def update_standard_file(self, document_id: str, data: dict):
        result = db.update_document(
            database_id=self.db_id,
            collection_id=self.collection_file_upload,
            document_id=document_id,
            data=data
        )
        return result
    
    def delete_standard_file(self, document_id: str):
        result = db.delete_document(
            database_id=self.db_id,
            collection_id=self.collection_file_upload,
            document_id=document_id
        )
        return result