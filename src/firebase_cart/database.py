import firebase_admin
from firebase_admin import credentials, firestore
from .models import FirebaseConfig

class FirebaseDB:
    def __init__(self, config: FirebaseConfig):
        cred = credentials.Certificate(config.credentials)
        if config.database_url:
            firebase_admin.initialize_app(cred, {'databaseURL': config.database_url})
        else:
            firebase_admin.initialize_app(cred)
        self.db = firestore.client()

    def get_cart_ref(self, cart_id: str):
        return self.db.collection("carts").document(cart_id)
    
    def get_cart_items_ref(self, user_id: str):
        return self.db.collection("carts").document(user_id)