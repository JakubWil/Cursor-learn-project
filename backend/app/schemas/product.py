from pydantic import BaseModel, HttpUrl


class Product(BaseModel):
    id: int
    name: str
    price: float
    url: str


__all__ = ["Product"]
