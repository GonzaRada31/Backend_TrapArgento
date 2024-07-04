from datetime import datetime
from app import db, login
from flask_login import UserMixin
from werkzeug.security import generate_password_hash, check_password_hash

# Modelo para la tabla de usuarios
class Usuario(UserMixin, db.Model):
    id = db.Column(db.Integer, primary_key=True)
    nombre = db.Column(db.String(100))
    apellido = db.Column(db.String(100))
    email = db.Column(db.String(120), index=True, unique=True)
    password_hash = db.Column(db.String(512))

    def set_password(self, password):   # Función para encriptar la contraseña
        self.password_hash = generate_password_hash(password)

    def check_password(self, password):    # Función para verificar la contraseña
        return check_password_hash(self.password_hash, password)

    def to_dict(self):  # Función para convertir el objeto en un diccionario
        return {
            'id': self.id,
            'nombre': self.nombre,
            'apellido': self.apellido,
            'email': self.email
        }
    
    def __repr__(self):     # Función para representar el objeto como string
        return f'<Usuario {self.email}>'
    
    

# Modelo para la tabla de artistas
class Artista(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    nombre = db.Column(db.String(100))
    descripcion = db.Column(db.Text)
    imagen = db.Column(db.String(255))
    canciones = db.relationship('Cancion', backref='artista', lazy='dynamic')
    discos = db.relationship('Disco', backref='artista', lazy='dynamic')
    videos = db.relationship('Video', backref='artista', lazy='dynamic')

# Modelo para la tabla de canciones
class Cancion(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    titulo = db.Column(db.String(100))
    album = db.Column(db.String(100))
    duracion = db.Column(db.Time)
    artista_id = db.Column(db.Integer, db.ForeignKey('artista.id'))

# Modelo para la tabla de discos
class Disco(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    titulo = db.Column(db.String(100))
    imagen = db.Column(db.String(255))
    artista_id = db.Column(db.Integer, db.ForeignKey('artista.id'))

# Modelo para la tabla de videos
class Video(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    titulo = db.Column(db.String(100))
    url = db.Column(db.String(255))
    artista_id = db.Column(db.Integer, db.ForeignKey('artista.id'))

# Modelo para la tabla de suscriptores
class Suscriptor(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    email = db.Column(db.String(255))

# Modelo para la tabla de "me gusta" de artistas
class MeGustaArtista(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    usuario_id = db.Column(db.Integer, db.ForeignKey('usuario.id'))
    artista_id = db.Column(db.Integer, db.ForeignKey('artista.id'))

# Modelo para la tabla de "me gusta" de canciones
class MeGustaCancion(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    usuario_id = db.Column(db.Integer, db.ForeignKey('usuario.id'))
    cancion_id = db.Column(db.Integer, db.ForeignKey('cancion.id'))

@login.user_loader
def load_user(id):
    return Usuario.query.get(int(id))
