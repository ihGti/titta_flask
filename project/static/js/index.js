// ログインボーナスボタンがクリックされたときにフォームを送信する
document.getElementById("loginB").addEventListener("submit", function(event) {
  event.preventDefault(); // フォームのデフォルトの送信を防止
  var form = this;
  var xhr = new XMLHttpRequest();
  xhr.open(form.method, form.action, true);
  xhr.setRequestHeader("Content-Type", "application/x-www-form-urlencoded");
  xhr.onload = function() {
      if (xhr.status === 200) {
          // サーバーからの応答を解析
          var response = JSON.parse(xhr.responseText);
          if (response.result === "points") {
              alert("ポイントが付与されました: " + response.points + "ポイント");
          } else if (response.result === "coupon") {
              alert("クーポンが付与されました: " + response.coupon + "獲得");
          }
      }
  };
  xhr.send();
});


$('#slider_js').slick({
  autoplay: true,
  infinite: true,
  speed: 700,
  slidesToShow: 3,
  slidesToScroll: 1,
  prevArrow: '<div class="slick-prev"></div>',
  nextArrow: '<div class="slick-next"></div>',
  centerMode: true,
  variableWidth: true,
  dots: true,
});

$(".slider_sJs").slick({
  arrows: true,
  infinite: true,
  speed: 500,
  slidesToShow: 4,
  slidesToScroll: 1,
  prevArrow: '<img src="/static/images/slick_prevI.png" class="slide-arrow prev-arrow">',
  nextArrow: '<img src="/static/images/slick_nextI.png" class="slide-arrow next-arrow">',
  variableWidth: true,
  dots: true,
});




