#!/usr/bin/python3
"""This module fetches some data from url"""
import requests
import sys
import json


if __name__ == "__main__":
    url = f'https://jsonplaceholder.typicode.com/'
    userid = sys.argv[1]
    resp = requests.get(url + f"users/{sys.argv[1]}")
    user = resp.json()
    params = {"userId": userid}
    taskz = requests.get(url + "todos", params=params).json()
    dat = {userid: []}
    for task in taskz:
        tk = {
                "task": task.get("title"),
                "completed": task.get("completed"),
                "username": user.get("name")}
        dat[userid].append(tk)
    with open(f"{userid}.json", "w") as f:
        json.dump(dat, f)
