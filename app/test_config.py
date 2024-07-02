# Este archivo se utiliza para ejecutar la aplicación Flask a modo de prueba.
import sys
import os

# Añadir la raíz del proyecto a la ruta del sistema
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

from app import create_app, db
from app.models import Usuario, Artista, Cancion, Disco, Video, Suscriptor, MeGustaArtista, MeGustaCancion

app = create_app()

with app.app_context():
    # Eliminar todos los datos existentes para evitar duplicados
    db.session.query(MeGustaArtista).delete()
    db.session.query(MeGustaCancion).delete()
    db.session.query(Usuario).delete()
    db.session.query(Artista).delete()
    db.session.query(Cancion).delete()
    db.session.query(Disco).delete()
    db.session.query(Video).delete()
    db.session.query(Suscriptor).delete()
    db.session.commit()

    # Datos de ejemplo para usuarios
    usuarios = [
        {'nombre': 'Juan', 'apellido': 'Perez', 'email': 'juan.perez@example.com', 'password': 'password1'},
        {'nombre': 'Maria', 'apellido': 'Gomez', 'email': 'maria.gomez@example.com', 'password': 'password2'},
        {'nombre': 'Pedro', 'apellido': 'Martinez', 'email': 'pedro.martinez@example.com', 'password': 'password3'},
        {'nombre': 'Lucia', 'apellido': 'Lopez', 'email': 'lucia.lopez@example.com', 'password': 'password4'},
        {'nombre': 'Carlos', 'apellido': 'Garcia', 'email': 'carlos.garcia@example.com', 'password': 'password5'},
        {'nombre': 'Ana', 'apellido': 'Rodriguez', 'email': 'ana.rodriguez@example.com', 'password': 'password6'},
        {'nombre': 'Miguel', 'apellido': 'Fernandez', 'email': 'miguel.fernandez@example.com', 'password': 'password7'},
        {'nombre': 'Laura', 'apellido': 'Sanchez', 'email': 'laura.sanchez@example.com', 'password': 'password8'},
        {'nombre': 'Jorge', 'apellido': 'Ramirez', 'email': 'jorge.ramirez@example.com', 'password': 'password9'},
        {'nombre': 'Marta', 'apellido': 'Diaz', 'email': 'marta.diaz@example.com', 'password': 'password10'}
    ]

    for user_data in usuarios:
        user = Usuario(
            nombre=user_data['nombre'],
            apellido=user_data['apellido'],
            email=user_data['email']
        )
        user.set_password(user_data['password'])
        db.session.add(user)

    # Datos de ejemplo para artistas
    artistas = [
        {'nombre': 'Duki', 'descripcion': 'Artista de trap argentino.', 'imagen': 'duki.jpg'},
        {'nombre': 'Cazzu', 'descripcion': 'Cantante y compositora de trap.', 'imagen': 'cazzu.jpg'},
        {'nombre': 'Khea', 'descripcion': 'Rapero y cantante argentino.', 'imagen': 'khea.jpg'},
        {'nombre': 'Nicki Nicole', 'descripcion': 'Cantante y rapera argentina.', 'imagen': 'nicki_nicole.jpg'},
        {'nombre': 'Trueno', 'descripcion': 'Rapero y freestyler argentino.', 'imagen': 'trueno.jpg'},
    ]

    for artista_data in artistas:
        artista = Artista(
            nombre=artista_data['nombre'],
            descripcion=artista_data['descripcion'],
            imagen=artista_data['imagen']
        )
        db.session.add(artista)

    # Datos de ejemplo para canciones
    canciones = [
        {'titulo': 'She Don\'t Give a FO', 'album': '24', 'duracion': '00:03:00', 'artista_id': 1},
        {'titulo': 'Loca', 'album': 'Single', 'duracion': '00:02:40', 'artista_id': 2},
        {'titulo': 'Mamichula', 'album': 'Single', 'duracion': '00:04:00', 'artista_id': 3},
        {'titulo': 'Colocao', 'album': 'Single', 'duracion': '00:03:20', 'artista_id': 4},
        {'titulo': 'Sangría', 'album': 'Atrevido', 'duracion': '00:03:00', 'artista_id': 5},
    ]

    for cancion_data in canciones:
        cancion = Cancion(
            titulo=cancion_data['titulo'],
            album=cancion_data['album'],
            duracion=cancion_data['duracion'],
            artista_id=cancion_data['artista_id']
        )
        db.session.add(cancion)

    # Datos de ejemplo para discos
    discos = [
        {'titulo': 'Super Sangre Joven', 'imagen': 'super_sangre_joven.jpg', 'artista_id': 1},
        {'titulo': 'Error 93', 'imagen': 'error_93.jpg', 'artista_id': 2},
        {'titulo': 'Trapicheo', 'imagen': 'trapicheo.jpg', 'artista_id': 3},
        {'titulo': 'Recuerdos', 'imagen': 'recuerdos.jpg', 'artista_id': 4},
        {'titulo': 'Atrevido', 'imagen': 'atrevido.jpg', 'artista_id': 5},
    ]

    for disco_data in discos:
        disco = Disco(
            titulo=disco_data['titulo'],
            imagen=disco_data['imagen'],
            artista_id=disco_data['artista_id']
        )
        db.session.add(disco)

    # Datos de ejemplo para videos
    videos = [
        {'titulo': 'Duki - Goteo', 'url': 'https://www.youtube.com/watch?v=Z0ff-g8aaF0', 'artista_id': 1},
        {'titulo': 'Cazzu - Mucha Data', 'url': 'https://www.youtube.com/watch?v=samRZHVDZ8Y', 'artista_id': 2},
        {'titulo': 'Khea - HotGirl Bummer', 'url': 'https://www.youtube.com/watch?v=F-1wlDkWfg8', 'artista_id': 3},
        {'titulo': 'Nicki Nicole - Colocao', 'url': 'https://www.youtube.com/watch?v=ZcIoPpPDqFk', 'artista_id': 4},
        {'titulo': 'Trueno - Atrevido', 'url': 'https://www.youtube.com/watch?v=ZyViXxUglzg', 'artista_id': 5},
    ]

    for video_data in videos:
        video = Video(
            titulo=video_data['titulo'],
            url=video_data['url'],
            artista_id=video_data['artista_id']
        )
        db.session.add(video)

    db.session.commit()
    print("Datos ficticios agregados con éxito.")
