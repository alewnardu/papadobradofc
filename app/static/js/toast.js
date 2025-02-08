
// Mostra os toasts automaticamente quando a página é carregada
document.addEventListener('DOMContentLoaded', function() {
    // Mostrar os toasts automaticamente quando a página for carregada
    var toastElements = document.querySelectorAll('.toast');
    toastElements.forEach(function(toastElement) {
        var toast = new bootstrap.Toast(toastElement);
        toast.show();
    });
});
