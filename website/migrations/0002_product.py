# Generated by Django 4.2.7 on 2023-12-01 19:14

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('website', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Product',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('product_name', models.CharField(max_length=100)),
                ('producer', models.CharField(max_length=100)),
                ('price', models.DecimalField(decimal_places=2, max_digits=10)),
                ('remains', models.PositiveIntegerField()),
                ('margin', models.DecimalField(decimal_places=2, max_digits=10)),
            ],
        ),
    ]