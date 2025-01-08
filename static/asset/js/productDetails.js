// productDetails Page

// hero


let productQuantity= document.querySelectorAll(`.productQuantity`)
let QuantityDecrementBtn= document.querySelectorAll(`.QuantityDecrementBtn`)
let QuantityIncrementBtn= document.querySelectorAll(`.QuantityIncrementBtn`)
let singleProductPrice= document.querySelectorAll(`.singleProductPrice`)
let totalPrice= document.querySelectorAll(`.totalPrice`)

productQuantity.forEach((eachProductQuantity,index)=>{
  
  if(eachProductQuantity.innerText){
    
    if(Number(eachProductQuantity.innerText)==1){
      QuantityDecrementBtn[index].disabled=true
      totalPrice[index].innerText=Number(singleProductPrice[index].innerText) * Number(eachProductQuantity.innerText)

    }else{
      // console.log(Number(singleProductPrice[index].innerText) , Number(eachProductQuantity.innerText))
      totalPrice[index].innerText=Number(singleProductPrice[index].innerText) * Number(eachProductQuantity.innerText)
    }
  }else{
    productQuantity[index].innerText=1
    QuantityDecrementBtn[index].disabled=true
    totalPrice[index].innerText=Number(singleProductPrice[index].innerText) * Number(eachProductQuantity.innerText)

  }
})


// function changeProductQuantity(quantity,index){
//   productQuantity[index].innerText=Number(productQuantity[index].innerText) + quantity

//   console.log(`nnkkk`)

//     if(Number(productQuantity[index].innerText)==1){
//         QuantityDecrementBtn[index].disabled=true
//     }else{
//         QuantityDecrementBtn[index].disabled=false
//     }

//     let changedTotalPrice=Number(singleProductPrice[index].innerText) * Number(productQuantity[index].innerText)
//     totalPrice[index].innerText=changedTotalPrice

// }


QuantityIncrementBtn.forEach((eachQuantityIncrementBtn,index)=>{
  eachQuantityIncrementBtn.addEventListener(`click`,(e)=>{
    let quantity= +1
    productQuantity[index].innerText=Number(productQuantity[index].innerText) + quantity

  
      if(Number(productQuantity[index].innerText)==1){
          QuantityDecrementBtn[index].disabled=true
      }else{
          QuantityDecrementBtn[index].disabled=false
      }
  
      let changedTotalPrice=Number(singleProductPrice[index].innerText) * Number(productQuantity[index].innerText)
      totalPrice[index].innerText=changedTotalPrice
  
  })
})
QuantityDecrementBtn.forEach((eachQuantityDecrementBtn,index)=>{
  eachQuantityDecrementBtn.addEventListener(`click`,(e)=>{
    let quantity= -1
    productQuantity[index].innerText=Number(productQuantity[index].innerText) + quantity

  
      if(Number(productQuantity[index].innerText)==1){
          QuantityDecrementBtn[index].disabled=true
      }else{
          QuantityDecrementBtn[index].disabled=false
      }
  
      let changedTotalPrice=Number(singleProductPrice[index].innerText) * Number(productQuantity[index].innerText)
      totalPrice[index].innerText=changedTotalPrice
  
  })
})



// Details and Description section

const productDetailsTogglers =document.querySelectorAll(`.productDetailsToggler`)
const productDetails =document.querySelectorAll(`.productDetail`)

productDetailsTogglers.forEach((eachProductDetailsTogglers,index)=>{
  eachProductDetailsTogglers.addEventListener(`click`,(e)=>{
    
    productDetailsTogglers.forEach((oneProductToggler)=>{
      oneProductToggler.classList.remove(`productDetailsTogglerAnimation`)
    })
    productDetailsTogglers[index].classList.add(`productDetailsTogglerAnimation`)
    
    productDetails.forEach((eachProductDetails)=>{
      // eachProductDetails.classList.remove(`d-flex`)
      eachProductDetails.classList.toggle(`d-none`,true)
    })
    productDetails[index].classList.remove(`d-none`)
    productDetails[index].classList.toggle(`d-flex`,true)
  })
})