<?
class Pessoa{   // cria a classe
    function dar_oi(){
        echo "Oi!";
    }
}

$pessoa = new Pessoa();    // cria a instância da classe
$pessoa->nome = "Alfredo";  // muda o atribute da classe

echo $pessoa->nome; 
echo "<br>";
$pessoa->dar_oi();  // executa a função da classe

?>