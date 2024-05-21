#!/usr/bin/python3
"""Export api to csv"""
import csv
import requests
import sys

if __name__ == '__main__':
    USER_ID = sys.argv[1]
    endpoint_url = 'https://jsonplaceholder.typicode.com/users/' + USER_ID
    res = requests.get(endpoint_url)
    """GET DATA"""
    user_name = res.json().get('username')
    todo_tasks = endpoint_url + '/todos'
    res = requests.get(todo_tasks)
    all_todo_tasks = res.json()

    with open('{}.csv'.format(USER_ID), 'w') as csvfile:
        for todo_tasks in all_todo_tasks:
            completed_status = todo_tasks.get('completed')
            """Complete"""
            task_title = todo_tasks.get('title')
            """Done"""
            csvfile.write('"{}","{}","{}","{}"\n'.format(
                USER_ID, user_name, completed_status, task_title))
