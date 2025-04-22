document.addEventListener('DOMContentLoaded', function () {
    const keyElement = document.getElementById('id_stripe_public_key');
  
    if (!keyElement) {
      console.warn("Stripe public key element not found – skipping Stripe setup.");
      return;
    }
  
    const stripePublicKey = JSON.parse(keyElement.textContent);
    const stripe = Stripe(stripePublicKey);
  
    const checkoutForm = document.querySelector('#checkout-form');
  
    if (!checkoutForm) {
      console.warn("Checkout form not found.");
      return;
    }
  
    checkoutForm.addEventListener('submit', function (e) {
      e.preventDefault();
  
      const formData = {
        full_name: document.querySelector('#full_name').value,
        email: document.querySelector('#email').value,
        phone: document.querySelector('#phone').value,
        street_address1: document.querySelector('#street_address1').value,
        street_address2: document.querySelector('#street_address2').value,
        country: document.querySelector('#country').value,
        postal_code: document.querySelector('#postal_code').value,
        town_or_city: document.querySelector('#town_or_city').value,
      };
  
      fetch('/cart/create-checkout-session/', {
        method: 'POST',
        headers: {
          'X-CSRFToken': getCookie('csrftoken'),
          'Content-Type': 'application/json'
        },
        body: JSON.stringify(formData)
      })
        .then(response => response.json())
        .then(data => {
          return stripe.redirectToCheckout({ sessionId: data.id });
        })
        .then(result => {
          if (result.error) {
            alert(result.error.message);
          }
        })
        .catch(error => {
          console.error('Stripe Checkout Error:', error);
        });
    });
  
    function getCookie(name) {
      let cookieValue = null;
      if (document.cookie && document.cookie !== '') {
        const cookies = document.cookie.split(';');
        for (let i = 0; i < cookies.length; i++) {
          const cookie = cookies[i].trim();
          if (cookie.substring(0, name.length + 1) === (name + '=')) {
            cookieValue = decodeURIComponent(cookie.substring(name.length + 1));
            break;
          }
        }
      }
      return cookieValue;
    }
  });
  