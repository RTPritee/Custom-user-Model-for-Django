# Generated by Django 4.1.4 on 2022-12-19 08:15

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('account', '0002_rename_user_account_user_name_and_more'),
    ]

    operations = [
        migrations.RenameField(
            model_name='account',
            old_name='user_name',
            new_name='user',
        ),
        migrations.AlterField(
            model_name='account',
            name='nid_no',
            field=models.CharField(blank=True, max_length=17, null=True),
        ),
    ]
