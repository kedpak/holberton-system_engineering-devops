#!/usr/bin/python3
"""
Python script to export data in the JSON format.
"""
import json
import requests
import sys


if __name__ == '__main__':
    r_users = requests.get('https://jsonplaceholder.typicode.com/users').json()
    r_todos = requests.get('https://jsonplaceholder.typicode.com/todos').json()

    json_list = []
    m = 0
    json_dict = {}
    for i in r_todos:
        json_list.append(str(i['userId']))
        json_dict.update(dict({json_list[m]: []}))
        m += 1

    with open('todo_all_employees.json', 'w') as out:
        m = 0
        for i in r_todos:
            for j in r_users:
                if j.get('id') == i.get('userId'):
                    user_name = j['username']
                    json_element = json_dict.get(str(j['id']))
            new_dict = {
                "task": i.get("title"),
                "completed": i.get("completed"),
                "username": user_name
            }
            json_element.append(new_dict)
        json.dump(json_dict, out)
