from fastapi import FastAPI
import uvicorn

app = FastAPI()

@app.get("/items/{item_id}")
def read_item(item_id: int):
    items = ["Laptop", "Phone", "Tablet"]
    
    if item_id < 0 or item_id >= len(items):
        return {"error": f"Item ID {item_id} not found. Valid IDs: 0-{len(items)-1}"}, 404
    
    item = items[item_id]
    
    return {"item": item}

uvicorn.run(app)
