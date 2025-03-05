import firebase_admin
from firebase_admin import credentials, auth
from fastapi import HTTPException, Security, Depends
from fastapi.security import HTTPBearer, HTTPAuthorizationCredentials
import logging

logging.basicConfig(level=logging.INFO)
logger = logging.getLogger("auth_manager")

# Load Firebase credentials (Replace with your JSON file path)
cred = credentials.Certificate("shopify-ads-b2a23-firebase-adminsdk-fbsvc-c3f903e8b0.json")  # 🔹 Update this
firebase_admin.initialize_app(cred)

# Security scheme for authorization headers
security = HTTPBearer()

def verify_firebase_token(credentials: HTTPAuthorizationCredentials = Security(security)):
    """
    Verifies the Firebase Authentication token.
    """
    token = credentials.credentials
    try:
        decoded_token = auth.verify_id_token(token)
        user_id = decoded_token["uid"]
        return user_id  # Successfully authenticated
    except Exception as e:
        logger.error(f"Authentication failed: {str(e)}")
        raise HTTPException(status_code=401, detail="Invalid or expired token")
