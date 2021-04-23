from flask import Flask, jsonify

app = Flask(__name__)


@app.route('/')
def home():
    return jsonify({'message': 'hello, world!'})


def test_client():
    pass


if __name__ == "__main__":
    app.run()
