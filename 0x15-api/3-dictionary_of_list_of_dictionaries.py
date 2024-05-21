#!/usr/bin/python3
"""
Using what you did in the task #0, extend your Python
script to export data in the JSON format.
"""

import json
import requests
from sys import argv


if __name__ == "__main__":

    users = requests.get("https://jsonplaceholder.typicode.com/users")
    empDATA = users.json()
    todos = requests.get('https://jsonplaceholder.typicode.com/todos')
    tasks = todos.json()
    todoAll = {}

    for user in empDATA:
        taskList = []
        for task in tasks:
            if task.get('userId') == user.get('id'):
                taskDict = {"username": user.get('username'),
                            "task": task.get('title'),
                            "completed": task.get('completed')}
                taskList.append(taskDict)
        todoAll[user.get('id')] = taskList

    with open('todo_all_employees.json', mode='w') as f:
        json.dump(todoAll, f)
