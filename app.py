from flask import Flask, render_template
from data_processing import DataProcessing
from map_of_the_world import CreatingMap

app = Flask(__name__)


@app.route("/")
def index():
    CreatingMap().map_of_the_world()
    return render_template("index.html")


@app.route("/mettup=<int:id>")
def graph_diff(id):
    return render_template("./graphs/" + get_graph[1] + ".html")


if __name__ == "__main__":
    app.run(debug=True)

