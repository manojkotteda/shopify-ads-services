# models.py
from pydantic import BaseModel, HttpUrl

class Product(BaseModel):
    title: str
    price: str
    currency: str
    description: str
    image: str
    url: HttpUrl

class SaveProductRequest(BaseModel):
    user_id: str
    url: HttpUrl
    image: str

class AdRequest(BaseModel):
    platform: str
    product: Product
