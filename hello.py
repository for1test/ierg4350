from flask import Flask

secret = "This is a secret"

app = Flask(__name__)

@app.route("/")
def hello_world():
    return f"<div>Hello, World! {secret}</div>"

if __name__ == "__main__":
    app.run()