function showTab(tabId) {
  const contents = document.querySelectorAll(".content");
  const tabs = document.querySelectorAll(".tab");

  contents.forEach((c) => c.classList.remove("active"));
  tabs.forEach((t) => t.classList.remove("active"));

  document.getElementById(tabId).classList.add("active");
  event.target.classList.add("active");
}
