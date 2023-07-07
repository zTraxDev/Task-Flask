function validar(){
var form = document.getElementById("form");
  
  // Agregar un escucha de evento para el submit
  form.addEventListener("submit", function(event) {
    // Prevenir el envío del formulario
    event.preventDefault();
    
    // Resetear el formulario
    form.reset();
    
    // Enviar el formulario
    form.submit();
});

}
