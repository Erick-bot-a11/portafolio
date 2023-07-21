from flask import Flask
from flask import render_template

app=Flask(__name__)

@app.route("/")
def inicio():
    return render_template("sitio/index.html")

@app.route("/sobre-mi")
def about():
    return render_template("sitio/about.html")

@app.route("/contacto")
def contacto():
    return render_template("sitio/contacto.html")

if __name__=="__main__":
    app.run(debug=True)