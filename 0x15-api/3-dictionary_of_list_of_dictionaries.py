#!/usr/bin/python3
"""api plus json"""
import json
import requests


if __name__ == "__main__":
    url = "https://jsonplaceholder.typicode.com/"
    users = requests.get(url + "users").json()
    data = {}
    for user in users:
        userid = user["id"]
        userurl = url + f"todos?userId={userid}"
        tasks = requests.get(userurl).json()

        data[userid] = [
                {
                    "task": task.get("title"),
                    "completed": task.get("completed"),
                    "username": user.get("username")
                    } for task in tasks]
    with open("todo_all_employees.json", "w") as f:
        json.dump(data, f)
