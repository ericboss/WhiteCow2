# Generated by Django 3.2 on 2021-04-20 05:36

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion
import django.utils.timezone
import embed_video.fields


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='CommunityAmmenities',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(blank=True, max_length=30, null=True)),
            ],
        ),
        migrations.CreateModel(
            name='CommunityAmmenitiesSale',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(blank=True, max_length=30, null=True)),
            ],
        ),
        migrations.CreateModel(
            name='Deals',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(blank=True, max_length=30, null=True)),
                ('date', models.DateTimeField(blank=True, default=django.utils.timezone.now, null=True)),
                ('property_status', models.CharField(blank=True, max_length=30, null=True)),
                ('owner', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
            options={
                'verbose_name_plural': 'Deals',
                'ordering': ['-date'],
            },
        ),
        migrations.CreateModel(
            name='ExpandSearchRadius',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(blank=True, max_length=30, null=True)),
            ],
        ),
        migrations.CreateModel(
            name='FeaturesInNycOnly',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(blank=True, max_length=30, null=True)),
            ],
        ),
        migrations.CreateModel(
            name='Garage',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(blank=True, max_length=30, null=True)),
            ],
        ),
        migrations.CreateModel(
            name='HeatingCooling',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(blank=True, max_length=30, null=True)),
            ],
        ),
        migrations.CreateModel(
            name='HomeSize',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('value', models.IntegerField(blank=True, null=True)),
            ],
        ),
        migrations.CreateModel(
            name='HomeSizeMaxSale',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('value', models.IntegerField(blank=True, null=True)),
            ],
        ),
        migrations.CreateModel(
            name='HomeSizeMinSale',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('value', models.IntegerField(blank=True, null=True)),
            ],
        ),
        migrations.CreateModel(
            name='InsideRooms',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(blank=True, max_length=30, null=True)),
            ],
        ),
        migrations.CreateModel(
            name='InUnitFeatures',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(blank=True, max_length=30, null=True)),
            ],
        ),
        migrations.CreateModel(
            name='Item',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('video', embed_video.fields.EmbedVideoField()),
            ],
        ),
        migrations.CreateModel(
            name='LotSize',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('value', models.IntegerField(blank=True, null=True)),
            ],
        ),
        migrations.CreateModel(
            name='LotViews',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(blank=True, max_length=30, null=True)),
            ],
        ),
        migrations.CreateModel(
            name='NoHoaFee',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(blank=True, max_length=30, null=True)),
            ],
        ),
        migrations.CreateModel(
            name='Ok',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(blank=True, max_length=30, null=True)),
            ],
        ),
        migrations.CreateModel(
            name='OutsideFeatures',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(blank=True, max_length=30, null=True)),
            ],
        ),
        migrations.CreateModel(
            name='PropertyStatus',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=30)),
            ],
            options={
                'verbose_name_plural': 'PropertyStatus',
            },
        ),
        migrations.CreateModel(
            name='PropertyType',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(blank=True, max_length=30, null=True)),
            ],
        ),
        migrations.CreateModel(
            name='PropertyTypeNycOnly',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(blank=True, max_length=30, null=True)),
            ],
        ),
        migrations.CreateModel(
            name='PropertyTypeSale',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(blank=True, max_length=30, null=True)),
            ],
        ),
        migrations.CreateModel(
            name='SchedulerTime',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(blank=True, max_length=40, null=True)),
            ],
        ),
        migrations.CreateModel(
            name='Sort',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(blank=True, max_length=30, null=True)),
            ],
        ),
        migrations.CreateModel(
            name='SortSale',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(blank=True, max_length=30, null=True)),
            ],
        ),
        migrations.CreateModel(
            name='Stories',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(blank=True, max_length=30, null=True)),
            ],
        ),
        migrations.CreateModel(
            name='SubscriptionDataForSale',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('primary_photo', models.JSONField(blank=True, null=True)),
                ('last_update_date', models.DateTimeField(blank=True, null=True)),
                ('source', models.JSONField(blank=True, null=True)),
                ('tags', models.CharField(blank=True, max_length=255, null=True)),
                ('permalink', models.CharField(blank=True, max_length=255, null=True)),
                ('status', models.CharField(blank=True, max_length=10, null=True)),
                ('list_date', models.DateTimeField(blank=True, null=True)),
                ('open_houses', models.CharField(blank=True, max_length=50, null=True)),
                ('description', models.JSONField(blank=True, null=True)),
                ('branding', models.JSONField(blank=True, null=True)),
                ('list_price', models.IntegerField(blank=True, null=True)),
                ('lead_attributes', models.JSONField(blank=True, null=True)),
                ('property_id', models.CharField(blank=True, max_length=255, null=True)),
                ('photos', models.JSONField(blank=True, null=True)),
                ('flags', models.JSONField(blank=True, null=True)),
                ('community', models.CharField(blank=True, max_length=50, null=True)),
                ('products', models.JSONField(blank=True, null=True)),
                ('virtual_tours', models.CharField(blank=True, max_length=50, null=True)),
                ('other_listings', models.JSONField(blank=True, null=True)),
                ('listing_id', models.CharField(blank=True, max_length=50, null=True)),
                ('price_reduced_amount', models.CharField(blank=True, max_length=50, null=True)),
                ('location', models.JSONField(blank=True, null=True)),
                ('matterport', models.CharField(blank=True, max_length=10, null=True)),
                ('deal', models.OneToOneField(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='deal_subscription_for_sale', to='deal.deals')),
                ('owner', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='SubscriptionDataForRent',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('photos', models.JSONField(blank=True, null=True)),
                ('branding', models.JSONField(blank=True, null=True)),
                ('other_listings', models.JSONField(blank=True, null=True)),
                ('list_price_min', models.IntegerField(blank=True, null=True)),
                ('href', models.CharField(blank=True, max_length=255, null=True)),
                ('when_indexed', models.DateTimeField(blank=True, null=True)),
                ('last_sold_price', models.FloatField(blank=True, null=True)),
                ('property_id', models.CharField(blank=True, max_length=255, null=True)),
                ('advertisers', models.JSONField(blank=True, null=True)),
                ('virtual_tours', models.CharField(blank=True, max_length=50, null=True)),
                ('seller_promotion', models.CharField(blank=True, max_length=50, null=True)),
                ('listing_id', models.CharField(blank=True, max_length=50, null=True)),
                ('price_reduced_amount', models.CharField(blank=True, max_length=50, null=True)),
                ('location', models.JSONField(blank=True, null=True)),
                ('last_update_date', models.DateTimeField(blank=True, null=True)),
                ('source', models.JSONField(blank=True, null=True)),
                ('permalink', models.CharField(blank=True, max_length=255, null=True)),
                ('list_date', models.DateTimeField(blank=True, null=True)),
                ('open_houses', models.CharField(blank=True, max_length=50, null=True)),
                ('last_sold_date', models.DateField(blank=True, null=True)),
                ('last_price_change_date', models.DateField(blank=True, null=True)),
                ('description', models.JSONField(blank=True, null=True)),
                ('last_price_change_amount', models.CharField(blank=True, max_length=50, null=True)),
                ('price_reduced_date', models.DateField(blank=True, null=True)),
                ('property_history', models.CharField(blank=True, max_length=50, null=True)),
                ('photo_count', models.IntegerField(blank=True, null=True)),
                ('list_price', models.CharField(blank=True, max_length=50, null=True)),
                ('lead_attributes', models.JSONField(blank=True, null=True)),
                ('list_price_max', models.IntegerField(blank=True, null=True)),
                ('tags', models.CharField(blank=True, max_length=255, null=True)),
                ('pet_policy', models.JSONField(blank=True, null=True)),
                ('products', models.JSONField(blank=True, null=True)),
                ('suppression_flags', models.CharField(blank=True, max_length=50, null=True)),
                ('status', models.CharField(blank=True, max_length=10, null=True)),
                ('flags', models.JSONField(blank=True, null=True)),
                ('community', models.CharField(blank=True, max_length=50, null=True)),
                ('matterport', models.BooleanField(blank=True, null=True)),
                ('primary_photo', models.JSONField(blank=True, null=True)),
                ('deal', models.OneToOneField(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='deal_subscription_for_rent', to='deal.deals')),
            ],
        ),
        migrations.CreateModel(
            name='AssetsForSale',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('sort', models.CharField(blank=True, max_length=255, null=True)),
                ('price_min', models.IntegerField(blank=True, null=True)),
                ('price_max', models.IntegerField(blank=True, null=True)),
                ('beds_min', models.IntegerField(blank=True, null=True)),
                ('beds_max', models.IntegerField(blank=True, null=True)),
                ('baths_min', models.IntegerField(blank=True, null=True)),
                ('baths_max', models.IntegerField(blank=True, null=True)),
                ('property_type', models.CharField(blank=True, max_length=255, null=True)),
                ('property_type_nyc_only', models.CharField(blank=True, max_length=255, null=True)),
                ('new_construction', models.CharField(blank=True, max_length=25, null=True)),
                ('hide_pending_contingent', models.CharField(blank=True, max_length=25, null=True)),
                ('has_virtual_tours', models.CharField(blank=True, max_length=25, null=True)),
                ('has_3d_tours', models.CharField(blank=True, max_length=25, null=True)),
                ('hide_foreclosure', models.CharField(blank=True, max_length=25, null=True)),
                ('price_reduced', models.CharField(blank=True, max_length=25, null=True)),
                ('open_house', models.CharField(blank=True, max_length=25, null=True)),
                ('keywords', models.CharField(blank=True, max_length=255, null=True)),
                ('no_hoa_fee', models.CharField(blank=True, max_length=25, null=True)),
                ('hoa_max', models.IntegerField(blank=True, null=True)),
                ('days_on_realtor', models.CharField(blank=True, max_length=25, null=True)),
                ('expand_search_radius', models.CharField(blank=True, max_length=25, null=True)),
                ('include_nearby_areas_slug_id', models.CharField(blank=True, max_length=255, null=True)),
                ('home_size_min', models.IntegerField(blank=True, null=True)),
                ('home_size_max', models.IntegerField(blank=True, null=True)),
                ('lot_size_min', models.IntegerField(blank=True, null=True)),
                ('lot_size_max', models.IntegerField(blank=True, null=True)),
                ('stories', models.CharField(blank=True, max_length=25, null=True)),
                ('garage', models.CharField(blank=True, max_length=25, null=True)),
                ('heating_cooling', models.CharField(blank=True, max_length=25, null=True)),
                ('inside_rooms', models.CharField(blank=True, max_length=255, null=True)),
                ('outside_features', models.CharField(blank=True, max_length=255, null=True)),
                ('lot_views', models.CharField(blank=True, max_length=255, null=True)),
                ('community_ammenities', models.CharField(blank=True, max_length=255, null=True)),
                ('deal', models.OneToOneField(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='deal_assets_for_sale', to='deal.deals')),
                ('owner', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='AssetsForRent',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('sort', models.CharField(blank=True, max_length=255, null=True)),
                ('price_min', models.IntegerField(blank=True, null=True)),
                ('price_max', models.IntegerField(blank=True, null=True)),
                ('beds_min', models.IntegerField(blank=True, null=True)),
                ('beds_max', models.IntegerField(blank=True, null=True)),
                ('baths_min', models.IntegerField(blank=True, null=True)),
                ('baths_max', models.IntegerField(blank=True, null=True)),
                ('property_type', models.CharField(blank=True, max_length=255, null=True)),
                ('expand_search_radius', models.CharField(blank=True, max_length=25, null=True)),
                ('include_nearby_areas_slug_id', models.CharField(blank=True, max_length=255, null=True)),
                ('home_size_min', models.IntegerField(blank=True, null=True)),
                ('home_size_max', models.IntegerField(blank=True, null=True)),
                ('in_unit_features', models.CharField(blank=True, max_length=255, null=True)),
                ('community_ammenities', models.CharField(blank=True, max_length=255, null=True)),
                ('cats_ok', models.CharField(blank=True, max_length=30, null=True)),
                ('dogs_ok', models.CharField(blank=True, max_length=30, null=True)),
                ('deal', models.OneToOneField(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='deal_assets_for_rent', to='deal.deals')),
            ],
        ),
        migrations.CreateModel(
            name='Adress',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('city', models.CharField(max_length=40)),
                ('state_code', models.CharField(max_length=10)),
                ('location', models.CharField(blank=True, default='', max_length=10)),
                ('offset', models.CharField(default='0', max_length=10)),
                ('limit', models.IntegerField(default=30)),
                ('deal', models.OneToOneField(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='deal_address', to='deal.deals')),
                ('owner', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]
