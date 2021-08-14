from flask import Flask, render_template, session, redirect

app = Flask(__name__)
app.secret_key = "Njamena, Chad"

@app.route("/")
def index():
    if 'visits' in session:
        session['visits'] += 1
        print(session['visits'])
    else:
        session['visits'] = 1
    return render_template("index.html", counter=session['visits'])

@app.route("/twice", methods=['POST'])
def add_two_visits():
    session['visits'] += 1
    return redirect("/")

@app.route("/clear", methods=['POST'])
def clear_session():
    session.pop('visits')
    return redirect("/")


if __name__ == "__main__":
    app.run(debug="True")