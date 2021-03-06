# Generated by Django 3.0.7 on 2020-12-06 16:55

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Item',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('added', models.DateTimeField(auto_now_add=True)),
                ('item_name', models.CharField(max_length=100)),
                ('image_link', models.URLField(blank=True)),
                ('availability', models.BooleanField(default=True)),
                ('stock', models.IntegerField()),
                ('rating', models.IntegerField(blank=True, default=3.5)),
                ('price', models.IntegerField()),
                ('description', models.TextField(blank=True, max_length=1000)),
                ('specifiation', models.TextField(blank=True, max_length=1000)),
                ('top_product', models.BooleanField(blank=True, default=False)),
                ('featured_product', models.BooleanField(blank=True, default=False)),
                ('item_name_normalized', models.CharField(blank=True, max_length=100)),
                ('item_type', models.CharField(default='Some Item', max_length=100)),
                ('item_sub_type', models.CharField(blank=True, max_length=100)),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
            options={
                'ordering': ['added'],
            },
        ),
    ]
