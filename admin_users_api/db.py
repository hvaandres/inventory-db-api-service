from main import client, db_id, collection_admin_users_id
from appwrite.services.databases import Databases
import secrets

db = Databases(client)

class CRUD:
    def __init__(self):
        self.db_id = db_id
        self.collection_admin_users_id = collection_admin_users_id

    def list_admin_users(self):
        result = db.list_documents(
            database_id=self.db_id,
            collection_id=self.collection_admin_users_id
        )
        return result
    
    def create_admin_user(self, data: dict):
        result = db.create_document(
            database_id=self.db_id,
            collection_id=self.collection_admin_users_id,
            document_id=secrets.token_hex(8),
            data=data
        )
        return result
    
    def retrieve_admin_user(self, document_id: str):
        result = db.get_document(
            database_id=self.db_id,
            collection_id=self.collection_admin_users_id,
            document_id=document_id
        )
        return result
    
    def update_admin_user(self, document_id: str, data: dict):
        result = db.update_document(
            database_id=self.db_id,
            collection_id=self.collection_admin_users_id,
            document_id=document_id,
            data=data
        )
        return result
    
    def delete_admin_user(self, document_id: str):
        result = db.delete_document(
            database_id=self.db_id,
            collection_id=self.collection_admin_users_id,
            document_id=document_id
        )
        return result