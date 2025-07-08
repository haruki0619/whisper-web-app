from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from .serializers import TranscribeSerializer

class TranscribeView(APIView):
    def post(self,request):
        serializer = TranscribeSerializer(data = request.data)
        if not serializer.is_valid():
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

        filename = serializer.validated_data["audio_file"].name
        return Response(
            {'message': f'ファイル「{filename}」を受け取りました。'},
            status=status.HTTP_200_OK
        )    