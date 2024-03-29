# Generated by Django 2.1.8 on 2019-07-13 01:13

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('index', '0001_initial'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='ad',
            options={'verbose_name': '今日推荐表', 'verbose_name_plural': '今日推荐表'},
        ),
        migrations.AlterModelOptions(
            name='banner',
            options={'verbose_name': '横幅表', 'verbose_name_plural': '横幅表'},
        ),
        migrations.AlterModelOptions(
            name='cart',
            options={'verbose_name': '购物车表', 'verbose_name_plural': '购物车表'},
        ),
        migrations.AlterModelOptions(
            name='goods',
            options={'verbose_name': '商品表', 'verbose_name_plural': '商品表'},
        ),
        migrations.AlterModelOptions(
            name='goodstype',
            options={'verbose_name': '商品类别表', 'verbose_name_plural': '商品类别表'},
        ),
        migrations.AlterModelOptions(
            name='user',
            options={'verbose_name': '用户表', 'verbose_name_plural': '用户表'},
        ),
        migrations.RemoveField(
            model_name='goodstype',
            name='isActive',
        ),
        migrations.AddField(
            model_name='goodstype',
            name='description',
            field=models.TextField(null=True, verbose_name='类型描述'),
        ),
        migrations.AlterField(
            model_name='ad',
            name='adImg',
            field=models.ImageField(default=True, upload_to='static/images/ad', verbose_name='广告图片'),
        ),
        migrations.AlterField(
            model_name='banner',
            name='bannerImg',
            field=models.ImageField(default=True, upload_to='static/images/banner', verbose_name='横幅图片'),
        ),
        migrations.AlterModelTable(
            name='ad',
            table='ad',
        ),
        migrations.AlterModelTable(
            name='banner',
            table='banner',
        ),
        migrations.AlterModelTable(
            name='cart',
            table='cart',
        ),
        migrations.AlterModelTable(
            name='goods',
            table='goods',
        ),
        migrations.AlterModelTable(
            name='goodstype',
            table='goods_type',
        ),
        migrations.AlterModelTable(
            name='user',
            table='user',
        ),
    ]
