import firebase_admin
from firebase_admin import credentials, firestore
from datetime import datetime

from dotenv import load_dotenv
import os
import json

load_dotenv()
key = json.loads(os.getenv('GOOGLE_CLOUD_CREDENTIALS'))

firebase_config = key
cred = credentials.Certificate(firebase_config)

# Initialize Firebase app only once
try:
    firebase_admin.get_app()
except ValueError:
    firebase_admin.initialize_app(cred)

def addDB(data, collection_id="journal", document_id="logs"):
    # Initialize Firestore database
    db = firestore.client()
    doc_ref = db.collection(u''+collection_id).add(data)

def updateDB(new_data, collection_id="journal", document_id="logs"):
    # Initialize Firestore database
    db = firestore.client()
    doc_ref = db.collection(u''+collection_id).document(document_id)
    doc_ref.update(new_data)

def readDB(collection_id="journal", document_id="logs"):
    # Initialize Firestore database
    db = firestore.client()
    doc_ref = db.collection(u''+collection_id)
    docs = doc_ref.stream()
    for doc in docs:
        if doc.id == document_id:
            return doc.to_dict()


