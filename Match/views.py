from rest_framework.generics import ListAPIView, GenericAPIView, RetrieveUpdateDestroyAPIView, get_object_or_404
from rest_framework.response import Response
from Human.paginations import Pagination
from Match.models import Match
from Match.serializers import MatchesSerializer, SingleMatchSerializer


class MatchesView(ListAPIView):
    queryset = Match.objects.all()
    serializer_class = MatchesSerializer
    pagination_class = Pagination


class SingleMatchView(GenericAPIView):

    def get(self, request, *args, **kwargs):
        match = get_object_or_404(Match, pair_id=kwargs['pk'])
        serializer = SingleMatchSerializer(match, many=False)
        return Response(serializer.data)
