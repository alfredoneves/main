import {Cliente} from "./Cliente.js"
import {ContaCorrente} from "./ContaCorrente.js"

const cliente1 = new Cliente("Alfredo", 3212312321);

const contaCorrente1 = new ContaCorrente(1001, cliente1);

const cliente2 = new Cliente("Ana", 9321569212);

const contaCorrente2 = new ContaCorrente(1001, cliente2);

contaCorrente1.depositar(400);
contaCorrente2.depositar(300);

contaCorrente1.transferir(100, contaCorrente2);

console.log(contaCorrente1);
console.log(contaCorrente2);
console.log(ContaCorrente.numeroContas);


