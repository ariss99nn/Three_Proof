import pandas as pd
from .models import User

def import_user_from_csv(file_route):
    df = pd.read_csv(file_route)
    for _, row in df.iterrows():
        User.objects.create(
            firstname = row['firstname'],
            lastname = row['lastname'],
            role =  row['role']
        )