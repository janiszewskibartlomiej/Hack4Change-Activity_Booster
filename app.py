from flask import Flask, render_template
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

@app.route("/add-meetup")
def add_meetup():
    towns = DataProcessing().get_all_towns()
    return render_template("add-meetup.html", towns=towns)

if __name__ == "__main__":
    app.run(debug=True)

