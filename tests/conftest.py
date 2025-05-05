import pytest
from app.main import items  # ou ton stockage réel

@pytest.fixture(autouse=True)
def reset_items():
    items.clear()
