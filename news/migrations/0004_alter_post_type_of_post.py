# Generated by Django 4.1.3 on 2022-12-26 23:49

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('news', '0003_rename_rating_author_author_rating_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='post',
            name='type_of_post',
            field=models.CharField(choices=[('NW', 'новость'), ('PS', 'статья')], max_length=2),
        ),
    ]