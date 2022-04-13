from django.core.cache import cache
from django.http import Http404
from rest_framework import status
from rest_framework.response import Response
from rest_framework.views import APIView

from musicalapp.models import MusicalWork
from musicalapp.serializers import WorkSerializer


class WorkView(APIView):
    def get_object(self, ISWC):
        try:
            return MusicalWork.objects.get(ISWC=ISWC)
        except MusicalWork.DoesNotExist:
            raise Http404

    def get(self, request, ISWC=None):
        cache_key = ISWC
        cache_time = 1800
        data = cache.get(cache_key)
        if not data:
            works = self.get_object(ISWC)
            serializer = WorkSerializer(works)
            data = serializer.data
            cache.set(cache_key, data, cache_time)
        return Response(data, status=status.HTTP_200_OK)
