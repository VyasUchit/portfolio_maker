function showContent(tabId, element) {
  // Hide all content
  document.querySelectorAll('.content-box').forEach(box => {
    box.classList.remove('active');
  });

  // Show target
  const target = document.getElementById(tabId);
  if (target) {
    target.classList.add('active');
  }

  // Remove nav-link active highlight
  document.querySelectorAll('.nav-link').forEach(link => link.classList.remove('active'));

  // Add active to clicked link
  if (element) element.classList.add('active');
}
function showContent(tabId, element) {
  document.querySelectorAll('.content-box').forEach(box => box.classList.remove('active'));
  document.getElementById(tabId).classList.add('active');

  document.querySelectorAll('.nav-link').forEach(link => link.classList.remove('active'));
  if (element) element.classList.add('active');
}
