# Generated by Django 4.1.3 on 2022-11-09 18:09

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('articles', '0004_slide'),
    ]

    operations = [
        migrations.AlterField(
            model_name='organizationabout',
            name='about',
            field=models.TextField(blank=True, null=True),
        ),
    ]
