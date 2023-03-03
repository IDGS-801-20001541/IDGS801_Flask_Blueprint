from flask import Blueprint
#establecer el blueprint 
alumnos = Blueprint('alumnos',__name__)

@alumnos.route('/getAlum',methods=['GET'])
def getdata():
    return {'key':'Alumnos'}

