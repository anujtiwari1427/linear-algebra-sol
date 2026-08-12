/**
 * Download plain text file.
 */
function downloadTxtFile(filename, textContent) {
  const blob = new Blob([textContent], { type: "text/plain;charset=utf-8" });
  const url = URL.createObjectURL(blob);
  const link = document.createElement("a");
  link.href = url; link.download = filename;
  document.body.appendChild(link); link.click();
  document.body.removeChild(link); URL.revokeObjectURL(url);
}

/**
 * Download PDF file using jsPDF.
 */
function downloadPdfFile(filename, title, textContent) {
  try {
    if (window.jspdf && window.jspdf.jsPDF) {
      const { jsPDF } = window.jspdf;
      const doc = new jsPDF();
      doc.setFillColor(33, 37, 41); doc.rect(0, 0, 210, 22, "F");
      doc.setTextColor(255, 255, 255); doc.setFont("helvetica", "bold"); doc.setFontSize(13);
      doc.text(title || "Linear Algebra Detailed Solution", 14, 14);
      doc.setTextColor(33, 37, 41); doc.setFont("courier", "normal"); doc.setFontSize(9.5);
      const lines = doc.splitTextToSize(textContent, 180);
      let y = 30; const lh = 4.8; const ph = doc.internal.pageSize.height;
      for (let i = 0; i < lines.length; i++) {
        if (y + lh > ph - 15) { doc.addPage(); y = 20; }
        doc.text(lines[i], 14, y); y += lh;
      }
      const pc = doc.internal.getNumberOfPages();
      doc.setFont("helvetica","italic"); doc.setFontSize(8); doc.setTextColor(120,120,120);
      for (let i=1;i<=pc;i++){doc.setPage(i);doc.text(`Linear Algebra Solver \u2014 Page ${i} of ${pc}`,14,ph-8);}
      doc.save(filename.endsWith(".pdf") ? filename : filename + ".pdf");
    } else { window.print(); }
  } catch(err) {
    console.error("PDF export error:", err);
    alert("Could not generate PDF. Printing page instead.");
    window.print();
  }
}

/* ============================================================
   Sidebar & App Initialisation
   ============================================================ */
document.addEventListener("DOMContentLoaded", () => {
  // Active nav link
  const path = window.location.pathname;
  document.querySelectorAll(".sidebar-wrapper .nav-link").forEach(link => {
    const href = link.getAttribute("href");
    if (href === path || (href !== "/" && path.startsWith(href))) link.classList.add("active");
  });

  // Restore sidebar state
  if (localStorage.getItem("sidebarState") === "collapsed") document.body.classList.add("sidebar-collapsed");

  const closeBtn = document.getElementById("sidebarCloseBtn");
  const openBtn  = document.getElementById("sidebarOpenBtn");
  if (closeBtn) closeBtn.addEventListener("click", () => { document.body.classList.add("sidebar-collapsed"); localStorage.setItem("sidebarState","collapsed"); });
  if (openBtn)  openBtn.addEventListener("click",  () => { document.body.classList.remove("sidebar-collapsed"); localStorage.setItem("sidebarState","open"); });

  // Init theme
  _applyThemeUI();

  // Close theme panel on outside click
  document.addEventListener("click", e => {
    const panel = document.getElementById("themeSwitcherPanel");
    const sw    = document.getElementById("themeSwitcher");
    if (panel && sw && !sw.contains(e.target)) panel.classList.remove("open");
  });
});

/* ============================================================
   3-Theme Switcher  (green | dark | blue)
   ============================================================ */
function openThemeSwitcher() {
  const p = document.getElementById("themeSwitcherPanel");
  if (p) p.classList.toggle("open");
}

function setTheme(theme) {
  const html = document.documentElement;
  if (theme === "green") { html.removeAttribute("data-theme"); }
  else { html.setAttribute("data-theme", theme); }
  localStorage.setItem("theme", theme);
  _applyThemeUI();
  const p = document.getElementById("themeSwitcherPanel");
  if (p) p.classList.remove("open");
}

function _applyThemeUI() {
  const theme = document.documentElement.getAttribute("data-theme") || "green";
  ["Green","Dark","Blue"].forEach(n => {
    const el = document.getElementById("swatch" + n);
    if (el) el.classList.toggle("active", theme === n.toLowerCase());
  });
  const icon = document.getElementById("themeSwitcherIcon");
  if (icon) icon.textContent = theme==="dark" ? "\ud83c\udf19" : theme==="blue" ? "\ud83d\udc99" : "\ud83c\udf3f";
}
