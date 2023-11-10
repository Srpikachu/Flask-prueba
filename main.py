from flask import Flask, send_file
import random
import os

app = Flask(__name__)
facts_list = ["La mayoría de las personas que sufren adicción tecnológica experimentan un fuerte estrés cuando se encuentran fuera del área de cobertura de la red o no pueden utilizar sus dispositivos", "Según un estudio realizado en 2018, más del 50 porciento de las personas de entre 18 y 34 años se consideran dependientes de sus smartphones", "El estudio de la dependencia tecnológica es una de las áreas más relevantes de la investigación científica moderna", "Según un estudio de 2019, más del 60 porciento de las personas responden a mensajes de trabajo en sus smartphones en los 15 minutos siguientes a salir del trabajo"
]

imagen_random = [
    "meme1.jpg",
    "meme2.jpg",
    "meme3.jpg",
    "meme4.jpg",
    "meme4.jpg",
    "mymeme.jpg",
]

@app.route("/")
def hello_world():
     return '<h1>Hello, World!</h1><a href="/random_fact">¡Ver un dato aleatorio!</a> <a href="/imagen_random">¡Ver un imagenes aleatorio!</a>'

@app.route("/random_fact")
def random_factor():
    return f'<h1>{random.choice(facts_list)}</h1>'

@app.route("/imagen_random")
def meme():
    img_meme = random.choice(imagen_random)
    img_path = os.path.join('imagen', img_meme)
    return send_file(img_path, mimetype='image/jpeg')
       


app.run(debug=True)
