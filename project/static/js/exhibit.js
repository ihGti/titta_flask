function selectImage(imageId) {
  document.getElementById(imageId).click();
}

function previewImage(inputId, targetImageId) {
  var input = document.getElementById(inputId);
  var targetImage = document.getElementById(targetImageId);
  var reader = new FileReader();

  reader.onload = function(e) {
    targetImage.src = e.target.result;
  }

  reader.readAsDataURL(input.files[0]);
}
