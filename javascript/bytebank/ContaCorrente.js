import {Cliente} from "./Cliente.js"
export class ContaCorrente{
	static numeroContas = 0;
	_cliente;
	set cliente(novoValor){
		if(novoValor instanceof Cliente){
			this._cliente = novoValor;
		};
	};
	get cliente(){
		return this._cliente;
	};

	_saldo = 0;
	get saldo(){
		return this._saldo;
	};
        _agencia;
	
	constructor(agencia, cliente){
		this._agencia = agencia;
		this._cliente = cliente;
		ContaCorrente.numeroContas += 1;
	};

        sacar(valor){
                if(this._saldo >= valor){
                        this._saldo -=valor;
                };
	};

	depositar(valor){
		this._saldo += valor;
	};

	transferir(valor, conta){
		if(this._saldo >= valor){
			this.sacar(valor);
			conta.depositar(valor);
		};
	};
};
