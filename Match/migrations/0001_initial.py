# Generated by Django 3.0.5 on 2020-04-13 16:17

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('Human', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Match',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('first_name', models.CharField(max_length=30, verbose_name='First name')),
                ('second_name', models.CharField(max_length=30, verbose_name='Second name')),
                ('age', models.IntegerField(verbose_name='Age')),
                ('gender', models.CharField(choices=[('male', 'male'), ('female', 'female')], max_length=6, verbose_name='Gender')),
                ('pair', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, related_name='match', to='Human.Human')),
            ],
        ),
    ]
