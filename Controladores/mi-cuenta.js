// Mi cuenta
document.addEventListener('DOMContentLoaded', function() {
    const forms = document.querySelectorAll('form');
    const cerrarSesionBtn = document.getElementById('cerrar-sesion');

    forms.forEach(form => {
        form.addEventListener('submit', function(event) {
            event.preventDefault();
            alert('Formulario enviado exitosamente.');
            form.reset();
        });
    });

    if (cerrarSesionBtn) {
        cerrarSesionBtn.addEventListener('click', function() {
            alert('Has cerrado sesión.');
            window.location.href = '../../index.html';
        });
    }
});