document.getElementById('login-form').addEventListener('submit', function(event) {
    event.preventDefault();
    
    // Aquí puedes agregar lógica para validar el usuario y contraseña
    const username = document.getElementById('username').value.trim();
    const password = document.getElementById('password').value.trim();
    
    // Por simplicidad, aquí se asume que el usuario y contraseña son correctos
    if (username === 'usuario' && password === 'password') {
        // Aquí rediriges al usuario a la página principal o donde desees
        window.location.href = 'index.html';
    } else {
        // Mensaje de error
        const errorMessage = document.getElementById('error-message');
        errorMessage.textContent = 'Usuario o contraseña incorrectos. Por favor, inténtalo de nuevo.';
    }
});
