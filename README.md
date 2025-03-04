# Shopify Product Scraper & Ad API

## 🚀 Overview
This FastAPI-based service extracts product details from Shopify stores and allows users to create ad campaigns using platforms like Meta or Google Ads. It supports fetching product information via Shopify's JSON API and integrates with an ad management system.

---

## 📦 Setup

### **1️⃣ Clone the Repository**
```bash
git clone https://github.com/yourusername/shopify-ad-api.git
cd shopify-ad-api
```

### **2️⃣ Install Dependencies**
```bash
pip install -r requirements.txt
```

### **3️⃣ Run the FastAPI Server**
```bash
uvicorn main:app --reload
```
- The API will be available at: `http://127.0.0.1:8000`
- Interactive API docs: `http://127.0.0.1:8000/docs`

---

## 📌 API Documentation

### **1️⃣ Extract Shopify Product Data**
**Endpoint:** `GET /api/v1/products`

#### **Request:**
```bash
curl -X GET "http://127.0.0.1:8000/api/v1/products?url=https://birdrockbaby.com"
```

#### **Response:**
```json
[
  {
    "title": "Seaside Diaper Bag",
    "description": "The Seaside Diaper Bag is a perfect companion for every mom on-the-go...",
    "price": "99.00",
    "currency": "USD",
    "image": "https://cdn.shopify.com/s/files/1/1298/6385/files/Brow-1.jpg?v=1715888613",
    "vendor": "BirdRock Baby",
    "url": "https://birdrockbaby.com/products/seaside-diaper-bag"
  }
]
```

### **2️⃣ Save a Product for Later Processing**
**Endpoint:** `POST /api/v1/save-product`

#### **Request:**
```bash
curl -X POST "http://127.0.0.1:8000/api/v1/save-product" -H "Content-Type: application/json" -d '{
  "user_id": "user123",
  "url": "https://birdrockbaby.com/products/seaside-diaper-bag",
  "image": "https://cdn.shopify.com/s/files/1/1298/6385/files/Brow-1.jpg?v=1715888613"
}'
```

#### **Response:**
```json
{
  "status": "success",
  "message": "Product saved successfully",
  "product_id": "123e4567-e89b-12d3-a456-426614174000"
}
```

### **3️⃣ Retrieve Saved Products**
**Endpoint:** `GET /api/v1/get-products/{user_id}`

#### **Request:**
```bash
curl -X GET "http://127.0.0.1:8000/api/v1/get-products/user123"
```

#### **Response:**
```json
{
  "user_id": "user123",
  "products": [
    {
      "url": "https://birdrockbaby.com/products/seaside-diaper-bag",
      "image": "https://cdn.shopify.com/s/files/1/1298/6385/files/Brow-1.jpg?v=1715888613"
    }
  ]
}
```

### **4️⃣ Create an Ad Campaign**
**Endpoint:** `POST /api/v1/create-ad`

#### **Request:**
```bash
curl -X POST "http://127.0.0.1:8000/api/v1/create-ad" -H "Content-Type: application/json" -d '{
  "platform": "Meta",
  "budget": 50.0,
  "target_audience": "Parents, Age 25-40, US",
  "product": {
    "title": "Seaside Diaper Bag",
    "price": "99.00",
    "currency": "USD",
    "description": "A stylish and functional diaper bag for parents.",
    "image": "https://cdn.shopify.com/s/files/1/1298/6385/files/Brow-1.jpg?v=1715888613",
    "url": "https://birdrockbaby.com/products/seaside-diaper-bag"
  }
}'
```

#### **Response:**
```json
{
  "status": "success",
  "ad_id": "123e4567-e89b-12d3-a456-426614174000",
  "message": "Ad campaign created successfully."
}
```

### **5️⃣ Retrieve an Ad Campaign**
**Endpoint:** `GET /api/v1/ads/{ad_id}`

#### **Request:**
```bash
curl -X GET "http://127.0.0.1:8000/api/v1/ads/123e4567-e89b-12d3-a456-426614174000"
```

#### **Response:**
```json
{
  "ad_id": "123e4567-e89b-12d3-a456-426614174000",
  "platform": "Meta",
  "product": {
    "title": "Seaside Diaper Bag",
    "price": "99.00",
    "currency": "USD",
    "description": "A stylish and functional diaper bag for parents.",
    "image": "https://cdn.shopify.com/s/files/1/1298/6385/files/Brow-1.jpg?v=1715888613",
    "url": "https://birdrockbaby.com/products/seaside-diaper-bag"
  },
  "budget": 50.0,
  "target_audience": "Parents, Age 25-40, US",
  "status": "pending"
}
```

---

## 🛠 Features
- ✅ **Extracts product details from Shopify JSON API**
- ✅ **Formats clean product descriptions**
- ✅ **Stores and retrieves saved products for users**
- ✅ **Supports multiple ad platforms (Meta, Google Ads)**
- ✅ **Stores ad campaigns in memory (Database integration planned)**

---

## 🔮 Future Enhancements
- [ ] **OAuth authentication** for Meta & Google Ads API integration.
- [ ] **Database storage** for ads instead of in-memory storage.
- [ ] **Support for multiple Shopify stores dynamically.**

---

## 📜 License
This project is open-source under the [MIT License](LICENSE). Feel free to contribute! 🎉

