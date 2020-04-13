from django.db import models


class Human(models.Model):
    GENDERS = (
        ('male', 'male'),
        ('female', 'female')
    )

    avatar = models.ImageField(upload_to='avatars/', null=True, blank=True)
    first_name = models.CharField(max_length=30, verbose_name='First name')
    second_name = models.CharField(max_length=30, verbose_name='Second name')
    age = models.IntegerField(verbose_name='Age')
    gender = models.CharField(max_length=6, choices=GENDERS, verbose_name='Gender')

    def __str__(self):
        return f'{self.first_name} {self.second_name}. {self.age} years.'
