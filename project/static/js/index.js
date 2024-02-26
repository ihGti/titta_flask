


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
              alert("クーポンが付与されました: クーポンを使用してください");
          }
      }
  };
  xhr.send();
});

$(function () {
    $('#slider_js').slick({
      arrows: true, // 前・次のボタンを表示する
      dots: true, // ドットナビゲーションを表示する
      appendDots: $('.S_dots'), // ドットナビゲーションの生成位置を変更
      speed: 1000, // スライドさせるスピード（ミリ秒）
      slidesToShow: 1, // 表示させるスライド数
      centerMode: true, // slidesToShowが奇数のとき、現在のスライドを中央に表示する
      variableWidth: true, // スライド幅の自動計算を無効化
    });
  });



