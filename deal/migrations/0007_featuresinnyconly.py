# Generated by Django 3.2 on 2021-04-11 22:54

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('deal', '0006_auto_20210411_2251'),
    ]

    operations = [
        migrations.CreateModel(
            name='FeaturesInNycOnly',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(blank=True, max_length=30, null=True)),
            ],
        ),
    ]
