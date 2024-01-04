#!/usr/bin/python3
""" Script to export data in the CSV format"""
import csv
import requests
import sys

if __name__ == "__main__":
    url = "https://jsonplaceholder.typicode.com/"
    user_id = sys.argv[1]
    user = requests.get(url + "users/{}".format(user_id)).json()
    username = user.get("username")
    todos = requests.get(url + "todos", params={"userId": user_id}).json()
    with open("{}.json".format(user_id), "w") as jsonfile:
        jsonfile.write("[")
        for todo in todos:
            jsonfile.write("{")
            jsonfile.write('"task": "{}", '.format(todo.get("title")))
            jsonfile.write('"completed": {}, '.format(todo.get("completed")))
            jsonfile.write('"username": "{}"'.format(username))
            jsonfile.write("}")
            if todo != todos[-1]:
                jsonfile.write(", ")
        jsonfile.write("]")