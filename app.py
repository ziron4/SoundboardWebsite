from flask import Flask, render_template, url_for
import os

app = Flask(__name__)

@app.route("/")
def home():
    files = os.listdir("static/sounds")
    return render_template("index.html", files=files)

@app.route("/play/<filename>")
def play_sound(filename):
    
    return f'<audio autoplay src="{url_for("static", filename=f"sounds/{filename}")}"></audio>'

if __name__ == "__main__":
    app.run(debug=True)