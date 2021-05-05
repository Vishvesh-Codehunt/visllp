from flask import Flask, render_template, url_for, redirect

app = Flask(__name__)

@app.route("/")
def home():
    return render_template("index.html")

@app.route("/services")
def services():
    return render_template("services.html")

@app.route("/contact")
def contact():
    return render_template("contact.html")

@app.route("/equipment-finance")
def equipment():
    return render_template("equipment.html")

@app.route("/vehicle-finance")
def vehicle():
    return render_template("vehicle.html")

@app.route("/leaders")
def team():
    return render_template("team.html")

@app.route("/leaders/nitin-bhatia")
def nitin():
    return render_template("nitinbhatia.html")

@app.route("/leaders/amit-desai")
def amit():
    return render_template("amit.html")

@app.route("/leaders/brijesh-shah")
def brijesh():
    return render_template("brijesh.html")

@app.route("/leaders/manoj-bharti")
def manoj():
    return render_template("manoj.html")

@app.route("/leaders/shivendra-chouhan")
def shivendra():
    return render_template("shivendra.html")

@app.route("/leaders/raxit-chhaya")
def raxit():
    return render_template("raxit.html")

@app.route("/leaders/jitendra-varyani")
def jitendra():
    return render_template("jitendra.html")


if __name__ == "__main__":
    app.run(debug=True)