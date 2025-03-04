# scraper.py
import requests
from bs4 import BeautifulSoup
from fastapi import HTTPException

def scrape_shopify_product(url: str) -> dict:
    """Scrapes product details from a Shopify URL."""
    headers = {"User-Agent": "Mozilla/5.0"}
    try:
        response = requests.get(url, headers=headers, timeout=10)
        if response.status_code != 200:
            raise HTTPException(status_code=400, detail="Failed to fetch the product page")

        soup = BeautifulSoup(response.text, "html.parser")

        return {
            "title": soup.find("meta", {"property": "og:title"})["content"] if soup.find("meta", {"property": "og:title"}) else "N/A",
            "price": soup.find("meta", {"property": "product:price:amount"})["content"] if soup.find("meta", {"property": "product:price:amount"}) else "N/A",
            "currency": soup.find("meta", {"property": "product:price:currency"})["content"] if soup.find("meta", {"property": "product:price:currency"}) else "N/A",
            "description": soup.find("meta", {"property": "og:description"})["content"] if soup.find("meta", {"property": "og:description"}) else "N/A",
            "image": soup.find("meta", {"property": "og:image"})["content"] if soup.find("meta", {"property": "og:image"}) else "N/A",
            "url": url,
        }
    except Exception as e:
        raise HTTPException(status_code=500, detail=f"Error parsing Shopify product: {str(e)}")
