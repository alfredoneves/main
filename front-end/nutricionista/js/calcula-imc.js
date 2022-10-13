var titulo = document.querySelector(".titulo");
titulo.textContent = "Aparecida Nutricionista";

var pacientes = document.querySelectorAll(".paciente");

for (var i = 0; i < pacientes.length; i++) {
                var paciente = pacientes[i];

                var tdPeso = paciente.querySelector(".info-peso");
                var peso = tdPeso.textContent;

                var tdAltura = paciente.querySelector(".info-altura");
                var altura = tdAltura.textContent;

                var tdImc = paciente.querySelector(".info-imc");

                var pesoEhValido = validaPeso;
                var alturaEhValida = validaAltura;

    if (!pesoEhValido) {
        console.log("Peso inválido!");
        pesoEhValido = false;
        tdImc.textContent = "Peso inválido";
        paciente.classList.add("paciente-invalido");
    }

    if (!alturaEhValida) {
        console.log("Altura inválida!");
        alturaEhValida = false;
        tdImc.textContent = "Altura inválida";
        paciente.classList.add("paciente-invalido");
    }

    if (pesoEhValido && alturaEhValida) {
        var imc = calculaImc(peso, altura);
        tdImc.textContent = imc;
    }
}

function calculaImc(peso, altura) {
                var imc = 0;
                imc = peso / (altura * altura);
                return imc.toFixed(2);
}

function validaPeso(peso) {
                if (peso > 0 && peso < 1000) {
                return true;
                } else {
                return false;
                }
}

function validaAltura(altura) {
                if (altura > 0 && altura <= 3.00) {
                return true;
                } else {
                return false;
                }
}

// form.js
function validaPaciente(paciente) {
                var erros = [];

                if (paciente.nome.length == 0) {
                                erros.push("O nome não pode ser em branco");
                }
                if (paciente.gordura.length == 0) {
                                erros.push("A gordura não pode ser em branco");
                }
                if (paciente.peso.length == 0) {
                                erros.push("O peso não pode ser em branco");
                }

                if (paciente.altura.length == 0) {
                                erros.push("A altura não pode ser em branco");
                }

                if (!validaPeso(paciente.peso)) {
                                erros.push("Peso é inválido");
                }

                if (!validaAltura(paciente.altura)) {
                                erros.push("Altura é inválida");
                }
                return erros;
}
