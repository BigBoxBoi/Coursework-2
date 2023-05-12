document.querySelectorAll('.toggle-description-btn').forEach(function(button) {
    button.addEventListener('click', function() {
      var target = button.dataset.target;
      document.querySelector(target).classList.toggle('show');
      button.textContent = button.textContent === 'Show Description' ? 'Hide Description' : 'Show Description';
    });
  });