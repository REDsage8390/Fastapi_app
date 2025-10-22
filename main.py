

from fastapi import FastAPI
from models import Product  

app=FastAPI()
@app.get("/")

def read_root():
    return {"message": "Hello,FastAPI!"}

products = [
    Product(id=1, name="phone",description="A smartphone",price=699.99,float=50),
    Product(id=2, name="laptop",description="A machine",price=60999.99,float=50),
    Product(id=3, name="tablet",description="A small computer",price=399.99,float=50),
]

@app.get("/products")
def get_products():
    return products