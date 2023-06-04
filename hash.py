import os
from flask import Flask
from flask import redirect as re

app = Flask(__name__)


@app.route('/<index>')
def hello(index):
    return re(index)



if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)
