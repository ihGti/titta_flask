document.getElementById('bounus').addEventListener('click', function(event) {
    event.preventDefault(); // ボタンのデフォルトの動作を無効化

    fetch('/login_bornus', {
        method: 'POST',
        headers: {
            'Content-Type': 'application/json'
        }
    })
    .then(response => response.json())
    .then(data => {
        // レスポンスからポイントやクーポン情報を取得してアラートで表示
        alert(`獲得したポイント: ${data.points}\n獲得したクーポン: ${data.coupon}`);
    })
    .catch(error => {
        console.error('Error:', error);
    });
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
