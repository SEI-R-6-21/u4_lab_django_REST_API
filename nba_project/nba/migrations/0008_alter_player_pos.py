# Generated by Django 4.1 on 2022-08-31 20:47

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('nba', '0007_alter_player_pos'),
    ]

    operations = [
        migrations.AlterField(
            model_name='player',
            name='pos',
            field=models.CharField(max_length=100),
        ),
    ]
