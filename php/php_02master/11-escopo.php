<?
header('Content-Type: text/html; charset=utf-8');
$i = 3;

for($i = 0; $i < 10; $i++){ // o escopo de $i não é local nos loops e condicionais
    echo "$i <br>";
}

echo "$i <br>"; 

$j = 10;
echo "j em escopo global = $j <br>";

function teste(){
    $j = 1;
    echo "j em escopo local = $j <br>";
}

teste();

// escopo global na função

function dobra(){
    global $j;
    
    $j = $j * 2;
}

dobra();

echo "novo valor de j após a função usar seu escopo global = $j <br>";

// escopo de varíavel static = o valor da variável se mantém após cada execução da função

echo "teste de variável static <br>";

function teste_static(){
    static $k = 0;  // só atribui valor na primeira execução
    $k++;
    echo "$k <br>";
}

teste_static();
teste_static();
teste_static();

// escopo de argumento de função
function soma($a, $b){
    return $a + $b;
}

$resultado = soma(10, 5);
echo "resultado da função soma = $resultado <br>";

?>