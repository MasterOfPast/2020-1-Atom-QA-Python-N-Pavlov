from flask import Flask
from random import randint
import json

app = Flask(__name__)
host = '0.0.0.0'
port = 5000
users = {}
fail_users = []
fail = ({}, 404)

try:
    with open("users.json", "r") as read_file:
        users = json.load(read_file)
    with open("fail.json", "r") as read_file:
        fail_users = json.load(read_file)
except Exception:
    pass


@app.route('/vk_id/<username>', methods=['GET'])
def get_user_by_id(username: str):
    print(users)
    print(fail_users)
    if username in users:
        return {'vk_id': users[username]}
    elif username in fail_users:
        return fail
    elif randint(1, 20) % 2 == 1:
        user_id = randint(1, 100000)
        users[username] = user_id
        with open("users.json", "w") as write_file:
            json.dump(users, write_file)
        return {'vk_id': users[username]}
    else:
        fail_users.append(username)
        with open("fail.json", "w") as write_file:
            json.dump(fail_users, write_file)
        return fail


@app.route('/status/<username>', methods=['GET'])
def stat(username: str):
    if username in users:
        return 1
    elif username in fail_users:
        return -1
    else:
        return 0


@app.route('/add_id/<username>', methods=['GET'])
def add(username: str):
    if stat(username) == -1:
        fail_users.remove(username)
        with open("fail.json", "w") as write_file:
            json.dump(fail_users, write_file)
        user_id = randint(1, 100000)
        users[username] = user_id
        with open("users.json", "w") as write_file:
            json.dump(users, write_file)
    elif stat(username) == 0:
        user_id = randint(1, 100000)
        users[username] = user_id
        with open("users.json", "w") as write_file:
            json.dump(users, write_file)


@app.route('/delete_id/<username>', methods=['GET'])
def delete(username: str):
    if stat(username) == 1:
        users.pop(username)
        with open("users.json", "w") as write_file:
            json.dump(users, write_file)
        fail_users.append(username)
        with open("fail.json", "w") as write_file:
            json.dump(fail_users, write_file)
    elif stat(username) == 0:
        fail_users.append(username)
        with open("fail.json", "w") as write_file:
            json.dump(fail_users, write_file)


app.run(host=host, port=port)
