from flask import Flask  # Import Flask to allow us to create our app
app = Flask(__name__)    # Create a new instance of the Flask class called "app"

@app.route('/')
def hello_world():
    return 'Hello World!'

@app.route("/dojo")
def dojo():
    return "Dojo!"

@app.route("/say/flask")
def flask():
    return "Hi Flask!"

@app.route("/say/michael")
def person_1():
    return "Hi Michael"

@app.route("/say/john")
def person_2():
    return "Hi John"

@app.route("/repeat/35/hello")
def hello35():
    return "hello " * 35

@app.route("/repeat/80/bye")
def bye80():
    return "bye " * 80

@app.route("/repeat/99/dogs")
def dogs99():
    return "dogs " * 99

@app.route("/repeat/<int:num>/<string:name>")
def cusie(num, name):
    return f"{name * num}"

@app.route("/hi/<string:name>")
def say_name(name):
    return f"Hello {name}"

@app.errorhandler(404)
def bad_request(e):
    return "Sorry! No response. Try again."

if __name__=="__main__":   # Ensure this file is being run directly and not from a different module    
    app.run(debug=True)    # Run the app in debug mode.