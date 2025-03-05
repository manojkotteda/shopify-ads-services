from fastapi import APIRouter, Depends, HTTPException, Query
from auth import verify_firebase_token
from scraper import scrape_shopify_products
from database import save_product, get_products
from models import SaveProductRequest

router = APIRouter()

@router.get("/products", response_model=list)
def get_product_details(
    url: str = Query(..., description="Shopify product URL"),
    user_id: str = Depends(verify_firebase_token)  # 🔹 Require authentication
):
    """Retrieves product details from a given Shopify product URL."""
    return scrape_shopify_products(url)

@router.post("/save-product")
def save_product_api(request: SaveProductRequest, user_id: str = Depends(verify_firebase_token)):
    """Saves a Shopify product URL and image in memory for later processing, associated with a user ID."""
    product_id = save_product(user_id, str(request.url), request.image)
    return {"status": "success", "message": "Product saved successfully", "product_id": product_id}

@router.get("/get-products/{user_id}")
def get_saved_products(user_id: str, authenticated_user: str = Depends(verify_firebase_token)):
    """Retrieves all saved products for a given user ID."""
    if user_id != authenticated_user:
        raise HTTPException(status_code=403, detail="Access denied")
    
    products = get_products(user_id)
    if not products:
        raise HTTPException(status_code=404, detail="No products found for this user")
    return {"user_id": user_id, "products": products}
