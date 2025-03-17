from django.db.models import Avg
from rest_framework import serializers
from movies.models import Movies


class MovieSerializer(serializers.ModelSerializer):

    rate = serializers.SerializerMethodField(read_only=True)

    class Meta:
        model = Movies
        fields = "__all__"

        def get_rate(self, obj):
            rate = obj.reviews.aggregate(Avg('stars'))['stars__avg']

            if rate:
                return round(rate, 1)
            return None

        def validate_title(self, value):
            if len(value) > 120:
                raise serializers.ValidationError('The title is too long')
            return value

        def validate_resume(self, value):
            if len(value) > 200:
                raise serializers.ValidationError('The resume is too long')
            return value
