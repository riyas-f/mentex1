# Generated by Django 4.0.4 on 2022-07-27 13:04

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('mentalapp', '0008_rename_cataegory_tbl_login_category'),
    ]

    operations = [
        migrations.AddField(
            model_name='tbl_idgen',
            name='userid',
            field=models.IntegerField(default=7),
            preserve_default=False,
        ),
    ]