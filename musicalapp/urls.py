from django.urls import path

from musicalapp.views import WorkView

urlpatterns = [
    path('work/', WorkView.as_view()),
    path('work/<str:ISWC>', WorkView.as_view()),
]
