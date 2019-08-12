import json

from django.shortcuts import render, redirect
from django.http import HttpResponse
from django.core import serializers
from .models import *

# Create your views here.


def index_views(request):
    return render(request, 'index.html', locals())


def login_views(request):
    if request.method == "GET":
        source_url = request.META.get('HTTP_REFERER', '/')
        request.session['source_url'] = source_url
        if 'id' in request.session and \
                'phone' in request.session:
            return redirect(source_url)
        else:
            if 'id' in request.COOKIES and \
                    "phone" in request.COOKIES:

                id = request.COOKIES.get('id')
                phone = request.COOKIES.get('phone')
                request.session['id'] = id
                request.session['phone'] = phone
                user = User.objects.filter(id=id, phone=phone)
                if user:
                    return redirect(source_url)
                else:
                    resp = redirect('/login/')
                    resp.delete_cookie('id')
                    resp.delete_cookie('phone')
                    return resp
            else:
                resp = render(request, 'login.html', locals())
                resp.set_cookie('source_url', source_url)
                return resp
    else:
        phone = request.POST.get('phone')
        pwd = request.POST.get('pwd')
        user = User.objects.filter(phone=phone, pwd=pwd)
        if user:
            request.session['id'] = user[0].id
            request.session['phone'] = phone
            source_url = request.COOKIES.get('source_url', '/')
            resp = redirect(source_url)
            if 'source_url' in request.COOKIES:
                resp.delete_cookie('source_url')
            if 'isSaved' in request.POST:
                expires = 60*60
                resp.set_cookie('id', user[0].id, expires)
                resp.set_cookie('phone', phone, expires)
            return resp
        else:
            errMsg = "用户名或密码错误"
            return render(request, 'login.html', locals())


def register_views(request):
    if request.method == "GET":
        # url = request.META.get('HTTP_REFERER', '/')
        # request.session['url'] = url
        if 'id' in request.session and 'phone' in request.session:
            resp = redirect('/')
            return resp
        else:
            return render(request, 'register.html')
    else:
        phone = request.POST['phone']
        pwd = request.POST['pwd']
        name = request.POST['name']
        email = request.POST['email']
        if phone == '' or pwd == '' or email == '':
            resp = redirect('/register')
            return resp
        else:
            user = User()
            user.phone = phone
            user.pwd = pwd
            user.name = name
            user.email = email
            user.save()
            request.session['id'] = user.id
            request.session['phone'] = user.phone
            url = request.session.get('url', '/')
            del request.session['url']
            resp = redirect(url)
            return resp


def more_views(request):
    return render(request, 'more.html')


def logout_views(request):
    if 'id' in request.session and 'phone' in request.session:
        del request.session['id']
        del request.session['phone']
        source_url = request.META.get("HTTP_REFERER", '/')
        resp = redirect(source_url)
        if 'id' in request.COOKIES and 'phone' in request.COOKIES:
            resp.delete_cookie('id')
            resp.delete_cookie('phone')
        return resp
    return redirect('/index/')


def check_login(request):
    if 'id' in request.session and \
            'phone' in request.session:
        status = 1
        id = request.session.get('id')
        name = User.objects.get(id=id).name
        dic = {
            'status': status,
            'name': name,
        }
        return HttpResponse(json.dumps(dic))
    else:
        if 'id' in request.COOKIES and \
                'phone' in request.COOKIES:
            status = 1
            id = request.COOKIES['id']
            phone = request.COOKIES['phone']
            name = User.objects.get(id=id).name
            request.session['id'] = id
            request.session['phone'] = phone
            dic = {
                'status': status,
                'name': name,
            }
            return HttpResponse(json.dumps(dic))
        else:
            dic = {
                "status": 0,
            }
            return HttpResponse(json.dumps(dic))


def check_phone(request):
    phone = request.GET['phone']
    user = User.objects.filter(phone=phone)
    if user:
        dic = {
            "status": 1,
            "data": "手机号已被占用"
        }
    else:
        dic = {
            "status": 0,
            "data": "手机号可用"
        }
    return HttpResponse(json.dumps(dic))


def banner_views(request):
    banners = Banner.objects.all()[:3]
    data = serializers.serialize('json', banners)
    return HttpResponse(data)


def adv_views(request):
    advs = Ad.objects.all()[:4]
    data = serializers.serialize('json', advs)
    return HttpResponse(data)


def get_goods(request):
    all_list = []
    goodsTypes = GoodsType.objects.all()
    for goodsType in goodsTypes:
        goods = goodsType.goods_set.filter(isActive=True).order_by('-id')[:5]
        dic = {
            "goodsType": json.dumps(goodsType.to_dic()),
            "goods": serializers.serialize('json', goods)
        }
        all_list.append(dic)
    data = json.dumps(all_list)
    return HttpResponse(data)


def cart_views(request):
    return render(request, 'cart.html', locals())


def add_cart(request):
    gid = request.GET['gid']
    add_number = 1
    if 'id' in request.session and 'phone' in request.session:
        user_id = request.session.get('id')
        cart = Cart.objects.filter(user_id=user_id, goods_id=gid)
        if cart:
            cart[0].amount += add_number
            cart[0].save()
            msg = '已更新购物车'
        else:
            cart = Cart(user_id=user_id, goods_id=gid, amount=add_number)
            cart.save()
            msg = "已添加购物车"
        dic = {
            "status": 1,
            "statusText": msg
        }
    else:
        dic = {
            "status": 0
        }
    return HttpResponse(json.dumps(dic))


def get_cart_goods(request):
    if "id" in request.session:
        uid = request.session['id']
        goodses = Cart.objects.filter(user_id=uid).values()
        goods_list = []
        all_list = []
        for good in goodses:
            goods_id = good['goods_id']
            goods = Goods.objects.get(id=goods_id)
            goods_list.append(goods)
        for good in goods_list:
            count = Cart.objects.get(goods_id=good.id, user_id=uid).amount
            dic = {
                "goods_id": good.id,
                "picture": str(good.img),
                "title": good.name,
                "price": str(good.price),
                "money": int(good.price) * int(count),
                "count": count
            }
            all_list.append(dic)
        return HttpResponse(json.dumps(all_list))
    else:
        return HttpResponse('登陆后查看购物车信息哦')


def delete_goods(request):
    goods_id = request.GET['goods_id']
    cart = Cart.objects.filter(goods_id=goods_id)
    cart.delete()
    dic = {
        "status": 1,
        "statusText": "商品移除成功"
    }
    jsonStr = json.dumps(dic)
    return HttpResponse(jsonStr)


def cart_count(request):
    if "id" in request.session:
        uid = request.session['id']
        cart_count = Cart.objects.filter(user_id=uid)
        dic = {
            "status": 1,
            "count": len(cart_count)
        }
    else:
        dic = {
            "status": 0,
            "count": 0
        }
    return HttpResponse(json.dumps(dic))