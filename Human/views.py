from rest_framework.generics import ListCreateAPIView, RetrieveUpdateDestroyAPIView
from Match.models import Match
from .models import Human
from .paginations import Pagination
from .serializers import HumanSerializer
from .utils import get_random_person


class HumansView(ListCreateAPIView):
    pagination_class = Pagination
    queryset = Human.objects.all()
    serializer_class = HumanSerializer

    def perform_create(self, serializer):
        serializer.save()
        gender = serializer.data['gender']
        if gender == 'male':
            first_name, second_name = get_random_person('female')
            Match.objects.update_or_create(
                first_name=first_name,
                second_name=second_name,
                gender='female',
                age=serializer.data['age'],
                pair_id=serializer.data['id']
            )
        elif gender == 'female':
            first_name, second_name = get_random_person('male')
            Match.objects.update_or_create(
                first_name=first_name,
                second_name=second_name,
                gender='male',
                age=serializer.data['age'],
                pair_id=serializer.data['id']
            )


class SingleHumanView(RetrieveUpdateDestroyAPIView):
    queryset = Human.objects.all()
    serializer_class = HumanSerializer
