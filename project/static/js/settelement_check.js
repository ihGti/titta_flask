function viewChange(){
    if(document.getElementById('point')){
        id = document.getElementById('point').value;
        if(id == 'yes'){
            document.getElementById('Box').style.display = "";
        }else if(id == 'no'){
            document.getElementById('Box').style.display = "none";
        }
    }
window.onload = viewChange;
}


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