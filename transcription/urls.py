
from django.urls import path, include
from .views import TranscribeView

app_name = "transcription"

urlpatterns = [
    path("transcribe/" , TranscribeView.as_view(),name = "transcribe")
    ]