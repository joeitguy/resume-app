from flask import Flask

app = Flask(__name__)

@app.route('/')
def home():
    return 'CTS API is live!'

if __name__ == '__main__':
    app.run()
