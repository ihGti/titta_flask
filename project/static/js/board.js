function chebg(chkID) {
    var checkbox = document.getElementById(chkID);
    var label = checkbox.parentNode;
    var liElement = checkbox.parentNode.parentNode;
    
    if (checkbox.checked) {
        label.style.backgroundColor = '#ffff00'; // 選択時の背景色
        label.style.color = '#3333333'; // 文字色
        liElement.style.backgroundColor = "#ffff00";
    } else {
        label.style.backgroundColor = '#ffffff'; // 未選択時の背景色
        label.style.color = '#333333'; // 文字色
        liElement.style.backgroundColor = "";
    }
}