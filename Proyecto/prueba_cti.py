import os
import csv
import requests
from datetime import datetime

class ApiService:
    BASE_URL = "https://jsonplaceholder.typicode.com/todos"

    @staticmethod
    def fetch_todos():
        response = requests.get(ApiService.BASE_URL)
        if response.status_code == 200:
            return response.json()
        else:
            raise Exception(f"Failed to fetch TODOs. Status Code: {response.status_code}")

def save_todo_as_csv(todo):
    current_date = datetime.now().strftime("%Y_%m_%d")
    filename = f"{current_date}_{todo['id']}.csv"

    with open(os.path.join("storage", filename), mode="w", newline="") as csvfile:
        fieldnames = ["userId", "id", "title", "completed"]
        writer = csv.DictWriter(csvfile, fieldnames=fieldnames)

        writer.writeheader()
        writer.writerow(todo)

def fetch_and_save_todos():
    api_service = ApiService()
    todos = api_service.fetch_todos()

    if not os.path.exists("storage"):
        os.makedirs("storage")

    for todo in todos:
        save_todo_as_csv(todo)

if __name__ == "__main__":
    fetch_and_save_todos()