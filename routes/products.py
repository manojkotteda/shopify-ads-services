# routes/products.py
from fastapi import APIRouter, Query, HTTPException
from database import save_product, get_products
from scraper import scrape_shopify_product
from models import Product, SaveProductRequest

router = APIRouter()

@router.get("/products", response_model=Product)
def get_product_details(url: str = Query(..., description="Shopify product URL")):
    """Retrieves product details from a given Shopify product URL."""
    return scrape_shopify_product(url)

@router.post("/save-product")
def save_product_api(request: SaveProductRequest):
    """Saves a Shopify product URL and image in memory for later processing, associated with a user ID."""
    product_id = save_product(request.user_id, str(request.url), request.image)
    return {"status": "success", "message": "Product saved successfully", "product_id": product_id}

@router.get("/get-products/{user_id}")
def get_saved_products(user_id: str):
    """Retrieves all saved products for a given user ID."""
    products = get_products(user_id)
    if not products:
        raise HTTPException(status_code=404, detail="No products found for this user")
    return {"user_id": user_id, "products": products}
