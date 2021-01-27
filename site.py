from flask import Flask, render_template, request, make_response, redirect, session, send_from_directory, make_response, g

app = Flask(__name__, template_folder="")

static_dir = "/static"

@app.route("/")
def run_game():
    return render_template("static/HtmlPerformanceTesting.html",
                           jsSource="http://localhost:5000//static/HtmlPerformanceTesting.js",
                           execSource="http://localhost:5000//static/HtmlPerformanceTesting",
                           pckSource="http://localhost:5000//static/HtmlPerformanceTesting.pck")





@app.route("/static/<path:filename>")
def main_static(filename):
    return send_from_directory(static_dir, filename)

if __name__ == "__main__":
    app.run()
