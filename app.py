from flask import Flask, render_template, url_for

app = Flask(__name__)

@app.route('/')
def index():
    return "Hello World 2!"

if __name__ == "__main__":
    app.run(debug==True)
