from flask import jsonify, request, Blueprint
from app import db
from app.models import Usuario

api = Blueprint('api', __name__)

@api.route('/api/usuarios', methods=['GET'])
def get_usuarios():
    usuarios = Usuario.query.all()
    return jsonify([usuario.to_dict() for usuario in usuarios])

@api.route('/api/usuario/<int:id>', methods=['GET'])
def get_usuario(id):
    usuario = Usuario.query.get_or_404(id)
    return jsonify(usuario.to_dict())

@api.route('/api/usuario', methods=['POST'])
def create_usuario():
    data = request.get_json() or {}
    if 'nombre' not in data or 'apellido' not in data or 'email' not in data or 'password' not in data:
        return jsonify({'error': 'Datos incompletos'}), 400
    if Usuario.query.filter_by(email=data['email']).first():
        return jsonify({'error': 'El usuario ya existe'}), 400
    usuario = Usuario(
        nombre=data['nombre'],
        apellido=data['apellido'],
        email=data['email']
    )
    usuario.set_password(data['password'])
    db.session.add(usuario)
    db.session.commit()
    return jsonify(usuario.to_dict()), 201

@api.route('/api/usuario/<int:id>', methods=['PUT'])
def update_usuario(id):
    usuario = Usuario.query.get_or_404(id)
    data = request.get_json() or {}
    if 'nombre' in data:
        usuario.nombre = data['nombre']
    if 'apellido' in data:
        usuario.apellido = data['apellido']
    if 'email' in data:
        usuario.email = data['email']
    if 'password' in data:
        usuario.set_password(data['password'])
    db.session.commit()
    return jsonify(usuario.to_dict())

@api.route('/api/usuario/<int:id>', methods=['DELETE'])
def delete_usuario(id):
    usuario = Usuario.query.get_or_404(id)
    db.session.delete(usuario)
    db.session.commit()
    return '', 204
