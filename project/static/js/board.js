function chebg(chkID) {
    var checkbox = document.getElementById(chkID);
    var label = checkbox.parentNode;
    var liElement = checkbox.parentNode.parentNode;
    
    if (checkbox.checked) {
        label.style.backgroundColor = '#7d8bae'; // 選択時の背景色
        label.style.color = '#ffffff'; // 文字色
        liElement.style.backgroundColor = "#7d8bae";
    } else {
        label.style.backgroundColor = '#ffffff'; // 未選択時の背景色
        label.style.color = '#333333'; // 文字色
        liElement.style.backgroundColor = "";
    }
}