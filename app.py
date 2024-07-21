from flask import *

app = Flask(__name__) 

@app.route("/")
@app.route("/open")
def open():
    return render_template("open.html")

@app.route("/home", methods=["POST", "GET"]) 
def home():
    usr = "<User Not Defined>" 
    if (request.method == "POST"): 
        usr = request.form["name"]
        if not usr:
            usr = "<User Not Defined>"
    return render_template("home.html",username=usr) 

if __name__ == "__main__": 
    app.run(debug=True,port=4949) 