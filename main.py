from flask import Flask, render_template, request
import requests

app = Flask(__name__)
@app.route('/', methods=['GET', 'POST'])
def index():
   quotable = quotable1()
   return render_template("index.html", quotable=quotable)

def quotable1():
    url = f"https://api.quotable.io/random"
    response = requests.get(url)
    return response.json()

if __name__ == '__main__':
   app.run(debug=True)