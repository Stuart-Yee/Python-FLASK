from flask import Flask, render_template, session, redirect, request

app = Flask(__name__)
app.secret_key = "Njamena, Chad"

@app.route("/")
def index():
    if 'visits' in session:
        session['visits'] += 1
    else:
        session['visits'] = 1
    if 'page_loads' in session:
        session['page_loads'] += 1
    else:
        session['page_loads'] = 1
    return render_template("index.html", counter=session['visits'], loads=session['page_loads'])

@app.route("/twice", methods=['POST'])
def add_two_visits():
    session['visits'] += 1
    return redirect("/")

@app.route("/reset", methods=['POST'])
def reset_visits():
    session.pop('visits')
    return redirect("/")

@app.route("/destroy_session", methods=['GET','POST'])
def clear_session():
    session.clear()
    return redirect("/")

@app.route("/custom_count", methods=['POST'])
def custom_incr():
    str_num = request.form["increment"]
    increment = int(str_num) - 1
    session['visits'] += increment
    return redirect("/")


if __name__ == "__main__":
    app.run(debug="True")