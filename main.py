from fastapi import FastAPI, HTTPException, Query
import requests
from bs4 import BeautifulSoup
import logging
from pydantic import BaseModel, HttpUrl
import uuid

app = FastAPI()

# Set up logging
logging.basicConfig(level=logging.INFO)

# In-memory database (dictionary)
in_memory_db = {}

# Shopify Product Data Model
class Product(BaseModel):
    title: str
    price: str
    currency: str
    description: str
    image: str
    url: HttpUrl

# Request Model for Saving Product
class SaveProductRequest(BaseModel):
    user_id: str
    url: HttpUrl
    image: str

# Shopify Product Scraper
def scrape_shopify_product(url: str):
    headers = {"User-Agent": "Mozilla/5.0"}
    try:
        response = requests.get(url, headers=headers, timeout=10)
        if response.status_code != 200:
            raise HTTPException(status_code=400, detail="Failed to fetch the product page")

        soup = BeautifulSoup(response.text, "html.parser")

        product_data = {
            "title": soup.find("meta", {"property": "og:title"})["content"] if soup.find("meta", {"property": "og:title"}) else "N/A",
            "price": soup.find("meta", {"property": "product:price:amount"})["content"] if soup.find("meta", {"property": "product:price:amount"}) else "N/A",
            "currency": soup.find("meta", {"property": "product:price:currency"})["content"] if soup.find("meta", {"property": "product:price:currency"}) else "N/A",
            "description": soup.find("meta", {"property": "og:description"})["content"] if soup.find("meta", {"property": "og:description"}) else "N/A",
            "image": soup.find("meta", {"property": "og:image"})["content"] if soup.find("meta", {"property": "og:image"}) else "N/A",
            "url": url,
        }
        return product_data
    except Exception as e:
        logging.error(f"Error parsing Shopify product: {str(e)}")
        raise HTTPException(status_code=500, detail="Error parsing Shopify product")

# API Endpoint to Extract Product Details
@app.get("/api/v1/products", response_model=Product)
def get_product_details(url: str = Query(..., description="Shopify product URL")):
    """
    Retrieves product details from a given Shopify product URL.
    """
    return scrape_shopify_product(url)

# Dummy Ad Integration Model
class AdRequest(BaseModel):
    platform: str
    product: Product

# Dummy Endpoint to Create an Ad
@app.post("/api/v1/ads")
def create_ad(ad_request: AdRequest):
    """
    Creates an ad campaign using the extracted product details.
    """
    logging.info(f"Creating ad for {ad_request.product.title} on {ad_request.platform}")
    
    # This is where Meta/Google Ads API integration would be added.
    return {"status": "success", "message": f"Ad for {ad_request.product.title} created on {ad_request.platform}"}

# API Endpoint to Save Shopify URL and Image
@app.post("/api/v1/save-product")
def save_product(request: SaveProductRequest):
    """
    Saves a Shopify product URL and image in memory for later processing, associated with a user ID.
    """
    product_id = str(uuid.uuid4())
    if request.user_id not in in_memory_db:
        in_memory_db[request.user_id] = {}
    
    in_memory_db[request.user_id][product_id] = {
        "url": request.url,
        "image": request.image
    }
    
    return {"status": "success", "message": "Product saved successfully", "product_id": product_id}

# API Endpoint to Retrieve Saved Products
@app.get("/api/v1/get-products/{user_id}")
def get_saved_products(user_id: str):
    """
    Retrieves all saved products for a given user ID.
    """
    if user_id not in in_memory_db:
        raise HTTPException(status_code=404, detail="No products found for this user")
    return {"user_id": user_id, "products": in_memory_db[user_id]}



# Run server with: `uvicorn main:app --host 0.0.0.0 --port 8000 --reload`
# use this path for docs `http://127.0.0.1:8000/docs`
