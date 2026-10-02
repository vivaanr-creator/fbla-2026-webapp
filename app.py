from flask import Flask, render_template

app = Flask(__name__)


@app.get("/")
def home():
    return render_template("home.html", title="Welcome", active_page="home")


@app.get("/explore")
def explore():
    return render_template("explore.html", title="Explore", active_page="explore")


@app.get("/experience")
def experience():
    return render_template("experience.html", title="Experience", active_page="experience")


if __name__ == "__main__":
    app.run(debug=True)
