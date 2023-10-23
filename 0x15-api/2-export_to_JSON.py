#!/usr/bin/python3
""" doc """

import json
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
    emp_name = requests.get(url).json().get("username")
    fieldnames = ['task', 'completed', 'username']
    new_dict = {}
    list_dicts = []
    for task in resp:
        completed = task.get("completed")
        values = [task.get("title"), completed, emp_name]
        list_dicts.append(dict(zip(fieldnames, values)))
    new_dict.update({"{}".format(argv[1]): list_dicts})
    with open("{}.json".format(argv[1]), 'w') as fd:
        json.dump(new_dict, fd)
