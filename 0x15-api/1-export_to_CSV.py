#!/usr/bin/python3
"""Rest Apis"""

import csv
import requests
import sys


if __name__ == "__main__":
    userid = sys.argv[1]
    url = "https://jsonplaceholder.typicode.com/"
    user = requests.get(url + "users/{}".format(userid)).json()
    username = user.get("username")
    tasks = requests.get(url + "todos", params={"userId": userid}).json()
    with open("{}.csv".format(userid), "w", newline="") as f:
        writer = csv.writer(f, quoting=csv.QUOTE_ALL)
        [writer.writerow(
            [userid, username, task.get("completed"), task.get("title")]
         ) for task in tasks]
