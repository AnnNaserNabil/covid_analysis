/* script.js */

document.addEventListener("DOMContentLoaded", function() {
    console.log("Custom script loaded!");

    // Example: Add custom behavior to the sidebar dropdown
    const dropdown = document.querySelector('.stSidebar select');
    if (dropdown) {
        dropdown.addEventListener('change', function() {
            console.log(`Country selected: ${this.value}`);
        });
    }
});