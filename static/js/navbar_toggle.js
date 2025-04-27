document.addEventListener('DOMContentLoaded', function () {
    var navbarToggler = document.querySelector('.navbar-toggler');
    var navbarCollapse = document.getElementById('navbarNav');
  
    navbarToggler.addEventListener('click', function () {
      var collapseInstance = bootstrap.Collapse.getOrCreateInstance(navbarCollapse);
      collapseInstance.toggle();
    });
  });
  