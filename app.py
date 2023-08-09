from flask import Flask
from flask import render_template

app = Flask(__name__, static_folder='public') #//Con esta le digo donde estara mi carpeta con archivos estaticos

@app.route("/")
def inicio():
    return render_template("sitio/index.html")

@app.route("/sobre-mi")
def about():
    return render_template("sitio/about.html")

@app.route("/contacto")
def contacto():
    return render_template("sitio/contacto.html")

@app.route("/proyectos")
def proyectos():
    return render_template("sitio/proyectos.html")

@app.route("/proyectos/salon")
def salon():
    return render_template("sitio/salon.html")

@app.route("/proyectos/camp")
def camp():
    return render_template("sitio/camp.html")

@app.route("/proyectos/task")
def task():
    return render_template("sitio/uptask.html")


@app.route("/proyectos/ine")
def ine():
    return render_template("sitio/ine.html")

if __name__=="__main__":
    app.run(debug=True)