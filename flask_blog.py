from flask import Flask, render_template, url_for, flash, redirect
from GUI.forms import CheckLocal, CheckMaterial
import funcoes
import os

caminho_base = os.path.dirname(os.path.abspath(__file__))
template = os.path.join(caminho_base, "GUI/templates")
static = os.path.join(caminho_base, "GUI/static")

app = Flask(__name__, template_folder=template, static_folder=static)

app.config['SECRET_KEY'] = '5791628bb0b13ce0c676dfde280ba245'


@app.route("/", methods=['GET', 'POST'])
@app.route("/home", methods=['GET', 'POST'])
def home():
    form_tipo = CheckMaterial()
    form_lugar = CheckLocal()
    # Caso o formulario de CheckLocal receba um submit
    if form_lugar.validate_on_submit():
        material_descartado = form_lugar.material_descartado.data.lower()
        lugar, distancia = funcoes.encontrar_lugar(material_descartado, form_lugar.coordenadas_x.data, form_lugar.coordenadas_y.data, True)
        if not distancia and isinstance(lugar,str):
            flash(lugar)
        else:
            flash(f"O lugar mais proximo onde você pode descartar seu material é esta a {round(distancia, 2)} KM, {lugar['nome']}, no endereço {lugar['endereco']}, o horario de atendimento é de {lugar['atendimento']}.")
        return redirect(url_for('home'))
    # Caso o formulario de CheckMaterial receba um submit
    if form_tipo.validate_on_submit():
        material = form_tipo.material.data.lower()
        tipo = funcoes.detectar_tipo(material, True)
        flash(f'Seu material poderá ser descartado como: {tipo}')
        return redirect(url_for('home'))

    return render_template('index.html', form_tipo=form_tipo, form_lugar=form_lugar)


if __name__ == "__main__":
    app.run(debug=True)