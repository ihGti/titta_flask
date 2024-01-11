var keisai = document.getElementById("on1");
var kinds = document.getElementById("on2");
var post = document.getElementById("on3");
var age= document.getElementById("on4");
var size = document.getElementById("on5");
var background= document.getElementById("on6");
var personal= document.getElementById("on7");
var health= document.getElementById("on8");
var place = document.getElementById("on9");

var keisaier = document.getElementById("keisaier");
var kindser = document.getElementById("kindser");
var poster = document.getElementById("poster");
var locationer = document.getElementById("locationer");
var gener = document.getElementById("gener");
var ageer = document.getElementById("ageer");
var sizeer = document.getElementById("sizeer");
var vaccineer = document.getElementById("vaccinner");
var caster = document.getElementById("caster");
var backgrounder = document.getElementById("backgrounder");
var personaler = document.getElementById("personalityer");
var healther = document.getElementById("healther");
var placeer = document.getElementById("placeer");


let inputvalue = [keisai,kinds,age,size,background,personal,health,place]
let erp = [keisaier,kindser,ageer,sizeer,backgrounder,personaler,healther,placeer]
let radioerp = [locationer,gener,vaccineer,caster]


function fostersub() {
    val = true
    val2 = true
    var location = radio("radio-001")
    var gen = radio("radio-002");
    var vaccine= radio("radio-003");
    var cast = radio("radio-004");
    let radiovalue = [location,gen,vaccine,cast]
    

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

    val2 = valid(age.value, ageer,"^\\d*$","半角英数で入力してください")

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