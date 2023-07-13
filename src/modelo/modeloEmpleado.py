from flask import jsonify, request
from modelo.coneccion import db_connection

def buscar_empleado(codigo):
    try:
        conn = db_connection()
        cur = conn.cursor()
        cur.execute("select ci, nombre , fecha_nac, procedencia FROM empleado WHERE ci= %s", (codigo,))
        datos = cur.fetchone()
        conn.close()
        if datos != None:
            empleado = {'ci': datos[0], 'nombre': datos[1],
                       'fecha_nac': datos[2], 'procedencia': datos[3]
                       }
            return empleado
        else:
            return None
    except Exception as ex:
            raise ex

class EmpleadoModel():
    @classmethod
    def listar_empleado(self):
        try:
            conn = db_connection()
            cur = conn.cursor()
            cur.execute("select ci, nombre, fecha_nac ,procedencia from empleado")
            datos = cur.fetchall()
            empleados = []
            for fila in datos:
                empleado = {
                        'ci':fila[0],
                        'nombre': fila[1],
                        'fecha_nac': fila[2],
                        'procedencia': fila[3]
                        }
                empleados.append(empleado)
            conn.close()
            return jsonify({'empleados': empleados, 'mensaje': "Empleados listados.", 'exito': True})
        except Exception as ex:
            return jsonify({'mensaje': "Errorr", 'exito': False})
        
    @classmethod
    def registrar_empleado(self):
        try:
            usuario = buscar_empleado(request.json['ci'])
            if usuario != None:
                return jsonify({'mensaje': "Cedula de identidad  ya existe, no se puede duplicar.", 'exito': False})
            else:
                conn = db_connection()
                cur = conn.cursor()
                cur.execute('INSERT INTO empleado values(%s,%s,%s,%s)', (request.json['ci'], request.json['nombre'], request.json['fecha_nac'],
                                                                            request.json['procedencia']))
                conn.commit()
                conn.close()
                return jsonify({'mensaje': "Empleado registrado.", 'exito': True})
        except Exception as ex:
            return jsonify({'mensaje': "Error", 'exito': False})
