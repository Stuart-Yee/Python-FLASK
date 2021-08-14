from flask import Flask, render_template

app = Flask(__name__)

@app.route("/")
def default():
    return "<html><head><title>Default</title></head><body><a href=\'/play\'>Go here, yeah?</a>"

@app.route("/play")
def index():
    return render_template("index.html", num=3, color="rgb(159,197,248)")

@app.route("/play/<int:number>")
def multiple_boxes(number):
    return render_template("index.html", num=number, color="rgb(159,197,248)")

@app.route("/play/<int:number>/<my_color>")
def many_box_colors(number, my_color):
    str(my_color)
    return render_template("index.html", num=number, color=my_color)







if __name__ == "__main__":
    app.run(debug=True)