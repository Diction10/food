function updateCart() {
    let cartItems = document.getElementsByClassName('cart-item');
    let total = 0;

    for (let i = 0; i < cartItems.length; i++) {
        let item = cartItems[i];
        let price = parseFloat(item.querySelector('.item-price').textContent.replace('$', ''));
        let quantity = parseInt(item.querySelector('.quantity').value);
        let itemTotal = price * quantity;
        total += itemTotal;

        item.querySelector('.item-total').textContent = '$' + itemTotal.toFixed(2);
    }

    document.getElementById('total').textContent = 'Total: $' + total.toFixed(2);
}

// Attach event listeners when the page loads
window.addEventListener('load', function() {
    let quantityInputs = document.getElementsByClassName('quantity');
    for (let i = 0; i < quantityInputs.length; i++) {
        quantityInputs[i].addEventListener('change', updateCart);
    }

    updateCart();
});



function checkout() {
   
    // // Get a reference to the anchor tag
    const postLink = document.getElementById('anchor-order');

    // // Add a click event listener
    postLink.addEventListener('click', function(event) {
        event.preventDefault();  // Prevent the default behavior of the anchor tag
        
        // Create a form element
        // const form = document.getElementById('quantity');
        // alert(form)
        // form.method = 'POST';
        // form.action = `/checkout/${item}`; // Replace with your actual endpoint
       let quantity = document.getElementById('quantity');

        alert(quantity.value)
        // form.submit();
        
    //     // Add any necessary form fields
    //     const csrfToken = document.getElementById('quantity');
    //     csrfToken.type = 'hidden';
    //     csrfToken.name = 'csrfmiddlewaretoken';  // Replace with your CSRF token field name
    //     csrfToken.value = 'your-csrf-token-value'; // Replace with the actual CSRF token value
    //     form.appendChild(csrfToken);
        
    // //     // Submit the form
    // //     // document.body.appendChild(form);
    //     form.submit();
    });
}