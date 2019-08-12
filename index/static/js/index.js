$(function () {
    change_address();
    loop();
    check_login();
    get_banner();
    get_adv();
    get_goods();
    cart_count();
});

function change_address() {
    $(".select>li").click(function () {
        $(".current").html(this.innerHTML)
    });
}

let index = 0;
let timer;
function autoPlay(){
    $(".wrapper>a").eq(index).attr('style', 'display:none;');
    // index++;
    // if(index == $(".wrapper>a").length){
    //     index=0;
    // }
    index = ++index == $(".wrapper>a").length ? 0 : index;
    $(".wrapper>a").eq(index).attr("style", "display:block");
    for(let i=0; i<$(".imgNav>li").length; i++){
         $(".imgNav>li").eq(i).attr('style', 'background:grey');
    }
    $(".imgNav>li").eq(index).attr('style', 'background:red');
}
function loop(){
    timer = setInterval(autoPlay, 3000);
    $(".wrapper").mouseover(function () {
        clearInterval(timer);
    });
    $(".wrapper").mouseout(function () {
        timer = setInterval(autoPlay, 3000);
    });
}

function check_login() {
    $.get('/check_login', function (data) {
        let html = '';
        if(data.status == 0){
            html +='<a href="/login">[Login]</a>&nbsp;';
            html +='<a href="/register">[Register Now]</a>';
        }else{
            html +='<a>[Welcome,' + data.name + ']</a>&nbsp;';
            html +='<a href="/logout">[Logout]</a>';
        }
        $('#login').html(html);
    }, 'json');
}

function get_banner() {
    $.get('/get_banner/', function (data) {
        let html1 = '';
        $.each(data, function (i, obj) {
            html1 += ' <a><img src="/' + obj.fields.bannerImg + '"></a>';
        });
        $(".wrapper").html(html1);
        let html2 = '';
        $.each(data, function (i, obj) {
            html2 += '<li><a href="#">'+ Number(i+1) +'</a></li>'
        });
        $(".imgNav").html(html2);
    },'json');
}


function get_adv() {
    $.get('/get_adv', function (data) {
        let html = '';
        $.each(data, function (i, obj) {
            html += '<a href="#"><img src="/' + obj.fields.adImg + '" ';
            if(i==3){
                html += 'class="lastAdv"';
            }
            html +='></a>';
        });
        $('#adv').html(html);
    }, 'json');
}

function get_goods() {
    $.get('/get_goods', function (data) {
        let html = '';
        $.each(data, function (i, obj) {
            let type = JSON.parse(obj.goodsType);
            html += '<div class="item" style="overflow: hidden;">';
              html += '<p class="goodsClass">';
                html += '<img src="/'+type.picture+'">';
                html += '<a href="/more">更多</a>';
              html += '</p>';
              html += '<ul>';
              let goods = JSON.parse(obj.goods);
                $.each(goods, function (i, good) {
                    html += '<li ';
                    if((i+1)%5==0){
                        html += "class=no-margin";
                    }
                    html +=  '>';
                      html += '<p><img src="/' + good.fields.img + '"></p>';
                      html += '<div class="content">';
                        html += '<a href="javascript:add_cart('+ good.pk +');">';
                          html += '<img src="/static/images/cart.png">';
                        html += '</a>';
                        html += '<p>' + good.fields.name + '</p>';
                        html += '<span>&yen;'+ good.fields.price + '</span>';
                      html += '</div>';
                    html += '</li>';
            });
              html += "</ul>";
            html += '</div>';
        });
        $("#main").html(html);
    },'json');
}

function add_cart(gid) {
    $.get('/add_cart', {'gid': gid}, function (data) {
        if (data.status == 0){
            alert('建议先登陆哦！');
        }else{
            alert(data.statusText);
        }
         cart_count();
    }, 'json');

}

function cart_count(){
    $.get('/cart_count', function (data) {
            let html = "<a href='/cart/'>我的购物车(" + data.count + ")</a>";
            $("#cart").html(html);
    }, 'json');
}






















