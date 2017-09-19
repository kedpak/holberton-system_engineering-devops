#!/usr/bin/python3
"""
Python script to export data in the JSON format.
"""
import json
import requests
import sys


if __name__ == '__main__':
    r_users = requests.get('https://jsonplaceholder.typicode.com/users/{}'
                           .format(sys.argv[1])).json()
    r_todos = requests.get('https://jsonplaceholder.typicode.com/todos')
    r_todos = r_todos.json()

    user_name = r_users['username']

    json_list = []
    for i in r_todos:
        if i['userId'] is int(sys.argv[1]):
            json_list.append(str(i['userId']))
            break
    json_dict = dict({json_list[0]: []})
    json_element = json_dict.get(sys.argv[1])
    with open('{}.json'.format(sys.argv[1]), 'w') as out:
        for i in r_todos:
            if i['userId'] == int(sys.argv[1]):
                new_dict = {
                    "task": i.get("title"),
                    "completed": i.get("completed"),
                    "username": user_name
                }
                json_element.append(new_dict)
        json.dump(json_dict, out)
