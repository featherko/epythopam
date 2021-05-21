"""Flask."""
from final.fre.heatmap import layer
from final.fre.pony_db import db_bind
from flask import Flask, render_template


app = Flask("Name", static_url_path="/static")


@app.route("/")
def startpage() -> str:
    """Start page."""
    return render_template("startpage_flask.html")


@app.route("/heatmap")
def heatmap() -> str:
    """Heatmap page."""
    layer()
    return render_template("heatmap.html")


@app.route("/histograms")
def histogram() -> str:
    """Histogram page."""
    return render_template("histograms.html")


if __name__ == "__main__":
    db_bind()
    app.run(debug=True)  # noqa: S201
