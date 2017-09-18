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
    task_title = []
    name = r_users['name']

    if len(sys.argv) > 1:
        try:
            for i in r_todos:
                if i['userId'] is int(sys.argv[1]):
                    total_tasks += 1
                if i['userId'] is int(sys.argv[1]) and i['completed'] is True:
                    task_count += 1
                    task_title.append(i['title'])
            print("Employee {} is done with tasks({}/{}):"
                  .format(name, task_count, total_tasks))
            for j in task_title:
                print("\t{}".format(j))
        except (ValueError):
            pass

