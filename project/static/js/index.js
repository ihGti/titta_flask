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