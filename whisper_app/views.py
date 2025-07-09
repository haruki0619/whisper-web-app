
from django.shortcuts import render

# トップページ用ビュー
# transcription アプリ内の index.html を使用してフォームを表示します
def index(request):
    """
    GET リクエストでフォームを表示するだけのビュー
    """
    return render(request, 'transcription/index.html')
