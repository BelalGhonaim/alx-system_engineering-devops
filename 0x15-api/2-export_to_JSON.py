#!/usr/bin/python3
""" Script to export data in the CSV format"""
import requests
import sys
import json

if __name__ == "__main__":
    url = "https://jsonplaceholder.typicode.com/"
    user_id = sys.argv[1]
    user = requests.get(url + "users/{}".format(user_id)).json()
    username = user.get("username")
    todos = requests.get(url + "todos", params={"userId": user_id}).json()
    json_info = {
        user_id: [
            {
                "task": todo.get("title"),
                "completed": todo.get("completed"),
                "username": username
            }
            for todo in todos
        ]
    }

    with open("{}.json".format(user_id), "w") as jsonfile:
        json.dump(json_info, jsonfile, indent=2)
