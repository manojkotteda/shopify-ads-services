# database.py
import uuid
from typing import Dict

# In-memory storage for products
in_memory_db: Dict[str, Dict[str, dict]] = {}

def save_product(user_id: str, url: str, image: str) -> str:
    """Saves product data in memory and returns a unique product ID."""
    product_id = str(uuid.uuid4())
    if user_id not in in_memory_db:
        in_memory_db[user_id] = {}
    
    in_memory_db[user_id][product_id] = {"url": url, "image": image}
    return product_id

def get_products(user_id: str) -> dict:
    """Retrieves all saved products for a given user ID."""
    return in_memory_db.get(user_id, {})
