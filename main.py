from fastapi import FastAPI, HTTPException
from pydantic import BaseModel

app = FastAPI(title="Todo API", version="1.0.0")


class Task(BaseModel):
    id: int | None = None
    title: str
    description: str
    completed: bool

tasks: list[Task] = []
task_id = 1

@app.get("/")
def root():
    return {"message": "Todo API"}

@app.get("/tasks", response_model=list[Task])
def get_tasks():
    return tasks

@app.post("/tasks", response_model=Task)
def create_task(task: Task):
    global task_id
    task.id = task_id
    tasks.append(task)
    task_id += 1
    return task

@app.put("/tasks/{id}", response_model=Task)
def update_task(id: int, updated_task: Task):
    for index, task in enumerate(tasks):
        if task.id == id:
            updated_task.id = id
            tasks[index] = updated_task
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
            return {"message": f"Task with id: {id} deleted"}
    raise HTTPException(
            status_code=404,
            detail="Task not found"
        )
