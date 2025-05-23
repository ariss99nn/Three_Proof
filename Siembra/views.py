from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from .models import Sowing
from .serializers import SowingSerializer

class SowingListCreateAPIView(APIView):
    def get(self, request):
        sowings = Sowing.objects.all()
        serializer = SowingSerializer(sowings, many=True)
        return Response(serializer.data)

    def post(self, request):
        serializer = SowingSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

class SowingRetrieveUpdateDestroyAPIView(APIView):
    def get_object(self, pk):
        try:
            return Sowing.objects.get(pk=pk)
        except Sowing.DoesNotExist:
            return None

    def get(self, request, pk):
        sowing = self.get_object(pk)
        if not sowing:
            return Response({"error": "Not found"}, status=status.HTTP_404_NOT_FOUND)
        serializer = SowingSerializer(sowing)
        return Response(serializer.data)

    def put(self, request, pk):
        sowing = self.get_object(pk)
        if not sowing:
            return Response({"error": "Not found"}, status=status.HTTP_404_NOT_FOUND)
        serializer = SowingSerializer(sowing, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def delete(self, request, pk):
        sowing = self.get_object(pk)
        if not sowing:
            return Response({"error": "Not found"}, status=status.HTTP_404_NOT_FOUND)
        sowing.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)
# This code defines the URL patterns for the Sowing API, allowing for listing, creating, retrieving, updating, and deleting sowings.