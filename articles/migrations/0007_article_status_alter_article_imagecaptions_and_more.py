# Generated by Django 4.1.3 on 2022-11-16 18:08

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('articles', '0006_alter_banner_bannerimage'),
    ]

    operations = [
        migrations.AddField(
            model_name='article',
            name='status',
            field=models.BooleanField(blank=True, default=True, null=True),
        ),
        migrations.AlterField(
            model_name='article',
            name='imagecaptions',
            field=models.CharField(blank=True, default='...', max_length=255, null=True),
        ),
        migrations.AlterField(
            model_name='article',
            name='imagethumbnail',
            field=models.ImageField(upload_to='articles/static/articles/images/post'),
        ),
        migrations.AlterField(
            model_name='banner',
            name='bannercaptions',
            field=models.CharField(blank=True, default='...', max_length=255, null=True),
        ),
        migrations.AlterField(
            model_name='slide',
            name='caption',
            field=models.CharField(blank=True, default='...', max_length=225, null=True),
        ),
        migrations.AlterField(
            model_name='slide',
            name='photo',
            field=models.ImageField(upload_to='articles/static/articles/images/about'),
        ),
    ]