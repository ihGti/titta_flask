function myfunc() {
  console.log(2);
  var message = "d" 
  if(window.confirm(message)){
    // 「はい」を選択した場合の処理

    return true //このまま画面遷移
  } else {
    // 「いいえ」を選択した場合の処理
    window.alert('キャンセルされました'); // 警告ダイアログを表示
		return false; // 送信を中止

  }

};
//window.confirm はい いいえの ダイアログ
//window.alert アラート
//window.prompt 使わない

