function selectImage(imageId) {
  document.getElementById(imageId).click();
}

function previewImage(inputId, targetImageId) {
  var input = document.getElementById(inputId);
  var targetImage = document.getElementById(targetImageId);
  var reader = new FileReader();

  reader.onload = function(e) {
    targetImage.src = e.target.result;
  }

  reader.readAsDataURL(input.files[0]);
}



function exhibisub(){
  var bigimage = document.getElementById("imageinput1");
  var title = document.getElementById("title");
  var setumei = document.getElementById("setumei");
  var situation = document.getElementById("situation");
  var  deli= document.getElementById("deli");
  var genre = document.getElementById("genre")
  var kane = document.getElementById("kane")
  var tag = document.getElementById("tag")

  let inputvalue = [bigimage, title, setumei, situation, deli, genre,  tag]
  var valuename = {"imageinput1":"画像", "title":"タイトル", "setumei":"説明", "situation":"商品状態", "deli":"配送方法", "genre":"ジャンル", "kane":"金額"  ,"tag":"タグ"};

    for(let i = 0; i < inputvalue.length; i++) { 
        var a = inputvalue[i].name
        if(inputvalue[i].value == false ) {
            window.alert(valuename[a] + "の項目が未入力です");
            return false
        }};

      if(kane.value != 0 && kane.value == false){
        window.alert(valuename["kane"] +"を入力してください")
        return false   
    }

    if(valid("-*", kane.value) == null){
      window.alert(valuename["kane"] + "の項目は整数で入力してください")
      return false
    }

    



    if(Math.sign(kane.value) == -1){
      window.alert(valuename["kane"] + "は正の数で入力してください")
      return false   

    }



  var message = "この内容で出品しますか？"      //json.key名   
  return getFunc(message);

};

function valid(invali, num){

  var con = new RegExp(invali);
  var postcode = num;
  var result = postcode.match(con);
  return result;

};
function getFunc(message) {// はい or いいえ ダイアログ
      

    if(window.confirm(message)){
          // 「はい」を選択した場合の処理
          window.alert("この内容で登録します");
          return true //このまま画面遷移
    } else {
          // 「いいえ」を選択した場合の処理
          window.alert('キャンセルされました'); // 警告ダイアログを表示
              return false; // 送信を中止
      
    };
};     