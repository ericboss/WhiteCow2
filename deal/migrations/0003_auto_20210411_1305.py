# Generated by Django 3.2 on 2021-04-11 13:05

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('deal', '0002_communityammenities_expandsearchradius_homesize_inunitfeatures_propertytype_sort'),
    ]

    operations = [
        migrations.AlterField(
            model_name='communityammenities',
            name='name',
            field=models.CharField(blank=True, max_length=30, null=True),
        ),
        migrations.AlterField(
            model_name='expandsearchradius',
            name='name',
            field=models.CharField(blank=True, max_length=30, null=True),
        ),
        migrations.AlterField(
            model_name='inunitfeatures',
            name='name',
            field=models.CharField(blank=True, max_length=30, null=True),
        ),
        migrations.AlterField(
            model_name='propertytype',
            name='name',
            field=models.CharField(blank=True, max_length=30, null=True),
        ),
        migrations.AlterField(
            model_name='sort',
            name='name',
            field=models.CharField(blank=True, max_length=30, null=True),
        ),
    ]
