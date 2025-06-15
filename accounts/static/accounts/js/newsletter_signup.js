document.addEventListener("DOMContentLoaded", function () {
  const form = document.getElementById("newsletter-form");
  const emailInput = document.getElementById("mce-EMAIL");

  if (form && emailInput) {
    form.addEventListener("submit", function (event) {
      event.preventDefault();

      const email = emailInput.value.trim();
      const emailPattern = /^[^\s@]+@[^\s@]+\.[^\s@]+$/;
      emailInput.setCustomValidity('');

      if (!emailPattern.test(email)) {
        emailInput.setCustomValidity("Please enter a valid email address.");
        emailInput.reportValidity();
        return;
      }

      // Check if already subscribed
      fetch("/accounts/newsletter/check-email/", {
        method: "POST",
        headers: {
          "Content-Type": "application/x-www-form-urlencoded",
          "X-CSRFToken": getCSRFToken(),
        },
        body: new URLSearchParams({ email: email }),
      })
        .then((res) => res.json())
        .then((data) => {
          if (data.subscribed) {
            alert("This email is already subscribed.");
          } else {
            
            navigator.sendBeacon(
              "/accounts/newsletter/save-email/",
              new URLSearchParams({ email: email })
            );
            
            form.submit();
          }
        })
        .catch((err) => {
          console.error("Error checking email:", err);
          form.submit();
        });
    });
  }

  function getCSRFToken() {
    const name = "csrftoken";
    const cookieValue = document.cookie
      .split("; ")
      .find((row) => row.startsWith(name + "="))
      ?.split("=")[1];
    return cookieValue || "";
  }
});
