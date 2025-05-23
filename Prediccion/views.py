from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from .models import Prediction
from .serializers import predictionSerializer

class PredictionListCreateAPIView(APIView):
    def get(self, request):
        predictions = Prediction.objects.all()
        serializer = predictionSerializer(predictions, many=True)
        return Response(serializer.data)

    def post(self, request):
        serializer = predictionSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save(created_by=request.user if request.user.is_authenticated else None)
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

class PredictionRetrieveUpdateDestroyAPIView(APIView):
    def get_object(self, pk):
        try:
            return Prediction.objects.get(pk=pk)
        except Prediction.DoesNotExist:
            return None

    def get(self, request, pk):
        prediction = self.get_object(pk)
        if not prediction:
            return Response({"error": "Not found"}, status=status.HTTP_404_NOT_FOUND)
        serializer = predictionSerializer(prediction)
        return Response(serializer.data)

    def put(self, request, pk):
        prediction = self.get_object(pk)
        if not prediction:
            return Response({"error": "Not found"}, status=status.HTTP_404_NOT_FOUND)
        serializer = predictionSerializer(prediction, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def delete(self, request, pk):
        prediction = self.get_object(pk)
        if not prediction:
            return Response({"error": "Not found"}, status=status.HTTP_404_NOT_FOUND)
        prediction.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)
