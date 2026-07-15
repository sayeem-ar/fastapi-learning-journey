# HTTP Methods & CRUD Operations

A beginner-friendly guide to understanding HTTP methods, how clients communicate with servers, and how CRUD operations work.

---

# Table of Contents

1. What is HTTP?
2. Client-Server Architecture
3. What are HTTP Methods?
4. GET Method
5. POST Method
6. PUT Method
7. DELETE Method
8. CRUD Operations
9. Complete CRUD Example
10. HTTP Status Codes
11. Summary

---

# What is HTTP?

**HTTP (HyperText Transfer Protocol)** is the communication protocol used between a **client** and a **server** over the internet.

Whenever you:

- Open a website
- Submit a login form
- Watch a YouTube video
- Buy something online

your browser (client) communicates with a server using **HTTP Requests**.

---

# Client-Server Architecture

```
+---------+        HTTP Request        +---------+
| Client  | -------------------------> | Server  |
| Browser |                            | Backend |
+---------+                            +---------+
                                             |
                                             |
                                      Reads/Writes
                                             |
                                      +--------------+
                                      |   Database   |
                                      +--------------+
```

### Flow

1. Client sends a request.
2. Server receives it.
3. Server processes it.
4. Server communicates with the database if needed.
5. Server sends a response back.

---

# What are HTTP Methods?

HTTP methods tell the server **what action should be performed**.

The four most commonly used methods are:

| Method | Purpose |
|---------|----------|
| GET | Read data |
| POST | Create data |
| PUT | Update data |
| DELETE | Remove data |

Together, these represent the basic operations performed on data.

---

# GET Method

## Purpose

Used to **retrieve (fetch) data** from the server.

GET requests should **not modify** any data.

---

## Flow

```
Client
   |
GET /users
   |
Server
   |
Database
   |
Returns users
   |
Client
```

---

## Example

Request

```
GET /users
```

Server Response

```json
[
  {
    "id": 1,
    "name": "John"
  },
  {
    "id": 2,
    "name": "Alice"
  }
]
```

---

## JavaScript Example

```javascript
fetch("/users")
    .then(response => response.json())
    .then(data => console.log(data));
```

---

## Real-Life Example

Imagine opening Instagram.

The app asks the server:

> Give me today's posts.

That is a GET request.

---

# POST Method

## Purpose

Used to **send new data** to the server.

POST usually creates a new resource.

---

## Flow

```
Client
   |
POST /users
   |
Server
   |
Database
   |
Creates new user
   |
Returns success
```

---

## Example

Request

```http
POST /users
```

Body

```json
{
    "name": "Alice",
    "age": 22
}
```

Server Response

```json
{
    "id": 3,
    "name": "Alice",
    "age": 22
}
```

---

## JavaScript Example

```javascript
fetch("/users", {
    method: "POST",
    headers: {
        "Content-Type": "application/json"
    },
    body: JSON.stringify({
        name: "Alice",
        age: 22
    })
});
```

---

## Real-Life Example

When you create a new Facebook account.

Your information is sent to the server.

That is a POST request.

---

# PUT Method

## Purpose

Used to **update existing data**.

Usually requires the ID of the resource.

---

## Flow

```
Client
   |
PUT /users/3
   |
Server
   |
Database
   |
Updates record
   |
Returns updated user
```

---

## Example

Request

```http
PUT /users/3
```

Body

```json
{
    "name": "Alice Smith",
    "age": 23
}
```

Server Response

```json
{
    "id": 3,
    "name": "Alice Smith",
    "age": 23
}
```

---

## JavaScript Example

```javascript
fetch("/users/3", {
    method: "PUT",
    headers: {
        "Content-Type": "application/json"
    },
    body: JSON.stringify({
        name: "Alice Smith",
        age: 23
    })
});
```

---

## Real-Life Example

You edit your profile picture or change your username.

The updated information is sent using PUT.

---

# DELETE Method

## Purpose

Used to remove data from the server.

---

## Flow

```
Client
   |
DELETE /users/3
   |
Server
   |
Database
   |
Deletes user
   |
Returns success
```

---

## Example

Request

```http
DELETE /users/3
```

Server Response

```json
{
    "message": "User deleted successfully"
}
```

---

## JavaScript Example

```javascript
fetch("/users/3", {
    method: "DELETE"
});
```

---

## Real-Life Example

Deleting an email from Gmail.

The client tells the server:

Delete email #123.

---

# CRUD Operations

CRUD stands for the four basic operations performed on data.

| Letter | Meaning | HTTP Method |
|---------|----------|-------------|
| C | Create | POST |
| R | Read | GET |
| U | Update | PUT |
| D | Delete | DELETE |

---

## CRUD Diagram

```
          CRUD

    Create  ---> POST

    Read    ---> GET

    Update  ---> PUT

    Delete  ---> DELETE
```

---

# Complete CRUD Example

Suppose we have a website that manages students.

## Create a Student

```
POST /students
```

Body

```json
{
    "name": "Rahim",
    "age": 20
}
```

---

## Read All Students

```
GET /students
```

Response

```json
[
    {
        "id": 1,
        "name": "Rahim",
        "age": 20
    }
]
```

---

## Read One Student

```
GET /students/1
```

---

## Update Student

```
PUT /students/1
```

Body

```json
{
    "name": "Rahim Ahmed",
    "age": 21
}
```

---

## Delete Student

```
DELETE /students/1
```

---

# HTTP Status Codes

After every request, the server returns a status code.

| Code | Meaning |
|------|----------|
| 200 | OK |
| 201 | Created |
| 204 | No Content |
| 400 | Bad Request |
| 401 | Unauthorized |
| 403 | Forbidden |
| 404 | Not Found |
| 500 | Internal Server Error |

---

## Examples

### Successful GET

```
GET /users
```

Response

```
200 OK
```

---

### Successful POST

```
POST /users
```

Response

```
201 Created
```

---

### User Not Found

```
GET /users/100
```

Response

```
404 Not Found
```

---

### Server Error

```
500 Internal Server Error
```

Usually means something went wrong on the server.

---

# Summary

| HTTP Method | CRUD Operation | Description |
|-------------|----------------|-------------|
| GET | Read | Retrieve data from the server |
| POST | Create | Send new data to create a resource |
| PUT | Update | Modify an existing resource |
| DELETE | Delete | Remove a resource |

---

# Key Takeaways

- **HTTP** is the protocol used for communication between clients and servers.
- The **client** (browser, mobile app, etc.) sends requests.
- The **server** processes those requests and often interacts with a **database**.
- **GET** retrieves data.
- **POST** creates new data.
- **PUT** updates existing data.
- **DELETE** removes data.
- These four methods map directly to **CRUD** operations:
  - **Create → POST**
  - **Read → GET**
  - **Update → PUT**
  - **Delete → DELETE**
- Servers typically respond with appropriate **HTTP status codes** (such as `200`, `201`, `404`, or `500`) to indicate the outcome of each request.

---

# Quick Reference

| Method | Action | CRUD | Request Body? | Example Endpoint |
|---------|--------|------|---------------|------------------|
| GET | Retrieve data | Read | Usually No | `GET /users` |
| POST | Create new data | Create | Yes | `POST /users` |
| PUT | Update existing data | Update | Yes | `PUT /users/1` |
| DELETE | Remove data | Delete | No | `DELETE /users/1` |
