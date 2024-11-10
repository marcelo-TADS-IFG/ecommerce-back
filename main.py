from fastapi import FastAPI
from app.controllers.product_controller import router as product_router
from app.controllers.category_controller import router as category_router
from app.controllers.subcategory_controller import router as subcategory_router
from app.connection.database import Base, database

import uvicorn

app = FastAPI()
app.include_router(product_router)
app.include_router(category_router)
app.include_router(subcategory_router)
Base.metadata.create_all(bind=database.engine)

@app.get("/")
def produtos():
    return {"produtos" : "todos"}

#@app.get("/")

def read_root():

    return {"Hello": "World"}
def main():

    uvicorn.run("main:app", host="127.0.0.1", port=8000, reload=True)

if __name__ == "__main__":

    main()