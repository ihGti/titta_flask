var on1 = document.getElementById("on1");
var on2 = document.getElementById("on2");
var on3 = document.getElementById("on3");
var on4 = document.getElementById("on4");
var on5 = document.getElementById("on5");
var on6= document.getElementById("on6");
var on7= document.getElementById("on7");
var on8= document.getElementById("on8");
var on9 = document.getElementById("on9");
var on10 = document.getElementById("on10");
var on11 = document.getElementById("on11");

var keisaier = document.getElementById("keisaier");
var kindser = document.getElementById("kindser");
var  ageer= document.getElementById("ageer");
var  sizeer= document.getElementById("sizeer");
var  hogoer= document.getElementById("hogoer");
var  hogoplaceer= document.getElementById("hogoplaceer");
var color = document.getElementById("colorer")
var  backgrounder= document.getElementById("backgrounder");
var  personaler= document.getElementById("personalutyer");
var  placer= document.getElementById("placer");
var  healther= document.getElementById("healther");
var  locationer= document.getElementById("locationer");
var  gener= document.getElementById("gener");
var  injuryer= document.getElementById("injuryer");


let inputvalue = [on1,on2,on3,on4,on5,on6,on7,on8,on9,on10,on11]
let erp = [keisaier,kindser,ageer,sizeer,hogoer,hogoplaceer,colorer,backgrounder,personaler,healther,placer]
let radioerp = [locationer,gener, injuryer]


function lostsub() {
    val = true
    val2 = true
    var radio2= radio("radio-002");
    var radio3 = radio("radio-003");
    let radiovalue = [radio2,radio3]
    

    for(let i = 0; i < inputvalue.length; i++) { 
        if(inputvalue[i].value == false) {
            erp[i].textContent = "必須項目です"
            val = false

        }else{

            erp[i].className = 'hideer';
            erp[i].textContent = ""   
        }
        erp[i].style.color = "#f00"
    };   

    for(let i = 0; i < radiovalue.length; i++) {
        if(radiovalue[i] == null){
            radioerp[i].textContent = "必須項目です";
            radioerp[i].style.color = "#f00"
            val = false
        }else{
            radioerp[i].textContent = ""
        }
    }

    val2 = valid(on3.value, ageer,"^\\d*$","半角英数で入力してください")

    if(val == false || val2 == false){
        scroll();
        errtitle.textContent = "入力に不備があります、確認してください"
        errtitle.style.padding = "20px 0 0 0"
        errtitle.style.fontSize = "1.4rem"
        errtitle.style.color = "#f00"
        return false
    }else{
        errtitle.textContent = ""
    }
     var message = "この内容で、登録を行いますか？"      //json.key名   
     return getFunc(message);

                   
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

let valid = (forvali,errbox,invali,valimsg) =>{

        var con = new RegExp(invali);
        var postcode = forvali;
        var result = postcode.match(con);
    

    if(result == null && forvali != false){
        errbox.textContent = valimsg
        errbox.style.color = "#f00"
        return  false
    }
};


function radio(byname) {
      //ラジオボタンオブジェクトを取得する
  var radios = document.getElementsByName(byname);
 
  //取得したラジオボタンオブジェクトから選択されたものを探し出す
  var result;
  for(var i=0; i<radios.length; i++){
    if (radios[i].checked) {
      //選択されたラジオボタンのvalue値を取得する
      result = radios[i].value;
      return result;
    }
  }
 
}


scroll = () =>{
    document.body.scrollIntoView({behavior: 'smooth'});
  };