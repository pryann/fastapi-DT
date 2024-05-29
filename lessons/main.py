from fastapi import FastAPI, HTTPException
from pydantic import BaseModel

app = FastAPI()


class Item(BaseModel):
    id: int | None = None
    name: str
    quantity: int


items: list[Item] = [
    Item(id=1, name="laptop", quantity=3),
    Item(id=2, name="phone", quantity=2),
    Item(id=3, name="tablet", quantity=8),
    Item(id=4, name="monitor", quantity=12),
]


@app.get("/")
def home():
    return "Hello World"


@app.get("/about")
def home():
    return {"message": "About"}


# query params
# http://127.0.0.1:8000/items?skip=2&limit=2
# R = read All
@app.get("/items")
def get_items(skip: int = 0, limit: int = 10):
    return items[skip : skip + limit]


# R = read One
@app.get("/items/{item_id}")
def get_items(item_id: int):
    for item in items:
        if item.id == item_id:
            return item
    raise HTTPException(status_code=404, detail="Item not found")


# C = Create
@app.post("/items")
def create_item(item: Item):
    if not item.id:
        # if last item id is the greatest
        # item.id = items[-1].id + 1
        # if not ordered by id
        item.id = max((item.id for item in items), default=0) + 1
    items.append(item)
    return item


# U = Update
@app.put("/items/{item_id}")
def update_item(item_id: int, item: Item):
    for index, list_item in enumerate(items):
        if list_item.id == item_id:
            list_item_dict = list_item.model_dump()
            list_item_dict.update(item.model_dump(exclude_unset=True))
            items[index] = Item(**list_item_dict)
            return items[index]
    raise HTTPException(status_code=404, detail="Item not found")


# D = Delete
@app.delete("/items/{item_id}")
def delete_item(item_id: int):
    for index, item in enumerate(items):
        if item.id == item_id:
            del items[index]
            return
    raise HTTPException(status_code=404, detail="Item not found")
