from fastapi import APIRouter, HTTPException, status

from app.core.supabase import supabase_client
from app.schemas.product import Product

router = APIRouter(prefix="/products", tags=["products"])


@router.post(
    "",
    response_model=Product,
    status_code=status.HTTP_201_CREATED,
)
def create_product(product: Product) -> Product:
    """Create a new product in Supabase."""
    # Use JSON mode so fields like HttpUrl become plain strings
    data = product.model_dump(mode="json")

    response = (
        supabase_client.table("products")
        .insert(data)
        .execute()
    )

    if not response.data:
        raise HTTPException(
            status_code=status.HTTP_500_INTERNAL_SERVER_ERROR,
            detail="Failed to create product",
        )

    # Supabase returns a list of inserted rows
    created = response.data[0]
    return Product(**created)


__all__ = ["router"]
