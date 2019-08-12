from django.db import models

# Create your models here.


class GoodsType(models.Model):
    # 商品类别表
    # 商品类别名称 varchar 30
    # 商品类别图片
    # 上架状态 boolean 默认true
    typeName = models.CharField(max_length=30, verbose_name="商品类别名称")
    typeImg = models.ImageField(upload_to='static/images/goodsType', verbose_name="商品类别图片")
    description = models.TextField(verbose_name="类型描述", null=True)

    def __str__(self):
        return self.typeName

    def to_dic(self):
        dic = {
            "typeName": self.typeName,
            "picture": self.typeImg.__str__(),
            "description": self.description,
        }
        return dic

    class Meta:
        db_table = "goods_type"
        verbose_name = "商品类别表"
        verbose_name_plural = verbose_name


class Goods(models.Model):
    # 商品表
    # 商品名称 varchar 30
    # 商品价格 decimal
    # 商品描述 varchar 100
    # 商品图片 Image
    # 上架状态 boolean 默认true
    # 商品类别 外键 goodsType_id
    name = models.CharField(max_length=30, verbose_name="商品名称")
    price = models.DecimalField(max_digits=6, decimal_places=2, verbose_name="商品价格")
    description = models.CharField(max_length=100, verbose_name="商品描述")
    img = models.ImageField(upload_to="static/images/upload", verbose_name="商品图片")
    isActive = models.BooleanField(default=True, verbose_name="上架状态")
    goodsType = models.ForeignKey(GoodsType, on_delete=True)

    def __str__(self):
        return self.name

    class Meta:
        db_table = "goods"
        verbose_name = "商品表"
        verbose_name_plural = verbose_name


class User(models.Model):
    # 用户表
    # 手机号
    # 用户密码
    # 用户昵称
    # 用户邮箱
    # 激活状态
    phone = models.CharField(max_length=11, verbose_name="手机号")
    pwd = models.CharField(max_length=200, verbose_name="密码")
    name = models.CharField(max_length=30, verbose_name="昵称")
    email = models.EmailField(verbose_name="邮箱")
    isActive = models.BooleanField(default=True, verbose_name="激活状态")

    def __str__(self):
        return self.name

    def __repr__(self):
        return '<User:%r>' % self.name

    class Meta:
        db_table = "user"
        verbose_name = "用户表"
        verbose_name_plural = verbose_name


class Cart(models.Model):
    # 购物车表
    # 用户id
    # 商品id
    # 购买数量
    user = models.ForeignKey(User, on_delete=True, verbose_name="用户id")
    goods = models.ForeignKey("Goods", on_delete=True, verbose_name="商品id")
    amount = models.IntegerField(verbose_name="商品数量")

    def __str__(self):
        return self.amount

    class Meta:
        db_table = "cart"
        verbose_name = "购物车表"
        verbose_name_plural = verbose_name


class Banner(models.Model):
    # 横幅表
    # 横幅名称
    # 横幅图片
    bannerName = models.CharField(max_length=30, verbose_name="横幅名称")
    bannerImg = models.ImageField(upload_to='static/images/banner', verbose_name="横幅图片", default=True)

    def __str__(self):
        return "banner" + str(self.id)

    class Meta:
        db_table = "banner"
        verbose_name = "横幅表"
        verbose_name_plural = verbose_name


class Ad(models.Model):
    # 广告表
    # 广告名称
    # 广告图片
    adName = models.CharField(max_length=30, verbose_name="广告名称")
    adImg = models.ImageField(upload_to='static/images/ad', verbose_name="广告图片", default=True)

    def __str__(self):
        return "Ad" + str(self.id)

    class Meta:
        db_table = "ad"
        verbose_name = "今日推荐表"
        verbose_name_plural = verbose_name











