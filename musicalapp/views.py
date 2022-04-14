from django.core.cache import cache
from django.shortcuts import get_object_or_404
from rest_framework import status
from rest_framework.response import Response
from rest_framework.views import APIView

from musicalapp.models import MusicalWork
from musicalapp.serializers import MusicalWorkSerializer


class WorkView(APIView):
    def get(self, request, ISWC=None):
        data = cache.get(ISWC)
        if not data:
            data = get_object_or_404(MusicalWork, ISWC=ISWC)
            cache.set(ISWC, data)
        serializer = MusicalWorkSerializer(data)
        return Response(serializer.data, status=status.HTTP_200_OK)
