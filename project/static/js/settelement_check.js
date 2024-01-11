function viewChange(){
    if(document.getElementById('point')){
        id = document.getElementById('point').value;
        if(id == 'yes'){
            document.getElementById('Box').style.display = "";
        }else if(id == 'no'){
            document.getElementById('Box').style.display = "none";
        }
    }
}
window.onload = viewChange;


function viewChange2(){
    if(document.getElementById('card')){
        id = document.getElementById('card').value;
        if(id == 'select1'){
            document.getElementById('Box2').style.display = "none";
        }else if(id == 'select2'){
            document.getElementById('Box2').style.display = "";
        }else if(id == 'select3'){
            document.getElementById('Box2').style.display = "";
        }
    }
window.onload = viewChange2;
}




// function settelesub(){
//     var point = document.getElementById("point");
//     var ku_pon = document.getElementById("ku-pon");
//     var card = document.getElementById("card");
//     var cardnum = document.getElementById("cardnum");
//     var yukou = document.getElementById("yukou");
//     var yukou2 = document.getElementById("yukou2")
//     var meigi = document.getElementById("meigi")
//     var cvv = document.getElementById("cvv")
  
//     let inputvalue = [card, cardnum,meigi, cvv]
//     var valuename = {"card":"カード", "cardnum":"カード番号","username":"名義人", "cvv":"cvv"};
  
//       for(let i = 0; i < inputvalue.length; i++) { 
//           var a = inputvalue[i].name
//           if(inputvalue[i].value == false) {
//               window.alert( "カード情報が未入力です");
//               return false
//           }};

  
  
//     var message = "この内容で出品しますか？"      //json.key名   
//     return getFunc(message);
  
//   };
    
  
//   function getFunc(message) {// はい or いいえ ダイアログ
        
  
//       if(window.confirm(message)){
//             // 「はい」を選択した場合の処理
//             window.alert("この内容で登録します");
//             return true //このまま画面遷移
//       } else {
//             // 「いいえ」を選択した場合の処理
//             window.alert('キャンセルされました'); // 警告ダイアログを表示
//                 return false; // 送信を中止
        
//       };
//   };     

