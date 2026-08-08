/**
 * Helper function to trigger a plain text (.txt) file download in the browser.
 * @param {string} filename - The name of the file to save (e.g. 'matrix_solution.txt')
 * @param {string} textContent - The plain text string content to download
 */
function downloadTxtFile(filename, textContent) {
  const blob = new Blob([textContent], { type: "text/plain;charset=utf-8" });
  const url = URL.createObjectURL(blob);
  const link = document.createElement("a");
  link.href = url;
  link.download = filename;
  document.body.appendChild(link);
  link.click();
  document.body.removeChild(link);
  URL.revokeObjectURL(url);
}

// Highlight active sidebar navigation item & handle open/close toggle
document.addEventListener("DOMContentLoaded", () => {
  const currentPath = window.location.pathname;
  const navLinks = document.querySelectorAll(".sidebar-wrapper .nav-link");

  navLinks.forEach((link) => {
    const href = link.getAttribute("href");
    if (href === currentPath || (href !== "/" && currentPath.startsWith(href))) {
      link.classList.add("active");
    }
  });

  // Restore sidebar collapse state
  const sidebarState = localStorage.getItem("sidebarState");
  if (sidebarState === "collapsed") {
    document.body.classList.add("sidebar-collapsed");
  }

  // Sidebar toggle handlers
  const closeBtn = document.getElementById("sidebarCloseBtn");
  const openBtn = document.getElementById("sidebarOpenBtn");

  if (closeBtn) {
    closeBtn.addEventListener("click", () => {
      document.body.classList.add("sidebar-collapsed");
      localStorage.setItem("sidebarState", "collapsed");
    });
  }

  if (openBtn) {
    openBtn.addEventListener("click", () => {
      document.body.classList.remove("sidebar-collapsed");
      localStorage.setItem("sidebarState", "open");
    });
  }
});

