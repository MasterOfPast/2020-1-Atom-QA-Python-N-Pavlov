import threading

from flask import Flask, abort, request

app = Flask(__name__)
# users = {}
users = {'1': {'name': 'Testname', 'surname': 'surtest', 'password': 'hello',
               "secret": 120}}
host = '127.0.0.1'
port = 5000


def run_mock():
    server = threading.Thread(target=app.run, kwargs={'host': host, 'port': port})
    server.start()
    return server


def shutdown_mock():
    terminate_func = request.environ.get('werkzeug.server.shutdown')
    if terminate_func:
        terminate_func()


@app.route('/user/<user_id>', methods=['GET'])
def get_user_by_id(user_id: int):
    user_id = str(user_id)
    if user_id in users:
        user = {'name': users[user_id]['name'],
                'surname': users[user_id]['surname']
                }
        return user
    else:
        abort(404)


@app.route('/users/add', methods=['POST'])
def add():
    global users
    users[str(len(users) + 1)] = {'name': request.form.get('name', ''),
                                  'surname': request.form.get('surname', ''),
                                  'password': request.form.get('password', ''),
                                  'secret': request.form.get('secret', 50)}
    return request.args


@app.route('/users/enter', methods=['POST'])
def enter():
    user_id = request.form.get('id', '1')
    password = request.form.get('password', '')
    if users[user_id]['password'] == password:
        return users[user_id]
    else:
        abort(400)


@app.route('/shutdown')
def shutdown():
    shutdown_mock()


if __name__ == '__main__':
    run_mock()
