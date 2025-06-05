from django.urls import path

from.views import(
    sensorList,
    sensorCreate,
    sensorDestroy,
    sensorRetrieve,
    sensorUpdate,
)

urlpatterns =[
    # Vista para listar todos los sensores (GET)
    path ("rutaList/", sensorList.as_view(), name="sensorList"),

    # Vista para crear un nuevo sensor (POST)
    path ("rutaCreate/", sensorCreate.as_view(), name="sensorCreate"),

    # Vistas de DETALLE - ¡Necesitan el ID del sensor!
    # El <int:pk> le dice a Django que capture un entero y lo pase como 'pk' a la vista.
    path ("rutaDelete/<int:pk>/", sensorDestroy.as_view(), name="sensorDelete"), # Cambié el nombre a 'sensorDelete' por claridad
    path ("rutaRetrieve/<int:pk>/", sensorRetrieve.as_view(), name="sensorRetrieve"),
    path ("rutaUpdate/<int:pk>/", sensorUpdate.as_view(), name="sensorUpdate"),
]