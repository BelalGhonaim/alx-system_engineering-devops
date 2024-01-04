#!/usr/bin/python3
"""Python script to export all list data in the JSON format"""
import json
import requests

if __name__ == "__main__":
    url = "https://jsonplaceholder.typicode.com/"
    users = requests.get(url + "users").json()
    json_info = {}

    for user in users:
        user_id = user.get("id")
        username = user.get("username")
        todos = requests.get(url + "todos", params={"userId": user_id}).json()
        json_info[user_id] = [
            {
                "task": todo.get("title"),
                "completed": todo.get("completed"),
                "username": username
            }
            for todo in todos
        ]

    with open("todo_all_employees.json", "w") as jsonfile:
        json.dump(json_info, jsonfile, indent=2)