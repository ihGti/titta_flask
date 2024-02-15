//もっと見るボタン要素
const moreBtn = document.querySelector("button");
window.addEventListener('DOMContentLoaded', draw);


//クリックしたら
moreBtn.addEventListener("click", () => {
  //もっと見るボタンの隣の要素を取得（本文）
  const prev = moreBtn.previousElementSibling; //activeクラスを付与・解除

  if (prev.classList.contains("active") === true) {
    prev.classList.remove("active");
    moreBtn.textContent = "閉じる";
  } else {
    prev.classList.add("active");
    moreBtn.textContent = "もっと見る";
  }
});

// リンク要素を取得
const popupLink = document.getElementById("popup-link");

// ポップアップコンテナ要素を取得
const popupContainer = document.getElementById("popup-container");

// 閉じるボタン要素を取得
const closeButton = document.getElementById("close-button");

const a = document.getElementById("saizukankakuninnBox")

// リンクをクリックしたときの処理
popupLink.addEventListener("click", function (e) {
  e.preventDefault(); // リンクのデフォルト動作を無効化
  popupContainer.style.display = "flex"; // ポップアップを表示
  popupLink.style.display = "none"
  a.style.display = "flex"
});
// 閉じるボタンをクリックしたときの処理
closeButton.addEventListener("click", function () {
  popupLink.style.display = "flex"
  popupContainer.style.display = "none"; // ポップアップを非表示
  a.style.display = "none"; // ポップアップを非表示
});

var cart = document.getElementById('cart')

cart.addEventListener("click", function(){
  alert('お試し出品機能を楽しめましたか？')
});
function draw() {
  

  //DBから引っ張ってきて代入して
  objhi = 400
  objwid = 300
  color = 0xFF0000
  //高さ、横幅、色
  three(objhi,objwid, color)
  
      
 }












//3d操作 
 three = (objhi,objwid, color) =>{ 
  //こっから初期設定多分触んない


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
  camera.position.set(0, 0, 1500);  
  //カメラ操作
  controls = new THREE.OrbitControls(camera, renderer.domElement);

  
  //光、気に食わないなら調節して
  const ambientLight = new THREE.AmbientLight(0xffffff, 0.5)
  const pointLight = new THREE.DirectionalLight(0xffffff, 0.8)
  pointLight.position.set(2, 3,4)
  scene.add(ambientLight,pointLight);

     
//なくても変わんないような気がする
window.addEventListener("resize", () => {
  sizes.width = window.innerWidth;
  sizes.height = window.innerHeight;
 
  camera.aspect = sizes.width / sizes.height;
  camera.updateProjectionMatrix();
 
  renderer.setSize(sizes.width, sizes.height);
  renderer.setPixelRatio(window.devicePixelRatio);
});


  scene.background = new THREE.Color( 0x000000 );

//ここまで初期設定

object = (objhi,objwid) => {
  
  //座標系のあれ、触んなくていい
  const exx = -250-(objwid /4)
  const deffx = -exx
  //高さをそろえる
  const deffhi = 500
  const objy = (objhi - deffhi)/2
  //ここまで触るなら計算して

  //こっから好みで触って

  //オブジェクト生成(高さ,横幅、x,y座標、色)
  const deffobj = objadd(250,500,deffx,objy,0xFFFFFF)

  //商品
  const exobj = objadd(objhi,objwid,exx,0,color)

  //変数名ぶち込んで
  scene.add(exobj,deffobj);  
 }; 

object(objhi,objwid)





//3dモデル使うなら使って
//    const loader = new THREE.ColladaLoader();
//    loader.load('ファイルまでのパス', collada => {
//    const model = collada.scene;
//    scene.add(model);
//  });
  
  //アニメーション
  function animate(time) {
    time *= 0.001;//フレームレート的な
    renderer.render(scene, camera);
    requestAnimationFrame(animate)
  }
  
  animate();
 
}



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
  box.position.y = y;
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
