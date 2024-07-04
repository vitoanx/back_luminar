from app.database import get_db

class Alumno:

    #contructor
    def __init__(self,id_alumno=None,nombre=None,apellido=None,email=None,foto=None):
        self.id_alumno = id_alumno
        self.nombre = nombre
        self.apellido = apellido
        self.email = email
        self.foto = foto

    def serialize(self):
        return {
            'id_alumno':self.id_alumno,
            'nombre':self.nombre,
            'apellido':self.apellido,
            'email':self.email,
            'foto':self.foto,
        }

    @staticmethod
    def get_all():
        #logica de buscar en la base todas las peliculas
        db = get_db()
        cursor = db.cursor()
        query = "SELECT * FROM alumnos"
        cursor.execute(query)
        #obtengo resultados
        rows = cursor.fetchall()
        alumnos = [Alumno(id_alumno=row[0], nombre=row[1], apellido=row[2], email=row[3], foto=row[4]) for row in rows]
        #cerramos el cursor
        cursor.close()
        return alumnos

    def save(self):
        db = get_db()
        cursor = db.cursor()
        if self.id_alumno:
            cursor.execute("""
                UPDATE alumnos SET nombre = %s, apellido = %s, email = %s, foto = %s
                WHERE id_alumno = %s
            """, (self.nombre, self.apellido, self.email, self.foto, self.id_alumno))
        else:
            cursor.execute("""
                INSERT INTO alumnos (nombre, apellido, email, foto) VALUES (%s, %s, %s, %s)
            """, (self.nombre, self.apellido, self.email, self.foto))
            #voy a obtener el último id generado
            self.id_alumno = cursor.lastrowid
        db.commit() #confirmar la accion
        cursor.close()

    @staticmethod
    def get_by_id(alumno_id):
        db = get_db()
        cursor = db.cursor()
        cursor.execute("SELECT * FROM alumnos WHERE id_alumno = %s", (alumno_id,))
        row = cursor.fetchone()
        cursor.close()
        if row:
            return Alumno(id_alumno=row[0], nombre=row[1], apellido=row[2], email=row[3], foto=row[4])
        return None

    def delete(self):
        db = get_db()
        cursor = db.cursor()
        cursor.execute("DELETE FROM alumnos WHERE id_alumno = %s", (self.id_alumno,))
        db.commit()
        cursor.close()
