<?
header('Content-Type: text/html; charset=utf-8');

// array 
// geralmente usam um tipo de dado, mas não é regra
echo "array simples <br>";
$arr0 = array(10,20,30);
echo $arr0[2]. "<br>";

for($i=0; $i<count($arr0); $i++){
    echo $arr0[$i]. "<br>";
}

// array associativo
echo "array associativo <br>";
$carro = array(
    "marca" => "Renault",
     "cor" => "vermelha",
      "preço" => 50000
    ); // key => value

$tamanho_array = count($carro); // armazena o tamanho do array 

foreach($carro as $atributo => $valor){
    echo "$atributo = $valor <br>";
}

// exercício sobre array com condicional e função
echo "exercício sobre array com condicional e função <br>";

$pessoa = array(
    "nome" => "alfredo",
    "idade" => 18,
    "país" => "brasil",
    "cidade" => "rio de janeiro"
);

function maioridade($idade){    // retorna verdadeiro se a idade for igual ou maior que 18 e falso se for menor
    if($idade >= 18){
        return true;
    } else{
        return false;
    }
}

if(maioridade($pessoa['idade'])){
    echo $pessoa['nome']. " é maior de idade <br>";
} else {
    echo $pessoa['nome']. " não é maior de idade <br>";
}


// NULL

$var_nula = NULL;

if(is_null($var_nula)){
    echo '$var_nula é do tipo NULL';
}
?>