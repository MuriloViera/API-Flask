from logging import debug
from flask import Flask #Importa a biblioteca
from api.garagem_service import garagem

app = Flask(__name__) #Instancia o framework

#Registrara rota
app.register_blueprint(garagem, url_prefix='/api/garagem/')

@app.route("/") #Endpoint da API, é o que vem depois do URL da API
def hello():
    return "API Controlde de Clientes"

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000, debug=True)    