    
const objpath = {"bicy":"/static/models/bicycle.obj","bottle":"/static/models/14042_750_mL_Wine_Bottle_r_v1_L3.obj"}


//もっと見るボタン要素
const moreBtn = document.querySelector("button");
window.addEventListener('DOMContentLoaded', draw);


//クリックしたら
moreBtn.addEventListener("click", () => {
  //もっと見るボタンの隣の要素を取得（本文）
  const prev = moreBtn.previousElementSibling; //activeクラスを付与・解除

  if (prev.classList.contains("active") === true) {
    prev.classList.remove("active");
    moreBtn.textContent = "もっと見る";
  } else {
    prev.classList.add("active");
    moreBtn.textContent = "閉じる";
  }
});

// リンク要素を取得
const popupLink = document.getElementById("popup-link");

// ポップアップコンテナ要素を取得
const popupContainer = document.getElementById("popup-container");

// 閉じるボタン要素を取得
const closeButton = document.getElementById("close-button");

const a = document.getElementById("saizukankakuninnBox")
const b = document.getElementById("bicy")
const c = document.getElementById("bottle")

// リンクをクリックしたときの処理
popupLink.addEventListener("click", function (e) {
  e.preventDefault(); // リンクのデフォルト動作を無効化
  popupContainer.style.display = "flex"; // ポップアップを表示
  popupLink.style.display = "none"
  a.style.display = "flex"
  b.style.display = "flex"
  c.style.display = "flex"
});
// 閉じるボタンをクリックしたときの処理
closeButton.addEventListener("click", function () {
  popupLink.style.display = "flex"
  popupContainer.style.display = "none"; // ポップアップを非表示
  a.style.display = "none"; // ポップアップを非表示
  b.style.display = "none"; // ポップアップを非表示
  c.style.display = "none"; // ポップアップを非表示
});




function draw() {
  

  //DBから引っ張ってきて代入して
  objhi = 400;
  objwid = 180;
  color = 0xFF0000;

  //比較モデルの初期設定
  var nmodel = "bicy";
  //高さ、横幅、色,初期のモデル
  three(objhi,objwid, color,nmodel)
  
      
 }










//3d操作 
 three = (objhi,objwid, color,nmodel) =>{ 
  //こっから初期設定多分触んない
  object = (objhi,objwid,color,boo) => {

    //こっから好みで触って
  
    //オブジェクト生成(高さ,横幅、x,y座標、色)
      //商品
      if (boo == false){
         exobj = objadd(objhi,objwid,exx,objhi/2-50,color)

      }else{
         exobj = objadd(objhi,objwid,exx,objhi/2,color)

      }
      //変数名ぶち込んで
      scene.add(exobj);  
    }; 
  
  


  const width = 480;
  const height = 300;

  // レンダラーを作成
  const renderer = new THREE.WebGLRenderer({
    canvas: document.querySelector('#canvas')
  });
  renderer.setSize(width, height);
  renderer.setPixelRatio(window.devicePixelRatio);

  // シーンを作成
  const scene = new THREE.Scene();
  const camera = new THREE.PerspectiveCamera(45, width / height, 1, 10000);

  // カメラの初期座標
  camera.position.set(0, 0, 750);  
  //カメラ操作
  controls = new THREE.OrbitControls(camera, renderer.domElement);

  
  //光、気に食わないなら調節して
  const ambientLight = new THREE.AmbientLight(0xffffff, 0.5)
  const pointLight = new THREE.DirectionalLight(0xffffff, 0.8)
  pointLight.position.set(2, 3)
  scene.add(ambientLight,pointLight);

  scene.background = new THREE.Color( 0x000000 );

    
  //座標系のあれ、触んなくていい
  var exx = objwid
  //触るなら計算して

//ここまで初期設定





    // 3Dモデルの読み込み 
  modelobj = (nmodel) =>{
      
    const objLoader = new THREE.OBJLoader();
    objLoader.load(
      objpath[nmodel],
      function (obj) {
        scene.add(obj);
        
        const box = new THREE.Box3().setFromObject(obj);
        const height = box.max.y - box.min.y;
        var objy = (height)/2

        if(nmodel == "bicy"){
          obj.rotation.set(0,1.5,0 );
          obj.scale.set(10,10,10);

        }else if(nmodel == "bottle"){
        obj.rotation.set(-1.5,0,0 );
        obj.scale.set(2,2,2);
        
        };
        const x = -(objwid)

        obj.position.x = x;
        obj.position.y = objy - 100;
      },
    );
    


  };



  modelobj(nmodel)

  object(objhi,objwid,color,true)


  function animate(time) {
    time *= 0.001;//フレームレート的な
    renderer.render(scene, camera);
    requestAnimationFrame(animate)
  } 
  






  
  animate();
 
}


function objBtn (button){ 
  nmodel = button.id
  three(objhi,objwid, color,nmodel)
}


//これなんか忘れた
loader = (path,objhi,objwid) =>{
};







  //アニメーションっていうかそんな感じのやつ





//ここ触んなくていいよ
objadd = (objhigh,objwid , x,y, color) =>{

    
  const geometry = new THREE.BoxGeometry(objwid,objhigh,objwid);
  const material = new THREE.MeshToonMaterial({
    color: color,
    visible: true,
    transparent: true,
    opacity: 1,
    wireframe: false,
  });
  const box = new THREE.Mesh(geometry, material);  

  box.position.x = x;
  box.position.y = y-100;
  return box
}







//2D表示だけど使わないんじゃない？
/*
two = () => {
    
  text  = (text, x,y) =>{ //座標を文字列の中央
    var xwidth = ctx.measureText( text ).width 
    xwidth = x - (xwidth/2)
    ctx.fillText(text,x,y)
  }


  var canvas = document.getElementById("canvas");
  if (canvas.getContext) {
    var ctx = canvas.getContext("2d");
    ctx.font = '20px Roboto medium';
    ctx.fillStyle = 'white'
  
    
      //DB側終わったら変えて
    //var x=(16+"cm")
    x = 20
    x2 = 10
    var y=(x+"cm")
    //var x2=(40+"cm")
    var y2=(x2+"cm")
    var equal = x2/x
    

  
    ctx.beginPath(); 
    ctx.rect(75, 280, 125, -150);
    ctx.fill();
    //text(x,115,250);
    text(y,0,225); 

    ctx.beginPath();
    ctx.rect(315, 280, 125, -150 * equal);
    ctx.fill();
    //text(x2,355,250);
    text(y2,240,225);
  }
}
*/
