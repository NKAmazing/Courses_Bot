from flask import Flask, render_template, request
from dotenv import load_dotenv
import os
from app.routes import bp as routes_bp


# Cargar variables de entorno desde archivo .env
load_dotenv()

# Obtener la clave de autenticación de Discord desde las variables de entorno
DISCORD_TOKEN = os.getenv('DISCORD_TOKEN')

# Configurar una instancia de la aplicación Flask
app = Flask(__name__)

app.register_blueprint(routes_bp)

# Iniciar la aplicación Flask
if __name__ == '__main__':
    app.run(debug = True, port = os.getenv("PORT"))