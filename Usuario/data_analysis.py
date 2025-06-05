import os
import django
import pandas as pd
from django.db.models import F
# Configura el entorno de Django
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'Back.settings')
django.setup()

from .models import User #Impotamos el modelo

# Obtenemos los datos de la tabla de usuarios
# usar .values() para obtener diccionarios, que es ideal para Pandas
def Create_DataFrame():
    users_data = User.objects.all().values(
        'id', 'firstname', 'lastname','phone', 'document', 'city',
        'role', 'created_at', 'groups', 'user_permissions')
    
    # Convertir la lista de diccionarios a DataFrame
    df_User = pd.DataFrame(list(users_data))
    return df_User

