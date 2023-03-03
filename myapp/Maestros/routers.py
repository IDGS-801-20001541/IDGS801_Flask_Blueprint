from flask import Blueprint
#establecer el blueprint 
maestros = Blueprint('maestros',__name__)

@maestros.route('/getmaes',methods=['GET'])
def getdata():
    return {'key':'Maestros'}

