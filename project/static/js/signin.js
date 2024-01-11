var email = document.getElementById("email");
var reemail = document.getElementById("reemail");
var Password = document.getElementById("Password");
var rePassword = document.getElementById("rePassword");
var sei = document.getElementById("sei");
var mei = document.getElementById("mei");

var sei_kana = document.getElementById("sei-kana");
var mei_kana = document.getElementById("mei-kana");
var username = document.getElementById("username");
var telphone = document.getElementById("telphone");
var yuubin = document.getElementById("yuubin");
var address = document.getElementById("address");
var image = document.getElementById("prof-image");

var emailer = document.getElementById("emailer");
var reemailer_equal = document.getElementById("reemailer_equal");
var reemailer = document.getElementById("remailer");
var Passworder = document.getElementById("Passworder");
var rePassworder_equal = document.getElementById("rePassworder_equal");
var rePassworder = document.getElementById("rePassworder");
var seier = document.getElementById("seier");
var meier = document.getElementById("meier");
var sei_kanaer = document.getElementById("sei-kanaer");
var mei_kanaer = document.getElementById("mei-kanaer");
var usernameer = document.getElementById("usernameer");
var telphoneer = document.getElementById("telphoneer");
var yuubiner = document.getElementById("yuubiner");
var addresser = document.getElementById("addresser");
var imageer = document.getElementById("prof_imageer");

let inputvalue = [email, reemail, Password, rePassword, sei, mei,sei_kana,mei_kana, username, telphone, yuubin,address, image]
let erp = [emailer, reemailer, Passworder, rePassworder, seier,meier, sei_kanaer, mei_kanaer, usernameer, telphoneer, yuubiner,addresser, imageer]
var valuename = {"email":"メールアドレス", "email_conform":"メールアドレス確認", "password":"パスワード","password_conform":"パスワード確認","sei":"性","mei":"名", "sei-kana":"姓カナ", "mei-kana":"名カナ" , "username":"ユーザーネーム", "telphone":"電話番号", "yuubin":"郵便番号","address":"住所", "prof_image":"画像"};



function signinsub() {
    

    for(let i = 0; i < inputvalue.length; i++) { 
        if(inputvalue[i].value == false) {
            erp[i].className = 'seer';
            erp[i].textContent = valuename[inputvalue[i].name] + "を入力して下さい"
            var val = false
        }else{
            erp[i].className = 'hideer';
            erp[i].textContent = ""   
        }
    };


    //ここ関数化したほうがいいかもね
    let forvali = [Password, telphone, yuubin, sei_kana, mei_kana]
    let errbox = [Passworder, telphoneer,yuubiner,sei_kanaer,mei_kanaer]
    let invali = ["^[0-9a-zA-Z]{8,32}$", "^0[5879]0-*[0-9]{4}-*[0-9]{4}$",'^\\d{3}-*\\d{4}$', '[ァ-ヴ]+', '[ァ-ヴ]+']
    let valimsg = ["半角英数字8文字以上32文字以内で入力して下さい","存在する電話番号を入力してください例08022346222","正しい形式で郵便番号を入力してください","姓 カナで入力してください", "名 カナで入力してください"]
    for(let i = 0; i <= 4; i++){
        if(valid(invali[i], forvali[i].value) == null){
            errbox[i].className = "seer"
            errbox[i].textContent = valimsg[i]
            var val = false
        }
        else{
            errbox[i].className = "hideer"
        }
    }
    //equea(比較１, 比較2, 変更を与えるID)
    equal(email,reemail,reemailer_equal)
    equal(Password,rePassword,rePassworder_equal)
    
   

    
    if(val == false){
        return false
    }

        var message = "この内容で、ユーザー登録を行いますか？"      //json.key名   
        return getFunc(message);

                   
};

function valid(invali, num){ //正規表現でバリデーション

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

function equal(content,content2,msg){ //二つの入力値が一致するかの比較

    if(content.value != content2.value){
        msg.textContent =valuename[content.name] + "が一致しません"
        msg.className = "seer"
        val =  false
      }else{
          msg.textContent =""
          msg.className = "hideer"
      }
}



function populateDropdown(selectElement, start, end){
    for (let i = start; i <= end; i++) {
        let option = document.createElement("option");
        option.value = i;
        option.text = i;
        selectElement.appendChild(option);
    }
}


let yearDropdown = document.getElementById("year");
let monthDropdown = document.getElementById("month");
let dayDropdown = document.getElementById("day");

populateDropdown(yearDropdown, 1900, new Date().getFullYear());
populateDropdown(monthDropdown, 1, 12);
populateDropdown(dayDropdown, 1, 31);