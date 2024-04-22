#!/usr/bin/python3
"""This module fetches some data from url"""
import requests
import sys
import csv


if __name__ == "__main__":
    url = f'https://jsonplaceholder.typicode.com/'
    resp = requests.get(url + f"users/{sys.argv[1]}")
    user = resp.json()
    name = user.get("name")
    params = {"userId": sys.argv[1]}
    tasks = requests.get(url + "todos", params=params)
    taskz = tasks.json()
    with open(f"{sys.argv[1]}.csv", "w", newline='') as f:
        writer = csv.writer(f, quoting=csv.QUOTE_ALL)
        for task in taskz:
            writer.writerow([
                sys.argv[1], name, task.get('completed'), task.get('title')])
