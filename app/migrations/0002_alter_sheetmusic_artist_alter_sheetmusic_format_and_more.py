# Generated by Django 5.0.5 on 2024-05-09 10:11

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='sheetmusic',
            name='artist',
            field=models.TextField(),
        ),
        migrations.AlterField(
            model_name='sheetmusic',
            name='format',
            field=models.TextField(),
        ),
        migrations.AlterField(
            model_name='sheetmusic',
            name='genres',
            field=models.TextField(),
        ),
        migrations.AlterField(
            model_name='sheetmusic',
            name='instruments',
            field=models.TextField(),
        ),
        migrations.AlterField(
            model_name='sheetmusic',
            name='item_type',
            field=models.TextField(),
        ),
        migrations.AlterField(
            model_name='sheetmusic',
            name='lead_time',
            field=models.TextField(),
        ),
        migrations.AlterField(
            model_name='sheetmusic',
            name='publisher',
            field=models.TextField(),
        ),
        migrations.AlterField(
            model_name='sheetmusic',
            name='title',
            field=models.TextField(),
        ),
    ]
