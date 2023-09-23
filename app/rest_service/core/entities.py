from datetime import datetime

from pydantic import BaseModel

class CatToy(BaseModel):
    """
    Represents a cat toy entity.
    """
    name: str
    description: str
    price: float

class CatToyPurchase(BaseModel):
    """
    Represents a cat toy purchase entity.
    """
    cat_toy_id: int
    customer_id: int
    quantity: int
    purchase_date: datetime.datetime  # You might need to import datetime