# Generated by Django 3.0.5 on 2020-04-13 18:55

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('Human', '0002_auto_20200413_2225'),
        ('Match', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='match',
            name='pair',
            field=models.OneToOneField(blank=True, on_delete=django.db.models.deletion.CASCADE, related_name='match', to='Human.Human'),
        ),
    ]
