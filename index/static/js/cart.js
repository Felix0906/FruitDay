
function check_login(){
  $.get('/check_login/',function(data){
    var html = "";
    if(data.status == 0){
      html += "<a href='/login/'>[登录]，</a>";
      html += "<a href='/register/'>[注册有惊喜]</a>";
    }else{
      html += "欢迎,"+data.name;
      html += "&nbsp;<a href='/logout/'>退出</a>";
    }
    $("#login").html(html);
  },'json');
}

function get_goods_cart() {
  $.get('/get_cart_goods/', function (data) {
    let html = "";
    $.each(data, function (i, obj) {
      html += "<div class='g-item'>";
        html += "<p class='check-box'>";
        html += "<input type='checkbox'>";
        html += "<img src='/" + obj.picture + "' width='80'>";
        html += "</p>";
        html += "<p class='goods'>"+ obj.title + "</p>";
        html += "<p class='price'>&yen;" + obj.price + "</p>";
        html += "<p class='quantity'>" + obj.count + "</p>";
        html += "<p class='t-sum'><b>&yen;" + obj.money + "</b></p>";
        html += "<p class='action'><a href='javascript:delete_goods(" + obj.goods_id +")'>移除</a></p>";
      html += "</div>";
    });
    $("#good-content").html(html);
  }, 'json')
}

function delete_goods(gid) {
  $.get("/delete_goods/", {"goods_id": gid}, function (data) {
    if(data.status == 1){
      get_goods_cart();
    }
  }, 'json')
}


$(function(){
  //检查登录状态
  check_login();
  get_goods_cart();
});









