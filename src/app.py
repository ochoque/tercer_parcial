from flask import Flask
from modelo.modeloEmpleado  import EmpleadoModel

app = Flask(__name__)	

@app.route('/')
def hello_world():
    return 'hola INF530'
   
@app.route('/empleados', methods=['GET'])
def listar_empleados():
    emp=EmpleadoModel.listar_empleado()
    return emp

@app.route('/empleados', methods=['POST'])
def crear_empleados():
    emp=EmpleadoModel.registrar_empleado()
    return emp



if __name__ == '__main__':
   		app.run(debug=False,host='0.0.0.0')