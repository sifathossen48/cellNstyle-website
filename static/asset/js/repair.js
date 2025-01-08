let serviceReciveMethod =document.querySelectorAll(`.serviceReciveMethod`)

let toogleMethods=()=>{
    serviceReciveMethod.forEach((eachServiceReciveMethod)=>{
        let child=document.querySelector(`.${eachServiceReciveMethod.value}`)

        if(eachServiceReciveMethod.checked){
            child.classList.add(`d-flex`)
            child.hidden=false;
            child.querySelectorAll('input, button, select, textarea').forEach((el) => {
                el.disabled = false;
            });
    
            // console.log(`${eachServiceReciveMethod.value}`)
        }else{
            child.classList.remove(`d-flex`)
            child.hidden=true;
            child.querySelectorAll('input, button, select, textarea').forEach((el) => {
                el.disabled = true;
            });
            // console.log(`.${eachServiceReciveMethod.value}`)
    
        }
    })
}
toogleMethods();




// Function to check if none of the checkboxes are checked

let problemCheckboxes = document.querySelectorAll('.problem');
let method = document.querySelector('.method');

function checkNoneChecked() {
  let noneChecked = true;
  problemCheckboxes.forEach((checkbox) => {
    if (checkbox.checked) {
      noneChecked = false;
    }
  });

  // If none are checked, show the warning
  if (noneChecked) {
    method.classList.add('showMethod');
  } else {
    method.classList.remove('showMethod');
  }
}

checkNoneChecked();


setInterval(() => {
    checkNoneChecked();
  }, 1000);

