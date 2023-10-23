#!/usr/bin/python3
""" doc """

import json
import requests

if __name__ == "__main__":
    url = "https://jsonplaceholder.typicode.com/todos"
    todos = requests.get(url).json()
    url = "https://jsonplaceholder.typicode.com/users"
    users = requests.get(url).json()
    ids_user = {}
    for user in users:
        ids_user.update({user.get("id"): user.get("username")})
    fieldnames = ['task', 'completed', 'username']
    new_dict = {}
    for task in todos:
        tmp_id = task.get("userId")
        list_dicts = new_dict.get(tmp_id)
        if list_dicts is None:
            list_dicts = []
        emp_name = ids_user.get(tmp_id)
        completed = task.get("completed")
        values = [task.get("title"), completed, emp_name]
        list_dicts.append(dict(zip(fieldnames, values)))
        new_dict.update({tmp_id: list_dicts})
    with open("todo_all_employees.json", 'w') as fd:
        json.dump(new_dict, fd)
