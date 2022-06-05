const sortByDate = document.querySelector(".sortByDate")
const sortByLike = document.querySelector(".sortByLike")

//최신순 정렬 -> 문제는 검색값, 필터값과 중복 안됨. 현재는 있는 내용을 지우고 다시 불러오는 형태
$(".sortByDate").on("click", function() {
  Array.from($(".filter-value")).forEach(value => value.classList.remove("current"))

  sortByLike.classList.remove("current")
  sortByDate.classList.add("current")
  $.ajax({
    type: "GET",
    url: "/list/order",
    data: {click_give: '최신순'},
    success: function (response) {
      $('.card-group').empty();
        let recipes = response['filtered_data']
        for (let i = 0; i < recipes.length; i++) {
            let name = recipes[i]['recipe_name']
            let img = recipes[i]['recipe_img']
            let like = recipes[i]['recipe_like']
            let writter = recipes[i]['recipe_writter']
            let temp_html = `<div class="col">
            <div class="card">
              <div class="card-img-div">
                  <img
                    src="${img}"
                    class="card-img-top"
                    alt="..."
                  />
              </div>
              <div class="card-body">
                <div class="card-info">
                  <a href="#" class="recipe-link"
                    ><span class="card-title" 
                      >${name}</span
                    ></a
                  >
                  <div class="card-bottom-row">
                    <span class="card-text">${writter}</span>
                    <div class="like-div">
                      <span class="like-text">추천</span>
                      <span class="like-num">${like}</span>
                    </div>
                  </div>
                </div>
                <div class="card-like">
                  <i class="fa-regular fa-thumbs-up like-icon"></i>
                </div>
              </div>
            </div>
          </div>`
            $('.card-group').append(temp_html)
        }
        let recipe_name = "";
                $('.card-title').on('click', function () {
                    recipe_name = $(this).text()
                    console.log(recipe_name)
                })

                $(document).on('click', '.card-title', function () {
                    if (recipe_name != null) {
                        document.location.href = `/detail?recipe_name=${recipe_name}`;
                    }
                })
        $('.spinner-border').hide();
        $('#searchInfo').empty();
    }
})
})

//인기순 정렬 -> 문제는 검색값, 필터값과 중복 안됨. 현재는 있는 내용을 지우고 다시 불러오는 형태
$(".sortByLike").on("click", function() {
  Array.from($(".filter-value")).forEach(value => value.classList.remove("current"))

  sortByDate.classList.remove("current")
  sortByLike.classList.add("current")
  $.ajax({
    type: "GET",
    url: "/list/order",
    data: {click_give: '추천순'},
    success: function (response) {
      $('.card-group').empty();
        let recipes = response['filtered_data']
        for (let i = 0; i < recipes.length; i++) {
            let name = recipes[i]['recipe_name']
            let img = recipes[i]['recipe_img']
            let like = recipes[i]['recipe_like']
            let writter = recipes[i]['recipe_writter']
            let temp_html = `<div class="col">
            <div class="card">
              <div class="card-img-div">
                  <img
                    src="${img}"
                    class="card-img-top"
                    alt="..."
                  />
              </div>
              <div class="card-body">
                <div class="card-info">
                  <a href="#" class="recipe-link"
                    ><span class="card-title"
                      >${name}</span
                    ></a
                  >
                  <div class="card-bottom-row">
                    <span class="card-text">${writter}</span>
                    <div class="like-div">
                      <span class="like-text">추천</span>
                      <span class="like-num">${like}</span>
                    </div>
                  </div>
                </div>
                <div class="card-like">
                  <i class="fa-regular fa-thumbs-up like-icon"></i>
                </div>
              </div>
            </div>
          </div>`
            $('.card-group').append(temp_html)
        }
        let recipe_name = "";
                $('.card-title').on('click', function () {
                    recipe_name = $(this).text()
                    console.log(recipe_name)
                })

                $(document).on('click', '.card-title', function () {
                    if (recipe_name != null) {
                        document.location.href = `/detail?recipe_name=${recipe_name}`;
                    }
                })
        $('.spinner-border').hide();
        $('#searchInfo').empty();
    }
})
})


//검색창 입력(자바스크립트에서 페이크값 내에서 검색되도록 구현함)
$("form").on("submit", function(event){
  event.preventDefault()
  Array.from($(".filter-value")).forEach(value => value.classList.remove("current"))
  sortByLike.classList.remove("current")
  sortByDate.classList.remove("current")
  const inputVal = $("#searchInput").val()
  $.ajax({
    type: "GET",
    url: "/list/search",
    data: {search_give: inputVal},
    success: function (response) {
      $('.card-group').empty();
        let recipes = response['filtered_data']
        for (let i = 0; i < recipes.length; i++) {
            let name = recipes[i]['recipe_name']
            let img = recipes[i]['recipe_img']
            let like = recipes[i]['recipe_like']
            let writter = recipes[i]['recipe_writter']
            let ing = recipes[i]['recipe_ing']
            let diff = recipes[i]['recipe_diff']
            let taste = recipes[i]['recipe_taste']
            let detail = recipes[i]['recipe_detail']
            let info = name + writter + ing + diff + taste + detail;
            if (info.includes(inputVal)) {
            let temp_html = `<div class="col">
            <div class="card">
              <div class="card-img-div">
                  <img
                    src="${img}"
                    class="card-img-top"
                    alt="..."
                  />
              </div>
              <div class="card-body">
                <div class="card-info">
                  <a href="#" class="recipe-link"
                    ><span class="card-title"
                      >${name}</span
                    ></a
                  >
                  <div class="card-bottom-row">
                    <span class="card-text">${writter}</span>
                    <div class="like-div">
                      <span class="like-text">추천</span>
                      <span class="like-num">${like}</span>
                    </div>
                  </div>
                </div>
                <div class="card-like">
                  <i class="fa-regular fa-thumbs-up like-icon"></i>
                </div>
              </div>
            </div>
          </div>`
            $('.card-group').append(temp_html)}
        }
        let recipe_name = "";
                $('.card-title').on('click', function () {
                    recipe_name = $(this).text()
                    console.log(recipe_name)
                })

                $(document).on('click', '.card-title', function () {
                    if (recipe_name != null) {
                        document.location.href = `/detail?recipe_name=${recipe_name}`;
                    }
                })
        const count = $('.card').length
        const searchInfo = `총 ${count}개의 "${inputVal}" 레시피가 있습니다.`
        $('#searchInfo').empty();
        $('#searchInfo').append(searchInfo);
        $('.spinner-border').hide();



    }
})
})


//필터 선택값 불러오기 -> TasteFilter만 작동함
function onTasteFilter(event) {
  Array.from($(".filter-value")).forEach(value => value.classList.remove("current"))
  $('#searchInfo').empty();
  sortByLike.classList.remove("current")
  sortByDate.classList.remove("current")
  event.target.classList.add("current")
  const value = event.target.innerText
  // const key = event.target.parentElement.id
  console.log(value)   //recipe_taste, 달달 이런식으로 값 가져옴
  $.ajax({
    type: "GET",
    url: "/list/filter",
    data: {taste_give:value, ing_give:null, diff_give:null, time_give:null},
    success: function (response) {
      $('.card-group').empty();
      $('.spinner-border').hide();
        let recipes = response['filtered_data'][0]
        for (let i = 0; i < recipes.length; i++) {
            let name = recipes[i]['recipe_name']
            let img = recipes[i]['recipe_img']
            let like = recipes[i]['recipe_like']
            let writter = recipes[i]['recipe_writter']
            let temp_html = `<div class="col">
            <div class="card">
              <div class="card-img-div">
                  <img
                    src="${img}"
                    class="card-img-top"
                    alt="..."
                  />
              </div>
              <div class="card-body">
                <div class="card-info">
                  <a href="#" class="recipe-link"
                    ><span class="card-title"
                      >${name}</span
                    ></a
                  >
                  <div class="card-bottom-row">
                    <span class="card-text">${writter}</span>
                    <div class="like-div">
                      <span class="like-text">추천</span>
                      <span class="like-num">${like}</span>
                    </div>
                  </div>
                </div>
                <div class="card-like">
                  <i class="fa-regular fa-thumbs-up like-icon"></i>
                </div>
              </div>
            </div>
          </div>`
            $('.card-group').append(temp_html)
        }
        let recipe_name = "";
                $('.card-title').on('click', function () {
                    recipe_name = $(this).text()
                    console.log(recipe_name)
                })

                $(document).on('click', '.card-title', function () {
                    if (recipe_name != null) {
                        document.location.href = `/detail?recipe_name=${recipe_name}`;
                    }
                })
    }
})
}

function onIngFilter(event) {
  Array.from($(".filter-value")).forEach(value => value.classList.remove("current"))
  $('#searchInfo').empty();
  sortByLike.classList.remove("current")
  sortByDate.classList.remove("current")
  const value = event.target.innerText
  // const key = event.target.parentElement.id
  console.log(value)   //recipe_taste, 달달 이런식으로 값 가져옴
  $.ajax({
    type: "GET",
    url: "/list/filter",
    data: {taste_give:null, ing_give:value, diff_give:null, time_give:null},
    success: function (response) {
      $('.card-group').empty();
      $('.spinner-border').hide();
        let recipes = response['filtered_data'][0]
        for (let i = 0; i < recipes.length; i++) {
            let name = recipes[i]['recipe_name']
            let img = recipes[i]['recipe_img']
            let like = recipes[i]['recipe_like']
            let writter = recipes[i]['recipe_writter']
            let temp_html = `<div class="col">
            <div class="card">
              <div class="card-img-div">
                  <img
                    src="${img}"
                    class="card-img-top"
                    alt="..."
                  />
              </div>
              <div class="card-body">
                <div class="card-info">
                  <a href="#" class="recipe-link"
                    ><span class="card-title"
                      >${name}</span
                    ></a
                  >
                  <div class="card-bottom-row">
                    <span class="card-text">${writter}</span>
                    <div class="like-div">
                      <span class="like-text">추천</span>
                      <span class="like-num">${like}</span>
                    </div>
                  </div>
                </div>
                <div class="card-like">
                  <i class="fa-regular fa-thumbs-up like-icon"></i>
                </div>
              </div>
            </div>
          </div>`
            $('.card-group').append(temp_html)
        }
        let recipe_name = "";
                $('.card-title').on('click', function () {
                    recipe_name = $(this).text()
                    console.log(recipe_name)
                })

                $(document).on('click', '.card-title', function () {
                    if (recipe_name != null) {
                        document.location.href = `/detail?recipe_name=${recipe_name}`;
                    }
                })
    }
})
}

function onTimeFilter(event) {
  Array.from($(".filter-value")).forEach(value => value.classList.remove("current"))
  $('#searchInfo').empty();
  sortByLike.classList.remove("current")
  sortByDate.classList.remove("current")
  const value = event.target.innerText
  // const key = event.target.parentElement.id
  console.log(value)   //recipe_taste, 달달 이런식으로 값 가져옴
  $.ajax({
    type: "GET",
    url: "/list/filter",
    data: {taste_give:null, ing_give:null, diff_give:null, time_give:value},
    success: function (response) {
      $('.card-group').empty();
      $('.spinner-border').hide();
        let recipes = response['filtered_data'][0]
        for (let i = 0; i < recipes.length; i++) {
            let name = recipes[i]['recipe_name']
            let img = recipes[i]['recipe_img']
            let like = recipes[i]['recipe_like']
            let writter = recipes[i]['recipe_writter']
            let temp_html = `<div class="col">
            <div class="card">
              <div class="card-img-div">
                  <img
                    src="${img}"
                    class="card-img-top"
                    alt="..."
                  />
              </div>
              <div class="card-body">
                <div class="card-info">
                  <a href="#" class="recipe-link"
                    ><span class="card-title"
                      >${name}</span
                    ></a
                  >
                  <div class="card-bottom-row">
                    <span class="card-text">${writter}</span>
                    <div class="like-div">
                      <span class="like-text">추천</span>
                      <span class="like-num">${like}</span>
                    </div>
                  </div>
                </div>
                <div class="card-like">
                  <i class="fa-regular fa-thumbs-up like-icon"></i>
                </div>
              </div>
            </div>
          </div>`
            $('.card-group').append(temp_html)
        }
        let recipe_name = "";
                $('.card-title').on('click', function () {
                    recipe_name = $(this).text()
                    console.log(recipe_name)
                })

                $(document).on('click', '.card-title', function () {
                    if (recipe_name != null) {
                        document.location.href = `/detail?recipe_name=${recipe_name}`;
                    }
                })
    }
})
}

function onDiffFilter(event) {
  Array.from($(".filter-value")).forEach(value => value.classList.remove("current"))
  $('#searchInfo').empty();
  sortByLike.classList.remove("current")
  sortByDate.classList.remove("current")
  const value = event.target.innerText
  // const key = event.target.parentElement.id
  console.log(value)   //recipe_taste, 달달 이런식으로 값 가져옴
  $.ajax({
    type: "GET",
    url: "/list/filter",
    data: {taste_give:null, ing_give:null, diff_give:value, time_give:null},
    success: function (response) {
      $('.card-group').empty();
      $('.spinner-border').hide();
        let recipes = response['filtered_data'][0]
        for (let i = 0; i < recipes.length; i++) {
            let name = recipes[i]['recipe_name']
            let img = recipes[i]['recipe_img']
            let like = recipes[i]['recipe_like']
            let writter = recipes[i]['recipe_writter']
            let temp_html = `<div class="col">
            <div class="card">
              <div class="card-img-div">
                  <img
                    src="${img}"
                    class="card-img-top"
                    alt="..."
                  />
              </div>
              <div class="card-body">
                <div class="card-info">
                  <a href="#" class="recipe-link"
                    ><span class="card-title"
                      >${name}</span
                    ></a
                  >
                  <div class="card-bottom-row">
                    <span class="card-text">${writter}</span>
                    <div class="like-div">
                      <span class="like-text">추천</span>
                      <span class="like-num">${like}</span>
                    </div>
                  </div>
                </div>
                <div class="card-like">
                  <i class="fa-regular fa-thumbs-up like-icon"></i>
                </div>
              </div>
            </div>
          </div>`
            $('.card-group').append(temp_html)
        }
        let recipe_name = "";
                $('.card-title').on('click', function () {
                    recipe_name = $(this).text()
                    console.log(recipe_name)
                })

                $(document).on('click', '.card-title', function () {
                    if (recipe_name != null) {
                        document.location.href = `/detail?recipe_name=${recipe_name}`;
                    }
                })
    }
})
}

Array.from($("#recipe_taste .filter-value")).forEach(value => value.addEventListener("click", onTasteFilter))
Array.from($("#recipe_ing .filter-value")).forEach(value => value.addEventListener("click", onIngFilter))
Array.from($("#recipe_time .filter-value")).forEach(value => value.addEventListener("click", onTimeFilter))
Array.from($("#recipe_diff .filter-value")).forEach(value => value.addEventListener("click", onDiffFilter))


//처음 데이터 출력
$(document).ready(function() {
  $('.d-flex').hide()
  showRecipes();
  setTimeout(loadMore, 2000)
})

//처음 데이터 출력
function showRecipes() {
    $.ajax({
        type: "GET",
        url: "/list/data",
        data: {scroll_give:"off"},
        success: function (response) {
            let recipes = response['append_data'][0]
            for (let i = 0; i < recipes.length; i++) {
                let name = recipes[i]['recipe_name']
                let img = recipes[i]['recipe_img']
                let like = recipes[i]['recipe_like']
                let writter = recipes[i]['recipe_writter']
                let temp_html = `<div class="col">
                <div class="card">
                  <div class="card-img-div">
                      <img
                        src="${img}"
                        class="card-img-top"
                        alt="..."
                      />
                  </div>
                  <div class="card-body">
                    <div class="card-info">
                      <a href="#" class="recipe-link"
                        ><span class="card-title"
                          >${name}</span
                        ></a
                      >
                      <div class="card-bottom-row">
                        <span class="card-text">${writter}</span>
                        <div class="like-div">
                          <span class="like-text">추천</span>
                          <span class="like-num">${like}</span>
                        </div>
                      </div>
                    </div>
                    <div class="card-like">
                      <i class="fa-regular fa-thumbs-up like-icon"></i>
                    </div>
                  </div>
                </div>
              </div>`
                $('.card-group').append(temp_html)



                let recipe_name = "";
                $('.card-title').on('click', function () {
                    recipe_name = $(this).text()
                    console.log(recipe_name)
                })

                $(document).on('click', '.card-title', function () {
                    if (recipe_name != null) {
                        document.location.href = `/detail?recipe_name=${recipe_name}`;
                    }
                })

            }
          $('.d-flex').show()
        }
    })

}

//스크롤 내릴때 더 불러옴
function loadMore() {
 // 스크롤이 맨 밑까지 가면 실행 되는 조건문
const target = document.querySelector(".spinner-border")
const option = {
  rootMargin: '0px'
}
const callback = (entry, observer) => {
  if(entry[0].isIntersecting) {
    console.log("load more!")
    $('.d-flex').empty()
    $.ajax({
      type: "GET",
      url: "/list/data",
      data: {scroll_give:"on"},
      success: function (response) {
          let recipes = response['append_data'][0]
          for (let i = 0; i < recipes.length; i++) {
              let name = recipes[i]['recipe_name']
              let img = recipes[i]['recipe_img']
              let like = recipes[i]['recipe_like']
              let writter = recipes[i]['recipe_writter']
              let temp_html = `<div class="col">
              <div class="card">
                <div class="card-img-div">
                    <img
                      src="${img}"
                      class="card-img-top"
                      alt="..."
                    />
                </div>
                <div class="card-body">
                  <div class="card-info">
                    <a href="#" class="recipe-link"
                      ><span class="card-title"
                        >${name}</span
                      ></a
                    >
                    <div class="card-bottom-row">
                      <span class="card-text">${writter}</span>
                      <div class="like-div">
                        <span class="like-text">추천</span>
                        <span class="like-num">${like}</span>
                      </div>
                    </div>
                  </div>
                  <div class="card-like">
                    <i class="fa-regular fa-thumbs-up like-icon"></i>
                  </div>
                </div>
              </div>
            </div>`
              $('.card-group').append(temp_html)

              let recipe_name = "";
              $('.card-title').on('click', function () {
                  recipe_name = $(this).text()
                  console.log(recipe_name)
              })

              $(document).on('click', '.card-title', function () {
                  if (recipe_name != null) {
                      document.location.href = `/detail?recipe_name=${recipe_name}`;
                  }
              })

          }

      }
  })
  }
}
const observer = new IntersectionObserver(callback, option);
observer.observe(target)
}

// //좋아요 처음 누르면 +1, 다시 누르면 -1
// const likeIcon = document.querySelector(".like-icon")
// function onLike(event) {
//     const parent = event.target.parentElement.parentElement;
//     let likeNum = parent.querySelector(".like-num")
//     if (likeIcon.classList.contains("liked")) {
//         likeNum.innerText = parseInt(likeNum.innerText) - 1
//         likeIcon.classList.remove("liked")
//     } else {
//         likeNum.innerText = parseInt(likeNum.innerText) + 1
//         likeIcon.classList.add("liked")
//     }
// }
// likeIcon.addEventListener("click", onLike);