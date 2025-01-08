// filter range

const rangeInputs=document.querySelectorAll(`.rangeInput`)
rangeInputs.forEach((eachRangeInput,index)=>{
  document.getElementById(`rangeOutput${index}`).innerText=`${eachRangeInput.min} - ${eachRangeInput.value}`
  eachRangeInput.addEventListener(`input`,(e)=>{
    let rangeValue=e.target.value
    let rangeMinimumValue=e.target.min

    document.getElementById(`rangeOutput${index}`).innerText=`${rangeMinimumValue} - ${rangeValue}`

  })
})


// filter details toggling 

// const detailsTogglers = document.querySelectorAll(".detailsToggler");
// const details = document.querySelectorAll(".details");
// const viewDetails = document.querySelectorAll(".viewDetails");
// const HideDetails = document.querySelectorAll(".HideDetails");
// detailsTogglers.forEach((eachDetailsToggler, index) => {
//   eachDetailsToggler.addEventListener("click", (e) => {
//     details[index].classList.toggle("detailsToggleAnimation");

//     detailsTogglers[index].classList.toggle("togglerAnimation");

//     viewDetails[index].classList.toggle("d-none");

//     HideDetails[index].classList.toggle("d-none");

//     detailsTogglers[index].firstElementChild.classList.toggle(
//       "togglerAnimation"
//     );
//   });
// });