from django.urls import path

from musicalapp.views import WorkView

urlpatterns = [
    path('musical/<str:ISWC>', WorkView.as_view()),
]
