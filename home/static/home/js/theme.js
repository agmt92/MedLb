// Function to toggle between dark and light themes
function toggleTheme() {
    // Check the current theme saved in local storage
    let theme = localStorage.getItem('theme');

    // If the theme is not set or is light, switch to dark theme
    if (theme !== 'dark') {
        document.body.classList.add('dark-theme');
        document.body.classList.remove('light-theme');
        localStorage.setItem('theme', 'dark');
    } else {
        // Otherwise, switch to light theme
        document.body.classList.add('light-theme');
        document.body.classList.remove('dark-theme');
        localStorage.setItem('theme', 'light');
    }
}

// On load, set the theme from local storage
document.addEventListener('DOMContentLoaded', () => {
    let theme = localStorage.getItem('theme');
    if (theme === 'dark') {
        document.body.classList.add('dark-theme');
    } else {
        document.body.classList.add('light-theme');
    }
});
