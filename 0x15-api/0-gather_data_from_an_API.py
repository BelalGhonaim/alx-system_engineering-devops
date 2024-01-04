#!/usr/bin/python3
# Python script that, using this REST API, for a given employee ID
# returns information about his/her TODO list progress.
import requests
import sys

if __name__ == "__main__":
    url = "https://jsonplaceholder.typicode.com/"
    user_id = sys.argv[1]
    user = requests.get(url + "users/{}".format(user_id)).json()
    todo = requests.get(url + "todos", params={"userId": user_id}).json()
    
    done = []
    for todos in todo:
        if todos.get("done") is True:
            completed.append(todos.get("title"))
            print("Employee {} is done with tasks({}/{}):"
                                                .format(user.get("name"), (len(done), len(todo)
                  .format(user.get("name"),
                          len(completed), len(todo)))
            for task_title in completed:
                print("\t {}".format(task_title))
