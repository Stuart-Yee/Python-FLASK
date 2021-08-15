from flask import Flask, render_template, redirect, request, session
from random import randint

app = Flask(__name__)
app.secret_key = "Tashkent"

@app.route("/")
def index():
    if "game" in session:
        block="reveal"
        color="red"
        session["guesses"] += 1
        if session["guess"] == session["secret_num"]:
            condition = f"{session['guess']} was the number!"
            session["reset"] = "reveal"
            color="green"
        elif session["guesses"] == 5:
            condition = f"You Lose! {session['secret_num']} was the number!"
            session["reset"] = "reveal"
        elif session["guess"] > session["secret_num"]:
            condition = "Too high!"
        elif session["guess"] < session["secret_num"]:
            condition = "Too low!"



    else:
        session["game"] = True
        session["secret_num"] = randint(1, 100)
        print(session["secret_num"])
        session["guess"] = 0
        session["guesses"] = 0
        block = "hidden"
        session["reset"] = "hidden"
        condition = None
        color = "red"

    return render_template("index.html",
                           condition=condition,
                           show=block,
                           reset=session["reset"],
                           color=color,
                           tries=session["guesses"])

@app.route("/guess", methods=["POST"])
def guess():
    session["guess"] = int(request.form["guess"])
    return redirect("/")

@app.route("/destroy")
def clear_session():
    session.clear()
    return redirect("/")

if __name__ == "__main__":
    app.run(debug=True)