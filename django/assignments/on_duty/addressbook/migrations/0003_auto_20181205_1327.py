# Generated by Django 2.1.1 on 2018-12-05 13:27

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('addressbook', '0002_auto_20181205_1326'),
    ]

    operations = [
        migrations.AlterField(
            model_name='address',
            name='apartment_number',
            field=models.CharField(blank=True, max_length=5, null=True, verbose_name='Apartment Number'),
        ),
        migrations.AlterField(
            model_name='address',
            name='city',
            field=models.CharField(blank=True, max_length=30, null=True, verbose_name='City'),
        ),
        migrations.AlterField(
            model_name='address',
            name='country',
            field=models.CharField(blank=True, max_length=30, null=True, verbose_name='Country'),
        ),
        migrations.AlterField(
            model_name='address',
            name='post_code',
            field=models.IntegerField(blank=True, null=True, verbose_name='Post Code'),
        ),
        migrations.AlterField(
            model_name='address',
            name='region',
            field=models.CharField(blank=True, max_length=30, null=True, verbose_name='Region'),
        ),
        migrations.AlterField(
            model_name='person',
            name='date_of_birth',
            field=models.DateField(blank=True, null=True, verbose_name='Date of birth'),
        ),
        migrations.AlterField(
            model_name='person',
            name='image',
            field=models.ImageField(blank=True, null=True, upload_to='person/', verbose_name='Image'),
        ),
    ]
