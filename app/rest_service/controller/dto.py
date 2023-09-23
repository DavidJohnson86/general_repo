from pydantic import BaseModel


class CatToyDTO(BaseModel):
    name: str
    description: str
    price: float

