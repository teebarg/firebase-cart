from pydantic import BaseModel
from typing import List, Optional, Dict, Any

class CartItem(BaseModel):
    item_id: str
    product_id: str
    name: str
    description: str | None
    slug: str
    image: str | None
    quantity: int
    price: int

class Cart(BaseModel):
    cart_id: str
    customer_id: str | None
    email: str | None
    items: List[CartItem]
    shipping_address: dict
    billing_address: dict
    subtotal: int
    tax_total: int
    shipping_total: int
    total: int

class FirebaseConfig(BaseModel):
    credentials: Dict[str, Any]
    database_url: Optional[str] = None