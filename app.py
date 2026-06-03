from flask import Flask, jsonify

app = Flask(__name__)


def get_message():
    return "Hello from App"


@app.route('/')
def hello():
    return jsonify({"message": "Hello, world!"})


if __name__ == '__main__':
    app.run(host='0.0.0.0', port=8080)
from flask import Flask, jsonify

app = Flask(__name__)


@app.route('/')
def hello():
    return jsonify({"message": "Hello, world!"})


if __name__ == '__main__':
    app.run(host='0.0.0.0', port=8080)
def get_message():
    return "Hello from App"


def main():
    print(get_message())


if __name__ == "__main__":
    main()