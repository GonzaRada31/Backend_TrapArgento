from flask import current_app as app, jsonify, request, url_for
from app import db
from app.models import Usuario

@app.route('/api/usuarios', methods=['GET'])
def get_usuarios():
    """
    Obtener todos los usuarios.
    """
    usuarios = Usuario.query.all()
    return jsonify([usuario.to_dict() for usuario in usuarios])

@app.route('/api/usuario/<int:id>', methods=['GET'])
def get_usuario(id):
    """
    Obtener un usuario por ID.
    """
    usuario = Usuario.query.get_or_404(id)
    return jsonify(usuario.to_dict())

@app.route('/api/usuario', methods=['POST'])
def create_usuario():
    """
    Crear un nuevo usuario.
    """
    data = request.get_json()
    if not data or not 'email' in data or not 'password' in data:
        return jsonify({'message': 'Faltan datos necesarios'}), 400

    nombre = data.get('nombre')
    apellido = data.get('apellido')
    email = data.get('email')
    password = data.get('password')

    if Usuario.query.filter_by(email=email).first() is not None:
        return jsonify({'message': 'El usuario ya existe'}), 400

    usuario = Usuario(nombre=nombre, apellido=apellido, email=email)
    usuario.set_password(password)
    db.session.add(usuario)
    db.session.commit()

    return jsonify(usuario.to_dict()), 201

@app.route('/api/usuario/<int:id>', methods=['PUT'])
def update_usuario(id):
    """
    Actualizar un usuario existente.
    """
    usuario = Usuario.query.get_or_404(id)
    data = request.get_json()
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

@app.route('/api/usuario/<int:id>', methods=['DELETE'])
def delete_usuario(id):
    """
    Eliminar un usuario por ID.
    """
    usuario = Usuario.query.get_or_404(id)
    db.session.delete(usuario)
    db.session.commit()
    return '', 204
