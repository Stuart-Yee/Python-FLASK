from flask import Flask, render_template
app = Flask(__name__)

@app.route("/")
def index():
    return render_template(
        "index.html",
        color1="red",
        color2="black",
        x=8,
        y=8
    )

@app.route("/<int:height>")
def custom_height(height):
    return render_template(
        "index.html",
        color1="red",
        color2="black",
        x=8,
        y=height
    )

@app.route("/<int:height>/<int:width>")
def custom_size(height, width):
    return render_template(
        "index.html",
        color1="red",
        color2="black",
        x=width,
        y=height
    )

@app.route("/<int:height>/<int:width>/<color>")
def change_color1(height, width, color):
    return render_template(
        "index.html",
        color1=str(color),
        color2="black",
        x=width,
        y=height
    )

@app.route("/<int:height>/<int:width>/<color>/<other_color>")
def custom_colors(height, width, color, other_color):
    return render_template(
        "index.html",
        color1=str(color),
        color2=str(other_color),
        x=width,
        y=height
    )














if __name__ == "__main__":
    app.run(debug=True)