//função para o alerta
setTimeout(function() {
    var alert = document.getElementById('myAlert');
    alert.classList.remove('show');
    alert.classList.add('hide');
    setTimeout(function() {
        alert.style.display = 'none';
    }, 1000);
}, 3000);
    