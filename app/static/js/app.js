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

/**
 * Helper function to trigger a PDF file download in the browser using jsPDF.
 * @param {string} filename - The name of the file to save (e.g. 'matrix_solution.pdf')
 * @param {string} title - Title header inside the PDF document
 * @param {string} textContent - The step-by-step solution text content
 */
function downloadPdfFile(filename, title, textContent) {
  try {
    if (window.jspdf && window.jspdf.jsPDF) {
      const { jsPDF } = window.jspdf;
      const doc = new jsPDF();
      
      // Header Bar
      doc.setFillColor(33, 37, 41);
      doc.rect(0, 0, 210, 22, "F");
      
      doc.setTextColor(255, 255, 255);
      doc.setFont("helvetica", "bold");
      doc.setFontSize(13);
      doc.text(title || "Linear Algebra Detailed Solution", 14, 14);
      
      doc.setTextColor(33, 37, 41);
      doc.setFont("courier", "normal");
      doc.setFontSize(9.5);
      
      const lines = doc.splitTextToSize(textContent, 180);
      let y = 30;
      const lineHeight = 4.8;
      const pageHeight = doc.internal.pageSize.height;
      
      for (let i = 0; i < lines.length; i++) {
        if (y + lineHeight > pageHeight - 15) {
          doc.addPage();
          y = 20;
        }
        doc.text(lines[i], 14, y);
        y += lineHeight;
      }
      
      const pageCount = doc.internal.getNumberOfPages();
      doc.setFont("helvetica", "italic");
      doc.setFontSize(8);
      doc.setTextColor(120, 120, 120);
      for (let i = 1; i <= pageCount; i++) {
        doc.setPage(i);
        doc.text(`Linear Algebra Solver — Page ${i} of ${pageCount}`, 14, pageHeight - 8);
      }
      
      doc.save(filename.endsWith(".pdf") ? filename : `${filename}.pdf`);
    } else {
      window.print();
    }
  } catch (err) {
    console.error("PDF export error:", err);
    alert("Could not generate PDF. Printing page instead.");
    window.print();
  }
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

  // Initialize theme toggle button state on load
  _applyThemeUI();
});

/**
 * Toggle between light and dark theme.
 * Persists choice in localStorage. Applied to <html data-theme="dark">.
 */
function toggleTheme() {
  const html = document.documentElement;
  const isDark = html.getAttribute("data-theme") === "dark";
  if (isDark) {
    html.removeAttribute("data-theme");
    localStorage.setItem("theme", "light");
  } else {
    html.setAttribute("data-theme", "dark");
    localStorage.setItem("theme", "dark");
  }
  _applyThemeUI();
}

function _applyThemeUI() {
  const isDark = document.documentElement.getAttribute("data-theme") === "dark";
  const icon = document.getElementById("themeIcon");
  const label = document.getElementById("themeLabel");
  if (icon) icon.textContent = isDark ? "☀️" : "🌙";
  if (label) label.textContent = isDark ? "Light Mode" : "Dark Mode";
}
