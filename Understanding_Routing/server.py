from flask import Flask
app = Flask(__name__)

@app.route("/")
def hello():
    return "Hello World!"

@app.route("/dojo")
def dojo():
    return "Dojo!"

@app.route("/say/<message>")
def say(message):
    message_str = str(message)
    new_msg = "Hi " + message_str.capitalize() +"!"
    return new_msg

@app.route("/repeat/<int:num>/<mystr>")
def repeater(num, mystr):
    mystr_str = str(mystr)
    message = f"<p> {mystr_str} </p>"
    return message * num

@app.route("/<non>")
def unrecognized(non):
    return f"Sorry, no response for {non}!"

@app.route("/int/<int:my_num>")
def add_to_five(my_num):
    return f"add 5 to it: {my_num + 5}"



if __name__ == "__main__":
    app.run(debug = True)