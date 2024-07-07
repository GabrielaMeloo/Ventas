document.addEventListener('DOMContentLoaded', function() {
    const lista = document.querySelector('#lista-carrito tbody');
    const vaciarCarritoBtn = document.getElementById('vaciar-carrito');
    const loadMoreBtn = document.querySelector('#load-more');
    let currentItem = 8;

    if (loadMoreBtn) {
        loadMoreBtn.onclick = () => {
            let boxes = [...document.querySelectorAll('.box-container .box')];
            for (var i = currentItem; i < currentItem + 4; i++) {
                if (boxes[i]) {
                    boxes[i].style.display = 'inline-block';
                }
            }
            currentItem += 4;
            if (currentItem >= boxes.length) {
                loadMoreBtn.style.display = 'none';
            }
        }
    }

    if (lista) {
        cargarCarritoDeLocalStorage();
    }

    const listaProductos = document.getElementById('lista-1');
    if (listaProductos) {
        listaProductos.addEventListener('click', function(e) {
            if (e.target.classList.contains('agregar-carrito')) {
                e.preventDefault();
                const elemento = e.target.closest('.box');
                if (elemento) {
                    leerDatosElemento(elemento);
                }
            }
        });
    }

    if (vaciarCarritoBtn) {
        vaciarCarritoBtn.addEventListener('click', vaciarCarrito);
    }
    if (lista) {
        lista.addEventListener('click', eliminarElemento);
    }

    const listaCarrito = document.querySelector('#lista-carrito tbody');
    const carrito = document.querySelector('#lista-carrito');
    const btnPagar = document.querySelector('#btn-pagar');
    const paymentForm = document.querySelector('#payment-form');
    const cancelarPago = document.querySelector('#cancelar-pago');
    const totalPrecio = document.querySelector('#total-precio');
    const pagoForm = document.querySelector('#pago-form');

    let articulosCarrito = [];

    if (carrito) {
        cargarEventListeners();
    }

    function cargarEventListeners() {
        if (carrito) carrito.addEventListener('click', eliminarProducto);
        if (btnPagar) btnPagar.addEventListener('click', mostrarFormularioPago);
        if (cancelarPago) cancelarPago.addEventListener('click', ocultarFormularioPago);
        if (pagoForm) pagoForm.addEventListener('submit', procesarPago);

        document.addEventListener('DOMContentLoaded', () => {
            articulosCarrito = JSON.parse(localStorage.getItem('carrito')) || [];
            carritoHTML();
        });
    }

    function leerDatosElemento(elemento) {
        const infoElemento = {
            imagen: elemento.querySelector('img').src,
            titulo: elemento.querySelector('h3').textContent,
            precio: elemento.querySelector('.precio').textContent,
            id: elemento.querySelector('.agregar-carrito').getAttribute('data-id')
        }
        insertarCarrito(infoElemento);
    }

    function insertarCarrito(elemento) {
        const row = document.createElement('tr');
        row.innerHTML = `
            <td>
                <img src="${elemento.imagen}" width="100" height="150px">
            </td>
            <td>
                ${elemento.titulo}
            </td>
            <td>
                ${elemento.precio}
            </td>
            <td>
                <a href="#" class="borrar" data-id="${elemento.id}">X</a>
            </td>
        `;
        lista.appendChild(row);
        guardarElementoEnLocalStorage(elemento);
    }

    function eliminarElemento(e) {
        e.preventDefault();
        if (e.target.classList.contains('borrar')) {
            const row = e.target.parentElement.parentElement;
            const elementoId = e.target.getAttribute('data-id');
            row.remove();
            eliminarElementoDeLocalStorage(elementoId);
        }
    }

    function vaciarCarrito() {
        while (lista.firstChild) {
            lista.removeChild(lista.firstChild);
        }
        localStorage.removeItem('carrito');
        return false;
    }

    function guardarElementoEnLocalStorage(elemento) {
        let elementos = obtenerElementosDeLocalStorage();
        elementos.push(elemento);
        localStorage.setItem('carrito', JSON.stringify(elementos));
    }

    function obtenerElementosDeLocalStorage() {
        let elementos;
        if (localStorage.getItem('carrito') === null) {
            elementos = [];
        } else {
            elementos = JSON.parse(localStorage.getItem('carrito'));
        }
        return elementos;
    }

    function eliminarElementoDeLocalStorage(elementoId) {
        let elementos = obtenerElementosDeLocalStorage();
        elementos = elementos.filter(elemento => elemento.id !== elementoId);
        localStorage.setItem('carrito', JSON.stringify(elementos));
    }

    function cargarCarritoDeLocalStorage() {
        let elementos = obtenerElementosDeLocalStorage();
        elementos.forEach(elemento => {
            const row = document.createElement('tr');
            row.innerHTML = `
                <td>
                    <img src="${elemento.imagen}" width="100" height="150px">
                </td>
                <td>
                    ${elemento.titulo}
                </td>
                <td>
                    ${elemento.precio}
                </td>
                <td>
                    <a href="#" class="borrar" data-id="${elemento.id}">X</a>
                </td>
            `;
            lista.appendChild(row);
        });
    }

    function eliminarProducto(e) {
        e.preventDefault();
        if (e.target.classList.contains('borrar-producto')) {
            const productoId = e.target.getAttribute('data-id');
            articulosCarrito = articulosCarrito.filter(producto => producto.id !== productoId);
            carritoHTML();
        }
    }

    function mostrarFormularioPago() {
        if (paymentForm) paymentForm.style.display = 'block';
    }

    function ocultarFormularioPago() {
        if (paymentForm) paymentForm.style.display = 'none';
    }

    function procesarPago(e) {
        e.preventDefault();

        const nombreTarjeta = document.querySelector('#nombre-tarjeta').value;
        const numeroTarjeta = document.querySelector('#numero-tarjeta').value;
        const expiracionTarjeta = document.querySelector('#expiracion-tarjeta').value;
        const cvvTarjeta = document.querySelector('#cvv-tarjeta').value;

        if (nombreTarjeta === '' || numeroTarjeta === '' || expiracionTarjeta === '' || cvvTarjeta === '') {
            alert('Por favor, completa todos los campos de la tarjeta.');
            return;
        }

        alert('Pago realizado exitosamente.');

        articulosCarrito = [];
        localStorage.removeItem('carrito');
        carritoHTML();
        window.location.href = '../../index.html';
    }

    function calcularTotal() {
        function calcularTotal() {
            let total = articulosCarrito.reduce((total, producto) => total + parseFloat(producto.precio), 0);
            if (totalPrecio) {
                totalPrecio.textContent = `$${total.toFixed(2)}`;
            }
        }
        
    }

    function carritoHTML() {
        while (listaCarrito && listaCarrito.firstChild) {
            listaCarrito.removeChild(listaCarrito.firstChild);
        }

        articulosCarrito.forEach(producto => {
            const row = document.createElement('tr');
            row.innerHTML = `
                <td><img src="${producto.imagen}" width="100"></td>
                <td>${producto.nombre}</td>
                <td>$${producto.precio}</td>
                <td><a href="#" class="borrar-producto" data-id="${producto.id}">X</a></td>
            `;

            if (listaCarrito) listaCarrito.appendChild(row);
        });

        calcularTotal();
        sincronizarStorage();
    }

    function sincronizarStorage() {
        localStorage.setItem('carrito', JSON.stringify(articulosCarrito));
    }
});



















