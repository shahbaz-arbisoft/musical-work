from django.urls import path

from musicalapp.views import WorkView

urlpatterns = [
    path('work/<str:ISWC>', WorkView.as_view()),
]
