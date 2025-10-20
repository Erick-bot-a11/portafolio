from flask import Flask
from flask import render_template
from flask import request,redirect,url_for,flash,session
import smtplib
import os


app = Flask(__name__, static_folder='public') #//Con esta le digo donde estara mi carpeta con archivos estaticos
# app.config['SESSION_TYPE'] = 'filesystem'
app.secret_key="anystringhere"
# app.config['SESSION_TYPE'] = 'memcached'
# app.config['SECRET_KEY'] = 'super secret key'
# sess = session()

@app.route("/")
def inicio():
    return render_template("sitio/index.html")

@app.route("/about")
def about():
    return render_template("sitio/about.html")

@app.route("/contacto",methods=["GET","POST"])
def contacto():
    if request.method=="POST":
        #Establece la conexion al servidor de SMTP
        conexion=smtplib.SMTP(host="smtp.gmail.com",port=587)
        conexion.ehlo()

        #Encriptacion TLS
        conexion.starttls()

        #inicia secion en el servidor de correos
        conexion.login(user="pichonerick388@gmail.com",password="aventjdpqvqebiem")
        nombre=request.form["nombre"]
        mensaje=request.form["mensaje"]
        remitente=request.form["correo"]
        conexion.sendmail(from_addr=remitente,to_addrs="pichonerick388@gmail.com",msg=nombre+"\n"+remitente+"\n"+mensaje)
        conexion.quit()
        flash("He recibido tu mensaje, te responderé pronto. Si quieres contarme más, puedes enviar otro mensaje.")
        return redirect(url_for("contacto"))
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
    port = int(os.environ.get("PORT", 5000))  
    app.run(host='0.0.0.0', port=port)