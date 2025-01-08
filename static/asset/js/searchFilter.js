console.log(window.location.pathname);

// index page menu searchbar

let input, filter, ul, li, a, b, i;
input = document.querySelector(".search-bar");
div = document.querySelector(".searchBarProductsWrapper");
a = document.querySelectorAll(`.searchBarProduct`);
b=document.querySelectorAll(".searchBarProductTitle")
let searchResults=document.querySelector(`.searchResults`)
searchResults.innerText=`Totall ${a.length}`

function filterFunction() {  

filter = input.value.toUpperCase();
  for (i = 0; i < a.length; i++) {

    let txtValue = b[i].innerText;
    let lightType = b[i].title;
    if (txtValue.toUpperCase().indexOf(filter) > -1 || lightType.toUpperCase().indexOf(filter) > -1) {
      a[i].style.display = "flex";
      a[i].classList.add("matchedWithSearch")
      let totalSearchResult=document.querySelectorAll(".matchedWithSearch")
      searchResults.innerText=`Totall Results ${totalSearchResult.length}`

    } else {
      a[i].style.display = "none";
      a[i].classList.remove("matchedWithSearch")
    }
   

  }

}
