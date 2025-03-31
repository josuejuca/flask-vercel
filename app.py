from flask import Flask

app = Flask(__name__)

@app.route('/')
def hello():
    return "Hello, Clancy"

if __name__ == '__main__':
    app.run()
