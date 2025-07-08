from rest_framework import serializers

class TranscribeSerializer(serializers.Serializer):
    audio_file = serializers.FileField()