#!/usr/bin/python3
"""Get data from an API and convert to Json"""
import csv
import json
import requests
import sys


if __name__ == '__main__':
    USER_ID = sys.argv[1]
    endpoint_url = 'https://jsonplaceholder.typicode.com/users/' + USER_ID
    res = requests.get(endpoint_url)
    """Documentation"""
    USERNAME = res.json().get('username')
    """Documentation"""
    todo_tasks = endpoint_url + '/todos'
    res = requests.get(todo_tasks)
    all_todo_tasks = res.json()

    dict_data = {USER_ID: []}
    for task in all_todo_tasks:
        TASK_COMPLETED_STATUS = task.get('completed')
        TASK_TITLE = task.get('title')
        dict_data[USER_ID].append({
                                  "task": TASK_TITLE,
                                  "completed": TASK_COMPLETED_STATUS,
                                  "username": USERNAME})
    """print(dict_data)"""
    with open('{}.json'.format(USER_ID), 'w') as f:
        json.dump(dict_data, f)
