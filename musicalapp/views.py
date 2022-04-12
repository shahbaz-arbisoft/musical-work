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
        works = self.get_object(ISWC)
        serializer = WorkSerializer(works)
        return Response(serializer.data, status=status.HTTP_200_OK)
