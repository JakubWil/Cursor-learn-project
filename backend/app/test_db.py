from app.core.supabase import supabase_client
from app.schemas.product import Product


def main() -> None:
    test_product = Product(
        id=999_999,
        name="Test product from script",
        price=1.23,
        url="https://example.com/test-product",
    )

    data = test_product.model_dump()

    try:
        response = (
            supabase_client.table("products")
            .insert(data)
            .execute()
        )
        print("Insert succeeded:", response.data)
    except Exception as exc:  # noqa: BLE001
        print("Insert failed:", repr(exc))


if __name__ == "__main__":
    main()

