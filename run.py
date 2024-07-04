from flask import Flask
from app.views import *
from app.database import init_app
from flask_cors import CORS

#inicializacion de la apliacion con Flask
app = Flask(__name__)

init_app(app)
#permitir solicitudes desde cualquier origin
CORS(app)

#registrar una ruta asociada a una vista
app.route('/',methods=['GET'])(index)
app.route('/api/alumnos/',methods=['GET'])(get_all_alumnos)
app.route('/api/alumnos/',methods=['POST'])(create_alumno)
app.route('/api/alumnos/<int:alumno_id>', methods=['GET'])(get_alumno)
app.route('/api/alumnos/<int:alumno_id>', methods=['PUT'])(update_alumno)
app.route('/api/alumnos/<int:alumno_id>', methods=['DELETE'])(delete_alumno)

if __name__ == '__main__':
    #levanta servidor de desarrollo flask
    app.run(debug=True)




