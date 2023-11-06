from flask import Flask

app = Flask(__name__)


@app.route('/')
def task():
    return 'this is my first task flask program'

@app.route('/path2')
def task2():
    return "this is my second task"

app.run(debug=True)
