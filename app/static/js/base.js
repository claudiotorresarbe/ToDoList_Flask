//função para o alerta
setTimeout(function() {
    var alert = document.getElementById('myAlert');
    alert.classList.remove('show');
    alert.classList.add('hide');
    setTimeout(function() {
        alert.style.display = 'none';
    }, 1000);
}, 3000);


//função para alterar o tema
const themeIcon = document.getElementById('themeIcon');

const updateThemeIcon = (theme) => {
const icons = {
    light: 'bi-sun',
    dark: 'bi-moon',
    auto: 'bi-circle-half'
};
themeIcon.className = 'bi ' + icons[theme];
};

document.querySelectorAll('.dropdown-item[data-theme]').forEach(btn => {
btn.addEventListener('click', () => {
    const theme = btn.getAttribute('data-theme');
    localStorage.setItem('theme', theme);

    if (theme === 'auto') {
    document.documentElement.removeAttribute('data-bs-theme');
    } else {
    document.documentElement.setAttribute('data-bs-theme', theme);
    }

    updateThemeIcon(theme);
});
});

// Aplica o tema salvo ao carregar a página
document.addEventListener('DOMContentLoaded', () => {
const savedTheme = localStorage.getItem('theme') || 'auto';
if (savedTheme !== 'auto') {
    document.documentElement.setAttribute('data-bs-theme', savedTheme);
}
updateThemeIcon(savedTheme);
});