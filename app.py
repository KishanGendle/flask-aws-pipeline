from flask import Flask
app = Flask(__name__)

@app.route('/')
def hello():
    return "AWS OIDC se deploy kiya hua Flask App chal raha hai!"

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)