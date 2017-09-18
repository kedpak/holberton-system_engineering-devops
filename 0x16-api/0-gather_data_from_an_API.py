#!/usr/bin/python3
"""
Script utilizes REST API for employee ID, and list progres
"""

import requests
import sys
import json

if __name__ == '__main__':
    r_users = requests.get('https://jsonplaceholder.typicode.com/users/{}'
                           .format(sys.argv[1])).json()
    r_todos = requests.get('https://jsonplaceholder.typicode.com/todos')
    r_todos = r_todos.json()

    task_count = 0
    total_tasks = 0
    name = r_users['name']

    for i in r_todos:
        if i['userId'] is int(sys.argv[1]):
            total_tasks += 1
        if i['userId'] is int(sys.argv[1]) and i['completed'] is True:
            task_count += 1
    print("Employee {} is done with tasks({}/{}):"
          .format(name, task_count, total_tasks))
    for j in r_todos:
        if j['completed'] is True and j['userId'] is int(sys.argv[1]):
            print("\t{}".format(j.get("title")))
