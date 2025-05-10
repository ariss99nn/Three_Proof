import pandas as pd
from .models import Usuario

def dataframe_user():
    queryset = Usuario.objects.all().values('id', 'firstname', 'lastname', 'document', 'contact', 'email', 'role', 'ubication')
    df = pd.DataFrame(list(queryset))
    return df 
