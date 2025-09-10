from fastapi import FastAPI, HTTPException
from pydantic import BaseModel
from typing import List

app = FastAPI(title="Todo API", version="1.0.0")


class Task(BaseModel):
    id: int
    title: str
    description: str
    completed: bool

tasks: List[Task] = []

@app.get("/")
def root():
    return {"message": "Todo API"}

@app.get("/tasks", response_model=List[Task])
def get_tasks():
    return tasks

@app.post("/tasks", response_model=Task)
def create_task(task: Task):
    for task in tasks:
        if task.id == task.id:
            raise HTTPException(
                status_code=400,
                detail="Task already exists"
            )
    tasks.append(task)
    return task

@app.put("/tasks/{id}", response_model=Task)
def update_task(id: int, updated_task: Task):
    for index, task in enumerate(tasks):
        if task.id == id:
            task[index] = updated_task
            return updated_task
        raise HTTPException(
            status_code=404,
            detail="Task not found"
        )
@app.delete("/tasks/{id}")
def delete_task(id:int):
    for index, task in enumerate(tasks):
        if task.id == id:
            tasks.pop(index)
            return {"message": f"Task {id} deleted"}
    raise HTTPException(
            status_code=404,
            detail="Task not found"
        )
