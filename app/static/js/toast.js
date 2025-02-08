
// Mostra os toasts automaticamente quando a página é carregada
var toastElements = document.querySelectorAll('.toast');
toastElements.forEach(function(toastElement) {
    var toast = new bootstrap.Toast(toastElement);
    toast.show();
});
