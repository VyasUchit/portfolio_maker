function showContent(id) {
  // Hide all content boxes
  document.querySelectorAll('.content-box').forEach(box => {
    box.classList.remove('active');
  });

  // Show the selected one
  document.getElementById(id).classList.add('active');
}

