from fastapi import FastAPI, HTTPException
from pydantic import BaseModel
from typing import List, Optional

app = FastAPI(title="Item Management API", description="A simple REST API for managing items")

# Pydantic model for Item
class Item(BaseModel):
    id: int
    name: str
    description: Optional[str] = None
    price: float
    in_stock: bool = True

# In-memory storage (in a real app, you'd use a database)
items_db = []
next_id = 1

@app.get("/")
async def root():
    return {"message": "Welcome to the Item Management API"}

# TODO: Implement the following endpoints:
# - GET /items - Return all items
# - GET /items/{item_id} - Return a specific item
# - POST /items - Create a new item
# - PUT /items/{item_id} - Update an existing item
# - DELETE /items/{item_id} - Delete an item

# Example starter endpoint
@app.get("/items", response_model=List[Item])
async def get_items():
    # Return all items from items_db
    pass

# Add more endpoints here...