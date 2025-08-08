# Flask User Management using REST API

A simple RESTful API built with **Flask** to manage user data using **in-memory storage** (Python dictionary). This project demonstrates how to perform basic CRUD operations (Create, Read, Update, Delete).

---

## 📦 Features

- `GET /users` – Retrieve all users
- `GET /users/<id>` – Retrieve a single user by ID
- `POST /users` – Create a new user
- `PUT /users/<id>` – Update an existing user
- `DELETE /users/<id>` – Delete a user
- `GET /` – Welcome route

---

## 🛠 Tech Stack

- Python 3
- Flask
- Postman or cURL (for testing)

---
DOWNLOAD FLASK MODULE

-> pip install Flask

📬 API Endpoints
🔹 Home
GET /
Returns welcome message

🔹 Get All Users
GET /users

{
  "1": {
    "name": "Alice",
    "email": "alice@example.com"
  },
  "2": {
    "name": "Bob",
    "email": "bob@email.com"
  }
}

Get a User by ID
GET /users/<user_id>

Example:
GET /users/1

Create a New User
POST /users

Body (raw → JSON):
{
  "name": "Charlie",
  "email": "charlie@example.com"
}

 Update an Existing User
PUT /users/<user_id>

Example:
PUT /users/1
{
  "name": "Alice Smith"
}

Delete a User
DELETE /users/<user_id>

Example:
DELETE /users/2

👉 Testing with Postman
1. Open Postman

2. Choose the method (GET, POST, PUT, DELETE)

3. Set the URL or /users/<id>

4. For POST and PUT, go to:
    4.1 Body → raw → JSON
    4.2 Enter JSON data




