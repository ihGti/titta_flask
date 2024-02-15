document.getElementById("profile_image").addEventListener("click", function () {
  document.getElementById("profile_image_input").click();
});

document
  .getElementById("profile_image_input")
  .addEventListener("change", function () {
    var file = this.files[0];
    if (file) {
      var reader = new FileReader();
      reader.onload = function (e) {
        document.getElementById("profile_image").src = e.target.result;
      };
      reader.readAsDataURL(file);
    }
  });

document
  .getElementById("profile_edit")
  .addEventListener("submit", function (e) {
    e.preventDefault(); // フォームの自動送信を防止
    var formData = new FormData(this);

    if (!formData.get("profile_image")) {
      formData.delete('profile_image');
    }
    // サーバーにデータを送信
    fetch("/prof_edit", {
      method: "POST",
      body: formData,
    })
      .then((response) => response.json())
      .then((data) => {
        // サーバーからのレスポンスを処理
        console.log(data);
        if (data.success) {
          window.location.href = "/myprof";
        }
      })
      .catch((error) => {
        console.error("Error:", error);
      });
  });
