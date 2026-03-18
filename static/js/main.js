document.addEventListener('DOMContentLoaded', () => {
    const navLinks = document.querySelectorAll('nav a');
    const currentPath = window.location.pathname;

    navLinks.forEach(link => {
        if (link.getAttribute('href') === currentPath) {
            link.classList.add('active');
        }
    });

    const form = document.querySelector('form');
    if (form) {
        form.addEventListener('submit', event => {
            const age = document.getElementById('age');
            const weight = document.getElementById('weight');
            const height = document.getElementById('height');

            if (!age.value || !weight.value || !height.value) {
                event.preventDefault();
                alert('Please fill in all required fields.');
            }
        });
    }

    document.querySelectorAll('a[href^="#"]').forEach(anchor => {
        anchor.addEventListener('click', function (e) {
            e.preventDefault();

            document.querySelector(this.getAttribute('href')).scrollIntoView({
                behavior: 'smooth'
            });
        });
    });
});
