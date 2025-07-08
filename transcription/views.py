from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from .serializers import TranscribeSerializer
from django.conf import settings
import whisper
import os


class TranscribeView(APIView):
    """
    POST /api/transcribe/ : 音声ファイルを受け取り、Whisper で文字起こし後に
    その結果を DB に保存し、JSON で返却する
    """
    def post(self,request):
        #受け取ったリクエストデータを検証（serializer）
        serializer = TranscribeSerializer(data = request.data)
        if not serializer.is_valid():
            # ファイルが添付されていない・形式が不正などの場合は 400 エラーを返す
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

        # アップロードされたファイルをローカルに保存する
        # シリアライザで検証済みのファイルオブジェクトを取得
        audio_file = serializer.validated_data['audio_file']

        # 保存先ディレクトリのパスを組み立て（プロジェクト直下の media/uploads）
        save_dir = os.path.join(settings.BASE_DIR, 'media', 'uploads')
        os.makedirs(save_dir, exist_ok=True)
        file_path = os.path.join(save_dir, audio_file.name)

        # 書き込みモード（バイナリ）でファイルを開く。
        # wb+ は「新規作成 or 上書き＋読み書き可」を意味する
        with open(file_path, 'wb+') as f:
            for chunk in audio_file.chunks():  # 大容量ファイルも扱えるように、チャンク単位で読み込み
                f.write(chunk)

        # ここまでで、サーバー内の media/uploads/ にファイルが置かれる

        # Whisper モデルをロードする
        # "base" モデルは軽量で動作も比較的速いが、
        # small/medium/large などに変えることも可能
        model = whisper.load_model("base")
        filename = serializer.validated_data["audio_file"].name
        # 文字起こしを実行
        result = model.transcribe(file_path)
        # 戻り値 result は辞書で、"text" キーに起こされた文字列が入っている

        #テキスト結果だけを取り出してクライアントに返す
        text = result.get('text', '').strip()
        return Response({'text': text}, status=status.HTTP_200_OK)

            