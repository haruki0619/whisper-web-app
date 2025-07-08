from rest_framework import serializers
"""
    API からのファイルアップロードデータを検証する

    Fields:
      audio_file (FileField): クライアントがアップロードする音声ファイル (wav/m4a/mp3 など)
"""
class TranscribeSerializer(serializers.Serializer):
    audio_file = serializers.FileField()