from flask import Flask

app = Flask(__name__)

@app.route('/')
def hello():
    return "Hello, Secure World!"

if __name__ == '__main__':
    app.run(ssl_context=('server.crt', 'server.key'))
