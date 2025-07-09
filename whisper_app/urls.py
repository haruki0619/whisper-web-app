from django.urls import path
from .views import index

app_name = 'whisper_app'  # 名前空間（後で URL を逆引きしやすくなる）

urlpatterns = [
    # ルートURL（http://127.0.0.1:8000/）にアクセスが来たら index を呼び出す
    path('', index, name='index'),
]