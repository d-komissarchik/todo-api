# Todo API

This is a simple **Todo API** built with **FastAPI**.  
It provides basic CRUD operations to manage tasks: create, read, update, and delete.  
All data is stored in memory (a Python list), so it will reset every time the server restarts.

---

## Requirements
- Python 3.10+
- FastAPI
- Uvicorn
- Pydantic

---

## Features
- Create a new task
- Get all tasks
- Update an existing task
- Delete a task
- Built-in unit tests

---

## API Endpoints

- **GET /tasks** — get all tasks
- **POST /tasks** — create a new task  
  Example request body:
  ```json
  {
    "title": "Buy milk",
    "description": "Remember after work",
    "completed": false
  }
  ```
- **PUT /tasks/{id}** — update a task by id
- **DELETE /tasks/{id}** — delete a task by id

---

## Installation and Running
1. Clone the repository
```
git clone https://github.com/username/todo-api.git
cd todo-api
```
2. Install dependencies
```
pip install -r requirements.txt
```
3. Run the server
```
uvicorn main:app --reload
```

The API will be available at:
http://127.0.0.1:8000/docs


## Running Tests

Tests are located in test_api.py.

---