from rest_framework import serializers

from musicalapp.models import MusicalWork


class MusicalWorkSerializer(serializers.ModelSerializer):

    def to_representation(self, instance):
        data = super().to_representation(instance)
        data["contributors"] = instance.contributors.values_list('name', flat=True)
        return data

    class Meta:
        model = MusicalWork
        fields = ('ISWC', 'title')
