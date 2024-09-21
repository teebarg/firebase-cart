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
    shipping_method: dict
    shipping_address: dict
    billing_address: dict
    subtotal: int
    tax_total: int
    delivery_fee: int
    total: int
    payment_session: dict


class FirebaseConfig(BaseModel):
    credentials: Dict[str, Any]
    database_url: Optional[str] = None


class Order(BaseModel):
    order_id: str
    status: str
    fulfillment_status: Optional[str] = None
    cart_id: str
    customer_id: Optional[str] = ""
    email: Optional[str] = ""
    line_items: List[CartItem]
    shipping_method: dict
    shipping_address: dict
    billing_address: dict
    subtotal: int
    tax_total: int
    delivery_fee: int
    total: int
    payment_session: dict
    fulfillments: Optional[list[dict]] = []
    payment_status: Optional[str] = ""
