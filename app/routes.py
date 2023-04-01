from flask import Blueprint

from bot.bot import search

# Crear blueprint para las rutas
bp = Blueprint('routes', __name__)

# Definir ruta para búsqueda
@bp.route('/search/<term>', methods=['GET'])
def search_route(term):
    results = search(term)
    return {'results': results}
