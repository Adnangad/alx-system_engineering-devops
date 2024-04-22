#!/usr/bin/python3
"""Fetches data from url"""
import json
import requests
import sys


if __name__ == "__main__":
    userid = sys.argv[1]
    url = "https://jsonplaceholder.typicode.com/"
    user = requests.get(url + "users/{}".format(userid)).json()
    username = user.get("username")
    params = {"userId": user_id}
    tasks = requests.get(url + "todos", params).json()
    data = {
        userid: [
            {
                "task": task.get("title"),
                "completed": task.get("completed"),
                "username": username
            }
            for task in tasks
        ]
    }
    with open("{}.json".format(userid), "w") as f:
        json.dump(data, f)
