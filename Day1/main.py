from fastapi import FastAPI, Request
from Day1.product_data import products

app = FastAPI()

@app.get("/")
def home():
    return "Welcome to the FastAPI application!"


@app.get("/contact")
def contact():
    return "Contact with me at: github.com/ar-sayeem"


@app.get("/products")
def get_products():
    return products


### Path Params...
@app.get("/product/{product_id}")
def get_product(product_id: int):
    for oneProduct in products:
        if oneProduct["id"] == product_id:
            return oneProduct

    return {"Error": "Product not found for this id."}


### Query Params...
@app.get("/greet")
def greet_user(request: Request):
    query_params = request.query_params
    return {
        "greet": f'Hello {query_params.get("name")}, Welcome to FastAPI Agent {query_params.get("id")}!'
    }
