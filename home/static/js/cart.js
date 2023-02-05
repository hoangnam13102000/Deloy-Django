const quantityInput = document.querySelector('.quantity-input');
quantityInput.addEventListener('change', updateTotal);

function updateTotal() {
    const quantity = this.value;
    const price = parseFloat(this.dataset.price);
    const total = quantity * price;
    // Update the total cost in the appropriate element on the page
    document.querySelector('.goods-page-total strong').textContent = total;
}

function updateTotal() {
    const quantity = this.value;
    const itemId = this.dataset.itemId;
    const csrf = document.querySelector('input[name="csrfmiddlewaretoken"]').value;
    const data = { 'quantity': quantity, 'item_id': itemId, 'csrfmiddlewaretoken': csrf };
    fetch(this.href, {
            method: 'POST',
            body: JSON.stringify(data),
            headers: {
                'Content-Type': 'application/json',
                'X-CSRFToken': csrf,
            }
        }).then(response => response.json())
        .then(data => {
            document.querySelector('.goods-page-total strong').textContent = data.total_price;
            document.querySelector('.shopping-total .price').textContent = data.total;
        });
}