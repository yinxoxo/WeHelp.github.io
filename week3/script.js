document.addEventListener("DOMContentLoaded", function () {
  const apiUrl =
    "https://padax.github.io/taipei-day-trip-resources/taipei-attractions-assignment-1";

  //取得網頁數據
  fetch(apiUrl)
    .then((response) => response.json())
    .then((data) => processResults(data.data.results));
});

function processResults(results) {
  const promotions = document.querySelectorAll(
    ".promotion-container .promotion"
  );
  const boxes = document.querySelectorAll(".container .box");
  updatePromotions(promotions, results);
  updateBoxes(boxes, results, promotions.length);
}

//處理小格子
function updatePromotions(promotions, results) {
  promotions.forEach((promotion, index) => {
    if (results[index]) {
      updatePromotion(promotion, results[index]);
    }
  });
}

function updatePromotion(promotion, result) {
  const promotionImg = promotion.querySelector("img");
  const promotionText = promotion.querySelector(".title-text");
  const imageUrl = extractFirstJpgUrl(result.filelist);

  if (imageUrl) {
    promotionImg.src = imageUrl;
    promotionText.textContent = result.stitle;
  }
}

//處理大格子
function updateBoxes(boxes, results, offset) {
  boxes.forEach((box, index) => {
    const resultIndex = index + offset;
    if (results[resultIndex]) {
      updateBox(box, results[resultIndex]);
    }
  });
}

function updateBox(box, result) {
  const boxImg = box.querySelector("img");
  const imageUrl = extractFirstJpgUrl(result.filelist);

  if (imageUrl) {
    boxImg.src = imageUrl;
    let textOverlay = box.querySelector(".text-overlay");
    if (!textOverlay) {
      textOverlay = document.createElement("div");
      textOverlay.className = "text-overlay";
      box.appendChild(textOverlay);
    }
    textOverlay.textContent = result.stitle;
  }
}

// 找到第一個.jpg的網址
function extractFirstJpgUrl(filelist) {
  const images = filelist
    .split("https://")
    .filter((url) => url.includes(".jpg"))
    .map((url) => "https://" + url);
  return images[0];
}
