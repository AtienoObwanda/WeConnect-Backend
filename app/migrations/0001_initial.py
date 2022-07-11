# Generated by Django 4.0.5 on 2022-07-11 02:18

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('accounts', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Hotel',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('hotel_name', models.CharField(max_length=100)),
                ('description', models.TextField(blank=True)),
                ('tagline', models.CharField(max_length=100)),
                ('facility1', models.CharField(blank=True, max_length=30, null=True)),
                ('facility2', models.CharField(blank=True, max_length=30, null=True)),
                ('facility3', models.CharField(blank=True, max_length=30, null=True)),
                ('facility4', models.CharField(blank=True, max_length=30, null=True)),
                ('facility5', models.CharField(blank=True, max_length=30, null=True)),
                ('cover_image', models.ImageField(upload_to='images/')),
            ],
        ),
        migrations.CreateModel(
            name='Room',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(choices=[('Standard', 'Standard'), ('Standard Twin', 'Standard Twin'), ('Deluxe', 'Deluxe'), ('Deluxe Twin', 'Deluxe Twin')], max_length=30)),
                ('tagline', models.CharField(max_length=100)),
                ('rate', models.PositiveIntegerField(blank=True, null=True)),
                ('image', models.ImageField(upload_to='images/')),
                ('hotel', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='app.hotel')),
            ],
        ),
        migrations.CreateModel(
            name='Bookings',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('date', models.DateTimeField(auto_now_add=True)),
                ('phone', models.IntegerField(blank=True, null=True)),
                ('check_in', models.DateTimeField()),
                ('check_out', models.DateTimeField()),
                ('amount', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='app.room')),
                ('hotel', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='app.hotel')),
                ('user', models.ManyToManyField(related_name='bookings', to='accounts.client')),
            ],
        ),
    ]
