const hamBurger = document.querySelector(".toggle-btn");

hamBurger.addEventListener("click", function () {
  document.querySelector("#sidebar").classList.toggle("expand");
});


function mostrarContenido(seccion) {
  // Ocultar todos los divs de contenido
  var divsContenido = document.querySelectorAll('.main > div');
  divsContenido.forEach(function(div) {
      div.style.display = 'none';
  });

  // Mostrar solo el div correspondiente a la sección seleccionada
  document.getElementById(seccion).style.display = 'block';
}

function editarPerfil() {
  // Ocultar el div con los datos del usuario
  document.getElementById("perfil").style.display = "none";
  // Mostrar el div con el formulario editable
  document.getElementById("formularioEditar").style.display = "block";
  // Llenar los campos del formulario con los datos actuales del usuario
  document.getElementById("nuevoCorreo").value = document.getElementById("correo").innerText;
  document.getElementById("nuevaClave").value = "";
}

function mostrarClave() {
  var claveInput = document.getElementById("clave");
  var botonMostrar = claveInput.nextElementSibling;

  if (claveInput.type === "password") {
      claveInput.type = "text";
      botonMostrar.textContent = "Ocultar";
  } else {
      claveInput.type = "password";
      botonMostrar.textContent = "Mostrar";
  }
}

function cancelarEdicion() {
  // Mostrar de nuevo el div con los datos del usuario
  document.getElementById("perfil").style.display = "block";
  // Ocultar el div con el formulario editable
  document.getElementById("formularioEditar").style.display = "none";
}

function validateForm() {
  var nombre = document.getElementById("nombre").value;
  var apellido = document.getElementById("apellido").value;
  var documento = document.getElementById("documento").value;

  var nameRegex = /^[a-zA-Z]+$/; // Expresión regular que solo permite letras
  var documentoRegex = /^[0-9]+$/; // Expresión regular que solo permite números para la documento

  if (!nameRegex.test(nombre)) {
    document.getElementById("nombre_error").innerHTML = "El nombre no puede contener números";
    return false;
  } else {
    document.getElementById("nombre_error").innerHTML = "";
  }

  if (!nameRegex.test(apellido)) {
    document.getElementById("apellido_error").innerHTML = "El apellido no puede contener números";
    return false;
  } else {
    document.getElementById("apellido_error").innerHTML = "";
  }

  if (!documentoRegex.test(documento)) {
      document.getElementById("documento_error").innerHTML = "El documento debe contener solo números";
      return false;
    } else {
      document.getElementById("documento_error").innerHTML = "";
    }


  checkPasswordMatch();

  return true; // Si ambos campos son válidos, el formulario se envía correctamente
}

function checkPasswordMatch() {
var contraseña = document.getElementById("contraseña").value;
var ccontraseña = document.getElementById("ccontraseña").value;

if (contraseña != ccontraseña) {
  document.getElementById("contraseña_error").innerHTML = "Las contraseñas no coinciden";
  return false; 
} else {
  document.getElementById("contraseña_error").innerHTML = "";
  
}
return true; 
}

function validarHoras() {
  var horaInicial = document.getElementById("horaInicio").value;
  var horaFinal = document.getElementById("horaFinal").value;

  if (horaInicial >= horaFinal) {
    alert("La hora final debe ser posterior a la hora inicial.");
    return false; // Detener el envío del formulario
  }

  return true; // Permitir el envío del formulario si la validación pasa
}

function mostrarFormularioPago(idAgenda) {
  // Mostrar el formulario de pago
  document.getElementById("formularioPago").style.display = "block";

  // Mostrar el ID de la agenda en el campo correspondiente del formulario
  document.getElementById("agenda").value = idAgenda;
}