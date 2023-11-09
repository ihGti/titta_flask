//もっと見るボタン要素
const moreBtn = document.querySelector("button");

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

// リンクをクリックしたときの処理
popupLink.addEventListener("click", function (e) {
  e.preventDefault(); // リンクのデフォルト動作を無効化
  popupContainer.style.display = "flex"; // ポップアップを表示
});

// 閉じるボタンをクリックしたときの処理
closeButton.addEventListener("click", function () {
  popupContainer.style.display = "none"; // ポップアップを非表示
});
