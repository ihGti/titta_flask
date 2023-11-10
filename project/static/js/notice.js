// タブのボタンを取得
$(".tab-button").click(function(){
    var target = $(this).data("target");
    
    // すべてのtab-contentを非表示にする
    $(".tab-content").removeClass("active");
    
    // クリックされたボタンに対応するコンテンツを表示する
    $("#" + target).addClass("active");
});


$(document).ready(function(){
    $(".tab-button").on("click", function(){
        // 全てのボタンからselectedクラスを削除
        $(".tab-button").removeClass("active-button");
        // クリックされたボタンにselectedクラスを追加
        $(this).addClass("active-button");
    });
});