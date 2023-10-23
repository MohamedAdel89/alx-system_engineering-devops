#!/usr/bin/python3
""" doc """

import csv
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
    with open("{}.csv".format(argv[1]), 'w') as fd:
        fieldnames = ['id', 'name', 'status', 'title']
        writer = csv.DictWriter(fd, fieldnames=fieldnames,
                                quoting=csv.QUOTE_ALL)
        for task in resp:
            completed = task.get("completed")
            writer.writerow({'id': '{}'.format(argv[1]),
                             'name': '{}'.format(emp_name),
                             'status': '{}'.format(str(completed)),
                             'title': '{}'.format(task.get("title"))})
