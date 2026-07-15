from pydantic import BaseModel

class ProductDTO(BaseModel):
    id: int
    title: str
    price: int = 0
    count: int = 0
    
# request body = client sends data to the server in the body of the request, typically in JSON format. This is commonly used for creating or updating resources on the server. In FastAPI, you can define a Pydantic model to validate and parse the incoming request body data.
# response body = server sends data back to the client in the body of the response, also typically in JSON format. This is used to return data from the server to the client after processing a request. In FastAPI, you can define a Pydantic model to structure and validate the response data.