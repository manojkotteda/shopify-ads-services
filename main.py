# main.py
from fastapi import FastAPI
from routes import products, ads
from middleware import setup_cors

app = FastAPI()

# Setup CORS middleware
setup_cors(app)

# Include the product and ad routes
app.include_router(products.router, prefix="/api/v1")
app.include_router(ads.router, prefix="/api/v1")

# Run server with: `uvicorn main:app --reload`
# Run server with: `uvicorn main:app --host 0.0.0.0 --port 8000 --reload`
# use this path for docs `http://127.0.0.1:8000/docs`
