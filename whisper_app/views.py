from django.shortcuts import render

# トップページ用ビュー
# whisper_app アプリ内の index.html を使用してフォームを表示します
def index(request):
    """
    GET リクエストでフォームを表示するだけのビュー
    """
    return render(request, 'whisper_app/index.html')
