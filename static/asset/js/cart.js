// Function to update total product prices and total amount

function changeTotalBill() {
    let subtotal = 0;
    let totalBill = 0;

    // Re-select all the price elements each time the function is called
    let allTotalPrices = document.querySelectorAll(`.totalPrice`);
    let deliveryCharge = document.querySelector(`.deliveryCharge`);
    
    // Recalculate the total product prices
    allTotalPrices.forEach((eachTotalPrice) => {
        subtotal += Number(eachTotalPrice.innerText);
    });

    // Update the total product prices and total amount
    document.querySelector(`.subtotal`).innerText = `${subtotal}$`;
    totalBill = subtotal + Number(deliveryCharge.innerText);
    document.querySelector(`.totalBill`).innerText = `${totalBill}$`;
}

// Function to attach event listeners to cartItems for deleting them

function attachDeleteListeners() {
    let cartItems = document.querySelectorAll(`.cartItem`);
    let cartItemDeleteBtns = document.querySelectorAll(`.cartItemDeleteBtn`);
    
    cartItemDeleteBtns.forEach((eachCartItemDeleteBtn, index) => {
        eachCartItemDeleteBtn.addEventListener(`click`, (e) => {
            // Remove the corresponding cart item
            cartItems[index].remove();
            
            // Recalculate total product prices
            changeTotalBill();
            
            // Re-attach event listeners after an item is deleted
            attachDeleteListeners();  // Recursively update the listeners
        });
    });
}

// Initial calculation of total prices
changeTotalBill();

// Attach event listeners for the first time
attachDeleteListeners();

// Change cartItems quantity
let QuantityChangingBtn= document.querySelectorAll(`.QuantityChangingBtn`)
QuantityChangingBtn.forEach((eachQuantityChangingBtn)=>{
    eachQuantityChangingBtn.addEventListener(`click`,(e)=>{
        // Recalculate total product prices
        changeTotalBill();
    })
})
