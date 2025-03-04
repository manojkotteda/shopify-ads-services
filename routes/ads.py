# routes/ads.py
from fastapi import APIRouter
from models import AdRequest
import logging

router = APIRouter()
logging.basicConfig(level=logging.INFO)

@router.post("/ads")
def create_ad(ad_request: AdRequest):
    """Creates an ad campaign using the extracted product details."""
    logging.info(f"Creating ad for {ad_request.product.title} on {ad_request.platform}")
    return {"status": "success", "message": f"Ad for {ad_request.product.title} created on {ad_request.platform}"}
