import os
import json
import firebase_admin
from firebase_admin import credentials, auth
from fastapi import HTTPException, Security, Depends
from fastapi.security import HTTPBearer, HTTPAuthorizationCredentials
from dotenv import load_dotenv
import logging

# Load .env from project root (one directory up from src/)
load_dotenv(dotenv_path=os.path.join(os.path.dirname(__file__), '..', '.env'))

# Setup logger
logging.basicConfig(level=logging.INFO)
logger = logging.getLogger("auth_manager")

# 🔹 Load Firebase credentials from environment variable
print(os.path.abspath)
firebase_credentials = os.getenv("FIREBASE_CREDENTIALS")

if not firebase_credentials:
    raise Exception("Firebase credentials not found in environment variables. Please check .env file.")

# Parse the JSON string into a dictionary
firebase_credentials_dict = json.loads(firebase_credentials)

# Initialize Firebase Admin SDK with credentials loaded from env
cred = credentials.Certificate(firebase_credentials_dict)
firebase_admin.initialize_app(cred)

# Security scheme for authorization headers
security = HTTPBearer()

def verify_firebase_token(credentials: HTTPAuthorizationCredentials = Security(security)):
    """
    Verifies the Firebase Authentication token from the frontend.
    """
    token = credentials.credentials
    try:
        decoded_token = auth.verify_id_token(token)
        user_id = decoded_token["uid"]
        logger.info(f"Authenticated user ID: {user_id}")
        return user_id  # Successfully authenticated user ID
    except Exception as e:
        logger.error(f"Authentication failed: {str(e)}")
        raise HTTPException(status_code=401, detail="Invalid or expired token")
