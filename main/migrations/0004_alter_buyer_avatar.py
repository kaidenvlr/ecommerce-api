# Generated by Django 4.2 on 2023-05-02 15:59

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0003_remove_buyer_name'),
    ]

    operations = [
        migrations.AlterField(
            model_name='buyer',
            name='avatar',
            field=models.ImageField(blank=True, null=True, upload_to='avatar'),
        ),
    ]
