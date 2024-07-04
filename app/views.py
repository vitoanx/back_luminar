from flask import jsonify, request
from app.models import Alumno

def index():
    response = {'message':'Hola Mundo API-REST Flask 🐍'}
    return jsonify(response)

def get_all_alumnos():
    alumnos = Alumno.get_all()
    return jsonify([alumno.serialize() for alumno in alumnos])

def get_alumno(alumno_id):
    alumno = Alumno.get_by_id(alumno_id)
    if not alumno:
        return jsonify({'message': 'Alumno no encontrado'}), 404
    return jsonify(alumno.serialize())

def create_alumno():
    #obtengo los datos enviados en formato json - convierte en un diccionario python
    data = request.json
    #PROCESO DE VALIDACION 
    #if(data['title']==''):
    #    return jsonify({'message':'El campo titulo es obligatorio'}), 500    
    new_alumno = Alumno(None,data['nombre'],data['apellido'],data['email'],data['foto'])
    new_alumno.save()
    response = {'message':'Alumno registrado con exito'}
    return jsonify(response) , 201

def update_alumno(alumno_id):
    alumno = Alumno.get_by_id(alumno_id)
    if not alumno:
        return jsonify({'message': 'Alumno not found'}), 404
    data = request.json
    alumno.nombre = data['nombre']
    alumno.apellido = data['apellido']
    alumno.email = data['email']
    alumno.foto = data['foto']
    alumno.save()
    return jsonify({'message': 'Alumno updated successfully'})

def delete_alumno(alumno_id):
    alumno = Alumno.get_by_id(alumno_id)
    if not alumno:
        return jsonify({'message': 'Alumno not found'}), 404
    alumno.delete()
    return jsonify({'message': 'Alumno deleted successfully'})
