#!/usr/bin/python3
"""This module fetches some data from url"""
import requests
import sys


if __name__ == "__main__":
    url = f'https://jsonplaceholder.typicode.com/'
    resp = requests.get(url + f"users/{sys.argv[1]}")
    user = resp.json()
    name = user.get("name")
    params = {"userId": sys.argv[1]}
    tasks = requests.get(url + "todos", params=params)
    taskz = tasks.json()
    completed_tasks = [
            task.get("title") for task in taskz if task['completed']]
    num_comp = len(completed_tasks)
    num_tasks = len(taskz)
    print(f'Employee {name} is done with tasks({num_comp}/{num_tasks})')
    for task in completed_tasks:
        print(f"\t{task}")
