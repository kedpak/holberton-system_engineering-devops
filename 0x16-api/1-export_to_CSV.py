#!/usr/bin/python3
"""
Python script to export data in the CSV format.
"""
import csv
import requests
import sys


if __name__ == '__main__':
    r_users = requests.get('https://jsonplaceholder.typicode.com/users/{}'
                           .format(sys.argv[1])).json()
    r_todos = requests.get('https://jsonplaceholder.typicode.com/todos')
    r_todos = r_todos.json()

    user_name = r_users['username']

    csv_list = []
    if len(sys.argv) > 1:
        for i in r_todos:
            string = "-"
            if i['userId'] is int(sys.argv[1]):
                seq = [
                    str(i['userId']),
                    user_name,
                    str(i['completed']),
                    i['title']
                ]
                string = string.join(seq)
                csv_list.append(string)

        with open('{}.csv'.format(sys.argv[1]), 'w') as out:
            writer = csv.writer(out, delimter=',',
                                quotechar='"', quoting=csv.QUOTE_ALL)
            for i in csv_list:
                i = i.split("-")
                writer.writerow(i)
