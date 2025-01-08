// slider

let slider = document.querySelectorAll(`.slider`);
let firstCardWidth = document.querySelectorAll(`.firstCard`);
let sliderPrevButton = document.querySelectorAll(`.sliderPrevButton`);
let sliderNextButton = document.querySelectorAll(`.sliderNextButton`);

// console.log(slider[0].scrollWidth)
// console.log(slider[0].clientWidth)

sliderNextButton.forEach((eachSliderNextButton, index) => {
  setInterval(() => {
    if (slider[index].scrollWidth <= slider[index].clientWidth) {
      sliderNextButton[index].style.display = `none`;
    } else {
      sliderNextButton[index].style.display = `inline-block`;
    }
  }, 1000);

  eachSliderNextButton.addEventListener(`click`, (e) => {
    slider[index].scrollLeft += firstCardWidth[index].offsetWidth;
  });
});
sliderPrevButton.forEach((eachSliderPrevButton, index) => {
  setInterval(() => {
    if (slider[index].scrollWidth <= slider[index].clientWidth) {
      sliderPrevButton[index].style.display = `none`;
    } else {
      sliderPrevButton[index].style.display = `inline-block`;
    }
  }, 1000);
  eachSliderPrevButton.addEventListener(`click`, (e) => {
    slider[index].scrollLeft += -firstCardWidth[index].offsetWidth;
  });
});