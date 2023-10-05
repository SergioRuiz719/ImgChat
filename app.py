import openai
from flask import Flask, request, render_template

app = Flask(__name__)

resultados = []


@app.route('/', methods=["GET", "POST"])
def index():
    if request.method == 'POST':
        descripcion = request.form.get("descripcion")
        nImagen = request.form.get("nImagen")
        nImagen = int(nImagen)
        for _ in range(nImagen):
            url_imagen = enviar_descripcion(descripcion)
            resultados.append(url_imagen)
    return render_template('index.html', resultados=resultados)


def enviar_descripcion(descripcion):
    openai.api_key = "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"
    respuesta = openai.Image.create(
            prompt=descripcion,
            n=1,
            size="512x512"
        )
    return respuesta["data"][0]["url"]


if __name__ == "__main__":
    app.run(debug=True, port=5000)
