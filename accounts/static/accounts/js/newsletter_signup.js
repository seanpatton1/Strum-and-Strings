document.addEventListener("DOMContentLoaded", function () {
  const form = document.getElementById("newsletter-form");
  const emailInput = document.getElementById("mce-EMAIL");

  if (form && emailInput) {
    form.addEventListener("submit", function (event) {
      const email = emailInput.value.trim();
      const emailPattern = /^[^\s@]+@[^\s@]+\.[^\s@]+$/;

      // Reset any previous validation errors
      emailInput.setCustomValidity('');

      // If invalid email, stop submission
      if (!emailPattern.test(email)) {
        event.preventDefault();
        emailInput.setCustomValidity("Please enter a valid email address.");
        emailInput.reportValidity();
        return;
      }

      // Send email to backend for tracking (if valid)
      navigator.sendBeacon(
        "/accounts/newsletter/save-email/",
        new URLSearchParams({ email: email })
      );
    });
  }
});
