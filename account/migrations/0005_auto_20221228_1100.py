# Generated by Django 3.2.2 on 2022-12-28 05:00

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('account', '0004_alter_account_pic'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='account',
            name='pic',
        ),
        migrations.AddField(
            model_name='account',
            name='birthday',
            field=models.DateField(blank=True, null=True),
        ),
        migrations.AddField(
            model_name='account',
            name='cover',
            field=models.ImageField(blank=True, null=True, upload_to=''),
        ),
    ]
