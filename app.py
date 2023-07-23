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

if __name__=="__main__":
    app.run(debug=True)