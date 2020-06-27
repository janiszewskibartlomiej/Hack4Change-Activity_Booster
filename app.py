from flask import Flask, render_template, request, url_for
from werkzeug.utils import redirect

from data_processing import DataProcessing
from map_of_the_world import CreatingMap

app = Flask(__name__)


@app.route("/")
def index():
    CreatingMap().map_of_the_world()
    return render_template("index.html")


@app.route("/meetup=<int:id>")
def graph_diff(id):
    return render_template("chat.html")


@app.route("/add-meetup", methods=['GET', 'POST'])
def add_meetup():
    if request.method == "GET":
        towns = DataProcessing().get_all_towns()
        return render_template("add-meetup.html", towns=towns)
    if request.method == "POST":
        return render_template("thanks.html")

@app.route("/thanks")
def thanks():
    return "TAHNKS"


if __name__ == "__main__":
    app.run(debug=True)
