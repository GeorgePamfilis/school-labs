from flask import Flask
app = Flask(___name__)

app.route('/')
def index():
    return "hey lab ratsies!"

if __name__ == '__main__':
    app.run()
