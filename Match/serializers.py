from rest_framework import serializers
from Human.serializers import HumanSerializer
from Match.models import Match


class MatchesSerializer(serializers.ModelSerializer):
    pair = HumanSerializer(read_only=True)

    class Meta:
        model = Match
        fields = ('id', 'first_name', 'second_name', 'age', 'pair')


class SingleMatchSerializer(serializers.ModelSerializer):
    class Meta:
        model = Match
        fields = ('id', 'first_name', 'second_name', 'age')
