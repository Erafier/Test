# Generated by Django 3.0.5 on 2020-04-13 16:17

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Human',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('avatar', models.ImageField(blank=True, null=True, upload_to='media/avatars/')),
                ('first_name', models.CharField(max_length=30, verbose_name='First name')),
                ('second_name', models.CharField(max_length=30, verbose_name='Second name')),
                ('age', models.IntegerField(verbose_name='Age')),
                ('gender', models.CharField(choices=[('male', 'male'), ('female', 'female')], max_length=6, verbose_name='Gender')),
            ],
        ),
    ]
