from flask import Flask, render_template, session, request, redirect

app = Flask(__name__)

app.secret_key = "9infgfe8shnb9sb"

@app.route("/")
def index():
    languages=["C#", "C++", "Python", "Java", "JavaScript", "Ruby"]
    locations=["San Jose", "Seattle", "Chicago", "Burbank", "Remote"]
    session.clear()

    return render_template("index.html", languages=languages, locations=locations)

@app.route("/capture", methods=["POST"])
def form_capture():
    session["name"] = request.form["name"]
    session["location"] = request.form["location"]
    session["language"] = request.form["language"]
    session["comment"] = request.form["comment"]

    return redirect("/result")

@app.route("/result")
def landing():
    if session.get("name"):
        return render_template("landing.html")
    else:
        return redirect("/")


if __name__ == "__main__":
    app.run(debug=True)