#FLASK
from flask import Flask, jsonify, render_template, request
import os, optparse
import yaml 


app = Flask(__name__)

developer = os.getenv("DEVELOPER", "Katherine Mazariegos")
environment=os.getenv("ENVIRONMENT","development")

data=yaml.load(open('info.yml')) 
#print(data['Nombre'])

@app.route("/demo")
def demo():
    return render_template("demo.html")

@app.route("/info")
def api_students():
    return render_template("info.html", data=data)
   
@app.route("/formacion")
def formacion():
    return render_template("formacion.html")


@app.route("/experiencia")
def experiencia():
    return render_template("experiencia.html")

@app.route("/")
def home():
    foo="bar"
    return render_template("home.html", mivariable=foo ,developer=developer)

if __name__ == "__main__":
    debug=False
    if environment == "development" or environment == "local":
        debug=True
    app.run(host="0.0.0.0",debug=debug)
