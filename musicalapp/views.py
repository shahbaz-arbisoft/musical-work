from django.core.cache import cache
from django.http import Http404
from rest_framework import status
from rest_framework.response import Response
from rest_framework.views import APIView

from musicalapp.models import Work
from musicalapp.serializers import WorkSerializer


# Create your views here.


class WorkView(APIView):
    def get_object(self, ISWC):
        try:
            return Work.objects.get(ISWC=ISWC)
        except Work.DoesNotExist:
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
