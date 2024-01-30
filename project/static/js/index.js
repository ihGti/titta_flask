var bornus = document.getElementById('loginB');

bornus.addEventListener('click',function(event){
    event.preventDefault();
    get_bounus();
});

function get_bounus(){
    // pythonからdef関数を取得
    fetch('/login_bornus',{
        method: 'POST',
        headers:{
            'Content-Type': 'application/json'
        }
    })
    .then(response => response.json())
    .then(data => {
        // 取得したログイン情報の表示
        if(data.type === 'points'){
            alert('ポイントボーナス'+ data.get_point + 'ポイント獲得');
        }
        else if(data.type === 'coupon'){
            alert('クーポンボーナス'+ data.get_coupon + 'クーポン獲得');
        }
    })
    .catch(error => {
        console.error('ログインボーナス情報の取得中にエラーが発生しました:', error);
    });
}
get_bounus();