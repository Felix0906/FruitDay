# Generated by Django 2.1.8 on 2019-07-13 01:15

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('index', '0002_auto_20190713_0913'),
    ]

    operations = [
        migrations.RenameField(
            model_name='cart',
            old_name='goods_id',
            new_name='goods',
        ),
        migrations.RenameField(
            model_name='cart',
            old_name='user_id',
            new_name='user',
        ),
    ]