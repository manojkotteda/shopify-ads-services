import requests
from fastapi import HTTPException
import logging

logging.basicConfig(level=logging.INFO)
logger = logging.getLogger("shopify_scraper")

def scrape_shopify_products(shopify_store_url: str):
    """
    Scrapes multiple product details from a Shopify store using its JSON API.
    """
    try:
        # Construct the API endpoint URL
        products_api_url = f"{shopify_store_url.rstrip('/')}/products.json"
        
        logger.info(f"Fetching products from Shopify API: {products_api_url}")
        response = requests.get(products_api_url, timeout=10)

        if response.status_code != 200:
            raise HTTPException(status_code=400, detail="Failed to fetch product data from Shopify API")

        data = response.json()

        if "products" not in data:
            raise HTTPException(status_code=404, detail="No products found in the Shopify API response")

        products = []
        for product in data["products"]:
            # Extract basic product details
            title = product.get("title", "N/A")
            description = product.get("body_html", "N/A")
            handle = product.get("handle", "N/A")
            product_url = f"{shopify_store_url.rstrip('/')}/products/{handle}"
            vendor = product.get("vendor", "N/A")

            # Get the first variant's price
            variants = product.get("variants", [])
            price = variants[0].get("price", "N/A") if variants else "N/A"

            # Extract product images (first image as main)
            images = product.get("images", [])
            image_url = images[0].get("src", "N/A") if images else "N/A"

            products.append({
                "title": title,
                "description": description,
                "price": price,
                "currency": "USD",  # Shopify stores generally use USD
                "image": image_url,
                "vendor": vendor,
                "url": product_url
            })

        return products

    except Exception as e:
        logger.error(f"Error fetching Shopify products: {str(e)}")
        raise HTTPException(status_code=500, detail="Error fetching Shopify products")
