#!/usr/bin/python3
"""This module fetches some data from url"""
import json
import requests
import sys

if __name__ == "__main__":
    url = f'https://jsonplaceholder.typicode.com/'
    userid = sys.argv[1]
    resp = requests.get(url + f"users/{sys.argv[1]}")
    user = resp.json()
    params = {"userId": userid}
    taskz_resp = requests.get(url + "todos", params=params)
    taskz = taskz_resp.json()
    
    # The error is in the following line
    dat = {userid: [{"task": task.get("title"),
                     "completed": task.get("completed"),
                     "username": user.get("name")}
                    for task in taskz]}
    
    with open(f"{userid}.json", "w") as f:
        json.dump(dat, f)
