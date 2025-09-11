import unittest
from fastapi.testclient import TestClient
from main import app

client = TestClient(app)

class TestTodoAPI(unittest.TestCase):

    def test_create_task(self):
        response = client.post("/tasks", json={
            "title": "Task 1",
            "description": "Desc 1",
            "completed": False
        })
        self.assertEqual(response.status_code, 200)
        data = response.json()
        self.assertEqual(data["title"], "Task 1")
        self.assertFalse(data["completed"])

    def test_get_tasks(self):
        client.post("/tasks", json={
            "title": "Task for get",
            "description": "Desc",
            "completed": False
        })
        response = client.get("/tasks")
        self.assertEqual(response.status_code, 200)
        data = response.json()
        self.assertIsInstance(data, list)
        self.assertGreaterEqual(len(data), 1)

    def test_update_task(self):
        task_response = client.post("/tasks", json={
            "title": "Task to update",
            "description": "Desc",
            "completed": False
        })
        task_id = task_response.json()["id"]

        response = client.put(f"/tasks/{task_id}", json={
            "title": "Updated Task",
            "description": "Updated Desc",
            "completed": True
        })
        self.assertEqual(response.status_code, 200)
        data = response.json()
        self.assertEqual(data["title"], "Updated Task")
        self.assertEqual(data["description"], "Updated Desc")
        self.assertTrue(data["completed"])

    def test_update_task_not_found(self):
        response = client.put("/tasks/111", json={
            "title": "Ghost Task",
            "description": "Does not exist",
            "completed": False
        })
        self.assertEqual(response.status_code, 404)
        data = response.json()
        self.assertEqual(data["detail"], "Task not found")

    def test_delete_task(self):
        task_response = client.post("/tasks", json={
            "title": "Task to delete",
            "description": "Desc",
            "completed": False
        })
        task_id = task_response.json()["id"]

        response = client.delete(f"/tasks/{task_id}")
        self.assertEqual(response.status_code, 200)
        data = response.json()
        self.assertIn("Task with id", data["message"])


        response = client.delete(f"/tasks/{task_id}")
        self.assertEqual(response.status_code, 404)
        data = response.json()
        self.assertEqual(data["detail"], "Task not found")

    def test_delete_task_not_found(self):
        response = client.delete("/tasks/123")
        self.assertEqual(response.status_code, 404)
        data = response.json()
        self.assertEqual(data["detail"], "Task not found")


if __name__ == "__main__":
    unittest.main()