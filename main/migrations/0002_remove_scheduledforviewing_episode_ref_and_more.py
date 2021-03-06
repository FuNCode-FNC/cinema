# Generated by Django 4.0.6 on 2022-07-10 21:39

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='scheduledforviewing',
            name='episode_ref',
        ),
        migrations.RemoveField(
            model_name='scheduledforviewing',
            name='film_ref',
        ),
        migrations.RemoveField(
            model_name='scheduledforviewing',
            name='user_pk',
        ),
        migrations.RemoveField(
            model_name='viewed',
            name='episode_ref',
        ),
        migrations.RemoveField(
            model_name='viewed',
            name='film_ref',
        ),
        migrations.RemoveField(
            model_name='viewed',
            name='user_pk',
        ),
        migrations.AddField(
            model_name='customer',
            name='fav_episode',
            field=models.ManyToManyField(to='main.episode'),
        ),
        migrations.AddField(
            model_name='customer',
            name='fav_films',
            field=models.ManyToManyField(to='main.film'),
        ),
        migrations.AddField(
            model_name='customer',
            name='fav_serial',
            field=models.ManyToManyField(to='main.serial'),
        ),
        migrations.DeleteModel(
            name='Favorites',
        ),
        migrations.DeleteModel(
            name='ScheduledForViewing',
        ),
        migrations.DeleteModel(
            name='Viewed',
        ),
    ]
