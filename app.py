from fastapi import FastAPI, HTTPException
import uvicorn

app = FastAPI()

@app.get("/items/{item_id}")
def read_item(item_id: int):
    items = ["Laptop", "Phone", "Tablet"]
    
    if item_id < 0 or item_id >= len(items):
        raise HTTPException(
            status_code=404,
            detail=f"Item with id {item_id} not found. Valid IDs are 0-{len(items) - 1}."
        )
    
    item = items[item_id]
    
    return {"item": item}

uvicorn.run(app)
