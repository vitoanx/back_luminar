from flask import Flask
from app.views import *
from app.database import init_app
from flask_cors import CORS

# Inicialización de la aplicación con Flask
app = Flask(__name__)

init_app(app)
# Permitir solicitudes desde cualquier origin
CORS(app)

# Registrar una ruta asociada a una vista
app.add_url_rule('/', view_func=index, methods=['GET'])
app.add_url_rule('/api/alumnos/', view_func=get_all_alumnos, methods=['GET'])
app.add_url_rule('/api/alumnos/', view_func=create_alumno, methods=['POST'])
app.add_url_rule('/api/alumnos/<int:alumno_id>', view_func=get_alumno, methods=['GET'])
app.add_url_rule('/api/alumnos/<int:alumno_id>', view_func=update_alumno, methods=['PUT'])
app.add_url_rule('/api/alumnos/<int:alumno_id>', view_func=delete_alumno, methods=['DELETE'])

if __name__ == '__main__':
    # Levanta servidor de desarrollo Flask
    app.run(debug=True)