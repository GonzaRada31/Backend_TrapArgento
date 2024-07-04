import os
import sys

# Añadir la raíz del proyecto a la ruta del sistema
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

from app import create_app, db
from app.models import Usuario

app = create_app()
app.app_context().push()

# Crear un usuario de prueba
if Usuario.query.filter_by(email='test@example.com').first() is None:
    user = Usuario(nombre='Test', apellido='User', email='test@example.com')
    user.set_password('password')
    db.session.add(user)
    db.session.commit()

print(Usuario.query.all())
