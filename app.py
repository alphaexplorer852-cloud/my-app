from fastapi import FastAPI
import uvicorn

app = FastAPI()

@app.get("/items/{item_id}")
def read_item(item_id: int):
    items = ["Laptop", "Phone", "Tablet"]
    
    # BUG: This will cause an "IndexError: list index out of range" 
    # if you request an ID of 3 or higher, resulting in a 
    # 500 Internal Server Error.
    item = items[item_id]
    
    return {"item": item}

uvicorn.run(app)

