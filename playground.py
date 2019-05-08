from flask import Flask, render_template
app = Flask(__name__)

@app.route("/play")
def index():
    return render_template("playground.html")

@app.route("/play/<time>")
def printMultiples(time):
    return render_template("playground3.html", num_times=int(time))

@app.route("/play/<time>/<color>")
def changeColor(time,color):
    return render_template("playground3.html", num_times=int(time),box_color=color)

if __name__=="__main__":
    app.run(debug=True)