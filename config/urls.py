from django.contrib import admin
from django.urls import path , include

from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
   path('admin/', admin.site.urls),

    # ここで transcription アプリの URL をマウント
    path('api/', include('transcription.urls')),

    # 既存の whisper_app の画面表示 URL をトップに置きたいなら
    path('', include('whisper_app.urls')),
]+ static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
