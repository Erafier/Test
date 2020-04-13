from django.db import models

from Human.models import Human


class Match(models.Model):
    GENDERS = (
        ('male', 'male'),
        ('female', 'female')
    )

    first_name = models.CharField(max_length=30, verbose_name='First name')
    second_name = models.CharField(max_length=30, verbose_name='Second name')
    age = models.IntegerField(verbose_name='Age')
    gender = models.CharField(max_length=6, choices=GENDERS, verbose_name='Gender')

    pair = models.OneToOneField(Human, on_delete=models.CASCADE, related_name='match', null=True)

    def __str__(self):
        return f'{self.first_name} {self.second_name}. Couple of {self.pair.first_name}'
