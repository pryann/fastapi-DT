from typing import List
from fastapi import FastAPI, HTTPException, status
from pydantic import BaseModel

app = FastAPI()


class BaseItem(BaseModel):
    name: str
    description: str


class Item(BaseItem):
    id: int
    user_id: int


class UpdateItem(BaseItem):
    pass


class User(BaseModel):
    id: int
    username: str
    email: str
    items: List[Item] = []


users = [
    User(id=1, username="user1", email="user1@domain.com"),
    User(id=2, username="user2", email="user2@domain.com"),
]

items = [
    Item(id=1, name="laptop", description="laptop description", user_id=1),
    Item(id=2, name="phone", description="phone description", user_id=1),
    Item(id=3, name="tablet", description="tablet description", user_id=2),
    Item(id=4, name="monitor", description="monitor description", user_id=2),
]


@app.get("/users/{user_id}/items")
async def fetch_user_items(user_id: int):
    return [item for item in items if item.user_id == user_id]


@app.get("/users/{user_id}/items/{item_id}")
async def get_user_item(user_id: int, item_id: int):
    for item in items:
        if item.id == item_id and item.user_id == user_id:
            return item
    raise HTTPException(status_code=404, detail="Item not found")


@app.post("/users/{user_id}/items", status_code=status.HTTP_201_CREATED)
async def create_user_item(user_id: int, item: Item):
    user = [user_db for user_db in users if user_db.id == user_id]
    item_from_list = [db_item for db_item in items if db_item.id == item.id]
    if not user:
        raise HTTPException(status_code=404, detail="User not found")
    if item_from_list:
        raise HTTPException(status_code=400, detail="Item already exists")
    items.append(item)
    return item


@app.put("/users/{user_id}/items/{item_id}")
async def update_user_item(user_id: int, item_id: int, item: UpdateItem):
    for db_item in items:
        if db_item.id == item_id and db_item.user_id == user_id:
            db_item.name = item.name
            db_item.description = item.description
            return db_item
    raise HTTPException(status_code=404, detail="Item not found")


@app.delete("/users/{user_id}/items/{item_id}", status_code=status.HTTP_204_NO_CONTENT)
async def delete_user_item(user_id: int, item_id: int):
    for db_item in items:
        if db_item.id == item_id and db_item.user_id == user_id:
            items.remove(db_item)
            return
    raise HTTPException(status_code=404, detail="Item not found")
