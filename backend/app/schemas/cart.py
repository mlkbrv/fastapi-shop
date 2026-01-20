from pydantic import BaseModel, Field
from typing import Optional

class CartItemBase(BaseModel):
    product_id: int = Field(..., description="The product id of the cart.")
    quantity: int = Field(..., gt=0, description="The quantity of the cart.")

class CartItemCreate(CartItemBase):
    pass

class CartItemUpdate(BaseModel):
    product_id: int = Field(..., description="The product id of the cart.")
    quantity: int = Field(..., gt=0, description="The quantity of the cart.")

class CartItem(BaseModel):
    product_id: int
    name: str = Field(..., description="Product name.")
    price: float = Field(..., gt=0, description="Price of the product.")
    quantity: int = Field(..., gt=0, description="Quantity of the product.")
    subtotal: float = Field(..., gt=0, description="Subtotal of the product.")
    image_url: Optional[str] = Field(..., description="Image url of the product.")

class CartResponse(BaseModel):
    items: list[CartItemBase] = Field(..., description="List of cart items.")
    total: float = Field(..., gt=0, description="Total value of the cart.")
    items_count: int = Field(..., gt=0, description="Total number of items in the cart.")