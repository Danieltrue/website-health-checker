from flask import Flask, render_template, request
import requests
import time
app = Flask(__name__)

@app.route("/")
def home():
    #panels
    panels = [
        {"title": "SuperHi API", "url": "https://api.superhi.com"},
        {"title": "SuperHi Editor", "url": "https://editor.superhi.com"},
        {"title": "SuperHi Website", "url": "https://www.superhi.com"},
        {"title": "BBC News", "url": "https://www.bbc.com/news"},
        {"title": "Besignq", "url": "https://www.besignq.com"},
    ]
    return render_template('index.html',panels=panels) 

@app.route("/about")
def about():
    return render_template("about.html")

@app.route("/ping")
def ping():
    url = request.args.get("url")
    #request
    
    start_time = time.time()
    r = requests.get(url)
    end_time = time.time()

    diff_time = int((end_time - start_time) * 1000)

    return {
        "url": url,
        "speed": diff_time,
        "code": r.status_code
    }