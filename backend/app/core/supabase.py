from functools import lru_cache

from supabase import Client, create_client

from app.core.config import settings


@lru_cache
def get_supabase_client() -> Client:
    """Return a singleton Supabase client instance."""
    return create_client(settings.SUPABASE_URL, settings.SUPABASE_KEY)


supabase_client = get_supabase_client()


__all__ = ["get_supabase_client", "supabase_client"]
