# Generated by Django 3.2 on 2024-09-15 12:51

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('recipes', '0001_initial'),
        ('favorite', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='favoriteitem',
            name='recipe',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='recipes.recipe'),
        ),
        migrations.AddField(
            model_name='favorite',
            name='recipes',
            field=models.ManyToManyField(related_name='favorite', through='favorite.FavoriteItem', to='recipes.Recipe'),
        ),
    ]