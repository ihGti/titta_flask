var email = document.getElementById("email");
var reemail = document.getElementById("reemail");
var Password = document.getElementById("Password");
var rePassword = document.getElementById("rePassword");
var username = document.getElementById("username");
var telphone = document.getElementById("telphone");
var yuubin = document.getElementById("yuubin");
var address = document.getElementById("address");
var image = document.getElementById("prof_image");
let inputvalue = [email, reemail, Password, rePassword,username, telphone, yuubin,address, image]
var valuename = {"email":"メールアドレス", "email_conform":"メールアドレス", "password":"パスワード","password_conform":"パスワード確認" , "username":"ユーザーネーム", "telphone":"電話番号", "yuubin":"郵便番号","address":"住所", "prof_image":"画像"};




function signinsub() {
    for(let i = 0; i < inputvalue.length; i++) { 
        var a = inputvalue[i].name
        if(inputvalue[i].value == false) {
            window.alert(valuename[a] + "の項目が未入力です");
            return false
        }};

    if(valid(3,Password.value) == null){
        window.alert("半角英数字8文字以上32文字以下でよろしく")
        return false
    }

        
    if(valid(2, telphone.value) == null){
        window.alert("電話番号が正しい形式ではありません")
        return false
    };

    if(valid(1, yuubin.value) == null){
        window.alert("郵便番号が正しい形式ではありません")
        return false
    };

    if(email.value != reemail.value){
        window.alert("メールアドレスが一致しません")
        return false
    }else if(Password.value != rePassword.value){
        window.alert("passwordが一致しません")
        return false
    }else{

    var message = "この内容で、ユーザー登録を行いますか？"      //json.key名   
    return getFunc(message);

    }               
};

function valid(select, num){

    var yubin = new RegExp('\\d{3}-\\d{4}');
    var phone = new RegExp("0[589]0-[0-9]{4}-[0-9]{4}");
    var pass = new RegExp("[0-9a-zA-Z]{8,32}");
    var postcode = num;
    if(select == 1){
        var result = postcode.match(yubin);

    }else if(select == 2){
        var result = postcode.match(phone);
    }else if(select == 3){
        var result = postcode.match(pass);
    };
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