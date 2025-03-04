# middleware.py
from fastapi.middleware.cors import CORSMiddleware

def setup_cors(app):
    """Configures CORS for the FastAPI app."""
    app.add_middleware(
        CORSMiddleware,
        allow_origins=["*"],  # Modify in production for security
        allow_credentials=True,
        allow_methods=["*"],
        allow_headers=["*"],
    )
