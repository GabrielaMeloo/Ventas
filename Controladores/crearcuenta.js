// Crear Cuenta
document.addEventListener('DOMContentLoaded', function() {
    const form = document.getElementById('crear-cuenta-form');
    const formMessage = document.getElementById('form-message');

    if (form) {
        form.addEventListener('submit', function(event) {
            event.preventDefault();
            if (formMessage) {
                formMessage.style.display = 'block';
                setTimeout(() => {
                    formMessage.style.display = 'none';
                }, 5000); // Oculta el mensaje después de 5 segundos
            }
            form.reset();
        });
    }
});
