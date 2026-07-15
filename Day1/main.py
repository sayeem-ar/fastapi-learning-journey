from fastapi import FastAPI, Request
from dtos import ProductDTO
from product_data import products

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
@app.get("/products/{product_id}")
def get_product(product_id: int):
    for oneProduct in products:
        if oneProduct["id"] == product_id:
            return oneProduct

    return {"error": "Product not found for this id."}


### Query Params...
@app.get("/greet")
def greet_user(request: Request):
    query_params = request.query_params
    return {
        "greet": f'Hello {query_params.get("name")}, Welcome to FastAPI Agent {query_params.get("id")}!'
    }


### body, headers - request header, query params    



### different types of HTTP Methods.

@app.post("/create_product")
def create_product(product_data: ProductDTO):
    new_product = product_data.model_dump()
    products.append(new_product)
    return {"status": "Product Created Successfully...", "product": product_data}

### pydantic model for data validation.


@app.put("/update_product/{product_id}")
def update_product(product_data: ProductDTO, product_id: int):
    
    for index, oneProduct in enumerate(products):
        if oneProduct.get("id") == product_id:
            products[index] = product_data.model_dump()
            return {"status": "Product Updated Successfully...", "product": product_data}

    return {"error": "Product not found for this ID..."}



@app.delete("/delete_product/{product_id}")
def delete_product(product_id: int):
    for index, oneProduct in enumerate(products):
        if oneProduct.get("id") == product_id:
            deleted_product = products.pop(index)
            return {"status": "Product Deleted Successfully...", "products":deleted_product}

        return {"error": "Product not found for this ID..."}



### How to validate data DTOS.

### How to call different HTTP Methods. Any Tools?


