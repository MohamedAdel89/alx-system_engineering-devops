#!/usr/bin/python3
""" doc """

import requests
from sys import argv

if __name__ == "__main__" and len(argv) == 2:
    url = "https://jsonplaceholder.typicode.com/todos"
    try:
        int(argv[1])
    except ValueError as e:
        exit
    data = {"userId": argv[1]}
    resp = requests.get(url, params=data).json()
    url = "https://jsonplaceholder.typicode.com/users/{}".format(argv[1])
    emp_name = requests.get(url).json().get("name")
    completed_tasks = []
    for task in resp:
        if task.get("completed") is True:
            completed_tasks.append(task.get("title"))
    if (emp_name) is not None:
        print("Employee {} is done with tasks({}/{}):".format(
            emp_name, len(completed_tasks), len(resp)))
        for title in completed_tasks:
            print("\t {}".format(title))
