var JSON_DATA_LIST;
var CURRENT_REVIEW_NUM = 0;

function insertTagsOnPage() {
  info_about_author = document.createElement("h5");
  document.getElementById('review').appendChild(info_about_author);
  message = document.createElement("p");
  document.getElementById('review').appendChild(message);
}


function updateTextOnPage() {
  var author = JSON_DATA_LIST[CURRENT_REVIEW_NUM].author;
  var age = JSON_DATA_LIST[CURRENT_REVIEW_NUM].age;
  var city = JSON_DATA_LIST[CURRENT_REVIEW_NUM].city;
  var message = JSON_DATA_LIST[CURRENT_REVIEW_NUM].message;
  c = document.getElementById('review').childNodes;
  //Нулевым элементов всегда идёт пустой текст, поэтому работает со слдедующими двумя,
  // которые добавили в insertTagsOnPage
  c[1].innerText = [author, age, city].join(' ');
  c[2].innerText = message;
}


$.getJSON("reviews.json", function (json) {
  JSON_DATA_LIST = json;
  insertTagsOnPage();
  updateTextOnPage();
});


$("#next-review").on("click", function (e) {
  e.preventDefault();
  getNextReview();
});

function getNextReview() {
  CURRENT_REVIEW_NUM = (CURRENT_REVIEW_NUM+1) % JSON_DATA_LIST.length;
  updateTextOnPage();
}

function getPrevReview() {
  if (CURRENT_REVIEW_NUM == 0)
    CURRENT_REVIEW_NUM = JSON_DATA_LIST.length-1;
  else
    CURRENT_REVIEW_NUM = (CURRENT_REVIEW_NUM-1) % JSON_DATA_LIST.length;
  updateTextOnPage();
}

$("#prev-review").on("click", function (e) {
  e.preventDefault();
  getPrevReview();
});

window.setInterval(getNextReview, 10000);