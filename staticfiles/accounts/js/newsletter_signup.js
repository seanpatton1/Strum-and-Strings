document.addEventListener("DOMContentLoaded", function () {
  const form = document.getElementById("newsletter-form");
  const emailInput = document.getElementById("mce-EMAIL");

  if (form && emailInput) {
    form.addEventListener("submit", function (event) {
      const email = emailInput.value;
      if (email) {
        navigator.sendBeacon(
          "/accounts/newsletter/save-email/",
          new URLSearchParams({ email: email })
        );
      }
    });
  }
});
