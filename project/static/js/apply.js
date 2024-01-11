a = document.getElementById("title")
b = document.getElementById("comment")
c = document.getElementById("imageinput1")
d = document.getElementById("prof-image")

era = document.getElementById("ertitle")
erb = document.getElementById("ercomment")
erc = document.getElementById("erimageinput1")
erd = document.getElementById("erprof-image")

var inputvalue = [a,b,c,d]
var  erp = [era,erb,erc,erd]    //関数でグローバル変数の二次元配列にぶちこむ形式にしたほうが楽だしかっこいいけど面倒

 applysub = () =>{
    
    for(let i = 0; i < inputvalue.length; i++) { 
        if(inputvalue[i].value == false) {
            erp[i].textContent = "必須項目です";
            val = false;

        }else{

            erp[i].textContent = "";

        };
        erp[i].style.color = "#f00";
    };   

    if(val == false){
        return false
    }

    var message = "この内容で、登録を行いますか？"      
    return getFunc(message);

                 

 }

 getFunc = (message) => {// はい or いいえ ダイアログ
      

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

scroll = () =>{
    document.body.scrollIntoView({behavior: 'smooth'});
  };

