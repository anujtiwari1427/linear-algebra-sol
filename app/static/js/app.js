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
