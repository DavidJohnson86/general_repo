from fastapi import FastAPI
from controller.dto import CatToyDTO
app = FastAPI()
from application.use_cases import CatToyService

def init_cat_toy_service():
    db_repository = None
    return CatToyService(db_repository=)

@app.get("/")
async def read_root() -> dict[str, str]:
    return {"message": "Welcome to the Tuxedo Cat Toy shop"}


@app.post("/cat-toys/")
async def create_cat_toy(toy: CatToyDTO):
    create_cat_toy = CatToyService()
    # Assuming you have some data store (e.g., a database) to store the cat toy
    # Here, we'll just return the created cat toy as an example
    return toy


@app.get("/cat-toys/")
async def get_cat_toys():
    # Retrieve and return a list of all cat toys from your data store
    # For example, you might query a database and return the results
    # Here, we'll return a list of dummy cat toys as an example
    cat_toys = [
        {"name": "Feather Wand", "description": "Interactive feather toy",
         "price": 9.99},
        {"name": "Catnip Mice", "description": "Set of 3 catnip-infused mice",
         "price": 5.99},
        # Add more cat toys as needed
    ]
    return cat_toys


@app.put("/cat-toys/{toy_id}")
async def update_cat_toy(toy_id: int, updated_toy: CatToyDTO):
    # Update the cat toy with the given toy_id in your data store
    # For example, you might update a database record using the toy_id
    # Here, we'll return the updated cat toy as an example
    updated_toy_data = updated_toy.dict()
    return updated_toy_data


@app.delete("/cat-toys/{toy_id}")
async def delete_cat_toy(toy_id: int):
    # Delete the cat toy with the given toy_id from your data store
    # For example, you might delete a database record using the toy_id
    # Here, we'll return a message as an example
    return {"message": f"Cat toy with ID {toy_id} has been deleted."}
