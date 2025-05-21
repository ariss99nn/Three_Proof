from rest_framework.views import APIView
from rest_framework.response import Response
from .models import Prediction
from .serializers import PredictionSerializer
# Create your views here.

class predictionView(APIView):
    def get(self, request):
        prediccion = Prediction.objects.all()
        serializer = PredictionSerializer(prediccion, many=True)
        return Response(serializer.data)
