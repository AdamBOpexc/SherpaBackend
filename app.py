from flask import Flask
import time

app = Flask(__name__)


@app.route('/api/time')
def hello_world():
    return {'time': time.time()}

if __name__ == '__main__':
    app.run(host='0.0.0.0')
